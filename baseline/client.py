from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from openai import OpenAI

from baseline.prompt import SYSTEM_PROMPT, build_user_prompt
from baseline.schemas import BaselineBrief, PatientIntake


@dataclass(frozen=True)
class GenerationResult:
    brief: BaselineBrief
    response_id: str
    latency_ms: int
    input_tokens: int | None
    output_tokens: int | None


class OpenAIBaselineClient:
    def __init__(
        self,
        model: str,
        system_prompt: str = SYSTEM_PROMPT,
        client: OpenAI | None = None,
    ) -> None:
        self.model = model
        self.system_prompt = system_prompt
        self.client = client or OpenAI()

    def generate(self, patient: PatientIntake) -> GenerationResult:
        started = perf_counter()
        response = self.client.responses.parse(
            model=self.model,
            input=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": build_user_prompt(patient)},
            ],
            text_format=BaselineBrief,
        )
        latency_ms = round((perf_counter() - started) * 1000)
        if response.output_parsed is None:
            raise RuntimeError("Model response did not contain a parsed BaselineBrief")
        usage = response.usage
        return GenerationResult(
            brief=response.output_parsed,
            response_id=response.id,
            latency_ms=latency_ms,
            input_tokens=getattr(usage, "input_tokens", None),
            output_tokens=getattr(usage, "output_tokens", None),
        )
