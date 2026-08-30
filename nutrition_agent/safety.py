from __future__ import annotations

import json
import re

from baseline.schemas import PatientIntake
from nutrition_agent.schemas import NutritionReasoningResult, SafetyReport, SafetyViolation


ASSERTIVE_SECTIONS = (
    "nutrition_considerations",
    "nutritional_risk_factors",
    "referral_candidates",
)

FORBIDDEN_PATTERNS = {
    "MEDICATION_CHANGE": r"\b(?:stop|discontinue|start|increase|decrease|change|adjust)\b.{0,40}\b(?:medication|dose|supplement|lisinopril|iron)\b",
    "NEW_INVESTIGATION": r"\b(?:order|request|obtain|check|repeat)\b.{0,35}\b(?:test|tests|labs?|panel|endoscopy|scan)\b",
    "DIAGNOSIS_ACTION": r"\b(?:diagnose|diagnosis is|likely has|probably has|suggestive of)\b",
}


def _normalized(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9.%/-]+", text.lower()))


def _field_values(patient: PatientIntake, field: str) -> list[str]:
    if field not in PatientIntake.model_fields:
        return []
    value = getattr(patient, field)
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _is_populated(values: list[str]) -> bool:
    return bool(values) and any(_normalized(value) not in {"", "not reported", "not known", "unknown"} for value in values)


def _fact_is_copied(fact: str, values: list[str]) -> bool:
    needle = _normalized(fact)
    return bool(needle) and any(needle in _normalized(value) for value in values)


def validate_draft(patient: PatientIntake, draft: NutritionReasoningResult) -> SafetyReport:
    violations: list[SafetyViolation] = []
    for section_name in ASSERTIVE_SECTIONS:
        section = getattr(draft, section_name)
        for index, item in enumerate(section):
            path = f"{section_name}[{index}]"
            valid_fields = [field for field in item.source_patient_fields if field in PatientIntake.model_fields]
            if len(valid_fields) != len(item.source_patient_fields):
                violations.append(SafetyViolation(
                    rule="INVALID_SOURCE_FIELD", item_path=path,
                    message="Every source_patient_field must be a PatientIntake field.",
                ))
            populated_fields = [field for field in valid_fields if _is_populated(_field_values(patient, field))]
            if not populated_fields:
                violations.append(SafetyViolation(
                    rule="UNGROUNDED_ITEM", item_path=path,
                    message="The item requires at least one populated source field.",
                ))
            for fact in item.supporting_patient_facts:
                source_values = [value for field in valid_fields for value in _field_values(patient, field)]
                if not _fact_is_copied(fact, source_values):
                    violations.append(SafetyViolation(
                        rule="UNSUPPORTED_FACT", item_path=path,
                        message=f"Supporting fact is not copied from its source fields: {fact!r}.",
                    ))
            if not item.supporting_patient_facts:
                violations.append(SafetyViolation(
                    rule="MISSING_SUPPORTING_FACT", item_path=path,
                    message="Assertive items require at least one copied supporting fact.",
                ))
            text = f"{item.statement} {item.rationale}"
            if section_name == "referral_candidates":
                text += f" {item.recommendation}"
            for rule, pattern in FORBIDDEN_PATTERNS.items():
                if re.search(pattern, text, flags=re.IGNORECASE):
                    violations.append(SafetyViolation(rule=rule, item_path=path, message="The item may exceed nutrition scope."))

    for index, item in enumerate(draft.nutrition_considerations[1:], start=1):
        populated = {
            field for field in item.source_patient_fields
            if _is_populated(_field_values(patient, field))
        }
        if len(populated) < 2 or len(item.supporting_patient_facts) < 2:
            violations.append(SafetyViolation(
                rule="SECONDARY_CONSIDERATION_GROUNDING",
                item_path=f"nutrition_considerations[{index}]",
                message="A secondary consideration requires two populated fields and two copied facts.",
            ))

    reported_labs = patient.existing_labs
    generated_labs = [lab.reported_result for lab in draft.relevant_existing_labs]
    if generated_labs != reported_labs:
        violations.append(SafetyViolation(
            rule="LAB_FIDELITY", item_path="relevant_existing_labs",
            message="Existing labs must be copied exactly, in input order, without additions.",
            severity="reject_draft",
        ))

    context_text = json.dumps(draft.known_medical_context, ensure_ascii=False)
    for rule, pattern in FORBIDDEN_PATTERNS.items():
        if re.search(pattern, context_text, flags=re.IGNORECASE):
            violations.append(SafetyViolation(
                rule=rule, item_path="known_medical_context",
                message="Known medical context may only reproduce reported context.", severity="reject_draft",
            ))
    return SafetyReport(accepted=not violations, violations=violations)


def drop_unsafe_items(
    patient: PatientIntake, draft: NutritionReasoningResult, report: SafetyReport
) -> NutritionReasoningResult:
    data = draft.model_dump(mode="python")
    drops: dict[str, set[int]] = {}
    reject_paths: set[str] = set()
    for violation in report.violations:
        match = re.fullmatch(r"([a-z_]+)\[(\d+)\]", violation.item_path)
        if match:
            drops.setdefault(match.group(1), set()).add(int(match.group(2)))
        elif violation.severity == "reject_draft":
            reject_paths.add(violation.item_path)
    for section, indexes in drops.items():
        data[section] = [item for index, item in enumerate(data[section]) if index not in indexes]
    if "relevant_existing_labs" in reject_paths:
        data["relevant_existing_labs"] = [
            {"reported_result": lab, "source_patient_field": "existing_labs", "limitation": None}
            for lab in patient.existing_labs
        ]
    if "known_medical_context" in reject_paths:
        data["known_medical_context"] = list(patient.known_diagnoses)
    data["limitations"] = [*data["limitations"], *sorted({f"Safety gate removed or rejected content under {v.rule}." for v in report.violations})]
    return NutritionReasoningResult.model_validate(data)
