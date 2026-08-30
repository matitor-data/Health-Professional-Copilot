# Nutrition Agent v2 — Development Experiment

Nutrition Agent v2 was run with `gpt-5-mini` on the same ten synthetic development cases as Agent
v1 and frozen baseline v4. All ten cases succeeded, two required the single permitted retry, and all
final drafts passed the safety gate.

## Referral changes

V2 removes referral generation from the model. A deterministic engine returns `not_indicated`,
`clarify_first`, or `supported`; only `supported` creates a final referral flag.

| Referral measure | Frozen baseline | Agent v1 | Agent v2 |
|---|---:|---:|---:|
| Referral recall | 0.90 | 0.70 | 0.80 |
| Referral precision | 0.60 | 0.30 | 0.80 |
| Presence accuracy | 0.70 | 0.60 | 0.80 |
| Unnecessary referrals per case | 0.30 | 0.40 | 0.00 |
| Missed referrals per case | 0.00 | 0.00 | 0.20 |
| Safe referral action proxy | 0.90 | 1.00 | 1.00 |

The two apparent misses are `dev_002` and `dev_009`. V2 intentionally classifies both as
`clarify_first`: treatment course is unreported in the former and rapid weight loss conflicts with
“Stable” in the latter. The existing rubric expects conditional referral flags, so it penalizes the
safer clarification pathway. This discrepancy requires prospective rubric review rather than a
post-hoc score change.

## Overall comparison

| Mean per case | Frozen baseline | Agent v1 | Agent v2 |
|---|---:|---:|---:|
| Information gap recall | 0.642 | 0.417 | 0.583 |
| Follow-up topic recall | 0.717 | 0.667 | 0.683 |
| Nutrition consideration recall | 0.500 | 0.650 | 0.450 |
| Nutrition consideration precision | 0.317 | 0.400 | 0.250 |
| Risk factor recall | 0.733 | 0.833 | 0.767 |
| Populated source-field rate | 0.860 | 0.973 | 0.926 |
| Output tokens | 3,982.5 | 5,418.1 | 5,953.0 |
| Latency (ms) | 50,040.8 | 61,435.0 | 67,892.3 |
| Estimated cost (USD) | 0.00835 | 0.01151 | 0.01249 |

V2 fixed unnecessary referrals and recovered much of v1's information-gap regression. It did not
preserve v1's nutrition-consideration gains and became more expensive because output reasoning
tokens rose despite lower input usage. V2 is safer than v1 but still does not meet the acceptance
criteria for replacing the frozen baseline.

Detailed reports are under `all_development_vs_frozen_baseline/` and `v1_vs_v2/`.
