from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean
from typing import Any

from baseline.runner import load_dataset
from baseline.schemas import BaselineBrief
from evaluation.metrics import evaluate_case


GPT_INPUT_PRICE = 0.25
GPT_OUTPUT_PRICE = 2.00
EMBEDDING_INPUT_PRICE = 0.02


def _json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _average(rows: list[dict[str, float]], key: str) -> float:
    return mean(row[key] for row in rows) if rows else 0.0


def _cost(input_tokens: int, output_tokens: int, embedding_tokens: int = 0) -> float:
    return (
        input_tokens * GPT_INPUT_PRICE
        + output_tokens * GPT_OUTPUT_PRICE
        + embedding_tokens * EMBEDDING_INPUT_PRICE
    ) / 1_000_000


def build_report(baseline_dir: Path, solution_dir: Path, dataset_path: Path) -> dict[str, Any]:
    dataset = load_dataset(dataset_path)
    cases = {case.case_id: case for case in dataset.cases}
    baseline_manifest = _json(baseline_dir / "manifest.json")
    solution_manifest = _json(solution_dir / "manifest.json")
    baseline_rows = {row["case_id"]: row for row in _jsonl(baseline_dir / "outputs.jsonl")}
    solution_rows = {row["case_id"]: row for row in _jsonl(solution_dir / "outputs.jsonl")}
    baseline_failures = _jsonl(baseline_dir / "failures.jsonl")
    solution_failures = _jsonl(solution_dir / "failures.jsonl")
    shared_ids = sorted(set(baseline_rows) & set(solution_rows) & set(cases))

    comparisons: list[dict[str, Any]] = []
    all_assessments: list[dict[str, Any]] = []
    gate_accepts = 0
    citation_count = 0
    valid_citation_count = 0

    for case_id in shared_ids:
        case = cases[case_id]
        baseline_row = baseline_rows[case_id]
        solution_row = solution_rows[case_id]
        baseline_brief = BaselineBrief.model_validate(baseline_row["brief"])
        solution_brief = BaselineBrief.model_validate(solution_row["brief"])
        baseline_metrics = evaluate_case(case, baseline_brief)
        solution_metrics = evaluate_case(case, solution_brief)
        nutrition = solution_row["nutrition_agent"]
        evidence = solution_row["evidence_agent"]
        assessments = evidence["assessments"]
        all_assessments.extend(assessments)
        gate_accepts += int(evidence["gate_report"]["accepted"])
        retrieved_by_id = {
            item["consideration_id"]: {
                result["chunk_id"] for result in item["retrieval_results"]
            }
            for item in evidence["trajectory"]
        }
        for assessment in assessments:
            refs = assessment["evidence_refs"]
            citation_count += len(refs)
            valid_citation_count += sum(
                ref in retrieved_by_id.get(assessment["consideration_id"], set()) for ref in refs
            )

        baseline_input = baseline_row.get("input_tokens") or 0
        baseline_output = baseline_row.get("output_tokens") or 0
        solution_input = (nutrition.get("input_tokens") or 0) + (evidence.get("model_input_tokens") or 0)
        solution_output = (nutrition.get("output_tokens") or 0) + (evidence.get("model_output_tokens") or 0)
        embedding_tokens = evidence.get("embedding_input_tokens") or 0
        comparisons.append({
            "case_id": case_id,
            "baseline_metrics": baseline_metrics,
            "solution_metrics": solution_metrics,
            "baseline_input_tokens": baseline_input,
            "baseline_output_tokens": baseline_output,
            "baseline_reasoning_tokens": baseline_row.get("reasoning_tokens") or 0,
            "baseline_visible_tokens": baseline_row.get("visible_output_tokens") or 0,
            "baseline_latency_ms": baseline_row.get("latency_ms") or 0,
            "baseline_cost_usd": _cost(baseline_input, baseline_output),
            "solution_input_tokens": solution_input,
            "solution_output_tokens": solution_output,
            "solution_reasoning_tokens": (
                (nutrition.get("reasoning_tokens") or 0) + (evidence.get("reasoning_tokens") or 0)
            ),
            "solution_visible_tokens": (
                (nutrition.get("visible_output_tokens") or 0)
                + (evidence.get("visible_output_tokens") or 0)
            ),
            "solution_embedding_tokens": embedding_tokens,
            "solution_latency_ms": (
                (nutrition.get("latency_ms") or 0) + (evidence.get("latency_ms") or 0)
            ),
            "solution_cost_usd": _cost(solution_input, solution_output, embedding_tokens),
        })

    metric_names = sorted(comparisons[0]["baseline_metrics"]) if comparisons else []
    aggregate_metrics = {
        name: {
            "baseline": mean(float(row["baseline_metrics"][name]) for row in comparisons),
            "solution": mean(float(row["solution_metrics"][name]) for row in comparisons),
        }
        for name in metric_names
    }
    for values in aggregate_metrics.values():
        values["delta"] = values["solution"] - values["baseline"]

    statuses: dict[str, int] = {}
    for assessment in all_assessments:
        status = assessment["support_status"]
        statuses[status] = statuses.get(status, 0) + 1
    supported_count = sum(statuses.get(status, 0) for status in ("supported", "partially_supported"))

    efficiency = {}
    for label, baseline_key, solution_key in (
        ("input_tokens", "baseline_input_tokens", "solution_input_tokens"),
        ("output_tokens", "baseline_output_tokens", "solution_output_tokens"),
        ("reasoning_tokens", "baseline_reasoning_tokens", "solution_reasoning_tokens"),
        ("visible_tokens", "baseline_visible_tokens", "solution_visible_tokens"),
        ("latency_ms", "baseline_latency_ms", "solution_latency_ms"),
        ("cost_usd", "baseline_cost_usd", "solution_cost_usd"),
    ):
        baseline_value = _average(comparisons, baseline_key)
        solution_value = _average(comparisons, solution_key)
        efficiency[label] = {
            "baseline": baseline_value,
            "solution": solution_value,
            "delta": solution_value - baseline_value,
        }

    return {
        "evaluation_type": "single locked synthetic prototype comparison",
        "dataset": str(dataset_path),
        "baseline_manifest": baseline_manifest,
        "solution_manifest": solution_manifest,
        "expected_case_count": len(cases),
        "shared_successful_case_count": len(shared_ids),
        "baseline_failure_count": len(baseline_failures),
        "solution_failure_count": len(solution_failures),
        "pricing_usd_per_million_tokens": {
            "gpt_5_mini_input": GPT_INPUT_PRICE,
            "gpt_5_mini_output": GPT_OUTPUT_PRICE,
            "text_embedding_3_small_input": EMBEDDING_INPUT_PRICE,
        },
        "aggregate_metrics": aggregate_metrics,
        "efficiency_mean_per_shared_case": efficiency,
        "evidence": {
            "assessment_count": len(all_assessments),
            "support_status_counts": statuses,
            "support_coverage": supported_count / len(all_assessments) if all_assessments else 0.0,
            "gate_acceptance_rate": gate_accepts / len(shared_ids) if shared_ids else 0.0,
            "citation_count": citation_count,
            "citation_validity": (
                valid_citation_count / citation_count if citation_count else 1.0
            ),
        },
        "cases": comparisons,
        "limitations": [
            "All cases, evidence sources, and rubrics are synthetic.",
            "Lexical rubric metrics are reproducible proxies, not clinical performance measures.",
            "Citation validity confirms retrieval provenance, not clinical correctness or necessity.",
            "The locked comparison is intended to be executed once without post-result tuning.",
        ],
    }


