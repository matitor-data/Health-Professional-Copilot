from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evaluation.compare import compare_runs, render_markdown


class CompareTests(unittest.TestCase):
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
                "latency_ms": 40000, "metrics": {"referral_flag_recall": 1.0},
                "brief": {field: [1, 2] for field in (
                    "information_to_clarify", "suggested_questions", "nutrition_considerations",
                    "nutritional_risk_factors", "referral_escalation_flags", "potential_blind_spots"
                )},
            }
            candidate_row = json.loads(json.dumps(base_row))
            candidate_row.update({"output_tokens": 1000, "latency_ms": 20000})
            (before / "outputs.jsonl").write_text(json.dumps(base_row) + "\n")
            (after / "outputs.jsonl").write_text(json.dumps(candidate_row) + "\n")
            report = compare_runs(before, after)
            delta = report["cases"][0]["delta"]
            self.assertEqual(delta["output_tokens"], -2000)
            self.assertEqual(delta["latency_ms"], -20000)
            self.assertEqual(delta["visible_output"]["characters"], 0)
            self.assertIn("case_021", render_markdown(report))


if __name__ == "__main__":
    unittest.main()
