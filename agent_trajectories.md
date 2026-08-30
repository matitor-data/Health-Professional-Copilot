# Agent Trajectories

This is a living record of representative system trajectories. Update it whenever an agent,
instruction, tool, retry policy, gate, or human checkpoint changes.

The repository contains the single-call baseline, the frozen Nutrition Agent, and the Evidence
Agent. The baseline trajectory remains the reference behavior for comparisons.

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

### Ten-case development trajectory

| Prompt | Run | Successful | Failed | Retry |
|---|---|---:|---:|---|
| `nutrition-baseline-v1` | `20260829T230906Z` | 10 | 0 | None |
| `nutrition-baseline-v2` | `20260829T230902Z` | 10 | 0 | None |
| `nutrition-baseline-v3` | `20260829T230907Z` | 10 | 0 | None |
| `nutrition-baseline-v4` | `20260829T232323Z` | 10 | 0 | None |

```text
1. The runner validated nutrition_cases_dev.json against EvaluationDataset.
2. For each prompt version it sent the same ten patient intakes to gpt-5-mini.
3. The API returned a structured BaselineBrief for every request; no retry was needed.
4. Pydantic enforced the common output budgets.
5. The evaluator calculated lexical metrics, deterministic checks, and labelled proxies.
6. The runner saved manifests, outputs, failures, and aggregate metrics locally.
7. The comparison tool aligned all ten shared case IDs and generated three pairwise reports.
8. Human checkpoint: v3 remains a candidate because grounding improved but token cost rose and
   referral scores require manual adjudication.
```

The development runs contain synthetic patient data only. Raw run artifacts remain git-ignored;
the aggregate and case-level comparison reports are retained under `evaluation/reports/development/`.

V4 added the instruction not to fill optional sections to their maximum and became the frozen
baseline. Its reference run recorded 39,825 output tokens: 23,872 reasoning tokens and 15,953
visible output tokens. The arithmetic was checked for every case, with no mismatches.

## 2. Nutrition Reasoning Agent trajectory

### Status

Implemented as `nutrition-agent-v1`; evidence retrieval remains pending.

### Representative execution

| Field | Value |
|---|---:|
| Synthetic case | `dev_004` |
| Run | `20260829T234753Z` |
| Model | `gpt-5-mini` |
| Successful / failed | 1 / 0 |
| Safety retries | 0 |
| Input tokens | 1,908 |
| Output tokens | 4,436 |
| Reasoning tokens | 2,240 |
| Visible output tokens | 2,196 |
| Latency | 45,856 ms |

```text
1. EvaluationDataset validates the synthetic patient intake.
2. PatientState marks reported and unreported fields, derives a non-diagnostic BMI, and checks
   contradictions.
3. nutrition-agent-v1 receives only the intake and normalized state.
4. The API returns a valid NutritionReasoningResult.
5. The deterministic gate verifies copied facts, populated source fields, secondary grounding,
   scope patterns, and exact existing-lab fidelity.
6. The first safety report is accepted, so no retry is sent.
7. The renderer converts the draft to BaselineBrief and the common evaluator calculates metrics.
8. The runner stores the patient state, draft, gate report, response identifiers, final brief,
   tokens, latency, and metrics locally.
```

### Human checkpoint and resulting change

An earlier run (`20260829T234525Z`) changed the observed phrase “food feels stuck” to
the clinical term “dysphagia” and named medical specialties in its referral recommendation. The
lexical gate had not caught this transformation. The final referral renderer was therefore changed
to build its trigger only from verbatim `supporting_patient_facts` and to use a fixed, generic
medical-evaluation recommendation determined by urgency. Run `20260829T234753Z` then verified the
corrected final trigger using only four copied intake facts and the recommendation “Seek prompt
medical evaluation.” It achieved referral recall and precision of 1.0 on this case with zero scope
proxy hits and no retry.

### Ten-case experiment trajectory

| Field | Value |
|---|---:|
| Run | `20260829T235358Z` |
| Successful / failed | 10 / 0 |
| Cases with retry | 2 |
| Total input tokens | 27,033 |
| Total output tokens | 54,181 |
| Reasoning / visible output tokens | 31,360 / 22,821 |
| Sum of per-case latency | 614,350 ms |

`dev_006` retried after the first draft referenced a derived BMI as though it were a patient field
and failed verbatim-fact grounding. `dev_007` retried after a referral candidate recommended a new
investigation. Both corrected drafts passed the gate.

The aggregate comparison improved nutrition-consideration recall/precision and patient-field
grounding, but referral recall/precision and information-gap recall regressed. Human inspection
identified unnecessary referrals in stable or negative-control cases. The checkpoint decision is
to reject Agent v1 as a baseline replacement and add deterministic referral eligibility rules
before rerunning the experiment.

### Agent v2 ten-case trajectory

