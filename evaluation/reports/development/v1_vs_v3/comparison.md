# Baseline Comparison Report

- Baseline run: `20260829T230906Z` (`nutrition-baseline-v1`)
- Candidate run: `20260829T230907Z` (`nutrition-baseline-v3`)
- Model: `gpt-5-mini`
- Shared successful cases: 10

## Aggregate results (mean per case)

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1256.80000 | 1504.80000 | 248.00000 |
| Output tokens | 3438.00000 | 3930.50000 | 492.50000 |
| Latency (ms) | 22723.90000 | 25944.00000 | 3220.10000 |
| Estimated cost (USD) | 0.00719 | 0.00824 | 0.00105 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1.000 | 1.000 | 0.000 |
| `followup_topic_recall` | 0.567 | 0.508 | -0.058 |
| `forbidden_suggestion_hits` | 0.100 | 0.100 | 0.000 |
| `information_gap_recall` | 0.725 | 0.667 | -0.058 |
| `nutrition_consideration_precision` | 0.267 | 0.400 | 0.133 |
| `nutrition_consideration_recall` | 0.400 | 0.600 | 0.200 |
| `output_budget_violations` | 0.000 | 0.000 | 0.000 |
| `populated_source_field_rate` | 0.888 | 0.982 | 0.094 |
| `rationale_sentence_violation_proxy` | 0.000 | 0.000 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.800 | 0.650 | -0.150 |
| `referral_flag_recall` | 1.000 | 0.900 | -0.100 |
| `risk_factor_recall` | 0.850 | 0.717 | -0.133 |
| `scope_violation_proxy_hits` | 0.400 | 0.300 | -0.100 |
| `secondary_consideration_grounding_proxy` | 0.650 | 0.900 | 0.250 |
| `supporting_evidence_count` | 0.000 | 0.000 | 0.000 |
| `treatment_assumption_proxy_hits` | 0.000 | 0.000 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_001

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,246 | 1,494 | 248 |
| Output tokens | 2,978 | 3,614 | 636 |
| Visible brief characters | 6,453 | 6,520 | 67 |
| Visible brief words | 552 | 591 | 39 |
| Latency (s) | 19.789 | 23.579 | 3.790 |
| Estimated cost (USD) | 0.00627 | 0.00760 | 0.00133 |

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
| `populated_source_field_rate` | 0.812 | 0.900 | 0.088 |
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
| Input tokens | 1,262 | 1,510 | 248 |
| Output tokens | 4,458 | 3,307 | -1,151 |
| Visible brief characters | 8,385 | 6,493 | -1,892 |
| Visible brief words | 798 | 586 | -212 |
| Latency (s) | 27.772 | 22.232 | -5.540 |
| Estimated cost (USD) | 0.00923 | 0.00699 | -0.00224 |

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
| `followup_topic_recall` | 0.667 | 0.667 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
| `nutrition_consideration_precision` | 1.000 | 0.667 | -0.333 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.889 | 0.923 | 0.034 |
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
| Input tokens | 1,299 | 1,547 | 248 |
| Output tokens | 3,357 | 3,994 | 637 |
| Visible brief characters | 6,750 | 6,400 | -350 |
| Visible brief words | 553 | 523 | -30 |
| Latency (s) | 24.341 | 28.858 | 4.517 |
| Estimated cost (USD) | 0.00704 | 0.00837 | 0.00134 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 4 | -1 |
| `suggested_questions` | 5 | 4 | -1 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 4 | +0 |
| `referral_escalation_flags` | 0 | 0 | +0 |
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
| `referral_flag_precision` | 1.000 | 1.000 | 0.000 |
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
| Input tokens | 1,255 | 1,503 | 248 |
| Output tokens | 4,078 | 5,853 | 1,775 |
| Visible brief characters | 7,449 | 7,931 | 482 |
| Visible brief words | 638 | 718 | 80 |
| Latency (s) | 28.472 | 39.985 | 11.513 |
| Estimated cost (USD) | 0.00847 | 0.01208 | 0.00361 |

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
| Input tokens | 1,255 | 1,503 | 248 |
| Output tokens | 3,383 | 4,311 | 928 |
| Visible brief characters | 7,163 | 7,437 | 274 |
| Visible brief words | 611 | 676 | 65 |
| Latency (s) | 23.655 | 29.366 | 5.711 |
| Estimated cost (USD) | 0.00708 | 0.00900 | 0.00192 |

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
| `information_gap_recall` | 1.000 | 1.000 | 0.000 |
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
| Input tokens | 1,245 | 1,493 | 248 |
| Output tokens | 3,300 | 4,116 | 816 |
| Visible brief characters | 6,937 | 6,516 | -421 |
| Visible brief words | 592 | 573 | -19 |
| Latency (s) | 22.532 | 26.547 | 4.015 |
| Estimated cost (USD) | 0.00691 | 0.00861 | 0.00169 |

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
| `nutrition_consideration_precision` | 0.000 | 0.333 | 0.333 |
| `nutrition_consideration_recall` | 0.000 | 0.500 | 0.500 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 1.000 | 1.000 | 0.000 |
| `rationale_sentence_violation_proxy` | 0 | 0 | 0.000 |
| `referral_flag_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `referral_flag_precision` | 0.000 | 0.000 | 0.000 |
| `referral_flag_recall` | 1.000 | 1.000 | 0.000 |
| `risk_factor_recall` | 1.000 | 1.000 | 0.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 0.000 | 0.500 | 0.500 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_007

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,292 | 1,540 | 248 |
| Output tokens | 3,292 | 4,258 | 966 |
| Visible brief characters | 7,848 | 7,638 | -210 |
| Visible brief words | 699 | 718 | 19 |
| Latency (s) | 21.172 | 26.550 | 5.378 |
| Estimated cost (USD) | 0.00691 | 0.00890 | 0.00199 |

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
| `risk_factor_recall` | 0.500 | 0.500 | 0.000 |
| `scope_violation_proxy_hits` | 1 | 1 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_008

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,212 | 1,460 | 248 |
| Output tokens | 3,169 | 2,281 | -888 |
| Visible brief characters | 6,066 | 3,262 | -2,804 |
| Visible brief words | 462 | 244 | -218 |
| Latency (s) | 19.833 | 14.232 | -5.601 |
| Estimated cost (USD) | 0.00664 | 0.00493 | -0.00171 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 3 | -2 |
| `nutrition_considerations` | 3 | 0 | -3 |
| `nutritional_risk_factors` | 4 | 0 | -4 |
| `referral_escalation_flags` | 0 | 0 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.250 | 0.250 | 0.000 |
| `forbidden_suggestion_hits` | 0 | 0 | 0.000 |
| `information_gap_recall` | 0.250 | 0.500 | 0.250 |
| `nutrition_consideration_precision` | 0.000 | 1.000 | 1.000 |
| `nutrition_consideration_recall` | 1.000 | 1.000 | 0.000 |
| `output_budget_violations` | 0 | 0 | 0.000 |
| `populated_source_field_rate` | 0.250 | 1.000 | 0.750 |
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
| Input tokens | 1,248 | 1,496 | 248 |
| Output tokens | 3,037 | 3,877 | 840 |
| Visible brief characters | 7,327 | 7,600 | 273 |
| Visible brief words | 659 | 678 | 19 |
| Latency (s) | 19.069 | 24.665 | 5.596 |
| Estimated cost (USD) | 0.00639 | 0.00813 | 0.00174 |

| Brief section | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `information_to_clarify` | 5 | 5 | +0 |
| `suggested_questions` | 5 | 5 | +0 |
| `nutrition_considerations` | 3 | 3 | +0 |
| `nutritional_risk_factors` | 4 | 3 | -1 |
| `referral_escalation_flags` | 1 | 1 | +0 |
| `potential_blind_spots` | 3 | 3 | +0 |

| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| `existing_lab_fidelity` | 1 | 1 | 0.000 |
| `followup_topic_recall` | 0.667 | 0.333 | -0.333 |
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
| `risk_factor_recall` | 1.000 | 0.000 | -1.000 |
| `scope_violation_proxy_hits` | 0 | 0 | 0.000 |
| `secondary_consideration_grounding_proxy` | 1.000 | 1.000 | 0.000 |
| `supporting_evidence_count` | 0 | 0 | 0.000 |
| `treatment_assumption_proxy_hits` | 0 | 0 | 0.000 |
| `valid_source_field_rate` | 1.000 | 1.000 | 0.000 |

## dev_010

| Efficiency | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Input tokens | 1,254 | 1,502 | 248 |
| Output tokens | 3,328 | 3,694 | 366 |
| Visible brief characters | 7,046 | 6,422 | -624 |
| Visible brief words | 599 | 533 | -66 |
| Latency (s) | 20.604 | 23.426 | 2.822 |
| Estimated cost (USD) | 0.00697 | 0.00776 | 0.00079 |

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
| `followup_topic_recall` | 0.750 | 0.500 | -0.250 |
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
