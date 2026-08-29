# Development Prompt Experiment

## Setup

The experiment ran `nutrition-baseline-v1`, `v2`, and `v3` with `gpt-5-mini` on the same 10
development cases. All versions used the current structured-output schema, so this isolates prompt
instructions under common section-size constraints. It does not recreate the original unconstrained
v1 schema. The cases are synthetic and have not been clinically validated.

All 30 API calls succeeded without retries. Estimated total cost was USD 0.23562 using USD 0.25 per
million input tokens and USD 2.00 per million output tokens.

## Aggregate results

| Measure (mean per case) | v1 | v2 | v3 |
|---|---:|---:|---:|
| Input tokens | 1,256.8 | 1,338.8 | 1,504.8 |
| Output tokens | 3,438.0 | 3,899.7 | 3,930.5 |
| Visible brief words | 616.3 | 583.8 | 584.0 |
| Estimated cost (USD) | 0.00719 | 0.00813 | 0.00824 |
| Nutrition consideration recall | 0.40 | 0.50 | 0.60 |
| Nutrition consideration precision | 0.27 | 0.30 | 0.40 |
| Referral flag recall | 1.00 | 0.90 | 0.90 |
| Referral flag precision | 0.80 | 0.60 | 0.65 |
| Populated source-field rate | 0.89 | 0.89 | 0.98 |
| Secondary-consideration grounding proxy | 0.65 | 0.85 | 0.90 |
| Scope-violation proxy hits | 0.40 | 0.40 | 0.30 |

## Interpretation

In the three-version experiment, v3 was the strongest candidate for nutrition considerations and grounding: compared with v1, recall
rose by 0.20, precision by 0.13, populated source-field rate by 0.09, and the secondary-grounding
proxy by 0.25. It also produced one fewer risk factor per case and about 32 fewer visible words.

The trade-off is unresolved. V3 used 492.5 more output tokens and cost about USD 0.00105 more per
case than v1. Referral recall fell from 1.00 to 0.90 and precision from 0.80 to 0.65. These lexical
scores require case-level human review before choosing a prompt. V3 should therefore remain a
development candidate rather than a frozen baseline. V4 was subsequently frozen after adding the
empty-section rule; its reference run and hashes are recorded in `baseline/frozen_baseline.json`,
and its comparison with v3 is under `v3_vs_frozen_v4/`.

Metrics ending in `_proxy` are heuristic warning signals, not semantic or clinical judgments.
Lexical recall/precision can miss valid paraphrases and count superficial token overlap. Empty
expected lists also make negative controls especially important to inspect manually.

## Artifacts

- `v1_vs_v2/comparison.{json,md}`
- `v1_vs_v3/comparison.{json,md}`
- `v2_vs_v3/comparison.{json,md}`
