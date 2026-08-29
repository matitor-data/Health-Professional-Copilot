# Baseline Comparison Report

- Baseline run: `20260829T230906Z` (`nutrition-baseline-v1`)
- Candidate run: `20260829T230902Z` (`nutrition-baseline-v2`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1256.80000 | 1338.80000 | 82.00000 |
| Output tokens | 3438.00000 | 3899.70000 | 461.70000 |
| Latency (ms) | 22723.90000 | 25727.30000 | 3003.40000 |
| Estimated cost (USD) | 0.00719 | 0.00813 | 0.00094 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.567 | 0.500 | -0.067 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.725 | 0.608 | -0.117 |
| `nutrition_consideration_precision` | 0.267 | 0.300 | 0.033 |
| `nutrition_consideration_recall` | 0.400 | 0.500 | 0.100 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.888 | 0.889 | 0.001 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.800 | 0.600 | -0.200 |
| `referral_flag_recall` | 1.000 | 0.900 | -0.100 |
| `risk_factor_recall` | 0.850 | 0.767 | -0.083 |
| `scope_violation_proxy_hits` | 0.400 | 0.400 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.650 | 0.850 | 0.200 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,246 | 1,328 | 82 |
| Output tokens | 2,978 | 3,424 | 446 |
| Visible brief characters | 6,453 | 5,726 | -727 |
| Visible brief words | 552 | 478 | -74 |
| Latency (s) | 19.789 | 23.695 | 3.906 |
| Estimated cost (USD) | 0.00627 | 0.00718 | 0.00091 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
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
| `populated_source_field_rate` | 0.812 | 0.769 | -0.043 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.500 | 0.500 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_002

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,262 | 1,344 | 82 |
| Output tokens | 4,458 | 3,946 | -512 |
| Visible brief characters | 8,385 | 7,305 | -1,080 |
| Visible brief words | 798 | 663 | -135 |
| Latency (s) | 27.772 | 24.810 | -2.962 |
| Estimated cost (USD) | 0.00923 | 0.00823 | -0.00100 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 2 | +1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 0.667 | -0.333 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.889 | 0.895 | 0.006 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 0.000 | -1.000 |
| `risk_factor_recall` | 0.000 | 0.000 | 0.000 |
| `scope_violation_proxy_hits` | 2 | 2 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,299 | 1,381 | 82 |
| Output tokens | 3,357 | 3,872 | 515 |
| Visible brief characters | 6,750 | 6,408 | -342 |
| Visible brief words | 553 | 530 | -23 |
| Latency (s) | 24.341 | 27.466 | 3.125 |
| Estimated cost (USD) | 0.00704 | 0.00809 | 0.00105 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 0 | 1 | +1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.333 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 0.667 | 0.667 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.000 | -1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.000 | 1.000 | 1.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,255 | 1,337 | 82 |
| Output tokens | 4,078 | 5,269 | 1,191 |
| Visible brief characters | 7,449 | 7,526 | 77 |
| Visible brief words | 638 | 619 | -19 |
| Latency (s) | 28.472 | 35.560 | 7.088 |
| Estimated cost (USD) | 0.00847 | 0.01087 | 0.00240 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 2 | +1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.333 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.667 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
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
| Input tokens | 1,255 | 1,337 | 82 |
| Output tokens | 3,383 | 3,638 | 255 |
| Visible brief characters | 7,163 | 6,958 | -205 |
| Visible brief words | 611 | 593 | -18 |
| Latency (s) | 23.655 | 26.863 | 3.208 |
| Estimated cost (USD) | 0.00708 | 0.00761 | 0.00053 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.333 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.000 | -1.000 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
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

## dev_006

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,245 | 1,327 | 82 |
| Output tokens | 3,300 | 4,067 | 767 |
| Visible brief characters | 6,937 | 7,455 | 518 |
| Visible brief words | 592 | 639 | 47 |
| Latency (s) | 22.532 | 26.064 | 3.532 |
| Estimated cost (USD) | 0.00691 | 0.00847 | 0.00155 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 1.000 | 0.000 |
| `forbidden_suggestion_hits` | 1 | 1 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_precision` | 0.000 | 0.667 | 0.667 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.000 | 1.000 | 1.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,292 | 1,374 | 82 |
| Output tokens | 3,292 | 3,924 | 632 |
| Visible brief characters | 7,848 | 7,975 | 127 |
| Visible brief words | 699 | 721 | 22 |
| Latency (s) | 21.172 | 24.381 | 3.209 |
| Estimated cost (USD) | 0.00691 | 0.00819 | 0.00128 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
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
| `risk_factor_recall` | 0.500 | 1.000 | 0.500 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,212 | 1,294 | 82 |
| Output tokens | 3,169 | 3,735 | 566 |
| Visible brief characters | 6,066 | 5,065 | -1,001 |
| Visible brief words | 462 | 368 | -94 |
| Latency (s) | 19.833 | 23.683 | 3.850 |
| Estimated cost (USD) | 0.00664 | 0.00779 | 0.00115 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 3 | -2 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.250 | 0.250 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.250 | 0.750 | 0.500 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.250 | 0.231 | -0.019 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.000 | 0.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_009

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,248 | 1,330 | 82 |
| Output tokens | 3,037 | 3,224 | 187 |
| Visible brief characters | 7,327 | 6,831 | -496 |
| Visible brief words | 659 | 583 | -76 |
| Latency (s) | 19.069 | 20.184 | 1.115 |
| Estimated cost (USD) | 0.00639 | 0.00678 | 0.00039 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.000 | -0.667 |
| `nutrition_consideration_precision` | 0.000 | 0.000 | 0.000 |
| `nutrition_consideration_recall` | 0.000 | 0.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.000 | -1.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,254 | 1,336 | 82 |
| Output tokens | 3,328 | 3,898 | 570 |
| Visible brief characters | 7,046 | 7,211 | 165 |
| Visible brief words | 599 | 644 | 45 |
| Latency (s) | 20.604 | 24.567 | 3.963 |
| Estimated cost (USD) | 0.00697 | 0.00813 | 0.00116 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.750 | 0.750 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.933 | 1.000 | 0.067 |
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
