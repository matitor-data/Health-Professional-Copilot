# Health Professional Copilot - Nutrition Module

## 01 - Who has this problem?

Nutrition professionals preparing for patient consultations.

During a consultation, nutrition professionals must combine patient-reported symptoms, dietary
patterns, established medical diagnoses, medications, supplements, lifestyle factors, relevant
existing laboratory results, and other contextual information while deciding what questions to ask
and which nutrition-related factors deserve further consideration.

Even experienced professionals cannot keep every possible presentation, nutritional risk factor,
interaction, and applicable guideline actively in mind during every consultation.

## 02 - What bottleneck makes it worth solving?

Nutrition consultations involve a large amount of information under limited time and attention.

Important details may be missing from the initial intake, information that appears unrelated may
become relevant when considered together, and useful follow-up questions may never be asked.

The problem is not simply access to information. The bottleneck is connecting the specific patient
context with the right questions, relevant nutrition considerations, nutritional risk factors, and
supporting evidence without overwhelming the professional.

A static intake form collects information, but it cannot determine what is still missing, what
deserves further exploration, or when the patient may require medical assessment.

## 03 - Does the agent solve it well?

Health Professional Copilot analyzes patient intake information before the consultation and acts as
a second layer of attention for the nutrition professional.

The Nutrition Module identifies potentially relevant missing information, suggests follow-up
questions, surfaces nutrition considerations and nutritional risk factors, and retrieves supporting
clinical evidence. When appropriate, it can raise a referral or escalation flag recommending that
the patient receive medical assessment.

Medical diagnoses are input context established by an appropriate medical professional. The module
does not generate diagnoses, prescribe or change medication, recommend new laboratory tests, or
make autonomous clinical decisions. The nutrition professional remains responsible for decisions
within their scope of practice.

By helping nutrition professionals prepare more thoroughly for consultations, the Nutrition Module
may indirectly benefit patients through more focused questions, fewer overlooked information gaps,
better-grounded nutrition considerations, and more timely identification of situations that may
require medical evaluation. It does not diagnose, replace professional judgment, or guarantee
improved clinical outcomes.

To test whether the system improves consultation preparation, we use a fixed set of synthetic
patient cases with a predefined rubric and compare the two-agent system with a simple, single-prompt
LLM baseline.

The central evaluation question is:

> Does the agent identify more expected information gaps, nutrition considerations, nutritional
> risk factors, and appropriate referral flags while producing fewer unsupported or out-of-scope
> suggestions?

## 04 - Can another person reproduce the result?

Use a fixed set of synthetic patient cases and, for the complete MVP, a curated collection of
approved clinical and nutrition guidelines.

Run both the baseline and Health Professional Copilot on exactly the same cases. Evaluate them with
the same predefined rubric for information gaps, suggested questions, nutrition considerations,
nutritional risk factors, referral flags, evidence coverage, and scope violations.

Every evidence-backed nutrition consideration or referral recommendation in the complete system
must trace back to an approved guideline passage or an approved deterministic rule. The baseline
does not use retrieval and must leave `supporting_evidence` empty.

A second person starting from a clean environment should be able to run the baseline and the agent
on the same cases, using the recorded model, prompt version, dataset hash, and configuration, and
reproduce the evaluation process.

## Current status

The repository contains the frozen single-call LLM baseline, frozen Nutrition Reasoning Agent v3,
and frozen Evidence Agent v1.1. The complete prototype includes deterministic nutrition safety and
referral rules, hybrid retrieval over an approved synthetic source collection, and an Evidence Gate
that prevents untraced citations from reaching the final brief.

The system is frozen for reproducible prototype comparison only. Its cases, evidence, and evaluation
rubrics are synthetic; it is not clinically validated, intended for production, or suitable for
patient-care decisions.

The one-time locked comparison is complete. The solution improved scope-safety proxies, citation
traceability, and visible concision but scored below the simple baseline on the current lexical
recall and precision metrics. See [`execution_report.md`](execution_report.md) for the preserved
result and limitations.

## Hot take and key insight

> The value of a clinical AI system is not in making the final decision. It is in helping the
> professional notice what might otherwise be missed. Every suggestion should remain a traceable
> hypothesis to verify, never an answer to accept.

This project also exposed an important engineering lesson: more agent reasoning does not
automatically produce better professional support. In the locked prototype evaluation, the agents
improved scope safety, output concision, and evidence traceability, but reduced measured information
recall. Verification can make suggestions safer, but safety and traceability must be evaluated
separately from whether the system notices the right information in the first place.

## Future direction

The current prototype implements only the Nutrition Module. In the future, Health Professional
Copilot could support additional healthcare professions through separate, scope-specific modules.
Each module should have its own professional responsibilities, input requirements, approved evidence
collection, deterministic safety rules, evaluation rubrics, and escalation pathways. Shared patient
context could then support collaboration between professionals without allowing one module to make
decisions outside its defined scope.

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

## Run the Nutrition Agent

Validate its deterministic preprocessing without an API call:

```bash
uv run python -m nutrition_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json --dry-run
```

Run one development case:

```bash
uv run python -m nutrition_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json --case-id dev_004
```

The agent normalizes the intake, generates a compact structured reasoning draft, applies
deterministic gap coverage, grounding, scope, and referral-eligibility checks, removes unsupported
items locally without a general retry, and renders the same `BaselineBrief` contract used by the baseline. Agent trajectories are saved under
`evaluation/agent_runs/<run_id>/` and ignored by Git.

## Run the complete Nutrition Module

Validate the complete pipeline without API calls:

```bash
uv run python -m evidence_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json \
  --case-id dev_003 --dry-run
```

Run the official synthetic demonstration from intake through the final evidence-enriched brief:

```bash
uv run python -m evidence_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json \
  --case-id dev_003 \
  --output-root evaluation/evidence_demo_runs
```

The saved trajectory contains the brief before and after evidence, retrieval queries and tool
results, model assessments, gate feedback, citations, separate reasoning and visible token counts,
and latency for both agents. The reference demonstration is run `20260830T153611Z`.

## Baseline boundary

The baseline uses one structured patient intake, one versioned prompt, one LLM call, and one
validated `BaselineBrief`. It has no tools, retrieval, citations, agent loop, Evidence Agent, or
Evidence Gate. `supporting_evidence` must therefore remain empty.

The deterministic evaluator provides approximate lexical concept matching for iteration. It is not
a substitute for clinical adjudication or semantic evaluation by qualified reviewers.

## Repository structure

```text
baseline/                  Prompt, schemas, OpenAI client, and runner
baseline/prompts/          Reproducible prompt versions v1-v4
nutrition_agent/           Patient state, reasoning client, safety gate, renderer, and runner
evidence_agent/            Hybrid retrieval, evidence assessment, gate, metrics, and runner
data/cases/development/    Synthetic cases used for iteration
data/cases/locked_test/    Synthetic cases not used for prompt tuning
data/nutrition_evidence_sources_v1/  Approved synthetic prototype sources
evaluation/                Metrics, recorded runs, locked manifests, and reports
results/evidence_retrieval/ Retrieval benchmark results
tests/                     Contract and safety tests
docs/                      Product specification and documentation index
```

See [`evaluation/README.md`](evaluation/README.md) and [`docs/README.md`](docs/README.md) for the
artifact layout and documentation index. Root-level deliverables remain in place intentionally so a
reviewer can find the reproduction guide, trajectories, execution report, changelog, and video
script without navigating the package tree.
