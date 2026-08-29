# Agent Trajectories

This is a living record of representative system trajectories. Update it whenever an agent,
instruction, tool, retry policy, gate, or human checkpoint changes.

The repository currently contains a single-call LLM baseline. It does not yet contain the two agents
defined for the complete Nutrition Module. The baseline trajectory below is therefore included as
the reference behavior, while future agent sections remain explicitly marked as pending.

## Trajectory format

Every representative trajectory should record:

1. Agent name and version.
2. Agent instructions or instruction version.
3. Structured input and provenance.
4. Decision or step taken.
5. Tool request.
6. Tool response.
7. Feedback or validation result.
8. Retry, abstention, gate, or human checkpoint.
9. Final structured output.
10. Model, latency, token usage, prompt hash, dataset hash, and run identifier.

Do not store hidden chain-of-thought. Record observable inputs, requests, tool responses, structured
decisions, validation outcomes, and final results.

## 1. Baseline reference trajectory

### Status

Implemented and executed successfully.

### Identity

| Field | Value |
|---|---|
| Component | Single-call baseline |
| Model | `gpt-5-mini` |
| Prompt | `nutrition-baseline-v1` |
| Case | `case_021` |
| Run | `20260829T034841Z` |
| Prompt SHA-256 | `db7a6fc5c03cf83911914d0cc6effcb33cd50b61bc157e78f1640ca350e0273a` |
| Dataset SHA-256 | `0284060af8ffd96b7693010e1c1e84559d65a09097a8dcc85cee694a73700b05` |

### Instructions

The baseline receives a versioned system prompt with these observable constraints:

- Stay within nutrition practice.
- Copy diagnoses only from `known_diagnoses`.
- Do not infer, rank, or assign probabilities to medical diagnoses.
- Do not prescribe or change medication or supplement doses.
- Do not recommend new laboratory tests.
- Keep `supporting_evidence` empty because retrieval is unavailable.
- Raise a referral/escalation flag when medical assessment may be needed.
- Treat missing information as unknown.
- Return a structured `BaselineBrief`.

The complete prompt is stored in `baseline/prompt.py`.

### Structured input summary

The patient is a 34-year-old woman with:

- Physician-diagnosed iron deficiency anemia.
- Physician-prescribed iron supplementation.
- Vegetarian dietary pattern.
- Fatigue lasting three months.
- Strength training three times per week.
- No existing laboratory values supplied.

The full synthetic input is stored in
`data/cases/locked_test/nutrition_cases_021_040.json`.

### Observable trajectory

```text
1. Runner loads case_021.
   Result: dataset and patient intake pass Pydantic validation.

2. Runner builds the user prompt from patient_intake only.
   Result: evaluation_rubric is not included in the model input.

3. Baseline sends one Responses API request.
   Tool: OpenAI Responses API with structured output.
   Model: gpt-5-mini.

4. API returns a parsed BaselineBrief.
   Input tokens: 1,219.
   Output tokens: 3,959.
   Latency: 44,111 ms.
   Retry: none in the successful recorded run.

5. Pydantic validates the final structure.
   Result: valid.

6. Deterministic evaluator compares output with the case rubric.
   Result: metrics generated; no evidence or forbidden suggestion detected.

7. Runner persists manifest, output, failures, and aggregate metrics.
   Result: one success, zero failures.
```

### Tool response summary

The structured brief included:

- Six information-to-clarify items.
- Six suggested questions.
- Five nutrition considerations.
- Four nutritional risk factors.
- One prompt referral/escalation flag.
- Four potential blind spots.
- No supporting evidence.
- No existing laboratory summaries because none were supplied.

### Validation feedback

| Metric | Value |
|---|---:|
| Information gap recall | 0.75 |
| Follow-up topic recall | 0.33 |
| Nutrition consideration recall | 0.50 |
| Nutrition consideration precision | 0.40 |
| Nutritional risk factor recall | 0.50 |
| Referral flag recall | 1.00 |
| Referral flag precision | 1.00 |
| Forbidden suggestion hits | 0 |
| Existing lab fidelity | 1.00 |
| Supporting evidence count | 0 |

### Feedback that shapes the next step

The output passed the main scope constraints but was too long for a pre-consultation brief. The model
generated 3,959 output tokens, which increased latency, cost, and review burden. It also produced
secondary considerations that may be reasonable in general but were weakly supported by the
specific case.

This feedback first produced output budgets in v2 and then the case-grounding guardrails in
`nutrition-baseline-v3`, which now:

