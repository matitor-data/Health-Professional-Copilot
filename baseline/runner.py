from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv

from baseline.client import OpenAIBaselineClient
from baseline.prompt import (
    AVAILABLE_PROMPT_VERSIONS,
    PROMPT_VERSION,
    build_user_prompt,
    load_system_prompt,
)
from baseline.schemas import EvaluationDataset
from evaluation.metrics import aggregate_metrics, evaluate_case

DEFAULT_DATASET = Path("data/cases/locked_test/nutrition_cases_021_040.json")


def load_dataset(path: Path) -> EvaluationDataset:
    return EvaluationDataset.model_validate_json(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the single-call Nutrition Module baseline")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-5-mini"))
    parser.add_argument(
        "--prompt-version",
        choices=AVAILABLE_PROMPT_VERSIONS,
        default=PROMPT_VERSION,
    )
    parser.add_argument("--case-id", action="append", help="Run only this case; repeatable")
    parser.add_argument("--output-root", type=Path, default=Path("evaluation/runs"))
    parser.add_argument("--dry-run", action="store_true", help="Validate data and prompts without calling the API")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = parse_args(argv)
    system_prompt = load_system_prompt(args.prompt_version)
    dataset = load_dataset(args.dataset)
    selected = [case for case in dataset.cases if not args.case_id or case.case_id in args.case_id]
    if args.case_id and len(selected) != len(set(args.case_id)):
        available = {case.case_id for case in dataset.cases}
        missing = sorted(set(args.case_id) - available)
        raise SystemExit(f"Unknown case IDs: {', '.join(missing)}")

    if args.dry_run:
        for case in selected:
            build_user_prompt(case.patient_intake)
        print(f"Validated {len(selected)} cases from {args.dataset}")
        print(f"Prompt version: {args.prompt_version}")
        return 0

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    client = OpenAIBaselineClient(args.model, system_prompt=system_prompt)
    rows: list[dict[str, object]] = []
    metric_rows: list[dict[str, float | int]] = []
    failures: list[dict[str, str]] = []

    for case in selected:
        try:
            result = client.generate(case.patient_intake)
            metrics = evaluate_case(case, result.brief)
            metric_rows.append(metrics)
            rows.append({
                "case_id": case.case_id,
                "brief": result.brief.model_dump(mode="json"),
                "metrics": metrics,
                "response_id": result.response_id,
                "latency_ms": result.latency_ms,
                "input_tokens": result.input_tokens,
                "output_tokens": result.output_tokens,
                "reasoning_tokens": result.reasoning_tokens,
                "visible_output_tokens": result.visible_output_tokens,
            })
        except Exception as exc:
            failures.append({"case_id": case.case_id, "error": f"{type(exc).__name__}: {exc}"})

    manifest = {
        "run_id": run_id,
        "created_at": datetime.now(UTC).isoformat(),
        "model": args.model,
        "prompt_version": args.prompt_version,
        "prompt_sha256": hashlib.sha256(system_prompt.encode()).hexdigest(),
        "dataset": str(args.dataset),
        "dataset_sha256": sha256(args.dataset),
        "selected_cases": [case.case_id for case in selected],
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "outputs.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    (run_dir / "failures.jsonl").write_text("".join(json.dumps(row) + "\n" for row in failures), encoding="utf-8")
    (run_dir / "metrics.json").write_text(json.dumps(aggregate_metrics(metric_rows), indent=2) + "\n", encoding="utf-8")
    print(f"Run written to {run_dir}: {len(rows)} succeeded, {len(failures)} failed")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
