# Changelog

This file records relevant project changes. The project is in early development and does not yet
have a published release.

## [Unreleased]

### Current status — 2026-08-30

#### Implemented

- Four self-contained synthetic nutrition evidence sources covering vegetarian iron assessment,
  known prediabetes, sodium in known chronic kidney disease, and endurance nutrition, with explicit
  scope boundaries and an approved-source registry for prototype use.
- Deterministic Evidence Agent retrieval foundation for the approved synthetic nutrition sources:
  manifest allowlisting, Markdown section chunking, stable lexical and topic ranking, content hashes,
  empty-result support, path-containment validation, typed results, and a local search CLI.
- Fixed bilingual retrieval benchmark with positive and no-answer queries, reporting source-level
  recall and precision at ranks 1 and 3 plus no-answer accuracy.
- Cached semantic retriever using `text-embedding-3-small` at 512 dimensions, cosine similarity,
  content-hash freshness validation, batched queries, and an explicit no-answer threshold.
- Reproducible comparator running deterministic and embedding retrieval against the same benchmark
  and recording per-system metrics, latency, API requests, and embedding input tokens.
- Hybrid Evidence Agent retriever using source-level reciprocal rank fusion, semantic candidates,
  and a guarded lexical fallback requiring at least two matched terms and a minimum lexical score;
  each result records which retrieval methods contributed.
- Curated bilingual topic aliases enrich both lexical scoring and embedding representations;
  non-discriminative vocabulary is excluded from lexical matching and alias metadata participates
  in chunk fingerprints so stale semantic indexes are rejected.
- Nutrition Agent v3 frozen for reproducible development comparison, with model, effective prompt,
  component, dataset, pathway-rubric, API-run, replay, report, metric, token, cost, and latency
  fingerprints recorded in `nutrition_agent/frozen_agent.json`.
- Freeze policy requires any functional change to create `nutrition-agent-v4` and a new manifest.
- Nutrition Agent v3 compact pipeline: the model now generates only nutrition signals,
  considerations, risks, optional questions, blind spots, and limitations using source references.
- Deterministic construction of patient overview, known medical context, existing laboratories,
  information gaps, core questions, and referral flags.
- Gap Coverage Engine covering contradictions, symptom course, weight context, established
  treatment, dietary intake, activity/recovery, and consultation priorities.
- Compact references such as `symptoms[0]` replace repeated supporting-fact text; invalid or empty
  references are removed locally without another model call.
- Nutrition Signal categories, category deduplication, cross-item lexical deduplication, and
  deterministic promotion of supported signals into consultation considerations.
- General correction retries removed from v3; unsupported items are dropped with an explicit
  limitation while critical deterministic sections remain available.
- Prospective `referral-pathways-v1` development rubric records `none`, `clarify_first`, or `refer`
  without modifying the original development rubrics or locked test set.
- Pathway accuracy, clarify-first case accuracy, and supported-referral case accuracy are recorded
  for v3 runs.
- Nutrition Agent v2 with deterministic referral eligibility states (`not_indicated`,
  `clarify_first`, and `supported`), two initial supported trigger rules, and automatic conversion
  of uncertain referral contexts into priority clarification questions.
- Referral-specific evaluation for presence accuracy, unnecessary referrals, missed referrals, and
  an action-safety proxy.
- Reduced prompt duplication by sending only unreported or contradictory normalized fields rather
  than the complete normalized intake a second time.
- Nutrition Reasoning Agent v1 with normalized patient state, structured intermediate reasoning,
  deterministic safety validation, at most one feedback retry, and safe rendering to the baseline
  `BaselineBrief` contract.
- Deterministic contradiction detection, source-field and copied-fact grounding, laboratory
  fidelity, secondary-consideration grounding, and scope checks.
- Deterministic referral rendering from copied patient facts with a generic medical-evaluation
  recommendation, preventing the final flag from introducing clinical terminology or specialties.
- Agent runner with per-case progress and complete trajectories containing drafts, gate feedback,
  retries, token usage, final briefs, and metrics.
- Frozen baseline `nutrition-baseline-v4`, with its model, prompt, schema, datasets, hashes, and
  reference run recorded in `baseline/frozen_baseline.json`.
- Separate recording of `reasoning_tokens` and `visible_output_tokens`; total output usage remains
  available as `output_tokens` for usage and cost calculations.
- Rule allowing optional lists to remain empty instead of filling sections to their maximum; the
  agreed minimum of three suggested questions remains in place.
- Separate development dataset with 10 synthetic cases targeting guardrails, negative controls,
  grounding, laboratory fidelity, contradictions, and referrals.
