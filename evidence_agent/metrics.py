from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from evidence_agent.rubric import evaluate_against_rubric, load_rubric


TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
STOP_WORDS = {"a", "an", "and", "for", "in", "of", "the", "to", "with"}


def _tokens(text: str) -> set[str]:
    return {
        token for token in TOKEN_PATTERN.findall(text.lower())
        if len(token) > 2 and token not in STOP_WORDS
    }


def _jaccard(left: str, right: str) -> float:
    a, b = _tokens(left), _tokens(right)
    return len(a & b) / len(a | b) if a and b else 0.0


def load_run(run_dir: Path | str) -> list[dict[str, Any]]:
    path = Path(run_dir) / "outputs.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def evaluate_run(rows: list[dict[str, Any]]) -> dict[str, Any]:
    statuses: Counter[str] = Counter()
    violation_rules: Counter[str] = Counter()
    total_assessments = total_refs = valid_refs = 0
    retrieved_assessments = cited_assessments = single_ref_assessments = 0
    limitations_present = eligible_rendered = ineligible_excluded = 0
    model_input = model_output = reasoning = visible = embedding = latency = 0

    for row in rows:
        evidence = row["evidence_agent"]
        trajectory = {item["consideration_id"]: item for item in evidence["trajectory"]}
        final_items = row["brief"]["supporting_evidence"]
        rendered_ids = {text.split(" ", 1)[0] for text in final_items}
        violation_rules.update(item["rule"] for item in evidence["gate_report"]["violations"])
        for assessment in evidence["assessments"]:
            total_assessments += 1
            status = assessment["support_status"]
            statuses[status] += 1
            retrieved = trajectory[assessment["consideration_id"]]["retrieval_results"]
            allowed = {item["chunk_id"] for item in retrieved}
            refs = assessment["evidence_refs"]
            retrieved_assessments += bool(retrieved)
            cited_assessments += bool(refs)
            single_ref_assessments += len(refs) == 1
            total_refs += len(refs)
            valid_refs += sum(ref in allowed for ref in refs)
            limitations_present += bool(assessment["limitations"])
            eligible = status in {"supported", "partially_supported"}
            eligible_rendered += eligible and assessment["consideration_id"] in rendered_ids
            ineligible_excluded += not eligible and assessment["consideration_id"] not in rendered_ids
        embedding += evidence["embedding_input_tokens"]
        model_input += evidence["model_input_tokens"]
        model_output += evidence["model_output_tokens"]
        reasoning += evidence["reasoning_tokens"]
        visible += evidence["visible_output_tokens"]
        latency += evidence["latency_ms"]

    supported = statuses["supported"] + statuses["partially_supported"]
    unresolved = total_assessments - supported
    gate_accepted = sum(row["evidence_agent"]["gate_report"]["accepted"] for row in rows)
    return {
        "case_count": len(rows),
        "successful_case_count": len(rows),
        "assessment_count": total_assessments,
        "support_status_counts": dict(statuses),
        "gate_acceptance_rate": gate_accepted / len(rows) if rows else 0.0,
        "blocking_gate_violation_count": sum(
            count for rule, count in violation_rules.items() if rule != "RETRIEVAL_EMPTY"
        ),
        "gate_event_counts": dict(violation_rules),
        "retrieval_coverage": retrieved_assessments / total_assessments if total_assessments else 0.0,
        "evidence_support_coverage": supported / total_assessments if total_assessments else 0.0,
        "full_support_rate": statuses["supported"] / total_assessments if total_assessments else 0.0,
        "unresolved_rate": unresolved / total_assessments if total_assessments else 0.0,
        "citation_validity": valid_refs / total_refs if total_refs else 1.0,
        "cited_assessment_rate": cited_assessments / total_assessments if total_assessments else 0.0,
        "single_citation_proxy": (
            single_ref_assessments / cited_assessments if cited_assessments else 1.0
        ),
        "limitation_coverage": limitations_present / total_assessments if total_assessments else 0.0,
        "eligible_render_fidelity": eligible_rendered / supported if supported else 1.0,
        "ineligible_exclusion_fidelity": ineligible_excluded / unresolved if unresolved else 1.0,
        "reference_count": total_refs,
        "usage": {
            "embedding_input_tokens": embedding,
            "model_input_tokens": model_input,
            "model_output_tokens": model_output,
            "reasoning_tokens": reasoning,
            "visible_output_tokens": visible,
            "latency_ms": latency,
        },
    }


