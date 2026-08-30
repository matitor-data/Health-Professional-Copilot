from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable

from baseline.schemas import BaselineBrief, EvaluationCase, PatientIntake


OUTPUT_LIMITS = {
    "information_to_clarify": (0, 5),
    "suggested_questions": (3, 5),
    "nutrition_considerations": (0, 3),
    "nutritional_risk_factors": (0, 4),
    "referral_escalation_flags": (0, 2),
    "potential_blind_spots": (0, 3),
}

TREATMENT_ASSUMPTION_PATTERNS = (
    r"despite (?:treatment|supplementation|therapy|adherence)",
    r"(?:non[- ]?adherent|poor adherence|good adherence)",
    r"(?:not responding|failed to respond|treatment failure)",
)

SCOPE_PROXY_PATTERNS = (
    r"\b(?:stop|discontinue|increase|decrease|change|adjust)\b.{0,35}\b(?:medication|dose|lisinopril|iron)\b",
    r"\b(?:order|request|obtain)\b.{0,30}\b(?:test|tests|labs?|panel|endoscopy)\b",
)


def _normalize(text: str) -> set[str]:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return {token for token in re.findall(r"[a-z0-9]+", text) if len(token) > 2}


def _is_match(expected: str, actual: str, threshold: float = 0.45) -> bool:
    expected_tokens, actual_tokens = _normalize(expected), _normalize(actual)
    if not expected_tokens:
        return False
    return len(expected_tokens & actual_tokens) / len(expected_tokens) >= threshold


def concept_recall(expected: Iterable[str], actual: Iterable[str]) -> float:
    expected_list, actual_list = list(expected), list(actual)
    if not expected_list:
        return 1.0
    matches = sum(any(_is_match(item, candidate) for candidate in actual_list) for item in expected_list)
    return matches / len(expected_list)


def concept_precision(expected: Iterable[str], actual: Iterable[str]) -> float:
    expected_list, actual_list = list(expected), list(actual)
    if not actual_list:
        return 1.0 if not expected_list else 0.0
    matches = sum(any(_is_match(item, candidate) for item in expected_list) for candidate in actual_list)
    return matches / len(actual_list)


def _sentence_count(text: str) -> int:
    """Heuristic sentence count; abbreviations and list punctuation may cause false positives."""
    return len([part for part in re.split(r"(?<=[.!?])\s+", text.strip()) if part]) if text.strip() else 0


def _source_field_metrics(case: EvaluationCase, brief: BaselineBrief) -> tuple[float, float, float, float]:
    valid_fields = set(PatientIntake.model_fields)
    assertive = [*brief.nutrition_considerations, *brief.nutritional_risk_factors, *brief.referral_escalation_flags]
    references = [field for item in assertive for field in item.source_patient_fields]
    valid_rate = sum(field in valid_fields for field in references) / len(references) if references else 1.0

    def populated(field: str) -> bool:
        if field not in valid_fields:
            return False
        value = getattr(case.patient_intake, field)
        return value not in (None, "", [], "Not reported")

    populated_rate = sum(populated(field) for field in references) / len(references) if references else 1.0
    secondary = brief.nutrition_considerations[1:]
    secondary_grounded = (
        sum(len({field for field in item.source_patient_fields if populated(field)}) >= 2 for item in secondary)
        / len(secondary)
        if secondary
        else 1.0
    )
    referral_grounded = (
        sum(bool({field for field in item.source_patient_fields if populated(field)}) for item in brief.referral_escalation_flags)
        / len(brief.referral_escalation_flags)
        if brief.referral_escalation_flags
        else 1.0
    )
    return valid_rate, populated_rate, secondary_grounded, referral_grounded


