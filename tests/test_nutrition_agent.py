from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from baseline.runner import load_dataset
from baseline.schemas import ExistingLabSummary
from nutrition_agent.patient_state import build_patient_state
from nutrition_agent.pipeline import build_brief
from nutrition_agent.prompt import COMPACT_SYSTEM_PROMPT, PROMPT_VERSION
from nutrition_agent.render import render_brief
from nutrition_agent.referrals import apply_referral_decisions, evaluate_referral_eligibility
from nutrition_agent.safety import drop_unsafe_items, validate_draft
from nutrition_agent.schemas import (
    CompactItem, CompactReasoningResult, NutritionReasoningResult, NutritionSignal,
    ReasonedItem, ReasonedRisk, ReferralCandidate,
)
from nutrition_agent.source_refs import resolve_source_ref


DATASET = Path("data/cases/development/nutrition_cases_dev.json")


def question(number: int) -> ReasonedItem:
    return ReasonedItem(
        statement=f"Question {number}", rationale="This clarifies consultation preparation.",
        source_patient_fields=[], supporting_patient_facts=[], confidence="high",
    )


class NutritionAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = {case.case_id: case for case in load_dataset(DATASET).cases}

    def test_patient_state_marks_missing_and_derives_bmi(self) -> None:
        state = build_patient_state(self.cases["dev_008"].patient_intake)
        fields = {field.field: field for field in state.fields}
        self.assertEqual(fields["dietary_pattern"].status, "not_reported")
        self.assertNotIn("bmi", state.derived_values)
        complete = build_patient_state(self.cases["dev_001"].patient_intake)
        self.assertEqual(complete.derived_values["bmi_status"], "derived_not_diagnostic")

    def test_patient_state_detects_contradictions(self) -> None:
        state = build_patient_state(self.cases["dev_009"].patient_intake)
        self.assertEqual(len(state.contradictions), 2)
        self.assertEqual(
            {field.field: field.status for field in state.fields}["recent_weight_change"],
            "contradictory",
        )

    def test_safety_gate_accepts_grounded_draft(self) -> None:
        patient = self.cases["dev_004"].patient_intake
        draft = NutritionReasoningResult(
            patient_overview="Preparation for a nutrition consultation.",
            suggested_questions=[question(1), question(2), question(3)],
            nutrition_considerations=[ReasonedItem(
                statement="Current intake may be limited by difficulty with solid foods.",
                rationale="The reported diet relies on liquids because solid foods are difficult.",
                source_patient_fields=["dietary_pattern"],
                supporting_patient_facts=[patient.dietary_pattern], confidence="high",
            )],
            referral_candidates=[ReferralCandidate(
                statement="Food feels stuck with rapid unintentional weight loss.",
                rationale="These observed facts warrant medical assessment outside nutrition scope.",
                source_patient_fields=["symptoms", "recent_weight_change"],
                supporting_patient_facts=[patient.symptoms[0], patient.recent_weight_change or ""],
                confidence="high", urgency="prompt",
                recommendation="Seek prompt medical evaluation.",
            )],
        )
        report = validate_draft(patient, draft)
        self.assertTrue(report.accepted, report.model_dump())
        rendered_referral = render_brief(draft).referral_escalation_flags[0]
        self.assertEqual(rendered_referral.trigger, "; ".join(draft.referral_candidates[0].supporting_patient_facts))
        self.assertEqual(rendered_referral.recommendation, "Seek prompt medical evaluation.")

    def test_safety_gate_drops_unsafe_item_and_restores_labs(self) -> None:
        patient = self.cases["dev_003"].patient_intake
        draft = NutritionReasoningResult(
            patient_overview="Preparation.",
            suggested_questions=[question(1), question(2), question(3)],
            nutritional_risk_factors=[ReasonedRisk(
                statement="Diagnose diabetes and change medication dose.",
                rationale="This exceeds the nutrition scope.", source_patient_fields=["unknown"],
                supporting_patient_facts=["invented fact"], confidence="low", priority="high",
            )],
            relevant_existing_labs=[ExistingLabSummary(reported_result="Altered value")],
        )
        report = validate_draft(patient, draft)
        self.assertFalse(report.accepted)
        cleaned = drop_unsafe_items(patient, draft, report)
        self.assertEqual(cleaned.nutritional_risk_factors, [])
        self.assertEqual(
            [lab.reported_result for lab in cleaned.relevant_existing_labs], patient.existing_labs
        )

    def test_referral_gate_blocks_negative_controls(self) -> None:
        for case_id in ("dev_001", "dev_003", "dev_006", "dev_010"):
            decisions = evaluate_referral_eligibility(self.cases[case_id].patient_intake)
            self.assertEqual(decisions[0].eligibility, "not_indicated", case_id)

    def test_referral_gate_supports_observed_red_flags(self) -> None:
        self.assertEqual(
            evaluate_referral_eligibility(self.cases["dev_004"].patient_intake)[0].eligibility,
            "supported",
        )
        decision = evaluate_referral_eligibility(self.cases["dev_005"].patient_intake)[0]
        self.assertEqual(decision.eligibility, "supported")
        self.assertEqual(decision.urgency, "urgent")

    def test_referral_gate_converts_contradiction_to_question(self) -> None:
        decision = evaluate_referral_eligibility(self.cases["dev_009"].patient_intake)[0]
        self.assertEqual(decision.eligibility, "clarify_first")
        draft = NutritionReasoningResult(
            patient_overview="Preparation.",
            suggested_questions=[question(1), question(2), question(3)],
        )
        updated = apply_referral_decisions(draft, [decision])
        self.assertEqual(updated.referral_candidates, [])
        self.assertIn("stable weight", updated.suggested_questions[0].statement)

    def test_compact_source_references(self) -> None:
        patient = self.cases["dev_005"].patient_intake
        self.assertEqual(resolve_source_ref(patient, "symptoms[0]"), ("symptoms", "repeated vomiting"))
        self.assertIsNone(resolve_source_ref(patient, "symptoms[99]"))
        self.assertIsNone(resolve_source_ref(patient, "bmi"))

    def test_compact_pipeline_builds_deterministic_sections(self) -> None:
        patient = self.cases["dev_004"].patient_intake
        state = build_patient_state(patient)
        decisions = evaluate_referral_eligibility(patient)
        compact = CompactReasoningResult(
            nutrition_signals=[NutritionSignal(
                category="symptom_related_intake",
                source_refs=["symptoms[0]", "dietary_pattern"],
                consultation_impact="Swallowing difficulty currently limits solid-food intake.",
            )],
            nutrition_considerations=[CompactItem(
                statement="Current intake may be inadequate because solid foods are difficult.",
                rationale="The reported swallowing difficulty and liquid diet can change nutrition preparation.",
                source_refs=["symptoms[0]", "dietary_pattern"],
            )],
        )
        brief, report = build_brief(patient, state, compact, decisions)
        self.assertTrue(report.accepted)
        self.assertGreaterEqual(len(brief.suggested_questions), 3)
        self.assertEqual(brief.known_medical_context, [])
        self.assertEqual(len(brief.referral_escalation_flags), 1)
        self.assertIn(patient.symptoms[0], brief.referral_escalation_flags[0].trigger)

    def test_compact_pipeline_removes_invalid_refs_without_retry(self) -> None:
        patient = self.cases["dev_010"].patient_intake
        compact = CompactReasoningResult(nutrition_considerations=[CompactItem(
            statement="Unsupported consideration.", rationale="This should be removed.",
            source_refs=["bmi"],
        )])
        brief, report = build_brief(
            patient, build_patient_state(patient), compact,
            evaluate_referral_eligibility(patient),
        )
        self.assertNotIn(
            "Unsupported consideration.",
            [item.topic for item in brief.nutrition_considerations],
        )
        self.assertEqual(report.violations[0].rule, "INVALID_OR_EMPTY_SOURCE_REF")

    def test_frozen_agent_matches_component_hashes(self) -> None:
        frozen = json.loads(Path("nutrition_agent/frozen_agent.json").read_text())
        self.assertEqual(frozen["status"], "frozen")
        self.assertEqual(frozen["agent_version"], PROMPT_VERSION)
        self.assertEqual(
            frozen["effective_prompt_sha256"],
            hashlib.sha256(COMPACT_SYSTEM_PROMPT.encode()).hexdigest(),
        )
        for path, expected_hash in frozen["component_files"].items():
            self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(), expected_hash, path)
        self.assertEqual(
            frozen["reference_api_run"]["output_tokens"],
            frozen["reference_api_run"]["reasoning_tokens"]
            + frozen["reference_api_run"]["visible_output_tokens"],
        )


if __name__ == "__main__":
    unittest.main()
