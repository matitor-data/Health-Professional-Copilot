# Nutrition Module Baseline

## What the baseline is

The baseline is the simplest version of the system for testing whether a language model can help
prepare for a nutrition consultation.

It is not intended to represent the final product. It serves as a comparison point: after adding
the two agents, evidence retrieval, and advanced safety rules, we can measure whether they actually
improve results over this simple implementation.

## How it works

The flow has four steps:

```text
Structured patient data
          ↓
  A versioned prompt
          ↓
    One LLM call
          ↓
Pydantic-validated brief
```

1. The runner loads one or more cases from the dataset.
2. Patient data is validated before being sent to the model.
3. The model receives a single prompt containing the Nutrition Module rules.
4. The response is converted into a structured brief and validated.
5. The brief is compared with the case's expected rubric.
6. Results, errors, and metrics are stored in a timestamped directory.

The baseline does not use tools, retrieval, a knowledge base, an Evidence Agent, an Evidence Gate,
or autonomous loops. Each patient produces at most one model call.

## Input information

Each case contains information such as:

- Age, sex, height, and weight.
- Reason for consultation and primary goal.
- Known medical diagnoses.
- Symptoms and duration.
- Medications and supplements.
- Dietary pattern, physical activity, and sleep.
- Recent weight changes.
- Existing laboratory results.
- Family history and additional notes.

Known diagnoses are input context. The baseline cannot invent, infer, or propose a medical
diagnosis.

## Brief contents

The output follows a fixed structure:

- `patient_overview`: a concise summary of the case.
- `known_medical_context`: diagnoses and medical context already reported.
- `information_to_clarify`: missing, ambiguous, or contradictory information.
- `suggested_questions`: between 3 and 5 high-value questions.
- `nutrition_considerations`: nutrition-related topics to review during the consultation.
- `nutritional_risk_factors`: risk factors relevant to the nutrition assessment.
- `referral_escalation_flags`: situations that may require medical evaluation.
- `potential_blind_spots`: areas that could otherwise be overlooked.
- `supporting_evidence`: remains empty because the baseline does not use retrieval.
- `relevant_existing_labs`: reproduces existing results without altering them.
- `limitations`: insufficient information or elements outside the module's scope.

Every generated consideration must identify the patient fields that motivated it.

The frozen `nutrition-baseline-v4` limits the brief to at most 5 gaps, 3 nutrition considerations,
4 risk factors, 2 referral flags, and 3 blind spots. Every rationale must consist of one concise
sentence.

These limits are ceilings, not targets. Optional lists may remain empty when the intake contains no
relevant and supported item; `suggested_questions` retains a range of 3 to 5 questions. Each run
records reasoning tokens and visible output tokens separately.

The baseline also avoids expanding generic risks from a dietary pattern, prioritizes only
information that could change the consultation, prohibits assumptions about treatment adherence or
response, distinguishes unreported information from evidence of absence, requires two specific
elements for secondary considerations, and requires every referral flag to describe only observed
facts.

## Safety boundaries

The prompt establishes that the baseline:

- Does not diagnose or propose disease probabilities.
- Does not add diagnoses that are absent from `known_diagnoses`.
- Does not prescribe or modify medications or supplement doses.
- Does not recommend ordering new laboratory tests.
- Does not invent sources or citations.
- Does not interpret missing information as a negative finding.
- May indicate that the patient could require medical evaluation without asserting a diagnosis.
- Must abstain when information is insufficient or outside nutrition scope.

## Dataset

The current dataset is located at:

```text
data/cases/locked_test/nutrition_cases_021_040.json
```

It contains 20 synthetic cases (`case_021` through `case_040`). Each case includes a patient intake
and a rubric with the expected concepts. The data was generated synthetically and has not been
clinically validated.

This file is treated as a locked set and should not be used to adjust the prompt. Cases created for
prompt experiments must be stored in a separate development set.

## Evaluation

The current evaluation approximately measures:

- Information-gap recall.
- Follow-up topic recall.
- Nutrition-consideration recall and precision.
- Nutritional risk-factor recall.
- Referral-flag recall and precision.
- Existing laboratory fidelity.
- Explicitly prohibited suggestions.
- The amount of generated evidence, which must be zero.

The current comparison is lexical: it searches for overlap between expected and generated concepts.
It is useful for producing reproducible results, but it does not replace semantic evaluation or
review by nutrition and medical professionals.

## Main files

```text
baseline/schemas.py     Input, dataset, and brief models
baseline/prompt.py      System rules and versioned prompt
baseline/client.py      Structured OpenAI call
baseline/runner.py      CLI, execution, and result persistence
evaluation/metrics.py   Initial deterministic metrics
tests/test_baseline.py  Contract and constraint tests
```

## How to run it

First, configure `OPENAI_API_KEY` in a `.env` file.

Validate the cases without making API calls:

```bash
uv run python -m baseline.runner --dry-run
```

Run one case:

```bash
uv run python -m baseline.runner --case-id case_021
```

Run all 20 cases:

```bash
uv run python -m baseline.runner
```

Each real execution creates:

```text
evaluation/runs/<run_id>/
├── manifest.json
├── outputs.jsonl
├── failures.jsonl
└── metrics.json
```

The manifest records the model, prompt version and hash, dataset and hash, and evaluated cases. This
makes it possible to compare executions reproducibly.

## What is missing from the complete MVP

The baseline does not include:

- Separate Nutrition Reasoning Agent and Evidence Agent components.
- Approved and versioned clinical sources.
- Extraction, chunking, embeddings, or retrieval.
- Evidence applicability validation.
- Evidence Gate.
- Complete deterministic referral and escalation rules.
- API and frontend.
- Patient persistence and authentication.
- Clinical evaluation of cases and results.

These components must be compared against the baseline before they are incorporated permanently.