| Field | Value |
|---|---:|
| Run | `20260830T003855Z` |
| Successful / failed | 10 / 0 |
| Cases with retry | 2 |
| Total input tokens | 23,314 |
| Total output tokens | 59,530 |
| Reasoning / visible output tokens | 35,648 / 23,882 |
| Sum of per-case latency | 678,923 ms |

V2 replaced model-selected referrals with deterministic eligibility decisions. It returned six
`not_indicated`, two `clarify_first`, and two `supported` decisions. This removed every unnecessary
referral observed in v1. `dev_002` retried after a medication-change scope violation and `dev_010`
retried after unsupported facts and secondary-grounding violations; both corrections passed.

Compared with v1, referral precision rose from 0.30 to 0.80 and gap recall from 0.417 to 0.583.
Nutrition-consideration recall fell from 0.65 to 0.45, and mean cost and latency increased. The
human checkpoint keeps the deterministic referral engine but rejects v2 as a baseline replacement.
The two rubric-level referral misses are `clarify_first` cases, which should be reviewed
prospectively rather than relabelled after observing the score.

### Agent v3 compact trajectory

| Field | Value |
|---|---:|
| API run | `20260830T010612Z` |
| Final deterministic replay | `20260830T011416Z` |
| Successful / failed | 10 / 0 |
| Retries | 0 |
| Total input / output tokens | 11,265 / 33,307 |
| Reasoning / visible output tokens | 25,856 / 7,451 |
| Sum of per-case latency | 249,232 ms |
| Items removed locally | 1 |

V3 made one compact model call per case. Source references were resolved locally; overview, known
medical context, existing labs, gaps, questions, referrals, and supported considerations were
rendered deterministically. The first deterministic output exposed generic gap wording, so the
stored drafts were replayed after adding signal-driven coverage rules without another API call.
The final checkpoint accepts v3 for a one-time locked synthetic prototype comparison. Because the
rules were tuned against the development rubrics and may be overfit, the result cannot be treated as
clinical validation or used for patient care.

### Frozen Agent v3 checkpoint

Agent v3 was frozen on 2026-08-30 in `nutrition_agent/frozen_agent.json`. The manifest records the
effective prompt, component files, schemas, development dataset, prospective pathway rubric,
reference API run, deterministic replay, comparison report, metrics, token usage, cost, and latency
by SHA-256 where applicable. Any functional change now requires `nutrition-agent-v4`; v3 remains a
fixed comparison point and is not represented as clinically validated.

## 3. Evidence Agent trajectory

### Status

Implemented and executed on synthetic development case `dev_003` in run
`evaluation/evidence_agent_runs/20260830T051645Z/`.

The frozen Nutrition Agent produced three considerations. Evidence Agent v1 created one query per
consideration, retrieved at most three approved chunks through the hybrid retriever, and evaluated
all three packets in one structured call. It returned two `supported` assessments and one
`partially_supported` assessment. The deterministic Evidence Gate confirmed that every cited chunk
had been retrieved for the corresponding consideration, and the final renderer populated
`supporting_evidence` without modifying the Nutrition Agent sections.

The evidence stage used 92 embedding input tokens, 1,462 model input tokens, 2,033 output tokens
(1,472 reasoning and 561 visible), and 43,830 ms. The observable trajectory includes the exact
queries, scores, retrieval methods, chunk hashes, model draft, finalized assessments, gate report,
and final brief. Human review found a valid but unnecessary secondary iron citation in the fiber
assessment; the next prompt version now requires the minimum necessary set of citations.

A second successful diagnostic run exists at `20260830T052052Z` because the command runner delayed
displaying completion from the first execution. It was not an Evidence Agent retry or a gate-driven
correction; both runs completed with one Nutrition Agent call, one embedding request, one Evidence
Agent call, and zero application-level retries.

### Ten-case Evidence Agent checkpoint

Run `20260830T053131Z` executed the complete two-agent pipeline on all ten development cases with 10
successes and zero failures. Across 20 nutrition considerations, the Evidence Agent produced 10
`supported`, four `partially_supported`, three `unsupported`, and three `retrieval_failed`
assessments. All ten gates accepted the safe final state; the only gate events were three expected,
non-blocking empty-retrieval notices. Eighteen cited references matched retrieved chunks, while six
unsupported or unresolved considerations were excluded from final `supporting_evidence`.

Manual review retained one open quality finding: `dev_003/NC-03` cited a secondary iron chunk that
was related but unnecessary. No retry was performed and the prompt or retrieval configuration was
not changed during the run. Aggregate counts and token usage are stored in the run's `summary.json`.

The earlier command-runner invocation also completed silently as run `20260830T052956Z`, producing
another 10 successes and zero failures. It returned 22 assessments (12 supported, six partially
supported, three retrieval-failed, and one outside-source-scope), compared with 20 assessments in
the reference run. Both had three safe empty-retrieval events and no blocking gate violations. This
was an infrastructure-level duplicate rather than an agent retry, but the differing consideration
and support distributions are evidence of run-to-run model variability that requires evaluation.