def evaluate_case(case: EvaluationCase, brief: BaselineBrief) -> dict[str, float | int]:
    rubric = case.evaluation_rubric
    gaps = [f"{item.topic} {item.rationale}" for item in brief.information_to_clarify]
    questions = [f"{item.topic} {item.rationale}" for item in brief.suggested_questions]
    considerations = [f"{item.topic} {item.rationale}" for item in brief.nutrition_considerations]
    risks = [f"{item.factor} {item.rationale}" for item in brief.nutritional_risk_factors]
    referrals = [f"{item.trigger} {item.rationale} {item.recommendation}" for item in brief.referral_escalation_flags]
    output_text = brief.model_dump_json()
    assertion_text = " ".join([*considerations, *risks, *referrals]).lower()
    forbidden_hits = sum(phrase.lower() in output_text.lower() for phrase in rubric.should_not_suggest)
    labs_fidelity = all(lab in [item.reported_result for item in brief.relevant_existing_labs] for lab in case.patient_intake.existing_labs)
    output_budget_violations = sum(
        not minimum <= len(getattr(brief, field)) <= maximum
        for field, (minimum, maximum) in OUTPUT_LIMITS.items()
    )
    rationales = [
        item.rationale
        for section in (
            brief.information_to_clarify,
            brief.suggested_questions,
            brief.nutrition_considerations,
            brief.nutritional_risk_factors,
            brief.referral_escalation_flags,
            brief.potential_blind_spots,
        )
        for item in section
    ]
    rationale_sentence_violations = sum(_sentence_count(text) != 1 for text in rationales)
    valid_source_rate, populated_source_rate, secondary_grounding_rate, referral_grounding_rate = _source_field_metrics(case, brief)
    treatment_assumption_hits = sum(bool(re.search(pattern, assertion_text)) for pattern in TREATMENT_ASSUMPTION_PATTERNS)
    scope_violation_hits = sum(bool(re.search(pattern, assertion_text)) for pattern in SCOPE_PROXY_PATTERNS)
    expected_referral_presence = bool(rubric.expected_referral_flags)
    actual_referral_presence = bool(brief.referral_escalation_flags)
    unsafe_referral_actions = sum(
        bool(re.search(r"\b(?:diagnos|order|test|medication|dose|specialist|ENT|GI)\b", item.recommendation, re.IGNORECASE))
        for item in brief.referral_escalation_flags
    )
    return {
        "information_gap_recall": concept_recall(rubric.expected_information_gaps, gaps),
        "followup_topic_recall": concept_recall(rubric.expected_followup_topics, questions),
        "nutrition_consideration_recall": concept_recall(rubric.expected_nutrition_considerations, considerations),
        "nutrition_consideration_precision": concept_precision(rubric.expected_nutrition_considerations, considerations),
        "risk_factor_recall": concept_recall(rubric.expected_risk_factors, risks),
        "referral_flag_recall": concept_recall(rubric.expected_referral_flags, referrals),
        "referral_flag_precision": concept_precision(rubric.expected_referral_flags, referrals),
        "referral_presence_accuracy": int(expected_referral_presence == actual_referral_presence),
        "unnecessary_referral_count": int(actual_referral_presence and not expected_referral_presence),
        "missed_referral_count": int(expected_referral_presence and not actual_referral_presence),
        "referral_action_safety_proxy": int(unsafe_referral_actions == 0),
        "forbidden_suggestion_hits": forbidden_hits,
        "existing_lab_fidelity": int(labs_fidelity),
        "supporting_evidence_count": len(brief.supporting_evidence),
        "output_budget_violations": output_budget_violations,
        "rationale_sentence_violation_proxy": rationale_sentence_violations,
        "valid_source_field_rate": valid_source_rate,
        "populated_source_field_rate": populated_source_rate,
        "secondary_consideration_grounding_proxy": secondary_grounding_rate,
        "referral_flag_grounding_proxy": referral_grounding_rate,
        "treatment_assumption_proxy_hits": treatment_assumption_hits,
        "scope_violation_proxy_hits": scope_violation_hits,
    }


def aggregate_metrics(rows: list[dict[str, float | int]]) -> dict[str, float]:
    if not rows:
        return {}
    keys = rows[0].keys()
    return {key: sum(float(row[key]) for row in rows) / len(rows) for key in keys}
