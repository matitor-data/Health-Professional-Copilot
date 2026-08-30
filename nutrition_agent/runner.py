from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv

from baseline.runner import DEFAULT_DATASET, load_dataset, sha256
from evaluation.metrics import aggregate_metrics, evaluate_case
from nutrition_agent.client import OpenAINutritionAgent
from nutrition_agent.patient_state import build_patient_state
from nutrition_agent.prompt import COMPACT_SYSTEM_PROMPT, PROMPT_VERSION

DEFAULT_REFERRAL_RUBRIC = Path("data/cases/development/referral_pathways_v1.json")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Nutrition Reasoning Agent")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-5-mini"))
    parser.add_argument("--case-id", action="append")
    parser.add_argument("--output-root", type=Path, default=Path("evaluation/agent_runs"))
    parser.add_argument("--referral-rubric", type=Path, default=DEFAULT_REFERRAL_RUBRIC)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = parse_args(argv)
    dataset = load_dataset(args.dataset)
    pathway_rubric = (
        json.loads(args.referral_rubric.read_text(encoding="utf-8"))
        if args.referral_rubric.is_file() else {"rubric_version": None, "cases": {}}
    )
    selected = [case for case in dataset.cases if not args.case_id or case.case_id in args.case_id]
    if args.case_id and len(selected) != len(set(args.case_id)):
        available = {case.case_id for case in dataset.cases}
        raise SystemExit(f"Unknown case IDs: {', '.join(sorted(set(args.case_id) - available))}")
    if args.dry_run:
        for case in selected:
            build_patient_state(case.patient_intake)
        print(f"Validated {len(selected)} cases for {PROMPT_VERSION} from {args.dataset}")
        return 0

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    agent = OpenAINutritionAgent(args.model)
    rows: list[dict[str, object]] = []
    metric_rows: list[dict[str, float | int]] = []
    failures: list[dict[str, str]] = []
    for case in selected:
        try:
            result = agent.generate(case.patient_intake)
            metrics = evaluate_case(case, result.brief)
            metrics.update({
                "referral_supported_count": sum(
                    decision.eligibility == "supported" for decision in result.referral_decisions
                ),
                "referral_clarify_first_count": sum(
                    decision.eligibility == "clarify_first" for decision in result.referral_decisions
                ),
            })
            expected_pathway = pathway_rubric["cases"].get(case.case_id)
            actual_pathway = {
                "supported": "refer", "clarify_first": "clarify_first",
                "not_indicated": "none",
            }[result.referral_decisions[0].eligibility]
            if expected_pathway is not None:
                metrics.update({
                    "referral_pathway_accuracy": int(actual_pathway == expected_pathway),
                    "clarify_first_case_accuracy": int(
                        (expected_pathway == "clarify_first") == (actual_pathway == "clarify_first")
                    ),
                    "supported_referral_case_accuracy": int(
                        (expected_pathway == "refer") == (actual_pathway == "refer")
                    ),
                })
            metric_rows.append(metrics)
            rows.append({
                "case_id": case.case_id,
                "brief": result.brief.model_dump(mode="json"),
                "metrics": metrics,
                "patient_state": result.patient_state.model_dump(mode="json"),
                "draft": result.draft.model_dump(mode="json"),
                "safety_reports": [report.model_dump(mode="json") for report in result.safety_reports],
                "referral_decisions": [
                    decision.model_dump(mode="json") for decision in result.referral_decisions
                ],
                "response_ids": result.response_ids,
                "retries": result.retries,
                "latency_ms": result.latency_ms,
                "input_tokens": result.input_tokens,
                "output_tokens": result.output_tokens,
                "reasoning_tokens": result.reasoning_tokens,
                "visible_output_tokens": result.visible_output_tokens,
            })
            print(f"Completed {case.case_id}: {result.retries} retries", flush=True)
        except Exception as exc:
            failures.append({"case_id": case.case_id, "error": f"{type(exc).__name__}: {exc}"})
            print(f"Failed {case.case_id}: {type(exc).__name__}", flush=True)
    manifest = {
        "run_id": run_id, "created_at": datetime.now(UTC).isoformat(), "model": args.model,
        "prompt_version": PROMPT_VERSION,
        "prompt_sha256": hashlib.sha256(COMPACT_SYSTEM_PROMPT.encode()).hexdigest(),
        "dataset": str(args.dataset), "dataset_sha256": sha256(args.dataset),
        "referral_rubric": str(args.referral_rubric) if args.referral_rubric.is_file() else None,
        "referral_rubric_version": pathway_rubric["rubric_version"],
        "referral_rubric_sha256": sha256(args.referral_rubric) if args.referral_rubric.is_file() else None,
        "selected_cases": [case.case_id for case in selected], "max_retries": 0,
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "outputs.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    (run_dir / "failures.jsonl").write_text("".join(json.dumps(row) + "\n" for row in failures), encoding="utf-8")
    (run_dir / "metrics.json").write_text(json.dumps(aggregate_metrics(metric_rows), indent=2) + "\n", encoding="utf-8")
    print(f"Agent run written to {run_dir}: {len(rows)} succeeded, {len(failures)} failed")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
