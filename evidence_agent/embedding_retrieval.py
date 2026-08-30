from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from time import perf_counter
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

from evidence_agent.retrieval import DEFAULT_SOURCE_DIR, EvidenceRetriever
from evidence_agent.schemas import RetrievalResult


DEFAULT_MODEL = "text-embedding-3-small"
DEFAULT_DIMENSIONS = 512
DEFAULT_MIN_SIMILARITY = 0.45
DEFAULT_INDEX_PATH = Path("data/evidence_indexes/nutrition_embeddings_v1.json")


def _cosine_similarity(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right, strict=True))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return numerator / (left_norm * right_norm)


class EmbeddingRetriever:
    """Semantic retrieval over the same approved chunks as the lexical baseline."""

    def __init__(
        self,
        lexical_retriever: EvidenceRetriever,
        vectors: dict[str, list[float]],
        *,
        model: str = DEFAULT_MODEL,
        dimensions: int = DEFAULT_DIMENSIONS,
        min_similarity: float = DEFAULT_MIN_SIMILARITY,
        client: OpenAI | None = None,
    ) -> None:
        self.lexical_retriever = lexical_retriever
        self.chunks = lexical_retriever.chunks
        self.vectors = vectors
        self.model = model
        self.dimensions = dimensions
        self.min_similarity = min_similarity
        self.client = client or OpenAI()
        self.last_query_stats: dict[str, int | float] = {}
        expected = {chunk.chunk_id for chunk in self.chunks}
        if set(vectors) != expected:
            raise ValueError("Embedding index does not match the approved evidence chunks.")
        if any(len(vector) != dimensions for vector in vectors.values()):
            raise ValueError("Embedding index dimensions do not match the configured dimensions.")

    @staticmethod
    def _chunk_input(chunk: Any) -> str:
        topics = ", ".join(chunk.topics)
        aliases = ", ".join(chunk.aliases)
        return (
            f"Title: {chunk.title}\nSection: {chunk.section}\nTopics: {topics}\n"
            f"Bilingual aliases: {aliases}\nContent: {chunk.text}"
        )

    @classmethod
    def build(
        cls,
        source_dir: Path | str = DEFAULT_SOURCE_DIR,
        *,
        model: str = DEFAULT_MODEL,
        dimensions: int = DEFAULT_DIMENSIONS,
        min_similarity: float = DEFAULT_MIN_SIMILARITY,
        client: OpenAI | None = None,
    ) -> tuple[EmbeddingRetriever, dict[str, int | float]]:
        api = client or OpenAI()
        lexical = EvidenceRetriever(source_dir)
        started = perf_counter()
        response = api.embeddings.create(
            model=model,
            dimensions=dimensions,
            input=[cls._chunk_input(chunk) for chunk in lexical.chunks],
        )
        vectors = {
            chunk.chunk_id: item.embedding
            for chunk, item in zip(lexical.chunks, response.data, strict=True)
        }
        stats: dict[str, int | float] = {
            "request_count": 1,
            "input_count": len(lexical.chunks),
            "input_tokens": response.usage.prompt_tokens,
            "latency_ms": round((perf_counter() - started) * 1000),
        }
        return cls(
            lexical, vectors, model=model, dimensions=dimensions,
            min_similarity=min_similarity, client=api,
        ), stats

    def save(self, path: Path | str = DEFAULT_INDEX_PATH) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        chunks = {
            chunk.chunk_id: {
                "content_sha256": chunk.content_sha256,
                "embedding": self.vectors[chunk.chunk_id],
            }
            for chunk in self.chunks
        }
        payload = {
            "index_version": "nutrition-embeddings-v1",
            "model": self.model,
            "dimensions": self.dimensions,
            "source_collection": str(self.lexical_retriever.source_dir),
            "chunks": chunks,
        }
        target.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")

    @classmethod
    def load(
        cls,
        path: Path | str = DEFAULT_INDEX_PATH,
        *,
        source_dir: Path | str = DEFAULT_SOURCE_DIR,
        min_similarity: float = DEFAULT_MIN_SIMILARITY,
        client: OpenAI | None = None,
    ) -> EmbeddingRetriever:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        lexical = EvidenceRetriever(source_dir)
        current_hashes = {chunk.chunk_id: chunk.content_sha256 for chunk in lexical.chunks}
        stored_hashes = {
            chunk_id: item["content_sha256"] for chunk_id, item in payload["chunks"].items()
        }
        if stored_hashes != current_hashes:
            raise ValueError("Embedding index is stale for the current evidence content.")
        vectors = {
            chunk_id: item["embedding"] for chunk_id, item in payload["chunks"].items()
        }
        return cls(
            lexical,
            vectors,
            model=payload["model"],
            dimensions=payload["dimensions"],
            min_similarity=min_similarity,
            client=client,
        )

    def _rank_vector(self, vector: list[float], top_k: int) -> list[RetrievalResult]:
        ranked: list[RetrievalResult] = []
        for chunk in self.chunks:
            score = _cosine_similarity(vector, self.vectors[chunk.chunk_id])
            if score >= self.min_similarity:
                ranked.append(RetrievalResult(
                    chunk_id=chunk.chunk_id,
                    source_id=chunk.source_id,
                    title=chunk.title,
                    section=chunk.section,
                    text=chunk.text,
                    score=score,
                    matched_terms=[],
                    retrieval_methods=["embedding"],
                    content_sha256=chunk.content_sha256,
                ))
        ranked.sort(key=lambda result: (-result.score, result.source_id, result.chunk_id))
        return ranked[:top_k]

    def search(self, query: str, top_k: int = 3) -> list[RetrievalResult]:
        return self.search_many([query], top_k=top_k)[0]

    def search_many(self, queries: list[str], top_k: int = 3) -> list[list[RetrievalResult]]:
        if top_k < 1:
            raise ValueError("top_k must be at least 1.")
        if not queries:
            return []
        started = perf_counter()
        response = self.client.embeddings.create(
            model=self.model,
            dimensions=self.dimensions,
            input=queries,
        )
        self.last_query_stats = {
            "request_count": 1,
            "input_count": len(queries),
            "input_tokens": response.usage.prompt_tokens,
            "latency_ms": round((perf_counter() - started) * 1000),
        }
        return [self._rank_vector(item.embedding, top_k) for item in response.data]


def _index_fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Build or query the nutrition embedding index.")
    parser.add_argument("query", nargs="?")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX_PATH)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--min-similarity", type=float, default=DEFAULT_MIN_SIMILARITY)
    args = parser.parse_args()
    if args.build:
        retriever, stats = EmbeddingRetriever.build(
            args.source_dir, min_similarity=args.min_similarity,
        )
        retriever.save(args.index)
        print(json.dumps({**stats, "index": str(args.index), "sha256": _index_fingerprint(args.index)}, indent=2))
        return
    if not args.query:
        parser.error("Provide a query or use --build.")
    retriever = EmbeddingRetriever.load(
        args.index, source_dir=args.source_dir, min_similarity=args.min_similarity,
    )
    print(json.dumps(
        [item.model_dump() for item in retriever.search(args.query, args.top_k)],
        indent=2,
        ensure_ascii=False,
    ))


if __name__ == "__main__":
    main()
