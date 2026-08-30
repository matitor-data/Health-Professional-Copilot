from __future__ import annotations

from baseline.schemas import BaselineBrief
from evidence_agent.agent_schemas import EvidenceAssessment


def render_supporting_evidence(assessments: list[EvidenceAssessment]) -> list[str]:
    rendered: list[str] = []
    for item in assessments:
        if item.support_status not in {"supported", "partially_supported"}:
            continue
        references = ", ".join(item.evidence_refs)
        text = f"{item.consideration_id} [{item.support_status}] {item.rationale} Sources: {references}."
        if item.limitations:
            text += " Limitations: " + " ".join(item.limitations)
        rendered.append(text)
    return rendered


def enrich_brief(brief: BaselineBrief, assessments: list[EvidenceAssessment]) -> BaselineBrief:
    limitations = list(brief.limitations)
    unresolved = [
        item for item in assessments
        if item.support_status in {"unsupported", "outside_source_scope", "retrieval_failed"}
    ]
    if unresolved:
        limitations.append(
            f"Evidence support was not established for {len(unresolved)} nutrition consideration(s)."
        )
    return brief.model_copy(update={
        "supporting_evidence": render_supporting_evidence(assessments),
        "limitations": limitations,
    })