- New deterministic evaluations for output budgets, valid source fields, and laboratory fidelity,
  plus explicitly labelled proxies for rationale length, grounding, treatment assumptions, and
  potential scope violations.
- Per-case aggregate summary in comparison reports.
- Prompts v1 through v4 stored as separate files and selectable with `--prompt-version`.
- Automated run comparator producing JSON and Markdown reports for metrics, tokens, visible size,
  latency, estimated cost, and item counts per section.
- `nutrition-baseline-v3` guardrails against generic risks, assumed facts, and referral flags that
  complete missing information.
- Requirement for two case-specific intake elements before producing a secondary nutrition
  consideration.
- Explicit distinction between unreported information and evidence of absence or insufficiency.
- `nutrition-baseline-v2` output budgets intended to reduce tokens, latency, and professional review
  burden.
- Pydantic constraints enforcing at most 5 gaps, 3–5 questions, 3 nutrition considerations, 4 risk
  factors, 2 referral flags, and 3 blind spots.
- One-sentence rationale requirement in both the prompt and schema descriptions.
- Product definition as the Nutrition Module of Health Professional Copilot.
- MVP specification at `docs/Health_Professional_Copilot_Nutrition_Module_MVP.pdf`.
- Single-LLM-call baseline with structured output.
- Original `nutrition-baseline-v1` prompt preserved alongside its reference execution manifest.
- Strict Pydantic schemas for the intake, dataset, rubric, and brief.
- Client using `OpenAI.responses.parse` for structured responses.
- Command-line runner with case selection and a `--dry-run` mode.
- Per-run manifests, outputs, failures, usage, and metrics.
- Initial deterministic lexical evaluation.
- Locked dataset with 20 synthetic cases, from `case_021` through `case_040`.
- Automated tests for datasets, prompts, rubric isolation, token comparison, freezing, and metrics.
- Initial project configuration using `uv`, environment variables, and usage documentation.

#### Verified

- Embedding retrieval at the preselected 0.45 similarity threshold improved recall@1 from 0.679 to
  0.714, precision@3 from 0.333 to 0.714, and no-answer accuracy from 0.500 to 1.000 on the fixed
  36-query benchmark; precision@1 was 0.714 and recall@3 remained 0.714.
- The embedding index required one request and 2,282 input tokens for 24 chunks; the comparison
  query batch required one request, 301 input tokens, and 4.224 seconds, versus 30 ms and no API
  usage for deterministic retrieval.
- Hybrid retrieval achieved recall@1/3 of 0.786, precision@1 of 0.786, precision@3 of 0.744, and
  no-answer accuracy of 1.000; it recovered 22 of 28 positive queries while rejecting all eight
  negative controls, outperforming both individual retrievers on this benchmark.
- After bilingual enrichment, the hybrid at the unchanged 0.45 threshold achieved recall@1/3 and
  precision@1 of 1.000, precision@3 of 0.976, and no-answer accuracy of 1.000 on the development
  benchmark. A 0.365 candidate matched recall and no-answer accuracy but reduced precision@3 to
  0.893, so 0.45 remains the selected development configuration pending locked evaluation.
- A new locked bilingual benchmark was created with 48 previously unused queries: 32 single-source
  positives, four multi-source positives, and 12 negative controls. Its SHA-256 is
  `49137514e595da147c9f3c11048dc63d5481bd4e8a76fbbad65b9f88ae6732c6`.
- The locked benchmark was executed exactly once without changing the selected configuration. The
  hybrid achieved recall@1 0.778, recall@3 0.833, precision@1 0.833, precision@3 0.819, and
  no-answer accuracy 1.000; the run used one request, 599 input tokens, and 1.670 seconds.
- Deterministic retrieval benchmark v1 across 36 fixed bilingual queries: source-level recall@1 and
  recall@3 of 0.679, precision@1 of 0.679, precision@3 of 0.333, and no-answer accuracy of 0.500.
- Retrieval found the expected source for 19 of 28 positive queries, always at rank 1 when found;
  the nine misses were Spanish paraphrases without enough lexical overlap, while four of eight
  negative controls produced false-positive retrievals.
- Agent v3 API run across 10 development cases: 10 successes, zero failures, zero retries, and one
  unsupported secondary consideration removed locally.
- Deterministic replay after gap and consideration rule refinement required no new model calls and
  achieved information-gap recall 0.892, nutrition-consideration recall 1.0, precision 0.767,
  pathway accuracy 1.0, and zero unnecessary referrals or scope proxy hits.
