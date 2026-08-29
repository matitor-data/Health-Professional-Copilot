# Health Professional Copilot - Nutrition Module

AI-assisted preparation for nutrition consultations. The module organizes patient intake,
surfaces nutrition-relevant information gaps and blind spots, and flags cases that may require
medical referral while remaining within the nutritionist's scope of practice.

Medical diagnoses are input context only. The system must not create diagnostic hypotheses,
change medication, or recommend new laboratory tests.

## Current status

The repository currently contains the single-call LLM baseline and a locked synthetic evaluation
set. The two-agent MVP, evidence retrieval, and evidence gate are intentionally not part of the
baseline.

## Setup

```bash
uv sync
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`. `OPENAI_MODEL` is optional and defaults to `gpt-5-mini`.

## Validate without an API call

```bash
uv run python -m baseline.runner --dry-run
python -m unittest discover -s tests -v
```

## Run the baseline

Run one case first:

```bash
uv run python -m baseline.runner --case-id case_021
```

Run the complete locked dataset:

```bash
uv run python -m baseline.runner
```

Each execution writes a versioned manifest, JSONL outputs, failures, and aggregate metrics under
`evaluation/runs/<run_id>/`. These run artifacts are ignored by Git.

## Baseline boundary

The baseline uses one structured patient intake, one versioned prompt, one LLM call, and one
validated `BaselineBrief`. It has no tools, retrieval, citations, agent loop, Evidence Agent, or
Evidence Gate. `supporting_evidence` must therefore remain empty.

The deterministic evaluator provides approximate lexical concept matching for iteration. It is not
a substitute for clinical adjudication or semantic evaluation by qualified reviewers.

## Repository structure

```text
baseline/                  Prompt, schemas, OpenAI client, and runner
data/cases/locked_test/    Synthetic cases not used for prompt tuning
evaluation/                Deterministic metrics and generated run artifacts
tests/                     Contract and safety tests
docs/                      Product specification
```
