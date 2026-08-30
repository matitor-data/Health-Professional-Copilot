from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_RUBRIC = Path("data/evaluations/evidence_agent/evidence_assessment_rubric_v1.json")


def load_rubric(path: Path | str = DEFAULT_RUBRIC) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def evaluate_against_rubric(
    rows: list[dict[str, Any]], rubric: dict[str, Any],
) -> dict[str, float | int]:
    expected_count = status_hits = 0
    required_total = required_hits = 0
    citation_total = allowed_citations = unnecessary_citations = 0
    abstention_total = abstention_hits = retrieval_misses = 0
    missing = unexpected = 0

    for row in rows:
        expected_items = {
            item["consideration_id"]: item for item in rubric["cases"][row["case_id"]]
        }
        actual_items = {
            item["consideration_id"]: item for item in row["evidence_agent"]["assessments"]
        }
        missing += len(set(expected_items) - set(actual_items))
        unexpected += len(set(actual_items) - set(expected_items))
        rendered_ids = {
            text.split(" ", 1)[0] for text in row["brief"]["supporting_evidence"]
        }
        for consideration_id, expected in expected_items.items():
            expected_count += 1
            actual = actual_items.get(consideration_id)
            if actual is None:
                continue
            status_hits += actual["support_status"] in expected["expected_statuses"]
            required = set(expected["required_source_ids"])
            allowed = set(expected["allowed_source_ids"])
            unnecessary = set(expected["unnecessary_source_ids"])
            cited_sources = {ref.split(":", 1)[0] for ref in actual["evidence_refs"]}
            required_total += len(required)
            required_hits += len(required & cited_sources)
            citation_total += len(cited_sources)
            allowed_citations += len(cited_sources & allowed)
            unnecessary_citations += len(cited_sources & unnecessary)
            expects_abstention = not required
            if expects_abstention:
                abstention_total += 1
                abstention_hits += consideration_id not in rendered_ids
            if required and actual["support_status"] == "retrieval_failed":
                retrieval_misses += 1

    return {
        "expected_assessment_count": expected_count,
        "missing_assessment_count": missing,
        "unexpected_assessment_count": unexpected,
        "support_status_accuracy": status_hits / expected_count if expected_count else 0.0,
        "required_source_recall": required_hits / required_total if required_total else 1.0,
        "allowed_source_precision": allowed_citations / citation_total if citation_total else 1.0,
        "unnecessary_citation_count": unnecessary_citations,
        "unnecessary_citation_rate": (
            unnecessary_citations / citation_total if citation_total else 0.0
        ),
        "correct_abstention_rate": abstention_hits / abstention_total if abstention_total else 1.0,
        "expected_source_retrieval_miss_count": retrieval_misses,
    }
