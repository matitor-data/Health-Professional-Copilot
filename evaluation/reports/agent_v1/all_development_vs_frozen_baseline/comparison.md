# Baseline Comparison Report

- Baseline run: `20260829T232323Z` (`nutrition-baseline-v4`)
- Candidate run: `20260829T235358Z` (`nutrition-agent-v1`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1554.80000 | 2703.30000 | 1148.50000 |
| Output tokens | 3982.50000 | 5418.10000 | 1435.60000 |
| Reasoning tokens | 2387.20000 | 3136.00000 | 748.80000 |
| Visible output tokens | 1595.30000 | 2282.10000 | 686.80000 |
| Latency (ms) | 50040.80000 | 61435.00000 | 11394.20000 |
| Estimated cost (USD) | 0.00835 | 0.01151 | 0.00316 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.717 | 0.667 | -0.050 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.642 | 0.417 | -0.225 |
| `nutrition_consideration_precision` | 0.317 | 0.400 | 0.083 |
| `nutrition_consideration_recall` | 0.500 | 0.650 | 0.150 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.860 | 0.973 | 0.114 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.600 | 0.300 | -0.300 |
| `referral_flag_recall` | 0.900 | 0.700 | -0.200 |
| `risk_factor_recall` | 0.733 | 0.833 | 0.100 |
| `scope_violation_proxy_hits` | 0.100 | 0.200 | 0.100 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,544 | 1,889 | 345 |
| Output tokens | 3,635 | 3,817 | 182 |
| Reasoning tokens | 2,304 | 2,048 | -256 |
| Visible output tokens | 1,331 | 1,769 | 438 |
| Visible brief characters | 4,887 | 4,832 | -55 |
| Visible brief words | 421 | 458 | 37 |
| Latency (s) | 51.322 | 42.246 | -9.076 |
| Estimated cost (USD) | 0.00766 | 0.00811 | 0.00045 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 1 | +1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.000 | -1.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.667 | 0.875 | 0.208 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_002

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,560 | 1,915 | 355 |
| Output tokens | 4,277 | 4,069 | -208 |
| Reasoning tokens | 2,624 | 2,432 | -192 |
| Visible output tokens | 1,653 | 1,637 | -16 |
| Visible brief characters | 6,439 | 4,594 | -1,845 |
| Visible brief words | 567 | 414 | -153 |
| Latency (s) | 59.683 | 45.551 | -14.132 |
| Estimated cost (USD) | 0.00894 | 0.00862 | -0.00033 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 3 | -2 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.667 | -0.333 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.929 | 1.000 | 0.071 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `risk_factor_recall` | 0.500 | 0.000 | -0.500 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,597 | 1,986 | 389 |
| Output tokens | 4,236 | 5,800 | 1,564 |
| Reasoning tokens | 2,560 | 3,584 | 1,024 |
| Visible output tokens | 1,676 | 2,216 | 540 |
| Visible brief characters | 6,278 | 5,896 | -382 |
| Visible brief words | 536 | 552 | 16 |
| Latency (s) | 67.861 | 64.126 | -3.735 |
| Estimated cost (USD) | 0.00887 | 0.01210 | 0.00323 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 1.000 | 0.500 |
| `nutrition_consideration_precision` | 0.500 | 0.500 | 0.000 |
| `nutrition_consideration_recall` | 0.500 | 0.500 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.667 | 0.333 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,553 | 1,908 | 355 |
| Output tokens | 4,402 | 5,119 | 717 |
| Reasoning tokens | 2,496 | 3,008 | 512 |
| Visible output tokens | 1,906 | 2,111 | 205 |
| Visible brief characters | 7,604 | 5,900 | -1,704 |
| Visible brief words | 686 | 568 | -118 |
| Latency (s) | 61.556 | 54.465 | -7.091 |
| Estimated cost (USD) | 0.00919 | 0.01072 | 0.00152 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 3 | -2 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 2 | -2 |
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

## dev_005

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,553 | 1,906 | 353 |
| Output tokens | 3,734 | 5,232 | 1,498 |
| Reasoning tokens | 2,112 | 3,392 | 1,280 |
| Visible output tokens | 1,622 | 1,840 | 218 |
| Visible brief characters | 6,273 | 4,851 | -1,422 |
| Visible brief words | 561 | 432 | -129 |
| Latency (s) | 46.361 | 53.443 | 7.082 |
| Estimated cost (USD) | 0.00786 | 0.01094 | 0.00308 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 2 | -3 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 0.000 | -0.500 |
| `nutrition_consideration_precision` | 0.000 | 0.500 | 0.500 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 0.000 | -1.000 |
| `risk_factor_recall` | 0.667 | 1.000 | 0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_006

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,543 | 5,656 | 4,113 |
| Output tokens | 4,303 | 8,531 | 4,228 |
| Reasoning tokens | 2,496 | 4,992 | 2,496 |
| Visible output tokens | 1,807 | 3,539 | 1,732 |
| Visible brief characters | 7,215 | 4,887 | -2,328 |
| Visible brief words | 636 | 436 | -200 |
| Latency (s) | 44.361 | 88.600 | 44.239 |
| Estimated cost (USD) | 0.00899 | 0.01848 | 0.00948 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 3 | -2 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 2 | -2 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 1.000 | 0.000 |
| `forbidden_suggestion_hits` | 1 | 1 | 0.000 |
| `information_gap_recall` | 0.333 | 0.000 | -0.333 |
| `nutrition_consideration_precision` | 0.333 | 0.000 | -0.333 |
| `nutrition_consideration_recall` | 0.500 | 0.000 | -0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,590 | 6,022 | 4,432 |
| Output tokens | 4,590 | 7,376 | 2,786 |
| Reasoning tokens | 2,944 | 3,392 | 448 |
| Visible output tokens | 1,646 | 3,984 | 2,338 |
| Visible brief characters | 6,165 | 5,348 | -817 |
| Visible brief words | 560 | 497 | -63 |
| Latency (s) | 51.720 | 97.491 | 45.771 |
| Estimated cost (USD) | 0.00958 | 0.01626 | 0.00668 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 3 | -1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.500 | 1.000 | 0.500 |
| `scope_violation_proxy_hits` | 0 | 1 | 1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,510 | 1,791 | 281 |
| Output tokens | 2,956 | 5,041 | 2,085 |
| Reasoning tokens | 1,856 | 3,456 | 1,600 |
| Visible output tokens | 1,100 | 1,585 | 485 |
| Visible brief characters | 4,208 | 4,287 | 79 |
| Visible brief words | 348 | 371 | 23 |
| Latency (s) | 35.258 | 59.539 | 24.281 |
| Estimated cost (USD) | 0.00629 | 0.01053 | 0.00424 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 3 | -1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 1 | 2 | +1 |
| `nutritional_risk_factors` | 1 | 1 | +0 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.500 | 0.250 | -0.250 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.750 | 0.500 | -0.250 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.000 | 0.857 | 0.857 |
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
| Input tokens | 1,546 | 2,060 | 514 |
| Output tokens | 3,974 | 4,237 | 263 |
| Reasoning tokens | 2,368 | 2,176 | -192 |
| Visible output tokens | 1,606 | 2,061 | 455 |
| Visible brief characters | 6,002 | 5,323 | -679 |
| Visible brief words | 522 | 484 | -38 |
| Latency (s) | 41.211 | 53.696 | 12.485 |
| Estimated cost (USD) | 0.00833 | 0.00899 | 0.00065 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.500 | 0.500 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 0.000 | -1.000 |
| `risk_factor_recall` | 0.000 | 1.000 | 1.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,552 | 1,900 | 348 |
| Output tokens | 3,718 | 4,959 | 1,241 |
| Reasoning tokens | 2,112 | 2,880 | 768 |
| Visible output tokens | 1,606 | 2,079 | 473 |
| Visible brief characters | 6,446 | 5,787 | -659 |
| Visible brief words | 572 | 544 | -28 |
| Latency (s) | 41.075 | 55.193 | 14.118 |
| Estimated cost (USD) | 0.00782 | 0.01039 | 0.00257 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 0 | 1 | +1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.750 | -0.250 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
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
