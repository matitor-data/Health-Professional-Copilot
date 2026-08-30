from __future__ import annotations

from typing import Literal

from pydantic import Field

from baseline.schemas import StrictModel
from evidence_agent.schemas import RetrievalResult


SupportStatus = Literal[
    "supported", "partially_supported", "unsupported",
    "outside_source_scope", "retrieval_failed",
]


class EvidenceAssessmentDraft(StrictModel):
    consideration_id: str
    support_status: Literal[
        "supported", "partially_supported", "unsupported", "outside_source_scope",
    ]
    evidence_refs: list[str] = Field(default_factory=list, max_length=3)
    rationale: str = Field(description="Exactly one concise sentence.")
    limitations: list[str] = Field(default_factory=list, max_length=3)


class EvidenceAssessmentBundle(StrictModel):
    assessments: list[EvidenceAssessmentDraft] = Field(default_factory=list)


class EvidenceAssessment(StrictModel):
    consideration_id: str
    consideration: str
    support_status: SupportStatus
    evidence_refs: list[str] = Field(default_factory=list, max_length=3)
    rationale: str
    limitations: list[str] = Field(default_factory=list, max_length=3)


class EvidenceGateViolation(StrictModel):
    rule: Literal[
        "DUPLICATE_CONSIDERATION_ID", "UNKNOWN_CONSIDERATION_ID",
        "MISSING_ASSESSMENT", "INVALID_EVIDENCE_REF", "SUPPORT_WITHOUT_EVIDENCE",
        "RETRIEVAL_EMPTY",
    ]
    consideration_id: str
    message: str


class EvidenceGateReport(StrictModel):
    accepted: bool
    violations: list[EvidenceGateViolation] = Field(default_factory=list)


class EvidenceTrajectoryItem(StrictModel):
    consideration_id: str
    query: str
    retrieval_results: list[RetrievalResult] = Field(default_factory=list)


class EvidenceAgentResult(StrictModel):
    assessments: list[EvidenceAssessment]
    gate_report: EvidenceGateReport
    trajectory: list[EvidenceTrajectoryItem]
