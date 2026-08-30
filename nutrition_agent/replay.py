from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from baseline.runner import load_dataset
from evaluation.metrics import aggregate_metrics, evaluate_case
from nutrition_agent.patient_state import build_patient_state
from nutrition_agent.pipeline import build_brief
from nutrition_agent.referrals import evaluate_referral_eligibility
from nutrition_agent.schemas import CompactReasoningResult


def main() -> int:
    parser = argparse.ArgumentParser(description="Replay a compact agent run through deterministic gates")
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument(
        "--referral-rubric", type=Path,
        default=Path("data/cases/development/referral_pathways_v1.json"),
    )
    args = parser.parse_args()
    source_manifest = json.loads((args.source_run / "manifest.json").read_text())
    dataset = load_dataset(Path(source_manifest["dataset"]))
    cases = {case.case_id: case for case in dataset.cases}
    rubric = json.loads(args.referral_rubric.read_text())
    source_rows = [json.loads(line) for line in (args.source_run / "outputs.jsonl").read_text().splitlines()]
    rows, metric_rows = [], []
    for source in source_rows:
        case = cases[source["case_id"]]
        state = build_patient_state(case.patient_intake)
        decisions = evaluate_referral_eligibility(case.patient_intake)
        draft = CompactReasoningResult.model_validate(source["draft"])
        brief, report = build_brief(case.patient_intake, state, draft, decisions)
        metrics = evaluate_case(case, brief)
        expected = rubric["cases"][case.case_id]
        actual = {"supported": "refer", "clarify_first": "clarify_first", "not_indicated": "none"}[
            decisions[0].eligibility
        ]
        metrics.update({
            "referral_supported_count": int(actual == "refer"),
            "referral_clarify_first_count": int(actual == "clarify_first"),
            "referral_pathway_accuracy": int(actual == expected),
            "clarify_first_case_accuracy": int((actual == "clarify_first") == (expected == "clarify_first")),
            "supported_referral_case_accuracy": int((actual == "refer") == (expected == "refer")),
        })
        metric_rows.append(metrics)
        rows.append({
            **source, "brief": brief.model_dump(mode="json"), "metrics": metrics,
            "patient_state": state.model_dump(mode="json"),
            "safety_reports": [report.model_dump(mode="json")],
            "referral_decisions": [decision.model_dump(mode="json") for decision in decisions],
        })
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output = args.output_root / run_id
    output.mkdir(parents=True, exist_ok=False)
    manifest = {
        **source_manifest, "run_id": run_id, "created_at": datetime.now(UTC).isoformat(),
        "replayed_from_run": source_manifest["run_id"],
        "deterministic_pipeline_replay": True,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (output / "outputs.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows))
    (output / "failures.jsonl").write_text("")
    (output / "metrics.json").write_text(json.dumps(aggregate_metrics(metric_rows), indent=2) + "\n")
    print(f"Replayed {len(rows)} cases to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
