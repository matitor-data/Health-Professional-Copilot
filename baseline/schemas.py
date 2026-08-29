from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PatientIntake(StrictModel):
    age: int = Field(ge=0, le=130)
    sex: str
    height_cm: float | None = Field(default=None, gt=0)
    weight_kg: float | None = Field(default=None, gt=0)
    reason_for_consultation: str
    primary_goal: str
    known_diagnoses: list[str] = Field(default_factory=list)
    symptoms: list[str] = Field(default_factory=list)
    symptom_duration: str = ""
    medications: list[str] = Field(default_factory=list)
    supplements: list[str] = Field(default_factory=list)
    dietary_pattern: str = ""
    physical_activity: str = ""
    sleep: str = ""
    recent_weight_change: str | None = None
    existing_labs: list[str] = Field(default_factory=list)
    family_history: list[str] = Field(default_factory=list)
    additional_notes: str = ""


class EvaluationRubric(StrictModel):
    expected_information_gaps: list[str]
    expected_followup_topics: list[str]
    expected_nutrition_considerations: list[str]
    expected_risk_factors: list[str]
    expected_referral_flags: list[str]
    expected_existing_context: list[str]
    should_not_suggest: list[str]
    supporting_sources: list[str]


class EvaluationCase(StrictModel):
    case_id: str
    case_type: list[str]
    difficulty: Literal["easy", "medium", "hard"]
    patient_intake: PatientIntake
    evaluation_rubric: EvaluationRubric


class DatasetMetadata(StrictModel):
    dataset_name: str
    specialty: str
    generation_method: str
    number_of_cases: int = Field(ge=1)
    case_id_range: str
    notes: str


class EvaluationDataset(StrictModel):
    dataset_metadata: DatasetMetadata
    cases: list[EvaluationCase]

    @model_validator(mode="after")
    def validate_dataset(self) -> "EvaluationDataset":
        if self.dataset_metadata.number_of_cases != len(self.cases):
            raise ValueError("dataset_metadata.number_of_cases does not match cases")
        ids = [case.case_id for case in self.cases]
        if len(ids) != len(set(ids)):
            raise ValueError("case_id values must be unique")
        return self


class BriefItem(StrictModel):
    topic: str
    rationale: str = Field(description="Exactly one concise sentence.")
    source_patient_fields: list[str] = Field(default_factory=list)


class NutritionConsideration(BriefItem):
    limiting_or_missing_facts: list[str] = Field(default_factory=list)


class NutritionalRiskFactor(StrictModel):
    factor: str
    rationale: str = Field(description="Exactly one concise sentence.")
    priority: Literal["low", "medium", "high"]
    source_patient_fields: list[str] = Field(default_factory=list)


class ReferralEscalationFlag(StrictModel):
    trigger: str
    rationale: str = Field(description="Exactly one concise sentence.")
    urgency: Literal["routine", "prompt", "urgent"]
    recommendation: str
    source_patient_fields: list[str] = Field(default_factory=list)


class ExistingLabSummary(StrictModel):
    reported_result: str
    source_patient_field: Literal["existing_labs"] = "existing_labs"
    limitation: str | None = None


class BaselineBrief(StrictModel):
    patient_overview: str
    known_medical_context: list[str] = Field(default_factory=list)
    information_to_clarify: list[BriefItem] = Field(default_factory=list, max_length=5)
    suggested_questions: list[BriefItem] = Field(min_length=3, max_length=5)
    nutrition_considerations: list[NutritionConsideration] = Field(default_factory=list, max_length=3)
    nutritional_risk_factors: list[NutritionalRiskFactor] = Field(default_factory=list, max_length=4)
    referral_escalation_flags: list[ReferralEscalationFlag] = Field(default_factory=list, max_length=2)
    potential_blind_spots: list[BriefItem] = Field(default_factory=list, max_length=3)
    supporting_evidence: list[str] = Field(default_factory=list)
    relevant_existing_labs: list[ExistingLabSummary] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
