from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from evidence_agent.schemas import EvidenceChunk, RetrievalResult, SourceRecord


DEFAULT_SOURCE_DIR = Path("data/nutrition_evidence_sources_v1")
SECTION_PATTERN = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
TITLE_PATTERN = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
SOURCE_ID_PATTERN = re.compile(r"\*\*Source ID:\*\*\s+`([^`]+)`")
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "de", "del", "do",
    "does", "el", "en", "for", "from", "in", "is", "la", "las", "los", "of", "on",
    "or", "para", "por", "que", "the", "to", "un", "una", "with",
}


def _normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(character for character in decomposed if not unicodedata.combining(character)).lower()


def _tokens(value: str) -> list[str]:
    return [
        token for token in TOKEN_PATTERN.findall(_normalize(value))
        if len(token) > 1 and token not in STOP_WORDS
    ]


def _slug(value: str) -> str:
    return "-".join(_tokens(value)) or "section"


class EvidenceRetriever:
    """Loads approved local sources and ranks their sections without model calls."""

    def __init__(self, source_dir: Path | str = DEFAULT_SOURCE_DIR) -> None:
        self.source_dir = Path(source_dir).resolve()
        self.records = self._load_registry()
        self.chunks = self._load_chunks()

    def _load_registry(self) -> list[SourceRecord]:
        registry_path = self.source_dir / "source_registry.json"
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
        records = [SourceRecord.model_validate(item) for item in payload.get("sources", [])]
        approved = [record for record in records if record.status == "approved"]
        if not approved:
            raise ValueError("The evidence registry contains no approved sources.")
        if len({record.source_id for record in approved}) != len(approved):
            raise ValueError("Approved source IDs must be unique.")
        return approved

    def _source_path(self, record: SourceRecord) -> Path:
        path = (self.source_dir / record.file).resolve()
        if not path.is_relative_to(self.source_dir):
            raise ValueError(f"Source path escapes evidence directory: {record.file}")
        if path.suffix.lower() != ".md" or not path.is_file():
            raise ValueError(f"Approved source is not a Markdown file: {record.file}")
        return path

    def _load_chunks(self) -> list[EvidenceChunk]:
        chunks: list[EvidenceChunk] = []
        for record in self.records:
            path = self._source_path(record)
            document = path.read_text(encoding="utf-8")
            source_id_match = SOURCE_ID_PATTERN.search(document)
            if not source_id_match or source_id_match.group(1) != record.source_id:
                raise ValueError(f"Source ID mismatch in {record.file}")
            title_match = TITLE_PATTERN.search(document)
            if not title_match:
                raise ValueError(f"Missing document title in {record.file}")
            title = title_match.group(1).strip()
            matches = list(SECTION_PATTERN.finditer(document))
            for index, match in enumerate(matches):
                section = match.group(1).strip()
                start = match.end()
                end = matches[index + 1].start() if index + 1 < len(matches) else len(document)
                text = document[start:end].strip()
                if not text or section in {"Provenance", "Tags"}:
                    continue
                digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
                chunks.append(EvidenceChunk(
                    chunk_id=f"{record.source_id}:{_slug(section)}",
                    source_id=record.source_id,
                    title=title,
                    section=section,
                    text=text,
                    topics=record.topics,
                    content_sha256=digest,
                ))
        if not chunks:
            raise ValueError("Approved evidence sources produced no retrievable chunks.")
        return chunks

    @staticmethod
    def _score(query: str, chunk: EvidenceChunk) -> tuple[int, list[str]]:
        query_tokens = _tokens(query)
        if not query_tokens:
            return 0, []
        query_counts = Counter(query_tokens)
        body_counts = Counter(_tokens(chunk.text))
        heading_counts = Counter(_tokens(f"{chunk.title} {chunk.section}"))
        topic_counts = Counter(_tokens(" ".join(chunk.topics)))
        matched = sorted({token for token in query_counts if token in body_counts or token in heading_counts or token in topic_counts})
        score = sum(
            min(query_counts[token], body_counts[token])
            + 3 * min(query_counts[token], heading_counts[token])
            + 5 * min(query_counts[token], topic_counts[token])
            for token in matched
        )
        normalized_query = " ".join(query_tokens)
        if len(query_tokens) > 1 and normalized_query in _normalize(chunk.text):
            score += 4
        return score, matched

    def search(self, query: str, top_k: int = 3, min_score: int = 1) -> list[RetrievalResult]:
        if top_k < 1:
            raise ValueError("top_k must be at least 1.")
        if min_score < 0:
            raise ValueError("min_score cannot be negative.")
        ranked: list[RetrievalResult] = []
        for chunk in self.chunks:
            score, matched_terms = self._score(query, chunk)
            if score >= min_score:
                ranked.append(RetrievalResult(
                    chunk_id=chunk.chunk_id,
                    source_id=chunk.source_id,
                    title=chunk.title,
                    section=chunk.section,
                    text=chunk.text,
                    score=score,
                    matched_terms=matched_terms,
                    content_sha256=chunk.content_sha256,
                ))
        ranked.sort(key=lambda result: (-result.score, result.source_id, result.chunk_id))
        return ranked[:top_k]


def load_default_retriever() -> EvidenceRetriever:
    return EvidenceRetriever(DEFAULT_SOURCE_DIR)


def main() -> None:
    parser = argparse.ArgumentParser(description="Search approved synthetic nutrition evidence.")
    parser.add_argument("query", help="Nutrition concept or consideration to retrieve evidence for.")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = parser.parse_args()
    results = EvidenceRetriever(args.source_dir).search(args.query, top_k=args.top_k)
    print(json.dumps([result.model_dump() for result in results], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
