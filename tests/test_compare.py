from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evaluation.compare import compare_runs, render_markdown
from evaluation.locked_compare import build_report as build_locked_report


class CompareTests(unittest.TestCase):
    def test_locked_comparator_on_versioned_locked_runs(self) -> None:
        report = build_locked_report(
            Path("evaluation/locked_runs/baseline/20260830T155457Z"),
            Path("evaluation/locked_runs/solution/20260830T161328Z"),
            Path("data/cases/locked_test/nutrition_cases_021_040.json"),
        )
        self.assertEqual(report["shared_successful_case_count"], 20)
        self.assertEqual(report["baseline_failure_count"], 0)
        self.assertEqual(report["solution_failure_count"], 0)
        self.assertEqual(report["evidence"]["citation_validity"], 1.0)

    def test_compare_runs(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            before, after = root / "before", root / "after"
            before.mkdir(); after.mkdir()
            for directory, run_id, version in [
                (before, "run-v1", "nutrition-baseline-v1"),
                (after, "run-v3", "nutrition-baseline-v3"),
            ]:
                (directory / "manifest.json").write_text(json.dumps({
                    "run_id": run_id, "prompt_version": version, "model": "gpt-5-mini"
                }))
            base_row = {
                "case_id": "case_021", "input_tokens": 1000, "output_tokens": 3000,
                "reasoning_tokens": 2000, "visible_output_tokens": 1000,
                "latency_ms": 40000, "metrics": {"referral_flag_recall": 1.0},
                "brief": {field: [1, 2] for field in (
                    "information_to_clarify", "suggested_questions", "nutrition_considerations",
                    "nutritional_risk_factors", "referral_escalation_flags", "potential_blind_spots"
                )},
            }
            candidate_row = json.loads(json.dumps(base_row))
            candidate_row.update({
                "output_tokens": 1000, "reasoning_tokens": 400,
                "visible_output_tokens": 600, "latency_ms": 20000,
            })
            (before / "outputs.jsonl").write_text(json.dumps(base_row) + "\n")
            (after / "outputs.jsonl").write_text(json.dumps(candidate_row) + "\n")
            report = compare_runs(before, after)
            delta = report["cases"][0]["delta"]
            self.assertEqual(delta["output_tokens"], -2000)
            self.assertEqual(delta["reasoning_tokens"], -1600)
            self.assertEqual(delta["visible_output_tokens"], -400)
            self.assertEqual(delta["latency_ms"], -20000)
            self.assertEqual(delta["visible_output"]["characters"], 0)
            self.assertIn("case_021", render_markdown(report))


if __name__ == "__main__":
    unittest.main()
