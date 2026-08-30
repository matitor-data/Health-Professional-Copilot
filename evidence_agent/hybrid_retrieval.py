from __future__ import annotations

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from evidence_agent.embedding_retrieval import (
    DEFAULT_INDEX_PATH,
    DEFAULT_MIN_SIMILARITY,
    EmbeddingRetriever,
)
from evidence_agent.retrieval import DEFAULT_SOURCE_DIR, EvidenceRetriever, _tokens
from evidence_agent.schemas import RetrievalResult


DEFAULT_RRF_K = 60
DEFAULT_MIN_LEXICAL_TERMS = 2
DEFAULT_MIN_LEXICAL_SCORE = 4


class HybridRetriever:
    """Source-level reciprocal-rank fusion of semantic and high-confidence lexical results."""

    def __init__(
        self,
        deterministic: EvidenceRetriever,
        embeddings: EmbeddingRetriever,
        *,
        rrf_k: int = DEFAULT_RRF_K,
        min_lexical_terms: int = DEFAULT_MIN_LEXICAL_TERMS,
        min_lexical_score: float = DEFAULT_MIN_LEXICAL_SCORE,
    ) -> None:
        if rrf_k < 1:
            raise ValueError("rrf_k must be at least 1.")
        self.deterministic = deterministic
        self.embeddings = embeddings
        self.chunks = deterministic.chunks
        self.rrf_k = rrf_k
        self.min_lexical_terms = min_lexical_terms
        self.min_lexical_score = min_lexical_score
        self.last_lexical_results: list[list[RetrievalResult]] = []
        self.last_semantic_results: list[list[RetrievalResult]] = []

    def _eligible_lexical(self, result: RetrievalResult) -> bool:
        chunk = next(chunk for chunk in self.chunks if chunk.chunk_id == result.chunk_id)
        metadata_terms = set(_tokens(" ".join([*chunk.topics, *chunk.aliases])))
        return (
            result.score >= self.min_lexical_score
            and len(set(result.matched_terms)) >= self.min_lexical_terms
            and bool(set(result.matched_terms) & metadata_terms)
        )

    def _fuse(
        self,
        lexical: list[RetrievalResult],
        semantic: list[RetrievalResult],
        top_k: int,
    ) -> list[RetrievalResult]:
        lexical = [result for result in lexical if self._eligible_lexical(result)]
        rankings = {"deterministic": lexical, "embedding": semantic}
        source_scores: dict[str, float] = {}
        representatives: dict[str, RetrievalResult] = {}
        methods: dict[str, set[str]] = {}

        for method, results in rankings.items():
            seen: set[str] = set()
            source_rank = 0
            for result in results:
                if result.source_id in seen:
                    continue
                seen.add(result.source_id)
                source_rank += 1
                source_scores[result.source_id] = (
                    source_scores.get(result.source_id, 0.0) + 1 / (self.rrf_k + source_rank)
                )
                methods.setdefault(result.source_id, set()).add(method)
                current = representatives.get(result.source_id)
                if current is None or method == "embedding":
                    representatives[result.source_id] = result

        ordered = sorted(source_scores, key=lambda source_id: (-source_scores[source_id], source_id))
        fused: list[RetrievalResult] = []
        for source_id in ordered[:top_k]:
            representative = representatives[source_id]
            fused.append(representative.model_copy(update={
                "score": source_scores[source_id],
                "retrieval_methods": sorted(methods[source_id]),
            }))
        return fused

    def search(self, query: str, top_k: int = 3) -> list[RetrievalResult]:
        return self.search_many([query], top_k=top_k)[0]

    def search_many(self, queries: list[str], top_k: int = 3) -> list[list[RetrievalResult]]:
        if top_k < 1:
            raise ValueError("top_k must be at least 1.")
        lexical = [
            self.deterministic.search(query, top_k=len(self.chunks)) for query in queries
        ]
        semantic = self.embeddings.search_many(queries, top_k=len(self.chunks))
        self.last_lexical_results = lexical
        self.last_semantic_results = semantic
        return [
            self._fuse(lexical_results, semantic_results, top_k)
            for lexical_results, semantic_results in zip(lexical, semantic, strict=True)
        ]


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Query hybrid nutrition evidence retrieval.")
    parser.add_argument("query")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX_PATH)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--min-similarity", type=float, default=DEFAULT_MIN_SIMILARITY)
    args = parser.parse_args()
    deterministic = EvidenceRetriever(args.source_dir)
    embeddings = EmbeddingRetriever.load(
        args.index, source_dir=args.source_dir, min_similarity=args.min_similarity,
    )
    retriever = HybridRetriever(deterministic, embeddings)
    print(json.dumps(
        [result.model_dump() for result in retriever.search(args.query, args.top_k)],
        indent=2,
        ensure_ascii=False,
    ))


if __name__ == "__main__":
    main()
