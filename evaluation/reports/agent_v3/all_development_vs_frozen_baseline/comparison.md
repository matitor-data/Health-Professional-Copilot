# Baseline Comparison Report

- Baseline run: `20260829T232323Z` (`nutrition-baseline-v4`)
- Candidate run: `20260830T011416Z` (`nutrition-agent-v3`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1554.80000 | 1126.50000 | -428.30000 |
| Output tokens | 3982.50000 | 3330.70000 | -651.80000 |
| Reasoning tokens | 2387.20000 | 2585.60000 | 198.40000 |
| Visible output tokens | 1595.30000 | 745.10000 | -850.20000 |
| Latency (ms) | 50040.80000 | 24923.20000 | -25117.60000 |
| Estimated cost (USD) | 0.00835 | 0.00694 | -0.00141 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.717 | 0.708 | -0.008 |
| `forbidden_suggestion_hits` | 0.100 | 0.000 | -0.100 |
| `information_gap_recall` | 0.642 | 0.892 | 0.250 |
| `missed_referral_count` | 0.000 | 0.200 | 0.200 |
| `nutrition_consideration_precision` | 0.317 | 0.767 | 0.450 |
| `nutrition_consideration_recall` | 0.500 | 1.000 | 0.500 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.860 | 1.000 | 0.140 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_action_safety_proxy` | 0.900 | 1.000 | 0.100 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.600 | 0.800 | 0.200 |
| `referral_flag_recall` | 0.900 | 0.800 | -0.100 |
| `referral_presence_accuracy` | 0.700 | 0.800 | 0.100 |
| `risk_factor_recall` | 0.733 | 0.650 | -0.083 |
| `scope_violation_proxy_hits` | 0.100 | 0.000 | -0.100 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `unnecessary_referral_count` | 0.300 | 0.000 | -0.300 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,544 | 1,098 | -446 |
| Output tokens | 3,635 | 4,257 | 622 |
| Reasoning tokens | 2,304 | 3,776 | 1,472 |
| Visible output tokens | 1,331 | 481 | -850 |
| Visible brief characters | 4,887 | 3,775 | -1,112 |
| Visible brief words | 421 | 294 | -127 |
| Latency (s) | 51.322 | 28.054 | -23.268 |
| Estimated cost (USD) | 0.00766 | 0.00879 | 0.00113 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.500 | -0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.500 | 0.500 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.667 | 1.000 | 0.333 |
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

## dev_002

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,560 | 1,100 | -460 |
| Output tokens | 4,277 | 3,456 | -821 |
| Reasoning tokens | 2,624 | 2,432 | -192 |
| Visible output tokens | 1,653 | 1,024 | -629 |
| Visible brief characters | 6,439 | 5,175 | -1,264 |
| Visible brief words | 567 | 416 | -151 |
| Latency (s) | 59.683 | 22.188 | -37.495 |
| Estimated cost (USD) | 0.00894 | 0.00719 | -0.00176 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `missed_referral_count` | 0 | 1 | 1.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.929 | 1.000 | 0.071 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 0 | -1.000 |
| `risk_factor_recall` | 0.500 | 1.000 | 0.500 |
| `scope_violation_proxy_hits` | 1 | 0 | -1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,597 | 1,070 | -527 |
| Output tokens | 4,236 | 3,545 | -691 |
| Reasoning tokens | 2,560 | 2,624 | 64 |
| Visible output tokens | 1,676 | 921 | -755 |
| Visible brief characters | 6,278 | 4,918 | -1,360 |
| Visible brief words | 536 | 368 | -168 |
| Latency (s) | 67.861 | 22.362 | -45.499 |
| Estimated cost (USD) | 0.00887 | 0.00736 | -0.00151 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 1.000 | 0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.667 | 0.167 |
| `nutrition_consideration_recall` | 0.500 | 1.000 | 0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 0 | 1 | 1.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 0.667 | 0.000 | -0.667 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,553 | 1,119 | -434 |
| Output tokens | 4,402 | 3,502 | -900 |
| Reasoning tokens | 2,496 | 2,368 | -128 |
| Visible output tokens | 1,906 | 1,134 | -772 |
| Visible brief characters | 7,604 | 5,195 | -2,409 |
| Visible brief words | 686 | 442 | -244 |
| Latency (s) | 61.556 | 22.137 | -39.419 |
| Estimated cost (USD) | 0.00919 | 0.00728 | -0.00191 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 1 | -3 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 1.000 | 0.333 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.333 | 0.333 | 0.000 |
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
| Input tokens | 1,553 | 1,088 | -465 |
| Output tokens | 3,734 | 3,862 | 128 |
| Reasoning tokens | 2,112 | 3,136 | 1,024 |
| Visible output tokens | 1,622 | 726 | -896 |
| Visible brief characters | 6,273 | 4,545 | -1,728 |
| Visible brief words | 561 | 366 | -195 |
| Latency (s) | 46.361 | 23.582 | -22.779 |
| Estimated cost (USD) | 0.00786 | 0.00800 | 0.00014 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 1.000 | 0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.667 | 0.667 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `risk_factor_recall` | 0.667 | 0.667 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_006

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,543 | 1,071 | -472 |
| Output tokens | 4,303 | 3,072 | -1,231 |
| Reasoning tokens | 2,496 | 2,112 | -384 |
| Visible output tokens | 1,807 | 960 | -847 |
| Visible brief characters | 7,215 | 4,870 | -2,345 |
| Visible brief words | 636 | 381 | -255 |
| Latency (s) | 44.361 | 19.003 | -25.358 |
| Estimated cost (USD) | 0.00899 | 0.00641 | -0.00258 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 2 | -2 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 1.000 | 0.000 |
| `forbidden_suggestion_hits` | 1 | 0 | -1.000 |
| `information_gap_recall` | 0.333 | 1.000 | 0.667 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.333 | 1.000 | 0.667 |
| `nutrition_consideration_recall` | 0.500 | 1.000 | 0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,590 | 1,063 | -527 |
| Output tokens | 4,590 | 3,049 | -1,541 |
| Reasoning tokens | 2,944 | 2,432 | -512 |
| Visible output tokens | 1,646 | 617 | -1,029 |
| Visible brief characters | 6,165 | 4,249 | -1,916 |
| Visible brief words | 560 | 345 | -215 |
| Latency (s) | 51.720 | 19.223 | -32.497 |
| Estimated cost (USD) | 0.00958 | 0.00636 | -0.00321 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 1 | -1 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 1 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 1.000 | 0.667 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 0.500 | 0.500 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,510 | 1,243 | -267 |
| Output tokens | 2,956 | 558 | -2,398 |
| Reasoning tokens | 1,856 | 384 | -1,472 |
| Visible output tokens | 1,100 | 174 | -926 |
| Visible brief characters | 4,208 | 2,453 | -1,755 |
| Visible brief words | 348 | 189 | -159 |
| Latency (s) | 35.258 | 4.471 | -30.787 |
| Estimated cost (USD) | 0.00629 | 0.00143 | -0.00486 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 1 | 0 | -1 |
| `nutritional_risk_factors` | 1 | 0 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 0 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.500 | 0.750 | 0.250 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.750 | 0.750 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.000 | 1.000 | 1.000 |
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
| Input tokens | 1,546 | 1,333 | -213 |
| Output tokens | 3,974 | 3,522 | -452 |
| Reasoning tokens | 2,368 | 2,752 | 384 |
| Visible output tokens | 1,606 | 770 | -836 |
| Visible brief characters | 6,002 | 4,206 | -1,796 |
| Visible brief words | 522 | 319 | -203 |
| Latency (s) | 41.211 | 30.013 | -11.198 |
| Estimated cost (USD) | 0.00833 | 0.00738 | -0.00096 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 1 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 0.667 | 0.333 |
| `missed_referral_count` | 0 | 1 | 1.000 |
| `nutrition_consideration_precision` | 0.000 | 0.500 | 0.500 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 0.000 | -1.000 |
| `referral_presence_accuracy` | 1 | 0 | -1.000 |
| `risk_factor_recall` | 0.000 | 0.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,552 | 1,080 | -472 |
| Output tokens | 3,718 | 4,484 | 766 |
| Reasoning tokens | 2,112 | 3,840 | 1,728 |
| Visible output tokens | 1,606 | 644 | -962 |
| Visible brief characters | 6,446 | 4,137 | -2,309 |
| Visible brief words | 572 | 312 | -260 |
| Latency (s) | 41.075 | 58.199 | 17.124 |
| Estimated cost (USD) | 0.00782 | 0.00924 | 0.00141 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 1.000 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
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

## Interpretation notes

- Negative token, latency, and cost deltas indicate improvement.
- Metric deltas use the current deterministic lexical evaluator and require manual review.
- Cost is estimated from the token prices passed to the comparison command.
- A shorter output is not automatically better if referral safety or relevant recall decreases.
