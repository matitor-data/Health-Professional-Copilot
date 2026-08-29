# Baseline Comparison Report

- Baseline run: `20260829T230907Z` (`nutrition-baseline-v3`)
- Candidate run: `20260829T232323Z` (`nutrition-baseline-v4`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1504.80000 | 1554.80000 | 50.00000 |
| Output tokens | 3930.50000 | 3982.50000 | 52.00000 |
| Reasoning tokens | n/a | 2387.20000 | n/a |
| Visible output tokens | n/a | 1595.30000 | n/a |
| Latency (ms) | 25944.00000 | 50040.80000 | 24096.80000 |
| Estimated cost (USD) | 0.00824 | 0.00835 | 0.00012 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.508 | 0.717 | 0.208 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.667 | 0.642 | -0.025 |
| `nutrition_consideration_precision` | 0.400 | 0.317 | -0.083 |
| `nutrition_consideration_recall` | 0.600 | 0.500 | -0.100 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.982 | 0.860 | -0.123 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.650 | 0.600 | -0.050 |
| `referral_flag_recall` | 0.900 | 0.900 | 0.000 |
| `risk_factor_recall` | 0.717 | 0.733 | 0.017 |
| `scope_violation_proxy_hits` | 0.300 | 0.100 | -0.200 |
| `secondary_consideration_grounding_proxy` | 0.900 | 1.000 | 0.100 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,494 | 1,544 | 50 |
| Output tokens | 3,614 | 3,635 | 21 |
| Reasoning tokens | n/a | 2,304 | n/a |
| Visible output tokens | n/a | 1,331 | n/a |
| Visible brief characters | 6,520 | 4,887 | -1,633 |
| Visible brief words | 591 | 421 | -170 |
| Latency (s) | 23.579 | 51.322 | 27.743 |
| Estimated cost (USD) | 0.00760 | 0.00766 | 0.00005 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.900 | 0.667 | -0.233 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.500 | 1.000 | 0.500 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_002

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,510 | 1,560 | 50 |
| Output tokens | 3,307 | 4,277 | 970 |
| Reasoning tokens | n/a | 2,624 | n/a |
| Visible output tokens | n/a | 1,653 | n/a |
| Visible brief characters | 6,493 | 6,439 | -54 |
| Visible brief words | 586 | 567 | -19 |
| Latency (s) | 22.232 | 59.683 | 37.451 |
| Estimated cost (USD) | 0.00699 | 0.00894 | 0.00195 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 0.667 | 1.000 | 0.333 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.923 | 0.929 | 0.005 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `risk_factor_recall` | 0.000 | 0.500 | 0.500 |
| `scope_violation_proxy_hits` | 2 | 1 | -1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,547 | 1,597 | 50 |
| Output tokens | 3,994 | 4,236 | 242 |
| Reasoning tokens | n/a | 2,560 | n/a |
| Visible output tokens | n/a | 1,676 | n/a |
| Visible brief characters | 6,400 | 6,278 | -122 |
| Visible brief words | 523 | 536 | 13 |
| Latency (s) | 28.858 | 67.861 | 39.003 |
| Estimated cost (USD) | 0.00837 | 0.00887 | 0.00050 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 0 | 1 | +1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 0.500 | 0.000 |
| `nutrition_consideration_precision` | 0.333 | 0.500 | 0.167 |
| `nutrition_consideration_recall` | 0.500 | 0.500 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,503 | 1,553 | 50 |
| Output tokens | 5,853 | 4,402 | -1,451 |
| Reasoning tokens | n/a | 2,496 | n/a |
| Visible output tokens | n/a | 1,906 | n/a |
| Visible brief characters | 7,931 | 7,604 | -327 |
| Visible brief words | 718 | 686 | -32 |
| Latency (s) | 39.985 | 61.556 | 21.571 |
| Estimated cost (USD) | 0.01208 | 0.00919 | -0.00289 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 2 | 1 | -1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.667 | 0.333 |
| `nutrition_consideration_precision` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.500 | 1.000 | 0.500 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_005

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,503 | 1,553 | 50 |
| Output tokens | 4,311 | 3,734 | -577 |
| Reasoning tokens | n/a | 2,112 | n/a |
| Visible output tokens | n/a | 1,622 | n/a |
| Visible brief characters | 7,437 | 6,273 | -1,164 |
| Visible brief words | 676 | 561 | -115 |
| Latency (s) | 29.366 | 46.361 | 16.995 |
| Estimated cost (USD) | 0.00900 | 0.00786 | -0.00114 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 2 | 1 | -1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.500 | -0.500 |
| `nutrition_consideration_precision` | 0.333 | 0.000 | -0.333 |
| `nutrition_consideration_recall` | 1.000 | 0.000 | -1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.667 | 0.667 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_006

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,493 | 1,543 | 50 |
| Output tokens | 4,116 | 4,303 | 187 |
| Reasoning tokens | n/a | 2,496 | n/a |
| Visible output tokens | n/a | 1,807 | n/a |
| Visible brief characters | 6,516 | 7,215 | 699 |
| Visible brief words | 573 | 636 | 63 |
| Latency (s) | 26.547 | 44.361 | 17.814 |
| Estimated cost (USD) | 0.00861 | 0.00899 | 0.00039 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 4 | +1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
| `forbidden_suggestion_hits` | 1 | 1 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_precision` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_recall` | 0.500 | 0.500 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.500 | 1.000 | 0.500 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,540 | 1,590 | 50 |
| Output tokens | 4,258 | 4,590 | 332 |
| Reasoning tokens | n/a | 2,944 | n/a |
| Visible output tokens | n/a | 1,646 | n/a |
| Visible brief characters | 7,638 | 6,165 | -1,473 |
| Visible brief words | 718 | 560 | -158 |
| Latency (s) | 26.550 | 51.720 | 25.170 |
| Estimated cost (USD) | 0.00890 | 0.00958 | 0.00068 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 2 | 1 | -1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.500 | 0.500 | 0.000 |
| `scope_violation_proxy_hits` | 1 | 0 | -1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,460 | 1,510 | 50 |
| Output tokens | 2,281 | 2,956 | 675 |
| Reasoning tokens | n/a | 1,856 | n/a |
| Visible output tokens | n/a | 1,100 | n/a |
| Visible brief characters | 3,262 | 4,208 | 946 |
| Visible brief words | 244 | 348 | 104 |
| Latency (s) | 14.232 | 35.258 | 21.026 |
| Estimated cost (USD) | 0.00493 | 0.00629 | 0.00136 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 3 | 4 | +1 |
| `nutrition_considerations` | 0 | 1 | +1 |
| `nutritional_risk_factors` | 0 | 1 | +1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.250 | 0.500 | 0.250 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 0.750 | 0.250 |
| `nutrition_consideration_precision` | 1.000 | 0.000 | -1.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 0.000 | -1.000 |
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

## dev_009

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,496 | 1,546 | 50 |
| Output tokens | 3,877 | 3,974 | 97 |
| Reasoning tokens | n/a | 2,368 | n/a |
| Visible output tokens | n/a | 1,606 | n/a |
| Visible brief characters | 7,600 | 6,002 | -1,598 |
| Visible brief words | 678 | 522 | -156 |
| Latency (s) | 24.665 | 41.211 | 16.546 |
| Estimated cost (USD) | 0.00813 | 0.00833 | 0.00021 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.333 | -0.333 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.000 | 0.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,502 | 1,552 | 50 |
| Output tokens | 3,694 | 3,718 | 24 |
| Reasoning tokens | n/a | 2,112 | n/a |
| Visible output tokens | n/a | 1,606 | n/a |
| Visible brief characters | 6,422 | 6,446 | 24 |
| Visible brief words | 533 | 572 | 39 |
| Latency (s) | 23.426 | 41.075 | 17.649 |
| Estimated cost (USD) | 0.00776 | 0.00782 | 0.00006 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.500 | 1.000 | 0.500 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
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
