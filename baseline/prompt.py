from __future__ import annotations

import json
from pathlib import Path

from baseline.schemas import PatientIntake

PROMPTS_DIR = Path(__file__).with_name("prompts")
AVAILABLE_PROMPT_VERSIONS = (
    "nutrition-baseline-v1",
    "nutrition-baseline-v2",
    "nutrition-baseline-v3",
)
PROMPT_VERSION = AVAILABLE_PROMPT_VERSIONS[-1]


def load_system_prompt(version: str = PROMPT_VERSION) -> str:
    if version not in AVAILABLE_PROMPT_VERSIONS:
        raise ValueError(f"Unknown prompt version: {version}")
    return (PROMPTS_DIR / f"{version}.txt").read_text(encoding="utf-8").strip()


SYSTEM_PROMPT = load_system_prompt()


def build_user_prompt(patient: PatientIntake) -> str:
    payload = json.dumps(patient.model_dump(mode="json"), ensure_ascii=False, indent=2)
    return f"Prepare the nutrition pre-consultation brief for this patient intake:\n\n{payload}"