- V3 reduced mean cost from USD 0.00835 for the frozen baseline to USD 0.00694, latency from 50.0 to
  24.9 seconds, input tokens from 1,555 to 1,127, and visible output words from 541 to 343.
- V3 risk-factor recall remained below the frozen baseline (0.650 versus 0.733), and the deterministic
  rules may be overfit to the development cases; professional review is required before locked-test use.
- Ten-case Agent v2 experiment: 10 successes, zero failures, two corrected retries, and zero final
  unnecessary referrals.
- From Agent v1 to v2, referral precision improved from 0.30 to 0.80, presence accuracy from 0.60 to
  0.80, and information-gap recall from 0.417 to 0.583.
- V2 classified `dev_002` and `dev_009` as `clarify_first`; the existing rubric counts these safer
  pathways as missed referral flags, so referral recall remained 0.80.
- V2 did not preserve Agent v1's nutrition-consideration improvement and increased mean cost to USD
  0.01249 and latency to 67.9 seconds per case.
- Ten-case Nutrition Agent v1 experiment: 10 successes, zero failures, and two safety retries.
- Against frozen baseline v4, Agent v1 improved nutrition-consideration recall from 0.50 to 0.65,
  precision from 0.317 to 0.40, risk recall from 0.733 to 0.833, and populated-field grounding from
  0.860 to 0.973.
- Agent v1 regressed information-gap recall from 0.642 to 0.417, referral recall from 0.90 to 0.70,
  and referral precision from 0.60 to 0.30; manual inspection found unnecessary referral flags in
  negative and stable cases.
- Agent v1 averaged 5,418 output tokens, USD 0.01151, and 61.4 seconds per case versus 3,983 tokens,
  USD 0.00835, and 50.0 seconds for the frozen baseline.
- Frozen v4 run across 10 cases: 10 successes, zero failures, 23,872 reasoning tokens, and 15,953
  visible output tokens; the two components sum exactly to `output_tokens` in every case.
- Complete development experiment with v1, v2, and v3 on the same 10 cases: 30 successful calls
  and zero failures.
- V3 achieved nutrition-consideration recall/precision of 0.60/0.40 versus 0.40/0.27 for v1 and
  improved the secondary-grounding proxy from 0.65 to 0.90.
- V3 did not reduce tokens or cost: it averaged 3,930.5 output tokens and USD 0.00824 per case,
  versus 3,438.0 tokens and USD 0.00719 for v1.
- Real `case_021` execution with `nutrition-baseline-v3`: one successful case and zero failures.
- Automated v1 versus v3 comparison generated in `evaluation/reports/v1_vs_v3_case021/`.
- V3 reduced the visible brief from 10,658 to 6,851 characters and latency from 44.111 to 36.044
  seconds.
- V3 increased total output tokens from 3,959 to 4,849 and estimated cost from USD 0.00822 to USD
  0.01007; token optimization is therefore not yet achieved.
- All 20 locked cases load and validate against their schemas.
- `--dry-run` works without making external calls.
- All thirty-six automated tests pass.
- Real Nutrition Agent execution on `dev_004`: one success, zero failures, zero retries, and a fully
  accepted first safety report; manual review identified and removed diagnostic wording from the
  referral renderer before accepting the implementation.
- The installed OpenAI SDK supports structured outputs through `responses.parse`.

#### Current limitations

- Nutrition Agent v2 is safer than v1 but is not eligible to replace the frozen baseline because
  information-gap and nutrition-consideration quality remain below the acceptance criteria.
- The complete comparison was performed on the development set; the 20 locked cases have not yet
  been used to select or validate the final prompt.
- The synthetic cases and their rubrics have not received clinical validation.
- Metrics use approximate lexical matching rather than semantic evaluation.
- The baseline does not retrieve evidence; `supporting_evidence` must remain empty.
- There is no functional API, user interface, authentication, or patient storage yet.
- The Evidence Agent, Evidence Gate, and knowledge base are not yet implemented.
- Complete deterministic referral and escalation rules are still pending.

#### Proposed next steps

- Run the frozen baseline on the 20 locked cases and save the first reference report.
- Review cases and rubrics with nutrition and medical professionals.
- Add semantic evaluation and professional adjudication.
- Run the Nutrition Reasoning Agent on all development cases and compare it with the frozen baseline.
- Build the approved source registry and Evidence Agent.
- Add deterministic scope, referral, and escalation rules.
- Implement the Evidence Gate before presenting evidence-backed claims.

## [0.1.0] — Pending

The `0.1.0` version declared in `pyproject.toml` is the package's development identifier. It does
not yet represent a published release.