The reproducible stability report is stored at
`evaluation/reports/evidence_agent/development_measurements_v1.json`. It records perfect structural
safety metrics in both runs but a consideration-alignment F1 of 0.619 and support-status agreement
of 0.846 among aligned items. Exact repeated considerations disagreed in `dev_001` and `dev_005`,
so Evidence Agent v1.1 remains a development candidate rather than a frozen component.

### Fixed-input evidence checkpoint

The development rubric in `data/evaluations/evidence_agent/evidence_assessment_rubric_v1.json`
labels the 20 exact considerations from reference run `20260830T053131Z`. The fixed runner bypasses
the Nutrition Agent and submits those same briefs to retrieval and Evidence Agent v1.1. This makes
the remaining variation attributable to the evidence stage.

Initial fixed runs exposed two problems: empty retrieval was always called `retrieval_failed`, even
when the source collection did not cover the topic, and lexical fallback could attach a secondary
source whose generic words matched but whose registered topic did not. Human review prompted two
general corrections: collection-aware empty-result states and topic/alias eligibility for lexical
fallback. No rubric label, source text, embedding threshold, or prompt was changed between the two
post-correction repetitions.

Runs `20260830T061425Z` and `20260830T151601Z` each completed all ten cases without retries or gate
failures. They produced the same 20 consideration texts and the same 15 citations; consideration
alignment, exact-text matching, and citation-set agreement were all 1.0. Support-state agreement was
0.85, with three disagreements. Rubric status accuracy was 0.80 and 0.75, required-source recall was
0.833 in both, allowed-source precision was 0.733 in both, and each run retained three unnecessary
citations. The checkpoint therefore confirms structural and citation stability but does not justify
freezing the Evidence Agent's semantic classification.

An attempted repetition at `20260830T151125Z` recorded ten `APIConnectionError` failures inside the
restricted environment. It was repeated with authorized API access as `20260830T151601Z`; this was
an infrastructure retry, not model feedback or a gate correction.

### Frozen Evidence Agent checkpoint and demonstration

Evidence Agent v1.1 was frozen on 2026-08-30 in `evidence_agent/frozen_agent.json` for synthetic
prototype comparison. The manifest fingerprints the prompt, functional code, retrieval settings,
source registry, embedding index, development rubric, reference report, fixed-input runs, and
demonstration. Any functional change requires `evidence-agent-v2`.

Run `evaluation/evidence_demo_runs/20260830T153611Z/` records the official one-case demonstration
for `dev_003`. Nutrition Agent produced three considerations in one model call. Hybrid retrieval
returned the permitted synthetic evidence packets, Evidence Agent classified two considerations as
`supported` and one as `partially_supported`, and the deterministic gate accepted the result with
no violations. The final brief contains three traceable evidence entries and preserves every
pre-evidence nutrition section.

The Nutrition stage used 1,070 input tokens and 3,400 output tokens (2,624 reasoning and 776 visible)
in 42.605 seconds. The evidence stage used 84 embedding tokens, 1,263 model input tokens, and 1,768
model output tokens (1,280 reasoning and 488 visible) in 18.193 seconds. This is a representative
synthetic trajectory, not a claim of clinical validity.

### Locked end-to-end trajectory

The frozen baseline and complete module were each executed once on the 20 locked synthetic cases.
Baseline run `20260830T155457Z` and solution run `20260830T161328Z` both completed 20/20 cases with
zero failures. No prompt, rule, source, index, model, or retrieval setting was changed after results
were observed, and neither system was rerun.

The locked lexical metrics rejected the primary quality hypothesis: the complete module produced
lower information-gap, consideration, risk-factor, and referral recall than the baseline. It did
reduce the scope-violation proxy from 0.15 to zero, reduce visible tokens by about 35%, preserve zero
unnecessary referrals, and achieve 1.0 Evidence Gate acceptance and citation provenance validity.
Mean cost rose by about 12% and mean latency by about 19%. Full hashes and results are recorded in
`evaluation/locked_execution_manifest_v1.json` and `execution_report.md`.

## 4. Deterministic gates and checkpoints

These components are not agents, but their observable decisions belong in each trajectory:

- Input/schema validation.
- Scope and safety rules.
- Referral/escalation rules.
- Evidence Gate decisions.
- Brief rendering decisions.
- Human accept, reject, correct, evidence-problem, and safety-concern feedback.

## 5. Removed experiments

The general model correction loop used by earlier Nutrition Agent versions was removed in v3.
Invalid optional items are now removed deterministically and core sections are rendered locally.
This reduced retry-driven cost and variability while retaining explicit limitations in the output.

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
