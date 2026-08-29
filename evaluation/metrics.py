from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable

from baseline.schemas import BaselineBrief, EvaluationCase


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


def evaluate_case(case: EvaluationCase, brief: BaselineBrief) -> dict[str, float | int]:
    rubric = case.evaluation_rubric
    gaps = [f"{item.topic} {item.rationale}" for item in brief.information_to_clarify]
    questions = [f"{item.topic} {item.rationale}" for item in brief.suggested_questions]
    considerations = [f"{item.topic} {item.rationale}" for item in brief.nutrition_considerations]
    risks = [f"{item.factor} {item.rationale}" for item in brief.nutritional_risk_factors]
    referrals = [f"{item.trigger} {item.rationale} {item.recommendation}" for item in brief.referral_escalation_flags]
    output_text = brief.model_dump_json()
    forbidden_hits = sum(phrase.lower() in output_text.lower() for phrase in rubric.should_not_suggest)
    labs_fidelity = all(lab in [item.reported_result for item in brief.relevant_existing_labs] for lab in case.patient_intake.existing_labs)
    return {
        "information_gap_recall": concept_recall(rubric.expected_information_gaps, gaps),
        "followup_topic_recall": concept_recall(rubric.expected_followup_topics, questions),
        "nutrition_consideration_recall": concept_recall(rubric.expected_nutrition_considerations, considerations),
        "nutrition_consideration_precision": concept_precision(rubric.expected_nutrition_considerations, considerations),
        "risk_factor_recall": concept_recall(rubric.expected_risk_factors, risks),
        "referral_flag_recall": concept_recall(rubric.expected_referral_flags, referrals),
        "referral_flag_precision": concept_precision(rubric.expected_referral_flags, referrals),
        "forbidden_suggestion_hits": forbidden_hits,
        "existing_lab_fidelity": int(labs_fidelity),
        "supporting_evidence_count": len(brief.supporting_evidence),
    }


def aggregate_metrics(rows: list[dict[str, float | int]]) -> dict[str, float]:
    if not rows:
        return {}
    keys = rows[0].keys()
    return {key: sum(float(row[key]) for row in rows) / len(rows) for key in keys}