def compare_runs(
    left: list[dict[str, Any]], right: list[dict[str, Any]], threshold: float = 0.35,
) -> dict[str, Any]:
    left_by_case = {row["case_id"]: row for row in left}
    right_by_case = {row["case_id"]: row for row in right}
    common_cases = sorted(set(left_by_case) & set(right_by_case))
    pairs: list[dict[str, Any]] = []
    left_total = right_total = 0
    exact_matches = 0

    for case_id in common_cases:
        left_items = left_by_case[case_id]["evidence_agent"]["assessments"]
        right_items = right_by_case[case_id]["evidence_agent"]["assessments"]
        left_total += len(left_items)
        right_total += len(right_items)
        candidates = []
        for left_index, left_item in enumerate(left_items):
            for right_index, right_item in enumerate(right_items):
                similarity = _jaccard(left_item["consideration"], right_item["consideration"])
                candidates.append((similarity, left_index, right_index))
        used_left: set[int] = set()
        used_right: set[int] = set()
        for similarity, left_index, right_index in sorted(candidates, reverse=True):
            if similarity < threshold or left_index in used_left or right_index in used_right:
                continue
            used_left.add(left_index)
            used_right.add(right_index)
            left_item, right_item = left_items[left_index], right_items[right_index]
            exact = left_item["consideration"].strip().lower() == right_item["consideration"].strip().lower()
            exact_matches += exact
            pairs.append({
                "case_id": case_id,
                "left_consideration": left_item["consideration"],
                "right_consideration": right_item["consideration"],
                "lexical_similarity": similarity,
                "exact_match": exact,
                "left_status": left_item["support_status"],
                "right_status": right_item["support_status"],
                "status_agreement": left_item["support_status"] == right_item["support_status"],
                "citation_set_agreement": set(left_item["evidence_refs"]) == set(right_item["evidence_refs"]),
            })

    matched = len(pairs)
    return {
        "common_case_count": len(common_cases),
        "left_assessment_count": left_total,
        "right_assessment_count": right_total,
        "assessment_count_difference": abs(left_total - right_total),
        "aligned_assessment_count": matched,
        "alignment_threshold": threshold,
        "consideration_alignment_precision_left": matched / left_total if left_total else 0.0,
        "consideration_alignment_recall_right": matched / right_total if right_total else 0.0,
        "consideration_alignment_f1": (
            2 * matched / (left_total + right_total) if left_total + right_total else 0.0
        ),
        "exact_consideration_match_rate": exact_matches / matched if matched else 0.0,
        "support_status_agreement": (
            sum(pair["status_agreement"] for pair in pairs) / matched if matched else 0.0
        ),
        "citation_set_agreement": (
            sum(pair["citation_set_agreement"] for pair in pairs) / matched if matched else 0.0
        ),
        "aligned_pairs": pairs,
    }


def build_report(run_dirs: list[Path], rubric_path: Path | None = None) -> dict[str, Any]:
    loaded = {path.name: load_run(path) for path in run_dirs}
    report: dict[str, Any] = {
        "report_id": "evidence-agent-development-measurements-v1",
        "metric_notes": {
            "citation_validity": "Checks only that every citation was retrieved for that consideration.",
            "single_citation_proxy": "Measures citation-count minimality, not semantic necessity.",
            "consideration_alignment": "Greedy lexical alignment at Jaccard >= 0.35; it is a stability proxy.",
            "support_status_agreement": "Agreement only among lexically aligned considerations.",
        },
        "runs": {run_id: evaluate_run(rows) for run_id, rows in loaded.items()},
    }
    if len(run_dirs) == 2:
        left, right = (path.name for path in run_dirs)
        report["stability"] = {
            "left_run": left,
            "right_run": right,
            **compare_runs(loaded[left], loaded[right]),
        }
    if rubric_path is not None:
        rubric = load_rubric(rubric_path)
        report["rubric_id"] = rubric["rubric_id"]
        report["rubric_evaluation"] = {
            run_id: evaluate_against_rubric(rows, rubric) for run_id, rows in loaded.items()
        }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure Evidence Agent runs.")
    parser.add_argument("run_dir", type=Path, nargs="+")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--rubric", type=Path)
    args = parser.parse_args()
    report = build_report(args.run_dir, args.rubric)
    serialized = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
