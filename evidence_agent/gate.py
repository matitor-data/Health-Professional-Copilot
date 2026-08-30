from __future__ import annotations

from baseline.schemas import NutritionConsideration
from evidence_agent.agent_schemas import (
    EvidenceAssessment, EvidenceAssessmentBundle, EvidenceGateReport, EvidenceGateViolation,
)
from evidence_agent.schemas import RetrievalResult


def validate_and_finalize(
    considerations: list[tuple[str, NutritionConsideration]],
    retrievals: dict[str, list[RetrievalResult]],
    draft: EvidenceAssessmentBundle | None,
    collection_coverage: dict[str, bool] | None = None,
) -> tuple[list[EvidenceAssessment], EvidenceGateReport]:
    expected = {consideration_id: consideration for consideration_id, consideration in considerations}
    violations: list[EvidenceGateViolation] = []
    drafts = draft.assessments if draft else []
    by_id = {}
    for item in drafts:
        if item.consideration_id not in expected:
            violations.append(EvidenceGateViolation(
                rule="UNKNOWN_CONSIDERATION_ID", consideration_id=item.consideration_id,
                message="The model returned an ID that was not requested.",
            ))
            continue
        if item.consideration_id in by_id:
            violations.append(EvidenceGateViolation(
                rule="DUPLICATE_CONSIDERATION_ID", consideration_id=item.consideration_id,
                message="Only the first assessment for this consideration was retained.",
            ))
            continue
        by_id[item.consideration_id] = item

    assessments: list[EvidenceAssessment] = []
    for consideration_id, consideration in considerations:
        retrieved = retrievals.get(consideration_id, [])
        allowed_refs = {result.chunk_id for result in retrieved}
        item = by_id.get(consideration_id)
        if not retrieved:
            covered = (collection_coverage or {}).get(consideration_id, True)
            violations.append(EvidenceGateViolation(
                rule="RETRIEVAL_EMPTY", consideration_id=consideration_id,
                message="No approved evidence chunk passed retrieval thresholds.",
            ))
            assessments.append(EvidenceAssessment(
                consideration_id=consideration_id, consideration=consideration.topic,
                support_status="retrieval_failed" if covered else "outside_source_scope",
                evidence_refs=[],
                rationale=(
                    "No approved source was retrieved for a topic represented in the collection."
                    if covered else "The approved prototype collection does not cover this topic."
                ),
                limitations=["Absence of evidence in this collection does not prove the consideration is false."],
            ))
            continue
        if item is None:
            violations.append(EvidenceGateViolation(
                rule="MISSING_ASSESSMENT", consideration_id=consideration_id,
                message="The model omitted a requested consideration.",
            ))
            assessments.append(EvidenceAssessment(
                consideration_id=consideration_id, consideration=consideration.topic,
                support_status="unsupported", evidence_refs=[],
                rationale="The model did not return a valid evidence assessment.", limitations=[],
            ))
            continue
        valid_refs = list(dict.fromkeys(ref for ref in item.evidence_refs if ref in allowed_refs))
        if any(ref not in allowed_refs for ref in item.evidence_refs):
            violations.append(EvidenceGateViolation(
                rule="INVALID_EVIDENCE_REF", consideration_id=consideration_id,
                message="One or more citations were not present in retrieved evidence and were removed.",
            ))
        status = item.support_status
        rationale = item.rationale
        if status in {"supported", "partially_supported"} and not valid_refs:
            violations.append(EvidenceGateViolation(
                rule="SUPPORT_WITHOUT_EVIDENCE", consideration_id=consideration_id,
                message="A supported status without a valid retrieved citation was downgraded.",
            ))
            status = "unsupported"
            rationale = "The claimed support did not include a valid retrieved evidence reference."
        assessments.append(EvidenceAssessment(
            consideration_id=consideration_id, consideration=consideration.topic,
            support_status=status, evidence_refs=valid_refs,
            rationale=rationale, limitations=item.limitations,
        ))
    blocking_rules = {
        "DUPLICATE_CONSIDERATION_ID", "UNKNOWN_CONSIDERATION_ID", "MISSING_ASSESSMENT",
        "INVALID_EVIDENCE_REF", "SUPPORT_WITHOUT_EVIDENCE",
    }
    return assessments, EvidenceGateReport(
        accepted=not any(violation.rule in blocking_rules for violation in violations),
        violations=violations,
    )