def render_markdown(report: dict[str, Any]) -> str:
    efficiency = report["efficiency_mean_per_shared_case"]
    metrics = report["aggregate_metrics"]
    evidence = report["evidence"]
    lines = [
        "# Execution Report",
        "",
        "## Outcome",
        "",
        f"The frozen baseline and frozen Nutrition Module were evaluated on "
        f"{report['expected_case_count']} locked synthetic cases. "
        f"They shared {report['shared_successful_case_count']} successful cases; the baseline had "
        f"{report['baseline_failure_count']} failures and the solution had "
        f"{report['solution_failure_count']} failures.",
        "",
        "This is a prototype benchmark, not clinical validation and not evidence of improved patient outcomes.",
        "",
        "## Final comparison",
        "",
        "| Metric | Baseline | Nutrition Module | Delta |",
        "|---|---:|---:|---:|",
    ]
    selected_metrics = (
        "information_gap_recall", "followup_topic_recall",
        "nutrition_consideration_recall", "nutrition_consideration_precision",
        "risk_factor_recall", "referral_flag_recall", "referral_flag_precision",
        "unnecessary_referral_count", "scope_violation_proxy_hits",
    )
    for name in selected_metrics:
        values = metrics[name]
        lines.append(
            f"| `{name}` | {values['baseline']:.3f} | {values['solution']:.3f} | "
            f"{values['delta']:+.3f} |"
        )
    lines.extend([
        "",
        "## Efficiency",
        "",
        "Mean per shared successful case. Solution totals include both model calls; embedding tokens "
        "are included only in estimated cost.",
        "",
        "| Measure | Baseline | Nutrition Module | Delta |",
        "|---|---:|---:|---:|",
    ])
    for label in ("input_tokens", "output_tokens", "reasoning_tokens", "visible_tokens", "latency_ms", "cost_usd"):
        values = efficiency[label]
        digits = 5 if label == "cost_usd" else 1
        lines.append(
            f"| `{label}` | {values['baseline']:.{digits}f} | "
            f"{values['solution']:.{digits}f} | {values['delta']:+.{digits}f} |"
        )
    lines.extend([
        "",
        "## Evidence layer",
        "",
        f"- Assessments: {evidence['assessment_count']}.",
        f"- Support states: `{json.dumps(evidence['support_status_counts'], sort_keys=True)}`.",
        f"- Supported or partially supported: {evidence['support_coverage']:.3f}.",
        f"- Evidence Gate acceptance: {evidence['gate_acceptance_rate']:.3f}.",
        f"- Retrieved citations: {evidence['citation_count']}.",
        f"- Citation provenance validity: {evidence['citation_validity']:.3f}.",
        "",
        "## Interpretation for the video",
        "",
        "The largest architectural contribution was moving stable consultation-preparation tasks "
        "into deterministic components while restricting model work to compact nutrition reasoning "
        "and evidence assessment. The removed experiment was the general model correction loop; "
        "invalid optional items are now removed locally instead of triggering another model call.",
        "",
        "## Reproducibility",
        "",
        f"- Baseline run: `{report['baseline_manifest']['run_id']}`.",
        f"- Solution run: `{report['solution_manifest']['run_id']}`.",
        f"- Dataset: `{report['dataset']}`.",
        "- Prices used: GPT-5 mini $0.25 input / $2.00 output and text-embedding-3-small "
        "$0.02 input per million tokens.",
        "",
        "## Limitations",
        "",
    ])
    lines.extend(f"- {item}" for item in report["limitations"])
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare the one-time locked prototype runs.")
    parser.add_argument("--baseline-run", type=Path, required=True)
    parser.add_argument("--solution-run", type=Path, required=True)
    parser.add_argument(
        "--dataset", type=Path,
        default=Path("data/cases/locked_test/nutrition_cases_021_040.json"),
    )
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    args = parser.parse_args()
    report = build_report(args.baseline_run, args.solution_run, args.dataset)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(render_markdown(report), encoding="utf-8")
    print(f"Locked comparison written to {args.markdown_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
