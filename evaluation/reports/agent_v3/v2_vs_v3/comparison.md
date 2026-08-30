# Baseline Comparison Report

- Baseline run: `20260830T003855Z` (`nutrition-agent-v2`)
- Candidate run: `20260830T011416Z` (`nutrition-agent-v3`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 2331.40000 | 1126.50000 | -1204.90000 |
| Output tokens | 5953.00000 | 3330.70000 | -2622.30000 |
| Reasoning tokens | 3564.80000 | 2585.60000 | -979.20000 |
| Visible output tokens | 2388.20000 | 745.10000 | -1643.10000 |
| Latency (ms) | 67892.30000 | 24923.20000 | -42969.10000 |
| Estimated cost (USD) | 0.01249 | 0.00694 | -0.00555 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.683 | 0.708 | 0.025 |
| `forbidden_suggestion_hits` | 0.100 | 0.000 | -0.100 |
| `information_gap_recall` | 0.583 | 0.892 | 0.308 |
| `missed_referral_count` | 0.200 | 0.200 | 0.000 |
| `nutrition_consideration_precision` | 0.250 | 0.767 | 0.517 |
| `nutrition_consideration_recall` | 0.450 | 1.000 | 0.550 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.926 | 1.000 | 0.074 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_action_safety_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_clarify_first_count` | 0.200 | 0.200 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.800 | 0.800 | 0.000 |
| `referral_flag_recall` | 0.800 | 0.800 | 0.000 |
| `referral_presence_accuracy` | 0.800 | 0.800 | 0.000 |
| `referral_supported_count` | 0.200 | 0.200 | 0.000 |
| `risk_factor_recall` | 0.767 | 0.650 | -0.117 |
| `scope_violation_proxy_hits` | 0.200 | 0.000 | -0.200 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `unnecessary_referral_count` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,552 | 1,098 | -454 |
| Output tokens | 4,829 | 4,257 | -572 |
| Reasoning tokens | 2,816 | 3,776 | 960 |
| Visible output tokens | 2,013 | 481 | -1,532 |
| Visible brief characters | 5,790 | 3,775 | -2,015 |
| Visible brief words | 553 | 294 | -259 |
| Latency (s) | 68.453 | 28.054 | -40.399 |
| Estimated cost (USD) | 0.01005 | 0.00879 | -0.00126 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 0.500 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.500 | 0.500 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
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
| Input tokens | 5,134 | 1,100 | -4,034 |
| Output tokens | 9,713 | 3,456 | -6,257 |
| Reasoning tokens | 5,888 | 2,432 | -3,456 |
| Visible output tokens | 3,825 | 1,024 | -2,801 |
| Visible brief characters | 5,453 | 5,175 | -278 |
| Visible brief words | 519 | 416 | -103 |
| Latency (s) | 115.209 | 22.188 | -93.021 |
| Estimated cost (USD) | 0.02071 | 0.00719 | -0.01352 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 1 | 2 | +1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.333 | 1.000 | 0.667 |
| `missed_referral_count` | 1 | 1 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 0 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
| `risk_factor_recall` | 0.000 | 1.000 | 1.000 |
| `scope_violation_proxy_hits` | 1 | 0 | -1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,524 | 1,070 | -454 |
| Output tokens | 4,676 | 3,545 | -1,131 |
| Reasoning tokens | 2,816 | 2,624 | -192 |
| Visible output tokens | 1,860 | 921 | -939 |
| Visible brief characters | 5,181 | 4,918 | -263 |
| Visible brief words | 506 | 368 | -138 |
| Latency (s) | 57.259 | 22.362 | -34.897 |
| Estimated cost (USD) | 0.00973 | 0.00736 | -0.00238 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

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
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
| `risk_factor_recall` | 0.333 | 0.000 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,573 | 1,119 | -454 |
| Output tokens | 4,582 | 3,502 | -1,080 |
| Reasoning tokens | 2,752 | 2,368 | -384 |
| Visible output tokens | 1,830 | 1,134 | -696 |
| Visible brief characters | 5,530 | 5,195 | -335 |
| Visible brief words | 510 | 442 | -68 |
| Latency (s) | 50.619 | 22.137 | -28.482 |
| Estimated cost (USD) | 0.00956 | 0.00728 | -0.00227 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 1 | 2 | +1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 1.000 | 0.333 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.333 | -0.167 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 1 | 1 | 0.000 |
| `risk_factor_recall` | 0.667 | 0.667 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_005

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,542 | 1,088 | -454 |
| Output tokens | 4,909 | 3,862 | -1,047 |
| Reasoning tokens | 2,944 | 3,136 | 192 |
| Visible output tokens | 1,965 | 726 | -1,239 |
| Visible brief characters | 5,675 | 4,545 | -1,130 |
| Visible brief words | 527 | 366 | -161 |
| Latency (s) | 52.412 | 23.582 | -28.830 |
| Estimated cost (USD) | 0.01020 | 0.00800 | -0.00221 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 2 | 1 | -1 |

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
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 1 | 1 | 0.000 |
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
| Input tokens | 1,525 | 1,071 | -454 |
| Output tokens | 4,364 | 3,072 | -1,292 |
| Reasoning tokens | 2,560 | 2,112 | -448 |
| Visible output tokens | 1,804 | 960 | -844 |
| Visible brief characters | 5,095 | 4,870 | -225 |
| Visible brief words | 450 | 381 | -69 |
| Latency (s) | 44.280 | 19.003 | -25.277 |
| Estimated cost (USD) | 0.00911 | 0.00641 | -0.00270 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
| `forbidden_suggestion_hits` | 1 | 0 | -1.000 |
| `information_gap_recall` | 0.333 | 1.000 | 0.667 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,517 | 1,063 | -454 |
| Output tokens | 5,946 | 3,049 | -2,897 |
| Reasoning tokens | 3,456 | 2,432 | -1,024 |
| Visible output tokens | 2,490 | 617 | -1,873 |
| Visible brief characters | 7,368 | 4,249 | -3,119 |
| Visible brief words | 756 | 345 | -411 |
| Latency (s) | 63.164 | 19.223 | -43.941 |
| Estimated cost (USD) | 0.01227 | 0.00636 | -0.00591 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 1 | -1 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

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
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.500 | -0.500 |
| `scope_violation_proxy_hits` | 1 | 0 | -1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,673 | 1,243 | -430 |
| Output tokens | 4,523 | 558 | -3,965 |
| Reasoning tokens | 2,688 | 384 | -2,304 |
| Visible output tokens | 1,835 | 174 | -1,661 |
| Visible brief characters | 5,188 | 2,453 | -2,735 |
| Visible brief words | 434 | 189 | -245 |
| Latency (s) | 49.444 | 4.471 | -44.973 |
| Estimated cost (USD) | 0.00946 | 0.00143 | -0.00804 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 1 | 0 | -1 |
| `nutritional_risk_factors` | 2 | 0 | -2 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 0 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.750 | 0.750 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.750 | -0.250 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.400 | 1.000 | 0.600 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
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
| Input tokens | 1,787 | 1,333 | -454 |
| Output tokens | 5,050 | 3,522 | -1,528 |
| Reasoning tokens | 2,944 | 2,752 | -192 |
| Visible output tokens | 2,106 | 770 | -1,336 |
| Visible brief characters | 6,148 | 4,206 | -1,942 |
| Visible brief words | 602 | 319 | -283 |
| Latency (s) | 55.121 | 30.013 | -25.108 |
| Estimated cost (USD) | 0.01055 | 0.00738 | -0.00317 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 1 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.667 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.667 | 0.000 |
| `missed_referral_count` | 1 | 1 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.500 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 1 | 1 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 0 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.000 | -1.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 5,487 | 1,080 | -4,407 |
| Output tokens | 10,938 | 4,484 | -6,454 |
| Reasoning tokens | 6,784 | 3,840 | -2,944 |
| Visible output tokens | 4,154 | 644 | -3,510 |
| Visible brief characters | 5,720 | 4,137 | -1,583 |
| Visible brief words | 528 | 312 | -216 |
| Latency (s) | 122.962 | 58.199 | -64.763 |
| Estimated cost (USD) | 0.02325 | 0.00924 | -0.01401 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 3 | +1 |
| `nutritional_risk_factors` | 2 | 1 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.750 | 1.000 | 0.250 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 1.000 | 0.500 |
| `nutrition_consideration_recall` | 0.500 | 1.000 | 0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.857 | 1.000 | 0.143 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 1 | 1 | 0.000 |
| `referral_clarify_first_count` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 1 | 1 | 0.000 |
| `referral_supported_count` | 0 | 0 | 0.000 |
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
