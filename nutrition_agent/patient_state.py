from __future__ import annotations

import re

from baseline.schemas import PatientIntake
from nutrition_agent.schemas import IntakeContradiction, NormalizedField, PatientState


NOT_REPORTED = {"", "not reported", "unknown", "not known", "n/a"}
EXPLICIT_ABSENCE = {"none", "no", "denies", "no current concerns reported"}


def _strings(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()] if str(value).strip() else []


def _status(values: list[str]) -> str:
    if not values or all(value.lower() in NOT_REPORTED for value in values):
        return "not_reported"
    if all(value.lower() in EXPLICIT_ABSENCE for value in values):
        return "explicitly_absent"
    return "reported"


def _detect_contradictions(patient: PatientIntake) -> list[IntakeContradiction]:
    notes = patient.additional_notes.lower()
    contradictions: list[IntakeContradiction] = []
    weight = (patient.recent_weight_change or "").lower()
    if "stable" in weight and re.search(r"(?:loss|lost|lose|gain|gained)\b", notes):
        contradictions.append(IntakeContradiction(
            fields=["recent_weight_change", "additional_notes"],
            observed_values=[patient.recent_weight_change or "", patient.additional_notes],
            explanation="The intake reports stable weight and also describes a weight change.",
        ))
    if re.search(r"(?:three|3) meals", patient.dietary_pattern.lower()) and re.search(
        r"skip(?:s|ped|ping)? (?:a )?(?:meal|breakfast|lunch|dinner)", notes
    ):
        contradictions.append(IntakeContradiction(
            fields=["dietary_pattern", "additional_notes"],
            observed_values=[patient.dietary_pattern, patient.additional_notes],
            explanation="The reported meal pattern conflicts with a note about skipped meals.",
        ))
    return contradictions


def build_patient_state(patient: PatientIntake) -> PatientState:
    contradictions = _detect_contradictions(patient)
    contradictory_fields = {field for item in contradictions for field in item.fields}
    fields = []
    for name, value in patient.model_dump(mode="python").items():
        values = _strings(value)
        status = "contradictory" if name in contradictory_fields else _status(values)
        fields.append(NormalizedField(field=name, status=status, values=values))

    derived: dict[str, float | str] = {}
    if patient.height_cm and patient.weight_kg:
        derived["bmi"] = round(patient.weight_kg / (patient.height_cm / 100) ** 2, 1)
        derived["bmi_status"] = "derived_not_diagnostic"
    return PatientState(fields=fields, contradictions=contradictions, derived_values=derived)

