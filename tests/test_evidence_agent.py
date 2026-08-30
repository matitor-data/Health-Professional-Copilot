from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from baseline.schemas import BaselineBrief, BriefItem, NutritionConsideration
from evidence_agent.agent_schemas import EvidenceAssessmentBundle, EvidenceAssessmentDraft
from evidence_agent.gate import validate_and_finalize
from evidence_agent.metrics import build_report
from evidence_agent.pipeline import enrich_brief, render_supporting_evidence
from evidence_agent.prompt import build_evidence_prompt
from evidence_agent.schemas import RetrievalResult


def consideration(topic: str = "Assess sodium intake") -> NutritionConsideration:
    return NutritionConsideration(
        topic=topic,
        rationale="Known CKD makes reported sodium sources relevant to this consultation.",
        source_patient_fields=["known_diagnoses"],
    )


def retrieval(chunk_id: str = "synthetic_ckd_sodium_v1:evidence-statements") -> RetrievalResult:
    return RetrievalResult(
        chunk_id=chunk_id,
        source_id="synthetic_ckd_sodium_v1",
        title="Sodium Assessment in Known Chronic Kidney Disease",
        section="Evidence statements",
        text="Sodium intake can be relevant when chronic kidney disease is known.",
        score=0.8,
        matched_terms=[],
        retrieval_methods=["embedding"],
        content_sha256="a" * 64,
    )


class EvidenceAgentTests(unittest.TestCase):
    def test_frozen_agent_matches_component_hashes(self) -> None:
        manifest = json.loads(Path("evidence_agent/frozen_agent.json").read_text())
        self.assertEqual(manifest["status"], "frozen")
        for path, expected_hash in manifest["component_files"].items():
            actual_hash = hashlib.sha256(Path(path).read_bytes()).hexdigest()
            self.assertEqual(actual_hash, expected_hash, path)

    def test_gate_accepts_retrieved_citation(self) -> None:
        item = consideration()
        result = retrieval()
        draft = EvidenceAssessmentBundle(assessments=[EvidenceAssessmentDraft(
            consideration_id="NC-01",
            support_status="supported",
            evidence_refs=[result.chunk_id],
            rationale="The retrieved chunk supports assessing sodium sources in known CKD.",
            limitations=["Individual targets require existing renal instructions."],
        )])
        assessments, report = validate_and_finalize(
            [("NC-01", item)], {"NC-01": [result]}, draft,
        )
        self.assertTrue(report.accepted)
        self.assertEqual(assessments[0].support_status, "supported")
        self.assertEqual(assessments[0].evidence_refs, [result.chunk_id])

    def test_gate_downgrades_invented_citation(self) -> None:
        draft = EvidenceAssessmentBundle(assessments=[EvidenceAssessmentDraft(
            consideration_id="NC-01", support_status="supported",
            evidence_refs=["invented:chunk"], rationale="Claimed support.", limitations=[],
        )])
        assessments, report = validate_and_finalize(
            [("NC-01", consideration())], {"NC-01": [retrieval()]}, draft,
        )
        self.assertFalse(report.accepted)
        self.assertEqual(assessments[0].support_status, "unsupported")
        self.assertEqual(assessments[0].evidence_refs, [])
        self.assertEqual(
            {violation.rule for violation in report.violations},
            {"INVALID_EVIDENCE_REF", "SUPPORT_WITHOUT_EVIDENCE"},
        )

    def test_gate_owns_empty_retrieval_status(self) -> None:
        assessments, report = validate_and_finalize(
            [("NC-01", consideration())], {"NC-01": []}, None,
        )
        self.assertEqual(assessments[0].support_status, "retrieval_failed")
        self.assertEqual(assessments[0].evidence_refs, [])
        self.assertEqual(report.violations[0].rule, "RETRIEVAL_EMPTY")
        self.assertTrue(report.accepted)

    def test_gate_distinguishes_outside_collection_from_retrieval_failure(self) -> None:
        assessments, report = validate_and_finalize(
            [("NC-01", consideration("Assess swallowing difficulty"))],
            {"NC-01": []}, None, {"NC-01": False},
        )
        self.assertEqual(assessments[0].support_status, "outside_source_scope")
        self.assertTrue(report.accepted)

    def test_gate_fills_missing_assessment(self) -> None:
        assessments, report = validate_and_finalize(
            [("NC-01", consideration())], {"NC-01": [retrieval()]},
            EvidenceAssessmentBundle(assessments=[]),
        )
        self.assertEqual(assessments[0].support_status, "unsupported")
        self.assertEqual(report.violations[0].rule, "MISSING_ASSESSMENT")

    def test_prompt_contains_only_packet_chunks(self) -> None:
        result = retrieval()
        prompt = build_evidence_prompt(
            [("NC-01", consideration())], {"NC-01": [result]},
        )
        self.assertIn(result.chunk_id, prompt)
        self.assertIn(result.text, prompt)
        self.assertNotIn("https://", prompt)

    def test_renderer_includes_only_supported_assessments(self) -> None:
        item = consideration()
        result = retrieval()
        supported, _ = validate_and_finalize(
            [("NC-01", item)], {"NC-01": [result]},
            EvidenceAssessmentBundle(assessments=[EvidenceAssessmentDraft(
                consideration_id="NC-01", support_status="supported",
                evidence_refs=[result.chunk_id], rationale="The source supports this assessment.",
                limitations=[],
            )]),
        )
        self.assertEqual(len(render_supporting_evidence(supported)), 1)
        brief = BaselineBrief(
            patient_overview="Preparation.",
            suggested_questions=[
                BriefItem(topic=f"Question {index}", rationale="Clarify the case.")
                for index in range(1, 4)
            ],
            nutrition_considerations=[item],
        )
        enriched = enrich_brief(brief, supported)
        self.assertEqual(len(enriched.supporting_evidence), 1)
        self.assertEqual(enriched.nutrition_considerations, brief.nutrition_considerations)

    def test_development_measurements_are_bounded(self) -> None:
        report = build_report([
            Path("evaluation/evidence_agent_runs/20260830T052956Z"),
            Path("evaluation/evidence_agent_runs/20260830T053131Z"),
        ])
        for metrics in report["runs"].values():
            for name in (
                "gate_acceptance_rate", "retrieval_coverage", "evidence_support_coverage",
                "citation_validity", "single_citation_proxy", "eligible_render_fidelity",
                "ineligible_exclusion_fidelity",
            ):
                self.assertGreaterEqual(metrics[name], 0.0)
                self.assertLessEqual(metrics[name], 1.0)
        self.assertEqual(report["stability"]["common_case_count"], 10)

    def test_evidence_rubric_matches_fixed_reference_briefs(self) -> None:
        report = build_report(
            [Path("evaluation/evidence_agent_runs/20260830T053131Z")],
            Path("data/evaluations/evidence_agent/evidence_assessment_rubric_v1.json"),
        )
        metrics = report["rubric_evaluation"]["20260830T053131Z"]
        self.assertEqual(metrics["expected_assessment_count"], 20)
        self.assertEqual(metrics["missing_assessment_count"], 0)
        self.assertEqual(metrics["unexpected_assessment_count"], 0)


if __name__ == "__main__":
    unittest.main()