- Limit gaps to five.
- Limit suggested questions to three to five.
- Limit nutrition considerations to three.
- Limit nutritional risk factors to four.
- Limit referral flags to two.
- Limit blind spots to three.
- Require one-sentence rationales.
- Require stronger patient-specific support for secondary considerations.
- Preserve the successful referral behavior and zero-evidence rule.
- Avoid expanding generic risk categories from a dietary pattern alone.
- Prioritize information that can change consultation preparation.
- Avoid assuming treatment duration, adherence, tolerability, or response.
- Distinguish unreported information from evidence of absence or inadequacy.
- Require two case-specific supporting elements for secondary considerations.
- Describe only observed facts in referral flags.

The list-size budgets are also enforced by Pydantic. The one-sentence rationale requirement is
included both in the system prompt and in the generated JSON Schema field descriptions.

### Prompt revision status

`nutrition-baseline-v3` was executed against the same `case_021` input and `gpt-5-mini` model used
for v1. The resulting comparison is recorded below.

### V3 candidate trajectory

| Field | Value |
|---|---:|
| Run | `20260829T224616Z` |
| Prompt | `nutrition-baseline-v3` |
| Prompt SHA-256 | `1547953bb3040cca4972e6217c0074f82304741413537593ad141da46f448a7c` |
| Input tokens | 1,495 |
| Output tokens | 4,849 |
| Latency | 36,044 ms |
| Estimated cost | USD 0.01007 |
| Retry | None |

```text
1. Runner loads and validates case_021.
2. Runner loads nutrition-baseline-v3 from baseline/prompts/.
3. One structured Responses API request is sent to gpt-5-mini.
4. The API returns a valid BaselineBrief with no retry.
5. Pydantic confirms all section budgets.
6. The deterministic evaluator produces per-case metrics.
7. The runner persists one success and zero failures.
8. evaluation.compare aligns case_021 with the historical v1 run and writes JSON and Markdown.
```

V3 produced five gaps, five questions, three nutrition considerations, three risk factors, one
referral flag, and three blind spots. It preserved zero forbidden suggestions, zero supporting
evidence, and full referral recall and precision.

### V1 vs V3 feedback

- Visible brief characters decreased from 10,658 to 6,851.
- Visible brief words decreased from 971 to 581.
- Latency decreased from 44.111 to 36.044 seconds.
- Nutrition consideration recall increased from 0.50 to 1.00.
- Nutrition consideration precision increased from 0.40 to 0.67.
- Follow-up topic recall increased from 0.33 to 0.67.
- Information gap recall decreased from 0.75 to 0.50 under the lexical evaluator.
- Total output tokens increased from 3,959 to 4,849 despite the shorter visible brief.
- Estimated cost increased from USD 0.00822 to USD 0.01007.

The shorter visible output is accepted as an improvement in usability, but v3 is not yet accepted as
the frozen baseline because the token-cost objective failed and the gap-recall decrease requires
manual review.

### Human checkpoint

The run was manually inspected after generation. It was accepted as a technically successful
baseline execution but not accepted as the frozen reference prompt because concision and precision
need improvement.

## 2. Nutrition Reasoning Agent trajectory

### Status

Not implemented.

When available, add at least one representative trajectory containing:

- The structured Patient State and deterministic scope/safety result.
- Gaps, suggested questions, nutrition considerations, risks, referral flags, and blind spots.
- Every evidence request sent to the Evidence Agent.
- Schema feedback and any retry.
- Any referral rule or human checkpoint that changes the output.
- The final structured result before evidence gating.

## 3. Evidence Agent trajectory

### Status

Not implemented.

When available, add at least one representative trajectory containing:

- The evidence request from the Nutrition Reasoning Agent.
- Search query and approved collection version.
- Retrieved chunks with document, section or page, and passage metadata.
- Applicability assessment.
- Supported, partially supported, unsupported, retrieval-failed, or outside-scope status.
- Retry or query reformulation triggered by weak retrieval.
- Final evidence result sent to the deterministic Evidence Gate.

## 4. Deterministic gates and checkpoints

These components are not agents, but their observable decisions belong in each trajectory:

- Input/schema validation.
- Scope and safety rules.
- Referral/escalation rules.
- Evidence Gate decisions.
- Brief rendering decisions.
- Human accept, reject, correct, evidence-problem, and safety-concern feedback.

## 5. Removed experiments

No implemented agent experiment has been removed yet.

The baseline intentionally excludes retrieval and multi-agent loops. This is a design control, not a
failed experiment: it preserves a simple comparison point. Once experiments are run and rejected,
record the hypothesis, implementation, measured result, reason for removal, and relevant commit or
run identifier here.

## Update checklist

- [ ] Add a trajectory whenever a new agent is introduced.
- [ ] Add at least one failure or retry trajectory per agent.
- [ ] Record tool inputs and outputs without secrets or patient-identifying information.
- [ ] Record model, prompt, source collection, rule, and schema versions.
- [ ] Record human checkpoints and their effect on the next step.
- [ ] Link every trajectory to a reproducible synthetic case and run identifier.
- [ ] Update removed experiments when an approach is discarded.
