from __future__ import annotations

import json
import unittest
from pathlib import Path

from baseline.prompt import PROMPT_VERSION, SYSTEM_PROMPT, build_user_prompt
from baseline.runner import load_dataset
from baseline.schemas import BaselineBrief, BriefItem, ExistingLabSummary
from evaluation.metrics import evaluate_case


DATASET = Path("data/cases/locked_test/nutrition_cases_021_040.json")


class BaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dataset = load_dataset(DATASET)

    def test_dataset_contract(self) -> None:
        self.assertEqual(len(self.dataset.cases), 20)
        self.assertEqual(self.dataset.dataset_metadata.number_of_cases, 20)

    def test_prompt_contains_scope_guards(self) -> None:
        prompt = SYSTEM_PROMPT.lower()
        self.assertIn("never generate, infer, rank", prompt)
        self.assertIn("never recommend ordering new laboratory tests", prompt)
        self.assertIn("supporting_evidence must be empty", prompt)
        self.assertEqual(PROMPT_VERSION, "nutrition-baseline-v1")

    def test_user_prompt_contains_only_intake(self) -> None:
        case = self.dataset.cases[0]
        prompt = build_user_prompt(case.patient_intake)
        self.assertIn(case.patient_intake.reason_for_consultation, prompt)
        self.assertNotIn("expected_information_gaps", prompt)

    def test_metric_evaluation_and_lab_fidelity(self) -> None:
        case = self.dataset.cases[1]
        brief = BaselineBrief(
            patient_overview="Nutrition consultation preparation.",
            information_to_clarify=[BriefItem(topic="HbA1c result", rationale="Actual value is unavailable")],
            relevant_existing_labs=[ExistingLabSummary(reported_result=case.patient_intake.existing_labs[0])],
        )
        metrics = evaluate_case(case, brief)
        self.assertEqual(metrics["existing_lab_fidelity"], 1)
        self.assertEqual(metrics["supporting_evidence_count"], 0)

    def test_dataset_is_valid_json(self) -> None:
        raw = json.loads(DATASET.read_text())
        self.assertEqual(raw["dataset_metadata"]["number_of_cases"], len(raw["cases"]))


if __name__ == "__main__":
    unittest.main()
