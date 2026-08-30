from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from evidence_agent.retrieval import DEFAULT_SOURCE_DIR, EvidenceRetriever


DEFAULT_BENCHMARK = Path("data/evaluations/evidence_retrieval_v1.json")


def evaluate_retrieval(
    retriever: EvidenceRetriever,
    benchmark_path: Path | str = DEFAULT_BENCHMARK,
    cutoffs: tuple[int, ...] = (1, 3),
) -> dict[str, Any]:
    benchmark = json.loads(Path(benchmark_path).read_text(encoding="utf-8"))
    positive = [item for item in benchmark["queries"] if item["relevant_source_ids"]]
    negative = [item for item in benchmark["queries"] if not item["relevant_source_ids"]]
    max_k = max(cutoffs)
    rows: list[dict[str, Any]] = []

    all_results = (
        retriever.search_many(
            [item["query"] for item in benchmark["queries"]], top_k=len(retriever.chunks)
        )
        if hasattr(retriever, "search_many")
        else [
            retriever.search(item["query"], top_k=len(retriever.chunks))
            for item in benchmark["queries"]
        ]
    )
    for item, results in zip(benchmark["queries"], all_results, strict=True):
        retrieved = list(dict.fromkeys(result.source_id for result in results))[:max_k]
        relevant = set(item["relevant_source_ids"])
        row: dict[str, Any] = {
            "query_id": item["query_id"],
            "query": item["query"],
            "relevant_source_ids": sorted(relevant),
            "retrieved_source_ids": retrieved,
        }
        for k in cutoffs:
            top = retrieved[:k]
            hits = sum(source_id in relevant for source_id in top)
            row[f"recall@{k}"] = hits / len(relevant) if relevant else None
            row[f"precision@{k}"] = hits / len(top) if relevant and top else (0.0 if relevant else None)
        rows.append(row)

    metrics: dict[str, float | int] = {
        "query_count": len(rows),
        "positive_query_count": len(positive),
        "negative_query_count": len(negative),
    }
    positive_rows = [row for row in rows if row["relevant_source_ids"]]
    for k in cutoffs:
        metrics[f"recall@{k}"] = sum(row[f"recall@{k}"] for row in positive_rows) / len(positive_rows)
        metrics[f"precision@{k}"] = sum(row[f"precision@{k}"] for row in positive_rows) / len(positive_rows)
    negative_rows = [row for row in rows if not row["relevant_source_ids"]]
    metrics["no_answer_accuracy"] = (
        sum(not row["retrieved_source_ids"] for row in negative_rows) / len(negative_rows)
    )
    return {"benchmark_id": benchmark["benchmark_id"], "metrics": metrics, "queries": rows}


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate deterministic evidence retrieval.")
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate_retrieval(EvidenceRetriever(args.source_dir), args.benchmark)
    serialized = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
