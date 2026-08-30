# Baseline Comparison Report

- Baseline run: `20260829T232323Z` (`nutrition-baseline-v4`)
- Candidate run: `20260829T234753Z` (`nutrition-agent-v1`)
- Model: `gpt-5-mini`
- Shared successful cases: 1

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1553.00000 | 1908.00000 | 355.00000 |
| Output tokens | 4402.00000 | 4436.00000 | 34.00000 |
| Reasoning tokens | 2496.00000 | 2240.00000 | -256.00000 |
| Visible output tokens | 1906.00000 | 2196.00000 | 290.00000 |
| Latency (ms) | 61556.00000 | 48861.00000 | -12695.00000 |
| Estimated cost (USD) | 0.00919 | 0.00935 | 0.00016 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
| `forbidden_suggestion_hits` | 0.000 | 0.000 | 0.000 |
| `information_gap_recall` | 0.667 | 0.333 | -0.333 |
| `nutrition_consideration_precision` | 0.333 | 0.500 | 0.167 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,553 | 1,908 | 355 |
| Output tokens | 4,402 | 4,436 | 34 |
| Reasoning tokens | 2,496 | 2,240 | -256 |
| Visible output tokens | 1,906 | 2,196 | 290 |
| Visible brief characters | 7,604 | 5,979 | -1,625 |
| Visible brief words | 686 | 565 | -121 |
| Latency (s) | 61.556 | 48.861 | -12.695 |
| Estimated cost (USD) | 0.00919 | 0.00935 | 0.00016 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.333 | -0.333 |
| `nutrition_consideration_precision` | 0.333 | 0.500 | 0.167 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## Interpretation notes

- Negative token, latency, and cost deltas indicate improvement.
- Metric deltas use the current deterministic lexical evaluator and require manual review.
- Cost is estimated from the token prices passed to the comparison command.
- A shorter output is not automatically better if referral safety or relevant recall decreases.
