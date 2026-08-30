from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from openai import OpenAI

from baseline.schemas import BaselineBrief
from evidence_agent.agent_schemas import EvidenceAgentResult, EvidenceAssessmentBundle, EvidenceTrajectoryItem
from evidence_agent.gate import validate_and_finalize
from evidence_agent.hybrid_retrieval import HybridRetriever
from evidence_agent.pipeline import enrich_brief
from evidence_agent.prompt import SYSTEM_PROMPT, build_evidence_prompt


@dataclass(frozen=True)
class EvidenceGenerationResult:
    brief: BaselineBrief
    evidence: EvidenceAgentResult
    draft: EvidenceAssessmentBundle | None
    response_id: str | None
    latency_ms: int
    embedding_input_tokens: int
    model_input_tokens: int
    model_output_tokens: int
    reasoning_tokens: int
    visible_output_tokens: int


class OpenAIEvidenceAgent:
    def __init__(
        self,
        model: str,
        retriever: HybridRetriever,
        client: OpenAI | None = None,
    ) -> None:
        self.model = model
        self.retriever = retriever
        self.client = client or OpenAI()

    def generate(self, brief: BaselineBrief) -> EvidenceGenerationResult:
        started = perf_counter()
        considerations = [
            (f"NC-{index:02d}", consideration)
            for index, consideration in enumerate(brief.nutrition_considerations, start=1)
        ]
        queries = [f"{item.topic}. {item.rationale}" for _, item in considerations]
        ranked = self.retriever.search_many(queries, top_k=3) if queries else []
        retrievals = {
            consideration_id: results
            for (consideration_id, _), results in zip(considerations, ranked, strict=True)
        }
        trajectory = [
            EvidenceTrajectoryItem(
                consideration_id=consideration_id,
                query=query,
                retrieval_results=retrievals[consideration_id],
            )
            for (consideration_id, _), query in zip(considerations, queries, strict=True)
        ]

        response = None
        draft = None
        if considerations and any(retrievals.values()):
            response = self.client.responses.parse(
                model=self.model,
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": build_evidence_prompt(considerations, retrievals)},
                ],
                text_format=EvidenceAssessmentBundle,
            )
            draft = response.output_parsed
            if draft is None:
                raise RuntimeError("Evidence Agent response did not contain a parsed assessment bundle.")

        assessments, gate_report = validate_and_finalize(considerations, retrievals, draft)
        result = EvidenceAgentResult(
            assessments=assessments, gate_report=gate_report, trajectory=trajectory,
        )
        usage = getattr(response, "usage", None)
        output_tokens = int(getattr(usage, "output_tokens", 0) or 0)
        output_details = getattr(usage, "output_tokens_details", None)
        reasoning_tokens = int(getattr(output_details, "reasoning_tokens", 0) or 0)
        return EvidenceGenerationResult(
            brief=enrich_brief(brief, assessments), evidence=result, draft=draft,
            response_id=getattr(response, "id", None),
            latency_ms=round((perf_counter() - started) * 1000),
            embedding_input_tokens=int(
                self.retriever.embeddings.last_query_stats.get("input_tokens", 0)
            ),
            model_input_tokens=int(getattr(usage, "input_tokens", 0) or 0),
            model_output_tokens=output_tokens,
            reasoning_tokens=reasoning_tokens,
            visible_output_tokens=output_tokens - reasoning_tokens,
        )
