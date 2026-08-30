from __future__ import annotations

import re

from baseline.schemas import (
    BaselineBrief, BriefItem, ExistingLabSummary, NutritionConsideration,
    NutritionalRiskFactor, PatientIntake, ReferralEscalationFlag,
)
from nutrition_agent.gaps import build_gap_coverage
from nutrition_agent.considerations import build_supported_considerations
from nutrition_agent.schemas import (
    CompactItem, CompactReasoningResult, PatientState, ReferralDecision,
    SafetyReport, SafetyViolation,
)
from nutrition_agent.source_refs import resolve_refs


def _tokens(text: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", text.lower()) if len(token) > 2}


def _similarity(left: str, right: str) -> float:
    a, b = _tokens(left), _tokens(right)
    return len(a & b) / min(len(a), len(b)) if a and b else 0.0


def _dedupe(items: list, text_attr: str, threshold: float = 0.75) -> list:
    kept = []
    for item in items:
        text = getattr(item, text_attr)
        if not any(_similarity(text, getattr(existing, text_attr)) >= threshold for existing in kept):
            kept.append(item)
    return kept


def _resolve_item(
    patient: PatientIntake, item: CompactItem, path: str, violations: list[SafetyViolation]
) -> tuple[list[str], list[str]] | None:
    resolved = resolve_refs(patient, item.source_refs)
    if resolved is None:
        violations.append(SafetyViolation(
            rule="INVALID_OR_EMPTY_SOURCE_REF", item_path=path,
            message="The item was removed because a compact source reference did not resolve.",
        ))
    return resolved


def build_brief(
    patient: PatientIntake,
    state: PatientState,
    compact: CompactReasoningResult,
    referral_decisions: list[ReferralDecision],
) -> tuple[BaselineBrief, SafetyReport]:
    violations: list[SafetyViolation] = []
    gaps, deterministic_questions = build_gap_coverage(patient, state, referral_decisions)
    questions = list(deterministic_questions)
    for index, item in enumerate(compact.suggested_questions):
        resolved = _resolve_item(patient, item, f"suggested_questions[{index}]", violations)
        if resolved and len(questions) < 5:
            fields, _ = resolved
            candidate = BriefItem(topic=item.statement, rationale=item.rationale, source_patient_fields=fields)
            if not any(_similarity(candidate.topic, existing.topic) >= 0.75 for existing in questions):
                questions.append(candidate)

    considerations: list[NutritionConsideration] = build_supported_considerations(patient)
    for index, item in enumerate(compact.nutrition_considerations):
        resolved = _resolve_item(patient, item, f"nutrition_considerations[{index}]", violations)
        if not resolved:
            continue
        fields, _ = resolved
        if considerations and len(set(item.source_refs)) < 2:
            violations.append(SafetyViolation(
                rule="SECONDARY_CONSIDERATION_GROUNDING",
                item_path=f"nutrition_considerations[{index}]",
                message="The secondary consideration was removed because it had fewer than two references.",
            ))
            continue
        considerations.append(NutritionConsideration(
            topic=item.statement, rationale=item.rationale, source_patient_fields=fields,
            limiting_or_missing_facts=[],
        ))

    signal_topics = {
        "intake_adequacy": "Assess energy and protein adequacy",
        "meal_pattern": "Align meal pattern with the consultation goal",
        "diet_quality": "Address case-specific dietary quality",
        "hydration": "Assess hydration within the reported context",
        "symptom_related_intake": "Account for symptom-related limits on intake",
        "weight_change": "Account for the reported weight-change context",
        "performance_recovery": "Support training fuel and recovery",
    }
    seen_categories: set[str] = set()
    for index, signal in enumerate(compact.nutrition_signals):
        if signal.category in seen_categories or len(considerations) >= 3:
            continue
        seen_categories.add(signal.category)
        resolved = resolve_refs(patient, signal.source_refs)
        if resolved is None:
            violations.append(SafetyViolation(
                rule="INVALID_SIGNAL_SOURCE_REF", item_path=f"nutrition_signals[{index}]",
                message="The signal was removed because a source reference did not resolve.",
            ))
            continue
        fields, _ = resolved
        if considerations and len(set(signal.source_refs)) < 2:
            continue
        candidate = NutritionConsideration(
            topic=signal_topics[signal.category], rationale=signal.consultation_impact,
            source_patient_fields=fields, limiting_or_missing_facts=[],
        )
        if not any(_similarity(candidate.topic, item.topic) >= 0.75 for item in considerations):
            considerations.append(candidate)

    risks: list[NutritionalRiskFactor] = []
    for index, item in enumerate(compact.nutritional_risk_factors):
        resolved = _resolve_item(patient, item, f"nutritional_risk_factors[{index}]", violations)
        if resolved:
            fields, _ = resolved
            risks.append(NutritionalRiskFactor(
                factor=item.statement, rationale=item.rationale, priority=item.priority,
                source_patient_fields=fields,
            ))

    blind_spots: list[BriefItem] = []
    for index, item in enumerate(compact.potential_blind_spots):
        resolved = _resolve_item(patient, item, f"potential_blind_spots[{index}]", violations)
        if resolved:
            fields, _ = resolved
            blind_spots.append(BriefItem(
                topic=item.statement, rationale=item.rationale, source_patient_fields=fields,
            ))

    referrals = [ReferralEscalationFlag(
        trigger="; ".join(decision.observed_facts),
        rationale="These reported observations meet an approved medical-referral rule.",
        urgency=decision.urgency or "routine",
        recommendation=f"Seek {decision.urgency or 'routine'} medical evaluation.",
        source_patient_fields=decision.source_patient_fields,
    ) for decision in referral_decisions if decision.eligibility == "supported"]

    limitations = [*compact.limitations]
    if violations:
        limitations.append(f"The deterministic validator removed {len(violations)} unsupported item(s).")
    brief = BaselineBrief(
        patient_overview=f"Nutrition consultation for: {patient.reason_for_consultation}",
        known_medical_context=[f"Reported established medical context: {item}" for item in patient.known_diagnoses],
        information_to_clarify=gaps,
        suggested_questions=questions[:5],
        nutrition_considerations=_dedupe(considerations, "topic")[:3],
        nutritional_risk_factors=_dedupe(risks, "factor")[:4],
        referral_escalation_flags=referrals[:2],
        potential_blind_spots=_dedupe(blind_spots, "topic")[:3],
        supporting_evidence=[],
        relevant_existing_labs=[ExistingLabSummary(reported_result=lab) for lab in patient.existing_labs],
        limitations=limitations,
    )
    return brief, SafetyReport(accepted=True, violations=violations)
