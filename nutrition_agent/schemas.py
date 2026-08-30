from __future__ import annotations

from typing import Literal

from pydantic import Field

from baseline.schemas import ExistingLabSummary, StrictModel


class NormalizedField(StrictModel):
    field: str
    status: Literal["reported", "not_reported", "explicitly_absent", "contradictory"]
    values: list[str] = Field(default_factory=list)


class IntakeContradiction(StrictModel):
    fields: list[str]
    observed_values: list[str]
    explanation: str


class PatientState(StrictModel):
    fields: list[NormalizedField]
    contradictions: list[IntakeContradiction] = Field(default_factory=list)
    derived_values: dict[str, float | str] = Field(default_factory=dict)


class ReasonedItem(StrictModel):
    statement: str
    rationale: str = Field(description="Exactly one concise sentence.")
    source_patient_fields: list[str] = Field(default_factory=list)
    supporting_patient_facts: list[str] = Field(default_factory=list)
    confidence: Literal["high", "medium", "low"]
    evidence_required: bool = False


class ReasonedRisk(ReasonedItem):
    priority: Literal["low", "medium", "high"]


class ReferralCandidate(ReasonedItem):
    urgency: Literal["routine", "prompt", "urgent"]
    recommendation: str


class NutritionReasoningResult(StrictModel):
    patient_overview: str
    known_medical_context: list[str] = Field(default_factory=list)
    information_gaps: list[ReasonedItem] = Field(default_factory=list, max_length=5)
    suggested_questions: list[ReasonedItem] = Field(min_length=3, max_length=5)
    nutrition_considerations: list[ReasonedItem] = Field(default_factory=list, max_length=3)
    nutritional_risk_factors: list[ReasonedRisk] = Field(default_factory=list, max_length=4)
    referral_candidates: list[ReferralCandidate] = Field(default_factory=list, max_length=2)
    potential_blind_spots: list[ReasonedItem] = Field(default_factory=list, max_length=3)
    relevant_existing_labs: list[ExistingLabSummary] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class SafetyViolation(StrictModel):
    rule: str
    item_path: str
    message: str
    severity: Literal["drop_item", "reject_draft"] = "drop_item"


class SafetyReport(StrictModel):
    accepted: bool
    violations: list[SafetyViolation] = Field(default_factory=list)


class ReferralDecision(StrictModel):
    eligibility: Literal["not_indicated", "clarify_first", "supported"]
    rule_id: str
    observed_facts: list[str] = Field(default_factory=list)
    source_patient_fields: list[str] = Field(default_factory=list)
    urgency: Literal["routine", "prompt", "urgent"] | None = None
    clarification_question: str | None = None


class CompactItem(StrictModel):
    statement: str
    rationale: str = Field(description="Exactly one concise sentence.")
    source_refs: list[str] = Field(default_factory=list)


class NutritionSignal(StrictModel):
    category: Literal[
        "intake_adequacy", "meal_pattern", "diet_quality", "hydration",
        "symptom_related_intake", "weight_change", "performance_recovery",
    ]
    source_refs: list[str]
    consultation_impact: str = Field(description="Exactly one concise sentence.")


class CompactRisk(CompactItem):
    priority: Literal["low", "medium", "high"]


class CompactReasoningResult(StrictModel):
    suggested_questions: list[CompactItem] = Field(default_factory=list, max_length=3)
    nutrition_signals: list[NutritionSignal] = Field(default_factory=list, max_length=6)
    nutrition_considerations: list[CompactItem] = Field(default_factory=list, max_length=3)
    nutritional_risk_factors: list[CompactRisk] = Field(default_factory=list, max_length=4)
    potential_blind_spots: list[CompactItem] = Field(default_factory=list, max_length=3)
    limitations: list[str] = Field(default_factory=list, max_length=3)
