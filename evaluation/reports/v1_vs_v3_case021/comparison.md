# Baseline Comparison Report

- Baseline run: `20260829T034841Z` (`nutrition-baseline-v1`)
- Candidate run: `20260829T224616Z` (`nutrition-baseline-v3`)
- Model: `gpt-5-mini`
- Shared successful cases: 1

## case_021

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,219 | 1,495 | 276 |
| Output tokens | 3,959 | 4,849 | 890 |
| Visible brief characters | 10,658 | 6,851 | -3,807 |
| Visible brief words | 971 | 581 | -390 |
| Latency (s) | 44.111 | 36.044 | -8.067 |
| Estimated cost (USD) | 0.00822 | 0.01007 | 0.00185 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 6 | 5 | -1 |
| `suggested_questions` | 6 | 5 | -1 |
| `nutrition_considerations` | 5 | 3 | -2 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 4 | 3 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.750 | 0.500 | -0.250 |
| `nutrition_consideration_precision` | 0.400 | 0.667 | 0.267 |
| `nutrition_consideration_recall` | 0.500 | 1.000 | 0.500 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.500 | 0.500 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |

## Interpretation notes

- Negative token, latency, and cost deltas indicate improvement.
- Metric deltas use the current deterministic lexical evaluator and require manual review.
- Cost is estimated from the token prices passed to the comparison command.
- A shorter output is not automatically better if referral safety or relevant recall decreases.
