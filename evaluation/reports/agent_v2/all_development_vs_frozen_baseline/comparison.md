# Baseline Comparison Report

- Baseline run: `20260829T232323Z` (`nutrition-baseline-v4`)
- Candidate run: `20260830T003855Z` (`nutrition-agent-v2`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1554.80000 | 2331.40000 | 776.60000 |
| Output tokens | 3982.50000 | 5953.00000 | 1970.50000 |
| Reasoning tokens | 2387.20000 | 3564.80000 | 1177.60000 |
| Visible output tokens | 1595.30000 | 2388.20000 | 792.90000 |
| Latency (ms) | 50040.80000 | 67892.30000 | 17851.50000 |
| Estimated cost (USD) | 0.00835 | 0.01249 | 0.00414 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.717 | 0.683 | -0.033 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.642 | 0.583 | -0.058 |
| `missed_referral_count` | 0.000 | 0.200 | 0.200 |
| `nutrition_consideration_precision` | 0.317 | 0.250 | -0.067 |
| `nutrition_consideration_recall` | 0.500 | 0.450 | -0.050 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.860 | 0.926 | 0.066 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_action_safety_proxy` | 0.900 | 1.000 | 0.100 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.600 | 0.800 | 0.200 |
| `referral_flag_recall` | 0.900 | 0.800 | -0.100 |
| `referral_presence_accuracy` | 0.700 | 0.800 | 0.100 |
| `risk_factor_recall` | 0.733 | 0.767 | 0.033 |
| `scope_violation_proxy_hits` | 0.100 | 0.200 | 0.100 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `unnecessary_referral_count` | 0.300 | 0.000 | -0.300 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,544 | 1,552 | 8 |
| Output tokens | 3,635 | 4,829 | 1,194 |
| Reasoning tokens | 2,304 | 2,816 | 512 |
| Visible output tokens | 1,331 | 2,013 | 682 |
| Visible brief characters | 4,887 | 5,790 | 903 |
| Visible brief words | 421 | 553 | 132 |
| Latency (s) | 51.322 | 68.453 | 17.131 |
| Estimated cost (USD) | 0.00766 | 0.01005 | 0.00239 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 2 | 2 | +0 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.500 | -0.500 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
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
| Input tokens | 1,560 | 5,134 | 3,574 |
| Output tokens | 4,277 | 9,713 | 5,436 |
| Reasoning tokens | 2,624 | 5,888 | 3,264 |
| Visible output tokens | 1,653 | 3,825 | 2,172 |
| Visible brief characters | 6,439 | 5,453 | -986 |
| Visible brief words | 567 | 519 | -48 |
| Latency (s) | 59.683 | 115.209 | 55.526 |
| Estimated cost (USD) | 0.00894 | 0.02071 | 0.01177 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 1 | -2 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.333 | -0.667 |
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
| `risk_factor_recall` | 0.500 | 0.000 | -0.500 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,597 | 1,524 | -73 |
| Output tokens | 4,236 | 4,676 | 440 |
| Reasoning tokens | 2,560 | 2,816 | 256 |
| Visible output tokens | 1,676 | 1,860 | 184 |
| Visible brief characters | 6,278 | 5,181 | -1,097 |
| Visible brief words | 536 | 506 | -30 |
| Latency (s) | 67.861 | 57.259 | -10.602 |
| Estimated cost (USD) | 0.00887 | 0.00973 | 0.00086 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 4 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 0.500 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.500 | 0.000 | -0.500 |
| `nutrition_consideration_recall` | 0.500 | 0.000 | -0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_action_safety_proxy` | 0 | 1 | 1.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 0.667 | 0.333 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,553 | 1,573 | 20 |
| Output tokens | 4,402 | 4,582 | 180 |
| Reasoning tokens | 2,496 | 2,752 | 256 |
| Visible output tokens | 1,906 | 1,830 | -76 |
| Visible brief characters | 7,604 | 5,530 | -2,074 |
| Visible brief words | 686 | 510 | -176 |
| Latency (s) | 61.556 | 50.619 | -10.937 |
| Estimated cost (USD) | 0.00919 | 0.00956 | 0.00036 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 2 | -2 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 1 | -2 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.667 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.333 | 0.500 | 0.167 |
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
| Input tokens | 1,553 | 1,542 | -11 |
| Output tokens | 3,734 | 4,909 | 1,175 |
| Reasoning tokens | 2,112 | 2,944 | 832 |
| Visible output tokens | 1,622 | 1,965 | 343 |
| Visible brief characters | 6,273 | 5,675 | -598 |
| Visible brief words | 561 | 527 | -34 |
| Latency (s) | 46.361 | 52.412 | 6.051 |
| Estimated cost (USD) | 0.00786 | 0.01020 | 0.00235 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.500 | 0.500 | 0.000 |
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
| Input tokens | 1,543 | 1,525 | -18 |
| Output tokens | 4,303 | 4,364 | 61 |
| Reasoning tokens | 2,496 | 2,560 | 64 |
| Visible output tokens | 1,807 | 1,804 | -3 |
| Visible brief characters | 7,215 | 5,095 | -2,120 |
| Visible brief words | 636 | 450 | -186 |
| Latency (s) | 44.361 | 44.280 | -0.081 |
| Estimated cost (USD) | 0.00899 | 0.00911 | 0.00012 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 3 | 2 | -1 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.667 | -0.333 |
| `forbidden_suggestion_hits` | 1 | 1 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.333 | 0.000 | -0.333 |
| `nutrition_consideration_recall` | 0.500 | 0.000 | -0.500 |
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
| Input tokens | 1,590 | 1,517 | -73 |
| Output tokens | 4,590 | 5,946 | 1,356 |
| Reasoning tokens | 2,944 | 3,456 | 512 |
| Visible output tokens | 1,646 | 2,490 | 844 |
| Visible brief characters | 6,165 | 7,368 | 1,203 |
| Visible brief words | 560 | 756 | 196 |
| Latency (s) | 51.720 | 63.164 | 11.444 |
| Estimated cost (USD) | 0.00958 | 0.01227 | 0.00269 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
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
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `referral_presence_accuracy` | 0 | 1 | 1.000 |
| `risk_factor_recall` | 0.500 | 1.000 | 0.500 |
| `scope_violation_proxy_hits` | 0 | 1 | 1.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 1 | 0 | -1.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,510 | 1,673 | 163 |
| Output tokens | 2,956 | 4,523 | 1,567 |
| Reasoning tokens | 1,856 | 2,688 | 832 |
| Visible output tokens | 1,100 | 1,835 | 735 |
| Visible brief characters | 4,208 | 5,188 | 980 |
| Visible brief words | 348 | 434 | 86 |
| Latency (s) | 35.258 | 49.444 | 14.186 |
| Estimated cost (USD) | 0.00629 | 0.00946 | 0.00317 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 1 | 1 | +0 |
| `nutritional_risk_factors` | 1 | 2 | +1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.500 | 0.750 | 0.250 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.750 | 1.000 | 0.250 |
| `missed_referral_count` | 0 | 0 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.000 | 0.400 | 0.400 |
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
| Input tokens | 1,546 | 1,787 | 241 |
| Output tokens | 3,974 | 5,050 | 1,076 |
| Reasoning tokens | 2,368 | 2,944 | 576 |
| Visible output tokens | 1,606 | 2,106 | 500 |
| Visible brief characters | 6,002 | 6,148 | 146 |
| Visible brief words | 522 | 602 | 80 |
| Latency (s) | 41.211 | 55.121 | 13.910 |
| Estimated cost (USD) | 0.00833 | 0.01055 | 0.00221 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 2 | 2 | +0 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 2 | 2 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 1.000 | 0.333 |
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
| `risk_factor_recall` | 0.000 | 1.000 | 1.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `unnecessary_referral_count` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,552 | 5,487 | 3,935 |
| Output tokens | 3,718 | 10,938 | 7,220 |
| Reasoning tokens | 2,112 | 6,784 | 4,672 |
| Visible output tokens | 1,606 | 4,154 | 2,548 |
| Visible brief characters | 6,446 | 5,720 | -726 |
| Visible brief words | 572 | 528 | -44 |
| Latency (s) | 41.075 | 122.962 | 81.887 |
| Estimated cost (USD) | 0.00782 | 0.02325 | 0.01542 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 4 | 5 | +1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 2 | -1 |
| `nutritional_risk_factors` | 3 | 2 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.750 | -0.250 |
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
