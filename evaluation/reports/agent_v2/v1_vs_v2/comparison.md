# Baseline Comparison Report

- Baseline run: `20260829T235358Z` (`nutrition-agent-v1`)
- Candidate run: `20260830T003855Z` (`nutrition-agent-v2`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 2703.30000 | 2331.40000 | -371.90000 |
| Output tokens | 5418.10000 | 5953.00000 | 534.90000 |
| Reasoning tokens | 3136.00000 | 3564.80000 | 428.80000 |
| Visible output tokens | 2282.10000 | 2388.20000 | 106.10000 |
| Latency (ms) | 61435.00000 | 67892.30000 | 6457.30000 |
| Estimated cost (USD) | 0.01151 | 0.01249 | 0.00098 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.683 | 0.017 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.417 | 0.583 | 0.167 |
| `missed_referral_count` | 0.000 | 0.200 | 0.200 |
| `nutrition_consideration_precision` | 0.400 | 0.250 | -0.150 |
| `nutrition_consideration_recall` | 0.650 | 0.450 | -0.200 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.973 | 0.926 | -0.048 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_action_safety_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.300 | 0.800 | 0.500 |
| `referral_flag_recall` | 0.700 | 0.800 | 0.100 |
| `referral_presence_accuracy` | 0.600 | 0.800 | 0.200 |
| `risk_factor_recall` | 0.833 | 0.767 | -0.067 |
| `scope_violation_proxy_hits` | 0.200 | 0.200 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `unnecessary_referral_count` | 0.400 | 0.000 | -0.400 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,889 | 1,552 | -337 |
| Output tokens | 3,817 | 4,829 | 1,012 |
| Reasoning tokens | 2,048 | 2,816 | 768 |
| Visible output tokens | 1,769 | 2,013 | 244 |
| Visible brief characters | 4,832 | 5,790 | 958 |
| Visible brief words | 458 | 553 | 95 |
| Latency (s) | 42.246 | 68.453 | 26.207 |
| Estimated cost (USD) | 0.00811 | 0.01005 | 0.00194 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 1 | 2 | +1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 3 | +1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.000 | 0.500 | 0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.875 | 1.000 | 0.125 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_002

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,915 | 5,134 | 3,219 |
| Output tokens | 4,069 | 9,713 | 5,644 |
| Reasoning tokens | 2,432 | 5,888 | 3,456 |
| Visible output tokens | 1,637 | 3,825 | 2,188 |
| Visible brief characters | 4,594 | 5,453 | 859 |
| Visible brief words | 414 | 519 | 105 |
| Latency (s) | 45.551 | 115.209 | 69.658 |
| Estimated cost (USD) | 0.00862 | 0.02071 | 0.01209 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 3 | 5 | +2 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 1 | 1 | +0 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 3 | +1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.333 | -0.333 |
| `missed_referral_count` | 0 | 1 | 1.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 0 | -1.000 |
| `risk_factor_recall` | 0.000 | 0.000 | 0.000 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,986 | 1,524 | -462 |
| Output tokens | 5,800 | 4,676 | -1,124 |
| Reasoning tokens | 3,584 | 2,816 | -768 |
| Visible output tokens | 2,216 | 1,860 | -356 |
| Visible brief characters | 5,896 | 5,181 | -715 |
| Visible brief words | 552 | 506 | -46 |
| Latency (s) | 64.126 | 57.259 | -6.867 |
| Estimated cost (USD) | 0.01210 | 0.00973 | -0.00236 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 2 | +0 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.500 | -0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.000 | -0.500 |
| `nutrition_consideration_recall` | 0.500 | 0.000 | -0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 0.333 | 0.333 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,908 | 1,573 | -335 |
| Output tokens | 5,119 | 4,582 | -537 |
| Reasoning tokens | 3,008 | 2,752 | -256 |
| Visible output tokens | 2,111 | 1,830 | -281 |
| Visible brief characters | 5,900 | 5,530 | -370 |
| Visible brief words | 568 | 510 | -58 |
| Latency (s) | 54.465 | 50.619 | -3.846 |
| Estimated cost (USD) | 0.01072 | 0.00956 | -0.00116 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 3 | 4 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 2 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.667 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.667 | 0.333 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.500 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_005

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,906 | 1,542 | -364 |
| Output tokens | 5,232 | 4,909 | -323 |
| Reasoning tokens | 3,392 | 2,944 | -448 |
| Visible output tokens | 1,840 | 1,965 | 125 |
| Visible brief characters | 4,851 | 5,675 | 824 |
| Visible brief words | 432 | 527 | 95 |
| Latency (s) | 53.443 | 52.412 | -1.031 |
| Estimated cost (USD) | 0.01094 | 0.01020 | -0.00074 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 2 | 5 | +3 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.000 | 0.500 | 0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.000 | -0.500 |
| `nutrition_consideration_recall` | 1.000 | 0.000 | -1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 0.000 | 1.000 | 1.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_006

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 5,656 | 1,525 | -4,131 |
| Output tokens | 8,531 | 4,364 | -4,167 |
| Reasoning tokens | 4,992 | 2,560 | -2,432 |
| Visible output tokens | 3,539 | 1,804 | -1,735 |
| Visible brief characters | 4,887 | 5,095 | 208 |
| Visible brief words | 436 | 450 | 14 |
| Latency (s) | 88.600 | 44.280 | -44.320 |
| Estimated cost (USD) | 0.01848 | 0.00911 | -0.00937 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 3 | 5 | +2 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 3 | +1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.667 | -0.333 |
| `forbidden_suggestion_hits` | 1 | 1 | 0.000 |
| `information_gap_recall` | 0.000 | 0.333 | 0.333 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 6,022 | 1,517 | -4,505 |
| Output tokens | 7,376 | 5,946 | -1,430 |
| Reasoning tokens | 3,392 | 3,456 | 64 |
| Visible output tokens | 3,984 | 2,490 | -1,494 |
| Visible brief characters | 5,348 | 7,368 | 2,020 |
| Visible brief words | 497 | 756 | 259 |
| Latency (s) | 97.491 | 63.164 | -34.327 |
| Estimated cost (USD) | 0.01626 | 0.01227 | -0.00399 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 3 | 5 | +2 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 3 | +1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,791 | 1,673 | -118 |
| Output tokens | 5,041 | 4,523 | -518 |
| Reasoning tokens | 3,456 | 2,688 | -768 |
| Visible output tokens | 1,585 | 1,835 | 250 |
| Visible brief characters | 4,287 | 5,188 | 901 |
| Visible brief words | 371 | 434 | 63 |
| Latency (s) | 59.539 | 49.444 | -10.095 |
| Estimated cost (USD) | 0.01053 | 0.00946 | -0.00107 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 3 | 5 | +2 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 2 | 1 | -1 |
| `nutritional_risk_factors` | 1 | 2 | +1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.250 | 0.750 | 0.500 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 1.000 | 0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.857 | 0.400 | -0.457 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_009

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 2,060 | 1,787 | -273 |
| Output tokens | 4,237 | 5,050 | 813 |
| Reasoning tokens | 2,176 | 2,944 | 768 |
| Visible output tokens | 2,061 | 2,106 | 45 |
| Visible brief characters | 5,323 | 6,148 | 825 |
| Visible brief words | 484 | 602 | 118 |
| Latency (s) | 53.696 | 55.121 | 1.425 |
| Estimated cost (USD) | 0.00899 | 0.01055 | 0.00156 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 2 | +0 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.667 | 0.333 |
| `missed_referral_count` | 0 | 1 | 1.000 |
| `nutrition_consideration_precision` | 0.500 | 0.500 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 0 | -1.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,900 | 5,487 | 3,587 |
| Output tokens | 4,959 | 10,938 | 5,979 |
| Reasoning tokens | 2,880 | 6,784 | 3,904 |
| Visible output tokens | 2,079 | 4,154 | 2,075 |
| Visible brief characters | 5,787 | 5,720 | -67 |
| Visible brief words | 544 | 528 | -16 |
| Latency (s) | 55.193 | 122.962 | 67.769 |
| Estimated cost (USD) | 0.01039 | 0.02325 | 0.01285 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 2 | +0 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 3 | +1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.750 | 0.750 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 0.500 | -0.500 |
| `nutrition_consideration_recall` | 1.000 | 0.500 | -0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 0.857 | -0.143 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## Interpretation notes

- Negative token, latency, and cost deltas indicate improvement.
- Metric deltas use the current deterministic lexical evaluator and require manual review.
- Cost is estimated from the token prices passed to the comparison command.
- A shorter output is not automatically better if referral safety or relevant recall decreases.
