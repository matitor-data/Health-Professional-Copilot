from __future__ import annotations

import json
import unittest
from pathlib import Path

from pydantic import ValidationError

from baseline.prompt import (
    AVAILABLE_PROMPT_VERSIONS,
    PROMPT_VERSION,
    SYSTEM_PROMPT,
    build_user_prompt,
    load_system_prompt,
)
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
        self.assertIn("at most 5 information_to_clarify", prompt)
        self.assertIn("between 3 and 5 suggested_questions", prompt)
        self.assertIn("every rationale must be one concise sentence", prompt)
        self.assertIn("do not expand an entire category of risks", prompt)
        self.assertIn("prioritize only information that could change", prompt)
        self.assertIn("never assume treatment duration, adherence", prompt)
        self.assertIn('distinguish "not reported"', prompt)
        self.assertIn("requires at least two specific supporting elements", prompt)
        self.assertIn("must describe exactly what was observed", prompt)
        self.assertEqual(PROMPT_VERSION, "nutrition-baseline-v3")

    def test_all_prompt_versions_are_loadable(self) -> None:
        self.assertEqual(len(AVAILABLE_PROMPT_VERSIONS), 3)
        for version in AVAILABLE_PROMPT_VERSIONS:
            self.assertIn("Stay within nutrition practice", load_system_prompt(version))
        self.assertEqual(
            "db7a6fc5c03cf83911914d0cc6effcb33cd50b61bc157e78f1640ca350e0273a",
            __import__("hashlib").sha256(load_system_prompt("nutrition-baseline-v1").encode()).hexdigest(),
        )

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
            suggested_questions=[
                BriefItem(topic="Question 1", rationale="Clarify the first relevant topic."),
                BriefItem(topic="Question 2", rationale="Clarify the second relevant topic."),
                BriefItem(topic="Question 3", rationale="Clarify the third relevant topic."),
            ],
            relevant_existing_labs=[ExistingLabSummary(reported_result=case.patient_intake.existing_labs[0])],
        )
        metrics = evaluate_case(case, brief)
        self.assertEqual(metrics["existing_lab_fidelity"], 1)
        self.assertEqual(metrics["supporting_evidence_count"], 0)

    def test_brief_enforces_output_budgets(self) -> None:
        item = BriefItem(topic="Topic", rationale="One concise rationale.")
        with self.assertRaises(ValidationError):
            BaselineBrief(
                patient_overview="Overview",
                information_to_clarify=[item] * 6,
                suggested_questions=[item] * 3,
            )
        with self.assertRaises(ValidationError):
            BaselineBrief(patient_overview="Overview", suggested_questions=[item] * 2)

    def test_dataset_is_valid_json(self) -> None:
        raw = json.loads(DATASET.read_text())
        self.assertEqual(raw["dataset_metadata"]["number_of_cases"], len(raw["cases"]))


if __name__ == "__main__":
    unittest.main()
