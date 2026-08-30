# Execution Report

## Outcome

The frozen baseline and frozen Nutrition Module were evaluated on 20 locked synthetic cases. They shared 20 successful cases; the baseline had 0 failures and the solution had 0 failures.

This is a prototype benchmark, not clinical validation and not evidence of improved patient outcomes.

### Executive conclusion

The locked comparison did **not** support the primary hypothesis that the complete module would
identify more expected consultation information than the simple baseline. Every measured recall or
precision metric shown below decreased. The solution did, however, eliminate scope-violation proxy
hits, preserve zero unnecessary referrals, reduce visible output by approximately 35%, and provide
fully traceable evidence citations. These safety and usability gains came with approximately 19%
more latency and 12% more estimated cost.

The result was preserved without tuning or rerunning either frozen system.

## Final comparison

| Metric | Baseline | Nutrition Module | Delta |
|---|---:|---:|---:|
| `information_gap_recall` | 0.693 | 0.351 | -0.342 |
| `followup_topic_recall` | 0.604 | 0.573 | -0.031 |
| `nutrition_consideration_recall` | 0.300 | 0.175 | -0.125 |
| `nutrition_consideration_precision` | 0.250 | 0.175 | -0.075 |
| `risk_factor_recall` | 0.754 | 0.550 | -0.204 |
| `referral_flag_recall` | 0.408 | 0.200 | -0.208 |
| `referral_flag_precision` | 0.500 | 0.200 | -0.300 |
| `unnecessary_referral_count` | 0.000 | 0.000 | +0.000 |
| `scope_violation_proxy_hits` | 0.150 | 0.000 | -0.150 |

## Efficiency

Mean per shared successful case. Solution totals include both model calls; embedding tokens are included only in estimated cost.

| Measure | Baseline | Nutrition Module | Delta |
|---|---:|---:|---:|
| `input_tokens` | 1547.2 | 1850.8 | +303.7 |
| `output_tokens` | 3923.8 | 4395.9 | +472.1 |
| `reasoning_tokens` | 2310.4 | 3347.2 | +1036.8 |
| `visible_tokens` | 1613.4 | 1048.8 | -564.7 |
| `latency_ms` | 42877.2 | 51194.3 | +8317.1 |
| `cost_usd` | 0.00823 | 0.00926 | +0.00102 |

Across all 20 cases, estimated cost was approximately USD 0.16469 for the baseline and USD 0.18512
for the complete module. Summed model-stage latency was approximately 14.3 and 17.1 minutes
respectively; wall-clock reproduction time varies with API conditions.

## Evidence layer

- Assessments: 43.
- Support states: `{"outside_source_scope": 15, "partially_supported": 16, "supported": 11, "unsupported": 1}`.
- Supported or partially supported: 0.628.
- Evidence Gate acceptance: 1.000.
- Retrieved citations: 29.
- Citation provenance validity: 1.000.

## Interpretation for the video

The largest architectural contribution was moving stable consultation-preparation tasks into deterministic components while restricting model work to compact nutrition reasoning and evidence assessment. The removed experiment was the general model correction loop; invalid optional items are now removed locally instead of triggering another model call.

## Reproducibility

- Baseline run: `20260830T155457Z`.
- Solution run: `20260830T161328Z`.
- Dataset: `data/cases/locked_test/nutrition_cases_021_040.json`.
- Prices used: GPT-5 mini $0.25 input / $2.00 output and text-embedding-3-small $0.02 input per million tokens.

## Limitations

- All cases, evidence sources, and rubrics are synthetic.
- Lexical rubric metrics are reproducible proxies, not clinical performance measures.
- Citation validity confirms retrieval provenance, not clinical correctness or necessity.
- The locked comparison is intended to be executed once without post-result tuning.
