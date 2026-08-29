# Baseline Comparison Report

- Baseline run: `20260829T230902Z` (`nutrition-baseline-v2`)
- Candidate run: `20260829T230907Z` (`nutrition-baseline-v3`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1338.80000 | 1504.80000 | 166.00000 |
| Output tokens | 3899.70000 | 3930.50000 | 30.80000 |
| Latency (ms) | 25727.30000 | 25944.00000 | 216.70000 |
| Estimated cost (USD) | 0.00813 | 0.00824 | 0.00010 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.500 | 0.508 | 0.008 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.608 | 0.667 | 0.058 |
| `nutrition_consideration_precision` | 0.300 | 0.400 | 0.100 |
| `nutrition_consideration_recall` | 0.500 | 0.600 | 0.100 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.889 | 0.982 | 0.093 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.600 | 0.650 | 0.050 |
| `referral_flag_recall` | 0.900 | 0.900 | 0.000 |
| `risk_factor_recall` | 0.767 | 0.717 | -0.050 |
| `scope_violation_proxy_hits` | 0.400 | 0.300 | -0.100 |
| `secondary_consideration_grounding_proxy` | 0.850 | 0.900 | 0.050 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,328 | 1,494 | 166 |
| Output tokens | 3,424 | 3,614 | 190 |
| Visible brief characters | 5,726 | 6,520 | 794 |
| Visible brief words | 478 | 591 | 113 |
| Latency (s) | 23.695 | 23.579 | -0.116 |
| Estimated cost (USD) | 0.00718 | 0.00760 | 0.00042 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
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
| `populated_source_field_rate` | 0.769 | 0.900 | 0.131 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 1 | 0 | -1.000 |
| `secondary_consideration_grounding_proxy` | 0.500 | 0.500 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_002

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,344 | 1,510 | 166 |
| Output tokens | 3,946 | 3,307 | -639 |
| Visible brief characters | 7,305 | 6,493 | -812 |
| Visible brief words | 663 | 586 | -77 |
| Latency (s) | 24.810 | 22.232 | -2.578 |
| Estimated cost (USD) | 0.00823 | 0.00699 | -0.00124 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 2 | 1 | -1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 0.667 | 0.667 | 0.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.895 | 0.923 | 0.028 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 0.000 | 0.000 | 0.000 |
| `risk_factor_recall` | 0.000 | 0.000 | 0.000 |
| `scope_violation_proxy_hits` | 2 | 2 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_003

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,381 | 1,547 | 166 |
| Output tokens | 3,872 | 3,994 | 122 |
| Visible brief characters | 6,408 | 6,400 | -8 |
| Visible brief words | 530 | 523 | -7 |
| Latency (s) | 27.466 | 28.858 | 1.392 |
| Estimated cost (USD) | 0.00809 | 0.00837 | 0.00029 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 0 | -1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 0.500 | -0.500 |
| `nutrition_consideration_precision` | 0.667 | 0.333 | -0.333 |
| `nutrition_consideration_recall` | 1.000 | 0.500 | -0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 1.000 | 1.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_004

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,337 | 1,503 | 166 |
| Output tokens | 5,269 | 5,853 | 584 |
| Visible brief characters | 7,526 | 7,931 | 405 |
| Visible brief words | 619 | 718 | 99 |
| Latency (s) | 35.560 | 39.985 | 4.425 |
| Estimated cost (USD) | 0.01087 | 0.01208 | 0.00121 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 2 | 2 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.667 | 0.333 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.667 | 0.333 | -0.333 |
| `nutrition_consideration_precision` | 0.000 | 0.333 | 0.333 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 0.500 | -0.500 |
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
| Input tokens | 1,337 | 1,503 | 166 |
| Output tokens | 3,638 | 4,311 | 673 |
| Visible brief characters | 6,958 | 7,437 | 479 |
| Visible brief words | 593 | 676 | 83 |
| Latency (s) | 26.863 | 29.366 | 2.503 |
| Estimated cost (USD) | 0.00761 | 0.00900 | 0.00139 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 2 | +1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.333 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_precision` | 0.000 | 0.333 | 0.333 |
| `nutrition_consideration_recall` | 0.000 | 1.000 | 1.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 0.667 | -0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_006

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,327 | 1,493 | 166 |
| Output tokens | 4,067 | 4,116 | 49 |
| Visible brief characters | 7,455 | 6,516 | -939 |
| Visible brief words | 639 | 573 | -66 |
| Latency (s) | 26.064 | 26.547 | 0.483 |
| Estimated cost (USD) | 0.00847 | 0.00861 | 0.00014 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 1.000 | 0.667 | -0.333 |
| `forbidden_suggestion_hits` | 1 | 1 | 0.000 |
| `information_gap_recall` | 0.333 | 0.333 | 0.000 |
| `nutrition_consideration_precision` | 0.667 | 0.333 | -0.333 |
| `nutrition_consideration_recall` | 1.000 | 0.500 | -0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 0.667 | 1.000 | 0.333 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 0.500 | -0.500 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,374 | 1,540 | 166 |
| Output tokens | 3,924 | 4,258 | 334 |
| Visible brief characters | 7,975 | 7,638 | -337 |
| Visible brief words | 721 | 718 | -3 |
| Latency (s) | 24.381 | 26.550 | 2.169 |
| Estimated cost (USD) | 0.00819 | 0.00890 | 0.00071 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 1 | 2 | +1 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.333 | 0.000 |
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
| `risk_factor_recall` | 1.000 | 0.500 | -0.500 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,294 | 1,460 | 166 |
| Output tokens | 3,735 | 2,281 | -1,454 |
| Visible brief characters | 5,065 | 3,262 | -1,803 |
| Visible brief words | 368 | 244 | -124 |
| Latency (s) | 23.683 | 14.232 | -9.451 |
| Estimated cost (USD) | 0.00779 | 0.00493 | -0.00287 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 3 | 3 | +0 |
| `nutrition_considerations` | 3 | 0 | -3 |
| `nutritional_risk_factors` | 3 | 0 | -3 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.250 | 0.250 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.750 | 0.500 | -0.250 |
| `nutrition_consideration_precision` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.231 | 1.000 | 0.769 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.000 | 1.000 | 1.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_009

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,330 | 1,496 | 166 |
| Output tokens | 3,224 | 3,877 | 653 |
| Visible brief characters | 6,831 | 7,600 | 769 |
| Visible brief words | 583 | 678 | 95 |
| Latency (s) | 20.184 | 24.665 | 4.481 |
| Estimated cost (USD) | 0.00678 | 0.00813 | 0.00135 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 5 | +1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.333 | 0.333 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.000 | 0.667 | 0.667 |
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
| Input tokens | 1,336 | 1,502 | 166 |
| Output tokens | 3,898 | 3,694 | -204 |
| Visible brief characters | 7,211 | 6,422 | -789 |
| Visible brief words | 644 | 533 | -111 |
| Latency (s) | 24.567 | 23.426 | -1.141 |
| Estimated cost (USD) | 0.00813 | 0.00776 | -0.00037 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 4 | 4 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 3 | 3 | +0 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.750 | 0.500 | -0.250 |
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
