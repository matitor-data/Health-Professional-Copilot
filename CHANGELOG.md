# Changelog

This file records relevant project changes. The project is in early development and does not yet
have a published release.

## [Unreleased]

### Current status — 2026-08-29

#### Implemented

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
- All eleven automated tests pass.
- The installed OpenAI SDK supports structured outputs through `responses.parse`.

#### Current limitations

- The complete comparison was performed on the development set; the 20 locked cases have not yet
  been used to select or validate the final prompt.
- The synthetic cases and their rubrics have not received clinical validation.
- Metrics use approximate lexical matching rather than semantic evaluation.
- The baseline does not retrieve evidence; `supporting_evidence` must remain empty.
- There is no functional API, user interface, authentication, or patient storage yet.
- The Nutrition Reasoning Agent, Evidence Agent, Evidence Gate, and knowledge base are not yet
  implemented.
- Complete deterministic referral and escalation rules are still pending.

#### Proposed next steps

- Run the frozen baseline on the 20 locked cases and save the first reference report.
- Review cases and rubrics with nutrition and medical professionals.
- Add semantic evaluation and professional adjudication.
- Implement the Nutrition Reasoning Agent and compare it with the frozen baseline.
- Build the approved source registry and Evidence Agent.
- Add deterministic scope, referral, and escalation rules.
- Implement the Evidence Gate before presenting evidence-backed claims.

## [0.1.0] — Pending

The `0.1.0` version declared in `pyproject.toml` is the package's development identifier. It does
not yet represent a published release.
