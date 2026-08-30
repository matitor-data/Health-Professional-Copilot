from __future__ import annotations

from baseline.schemas import (
    BaselineBrief,
    BriefItem,
    NutritionConsideration,
    NutritionalRiskFactor,
    ReferralEscalationFlag,
)
from nutrition_agent.schemas import NutritionReasoningResult


def render_brief(draft: NutritionReasoningResult) -> BaselineBrief:
    referral_recommendations = {
        "routine": "Seek appropriate routine medical evaluation.",
        "prompt": "Seek prompt medical evaluation.",
        "urgent": "Seek urgent medical evaluation.",
    }
    return BaselineBrief(
        patient_overview=draft.patient_overview,
        known_medical_context=draft.known_medical_context,
        information_to_clarify=[
            BriefItem(topic=item.statement, rationale=item.rationale, source_patient_fields=item.source_patient_fields)
            for item in draft.information_gaps
        ],
        suggested_questions=[
            BriefItem(topic=item.statement, rationale=item.rationale, source_patient_fields=item.source_patient_fields)
            for item in draft.suggested_questions
        ],
        nutrition_considerations=[
            NutritionConsideration(
                topic=item.statement, rationale=item.rationale,
                source_patient_fields=item.source_patient_fields,
                limiting_or_missing_facts=[],
            ) for item in draft.nutrition_considerations
        ],
        nutritional_risk_factors=[
            NutritionalRiskFactor(
                factor=item.statement, rationale=item.rationale, priority=item.priority,
                source_patient_fields=item.source_patient_fields,
            ) for item in draft.nutritional_risk_factors
        ],
        referral_escalation_flags=[
            ReferralEscalationFlag(
                trigger="; ".join(item.supporting_patient_facts),
                rationale="These reported observations may require medical assessment beyond nutrition scope.",
                urgency=item.urgency,
                recommendation=referral_recommendations[item.urgency],
                source_patient_fields=item.source_patient_fields,
            ) for item in draft.referral_candidates
        ],
        potential_blind_spots=[
            BriefItem(topic=item.statement, rationale=item.rationale, source_patient_fields=item.source_patient_fields)
            for item in draft.potential_blind_spots
        ],
        supporting_evidence=[],
        relevant_existing_labs=draft.relevant_existing_labs,
        limitations=draft.limitations,
    )
