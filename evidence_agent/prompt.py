from __future__ import annotations

import json

from baseline.schemas import NutritionConsideration
from evidence_agent.schemas import RetrievalResult


PROMPT_VERSION = "evidence-agent-v1.1"

SYSTEM_PROMPT = """You are the Evidence Agent in a nutrition consultation-preparation module.

For each nutrition consideration, determine only whether the supplied synthetic evidence chunks
support it. The chunks are prototype test evidence, not clinical guidelines.

Rules:
- Use only the chunks supplied for that exact consideration.
- Never invent a source ID, chunk ID, fact, quotation, URL, diagnosis, investigation, or treatment.
- Do not use general knowledge to fill an evidence gap.
- supported: the consideration is directly supported by at least one supplied chunk.
- partially_supported: only part of the consideration is directly supported.
- unsupported: chunks were retrieved but do not support the consideration.
- outside_source_scope: the consideration asks about a topic the supplied collection does not cover.
- Cite only exact retrieved chunk IDs.
- Cite the minimum number of chunks necessary; do not cite a chunk merely because it is related.
- State material limitations from the chunks when they narrow applicability.
- Keep each rationale to one concise sentence.
- Empty lists are allowed.
- Return exactly one assessment for every consideration ID supplied.
"""


def build_evidence_prompt(
    considerations: list[tuple[str, NutritionConsideration]],
    retrievals: dict[str, list[RetrievalResult]],
) -> str:
    payload = []
    for consideration_id, consideration in considerations:
        payload.append({
            "consideration_id": consideration_id,
            "consideration": consideration.model_dump(mode="json"),
            "retrieved_chunks": [
                {
                    "chunk_id": result.chunk_id,
                    "source_id": result.source_id,
                    "section": result.section,
                    "content_sha256": result.content_sha256,
                    "text": result.text,
                }
                for result in retrievals.get(consideration_id, [])
            ],
        })
    return "Evaluate this evidence packet:\n" + json.dumps(payload, ensure_ascii=False)
