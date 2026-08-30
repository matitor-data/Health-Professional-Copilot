from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter

from dotenv import load_dotenv

from evidence_agent.embedding_retrieval import (
    DEFAULT_INDEX_PATH,
    DEFAULT_MIN_SIMILARITY,
    EmbeddingRetriever,
)
from evidence_agent.evaluate import DEFAULT_BENCHMARK, evaluate_retrieval
from evidence_agent.hybrid_retrieval import HybridRetriever
from evidence_agent.retrieval import DEFAULT_SOURCE_DIR, EvidenceRetriever


class _PrecomputedRetriever:
    def __init__(self, chunks: list[object], results: list[list[object]]) -> None:
        self.chunks = chunks
        self.results = results

    def search_many(self, queries: list[str], top_k: int) -> list[list[object]]:
        if len(queries) != len(self.results):
            raise ValueError("Precomputed query count does not match benchmark.")
        return [results[:top_k] for results in self.results]


DEFAULT_OUTPUT = Path("results/evidence_retrieval/comparison_v1.json")


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Compare lexical and embedding evidence retrieval.")
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX_PATH)
    parser.add_argument("--min-similarity", type=float, default=DEFAULT_MIN_SIMILARITY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    deterministic = EvidenceRetriever(args.source_dir)
    started = perf_counter()
    deterministic_report = evaluate_retrieval(deterministic, args.benchmark)
    deterministic_latency = round((perf_counter() - started) * 1000)

    embeddings = EmbeddingRetriever.load(
        args.index,
        source_dir=args.source_dir,
        min_similarity=args.min_similarity,
    )
    hybrid = HybridRetriever(deterministic, embeddings)
    hybrid_report = evaluate_retrieval(hybrid, args.benchmark)
    embedding_report = evaluate_retrieval(
        _PrecomputedRetriever(embeddings.chunks, hybrid.last_semantic_results), args.benchmark,
    )
    payload = {
        "comparison_id": "evidence-retrieval-comparison-v1",
        "created_at": datetime.now(UTC).isoformat(),
        "benchmark": str(args.benchmark),
        "systems": {
            "deterministic": {
                "metrics": deterministic_report["metrics"],
                "latency_ms": deterministic_latency,
                "api_requests": 0,
                "input_tokens": 0,
            },
            "embeddings": {
                "model": embeddings.model,
                "dimensions": embeddings.dimensions,
                "min_similarity": embeddings.min_similarity,
                "metrics": embedding_report["metrics"],
                **embeddings.last_query_stats,
            },
            "hybrid": {
                "embedding_model": embeddings.model,
                "embedding_dimensions": embeddings.dimensions,
                "min_similarity": embeddings.min_similarity,
                "rrf_k": hybrid.rrf_k,
                "min_lexical_terms": hybrid.min_lexical_terms,
                "min_lexical_score": hybrid.min_lexical_score,
                "metrics": hybrid_report["metrics"],
                **embeddings.last_query_stats,
            },
        },
        "query_results": {
            "deterministic": deterministic_report["queries"],
            "embeddings": embedding_report["queries"],
            "hybrid": hybrid_report["queries"],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["systems"], indent=2))


if __name__ == "__main__":
    main()
