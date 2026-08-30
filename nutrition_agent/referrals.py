from __future__ import annotations

import re

from baseline.schemas import PatientIntake
from nutrition_agent.schemas import NutritionReasoningResult, ReasonedItem, ReferralCandidate, ReferralDecision


def _find(items: list[str], pattern: str) -> str | None:
    return next((item for item in items if re.search(pattern, item, re.IGNORECASE)), None)


def evaluate_referral_eligibility(patient: PatientIntake) -> list[ReferralDecision]:
    symptoms = patient.symptoms
    swallowing = _find(symptoms, r"(?:stuck|swallow)")
    weight_loss = (
        patient.recent_weight_change
        if patient.recent_weight_change
        and re.search(r"unintentional.*(?:loss|lost)|(?:loss|lost).*unintentional", patient.recent_weight_change, re.IGNORECASE)
        else None
    )
    if swallowing and weight_loss:
        return [ReferralDecision(
            eligibility="supported", rule_id="SWALLOWING_DIFFICULTY_WITH_WEIGHT_LOSS",
            observed_facts=[swallowing, weight_loss],
            source_patient_fields=["symptoms", "recent_weight_change"], urgency="prompt",
        )]

    vomiting = _find(symptoms, r"vomit")
    dizziness = _find(symptoms, r"dizz")
    low_urine = _find(symptoms, r"(?:little|low|reduced).*urin")
    limited_fluids = patient.dietary_pattern if re.search(
        r"(?:only|small).*sip|very little.*(?:fluid|water)", patient.dietary_pattern, re.IGNORECASE
    ) else None
    dehydration_signals = [fact for fact in (dizziness, low_urine, limited_fluids) if fact]
    if vomiting and len(dehydration_signals) >= 2:
        facts = [vomiting, *dehydration_signals]
        fields = ["symptoms", *( ["dietary_pattern"] if limited_fluids else [])]
        return [ReferralDecision(
            eligibility="supported", rule_id="VOMITING_WITH_LIMITED_HYDRATION_SIGNALS",
            observed_facts=facts, source_patient_fields=list(dict.fromkeys(fields)), urgency="urgent",
        )]

    notes = patient.additional_notes
    if (patient.recent_weight_change or "").lower() == "stable" and re.search(
        r"unintentional.*(?:loss|lost)|(?:loss|lost).*unintentional", notes, re.IGNORECASE
    ):
        return [ReferralDecision(
            eligibility="clarify_first", rule_id="CONTRADICTORY_WEIGHT_CHANGE",
            observed_facts=[patient.recent_weight_change or "", notes],
            source_patient_fields=["recent_weight_change", "additional_notes"],
            clarification_question="Your intake reports both stable weight and unintentional weight loss; which is current, and what changed over what period?",
        )]

    fatigue = _find(symptoms, r"fatigue")
    if fatigue and patient.known_diagnoses and patient.supplements:
        return [ReferralDecision(
            eligibility="clarify_first", rule_id="SYMPTOM_WITH_UNCLEAR_TREATMENT_COURSE",
            observed_facts=[fatigue], source_patient_fields=["symptoms"],
            clarification_question="Has the reported fatigue worsened, and what treatment duration, adherence, response, and medical follow-up were actually established?",
        )]
    return [ReferralDecision(eligibility="not_indicated", rule_id="NO_APPROVED_TRIGGER")]


def supported_referrals(decisions: list[ReferralDecision]) -> list[ReferralCandidate]:
    return [ReferralCandidate(
        statement="; ".join(decision.observed_facts),
        rationale="These reported observations meet an approved referral eligibility rule.",
        source_patient_fields=decision.source_patient_fields,
        supporting_patient_facts=decision.observed_facts,
        confidence="high", evidence_required=False,
        urgency=decision.urgency or "routine", recommendation="Seek appropriate medical evaluation.",
    ) for decision in decisions if decision.eligibility == "supported"]


def apply_referral_decisions(
    draft: NutritionReasoningResult, decisions: list[ReferralDecision]
) -> NutritionReasoningResult:
    data = draft.model_dump(mode="python")
    data["referral_candidates"] = [item.model_dump(mode="python") for item in supported_referrals(decisions)]
    clarification_items = [ReasonedItem(
        statement=decision.clarification_question or "Clarify the possible referral trigger.",
        rationale="This must be clarified before deciding whether medical referral is indicated.",
        source_patient_fields=decision.source_patient_fields,
        supporting_patient_facts=decision.observed_facts,
        confidence="high", evidence_required=False,
    ).model_dump(mode="python") for decision in decisions if decision.eligibility == "clarify_first"]
    if clarification_items:
        existing_questions = [
            item for item in data["suggested_questions"]
            if item["statement"] not in {new["statement"] for new in clarification_items}
        ]
        data["suggested_questions"] = [*clarification_items, *existing_questions][:5]
        existing_gaps = data["information_gaps"]
        clarification_gaps = [{**item, "statement": "Clarify before considering medical referral"} for item in clarification_items]
        data["information_gaps"] = [*clarification_gaps, *existing_gaps][:5]
    return NutritionReasoningResult.model_validate(data)
