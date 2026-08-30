from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from openai import OpenAI

from baseline.schemas import BaselineBrief, PatientIntake
from nutrition_agent.patient_state import build_patient_state
from nutrition_agent.pipeline import build_brief
from nutrition_agent.prompt import COMPACT_SYSTEM_PROMPT, build_compact_prompt
from nutrition_agent.referrals import evaluate_referral_eligibility
from nutrition_agent.schemas import CompactReasoningResult, PatientState, ReferralDecision, SafetyReport


@dataclass(frozen=True)
class AgentGenerationResult:
    brief: BaselineBrief
    patient_state: PatientState
    draft: CompactReasoningResult
    safety_reports: list[SafetyReport]
    referral_decisions: list[ReferralDecision]
    response_ids: list[str]
    retries: int
    latency_ms: int
    input_tokens: int
    output_tokens: int
    reasoning_tokens: int
    visible_output_tokens: int


class OpenAINutritionAgent:
    def __init__(self, model: str, client: OpenAI | None = None) -> None:
        self.model = model
        self.client = client or OpenAI()

    def _call(self, prompt: str):
        return self.client.responses.parse(
            model=self.model,
            input=[
                {"role": "system", "content": COMPACT_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            text_format=CompactReasoningResult,
        )

    def generate(self, patient: PatientIntake) -> AgentGenerationResult:
        started = perf_counter()
        state = build_patient_state(patient)
        referral_decisions = evaluate_referral_eligibility(patient)
        responses = [self._call(build_compact_prompt(patient, state))]
        draft = responses[0].output_parsed
        if draft is None:
            raise RuntimeError("Agent response did not contain a parsed CompactReasoningResult")
        brief, report = build_brief(patient, state, draft, referral_decisions)
        reports = [report]

        def usage(name: str) -> int:
            return sum(int(getattr(response.usage, name, 0) or 0) for response in responses)

        output_tokens = usage("output_tokens")
        reasoning_tokens = sum(
            int(getattr(getattr(response.usage, "output_tokens_details", None), "reasoning_tokens", 0) or 0)
            for response in responses
        )
        return AgentGenerationResult(
            brief=brief, patient_state=state, draft=draft, safety_reports=reports,
            referral_decisions=referral_decisions,
            response_ids=[response.id for response in responses], retries=len(responses) - 1,
            latency_ms=round((perf_counter() - started) * 1000),
            input_tokens=usage("input_tokens"), output_tokens=output_tokens,
            reasoning_tokens=reasoning_tokens,
            visible_output_tokens=output_tokens - reasoning_tokens,
        )
