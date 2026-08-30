from __future__ import annotations

import json

from baseline.schemas import PatientIntake
from nutrition_agent.schemas import NutritionReasoningResult, PatientState, SafetyViolation


PROMPT_VERSION = "nutrition-agent-v3"

SYSTEM_PROMPT = """You are the Nutrition Reasoning Agent of Health Professional Copilot.
Prepare a pre-consultation draft for a nutrition professional, never a diagnosis or treatment plan.

Rules:
- Use only facts present in the patient intake. Copy every supporting_patient_fact verbatim from a
  field named in source_patient_fields.
- A medical diagnosis may appear only when copied from known_diagnoses and labelled as reported
  medical context.
- Never diagnose, rank diagnoses, recommend tests, or start, stop, or change medication or doses.
- Treat not_reported as unknown and contradictory as requiring clarification.
- Include only items that could change consultation preparation; optional sections may be empty.
- Return 3 to 5 concise suggested questions and respect every schema limit.
- A secondary nutrition consideration requires at least two populated source fields and two copied
  supporting facts.
- referral_candidates must be empty because a deterministic eligibility engine handles referrals.
- Copy existing laboratory strings exactly. Do not add new tests or interpretation.
- evidence_required marks a claim that should later be checked by the Evidence Agent; do not invent
  evidence or citations.
- Every rationale must be exactly one concise sentence.
- Produce 4 to 5 distinct information gaps when supported, prioritizing contradictions, symptom
  course, dietary intake, known treatment context, and consultation goals without inventing facts.
"""

COMPACT_SYSTEM_PROMPT = """You are the compact nutrition reasoning component of Health Professional Copilot.
The application handles patient overview, medical context, gaps, referrals, and laboratory copying.
Generate only additional nutrition reasoning requested by the schema.

Rules:
- Use source_refs such as symptoms[0], known_diagnoses[0], dietary_pattern, or physical_activity.
- Every source_ref must resolve to an explicitly reported intake value; never reference derived or
  not-reported values.
- Do not diagnose, recommend tests, or recommend starting, stopping, or changing treatment.
- Generate a consideration only when it can change consultation preparation.
- A secondary consideration needs at least two distinct source_refs.
- Return at most one item per nutrition-signal category and avoid repeating the same idea across
  considerations, risks, questions, and blind spots.
- Do not generate referrals, patient overview, medical context, laboratory summaries, confidence,
  citations, or supporting-fact text.
- Every rationale and consultation_impact must be exactly one concise sentence.
- Optional sections may be empty; do not fill them to their maximum.
"""


def build_agent_prompt(
    patient: PatientIntake,
    state: PatientState,
    previous_draft: NutritionReasoningResult | None = None,
    feedback: list[SafetyViolation] | None = None,
) -> str:
    payload: dict[str, object] = {
        "task": "Create the nutrition pre-consultation reasoning draft.",
        "patient_intake": patient.model_dump(mode="json"),
        "normalized_patient_state": {
            "notable_fields": [
                field.model_dump(mode="json") for field in state.fields
                if field.status in {"not_reported", "contradictory"}
            ],
            "contradictions": [item.model_dump(mode="json") for item in state.contradictions],
            "derived_values": state.derived_values,
            "note": "Derived values are context only and must never appear in source_patient_fields.",
        },
    }
    if previous_draft is not None:
        payload["previous_draft"] = previous_draft.model_dump(mode="json")
        payload["safety_feedback"] = [item.model_dump(mode="json") for item in feedback or []]
        payload["task"] = "Correct the previous draft using every safety feedback item."
    return json.dumps(payload, ensure_ascii=False, indent=2)


def build_compact_prompt(patient: PatientIntake, state: PatientState) -> str:
    notable_state = {
        "notable_fields": [
            field.model_dump(mode="json") for field in state.fields
            if field.status in {"not_reported", "contradictory"}
        ],
        "contradictions": [item.model_dump(mode="json") for item in state.contradictions],
    }
    return json.dumps({
        "task": "Generate compact nutrition signals and only non-deterministic nutrition content.",
        "patient_intake": patient.model_dump(mode="json"),
        "notable_patient_state": notable_state,
    }, ensure_ascii=False, indent=2)
