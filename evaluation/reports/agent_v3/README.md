# Nutrition Agent v3 — Development Experiment

Agent v3 ran once on all ten synthetic development cases with `gpt-5-mini`. The model calls all
succeeded with zero retries. After inspecting deterministic gap coverage, the same stored compact
drafts were replayed through improved general-purpose gap and nutrition-consideration rules; no
additional model calls or token cost were incurred. The final replay run is `20260830T011416Z`,
derived from API run `20260830T010612Z`.

## Final comparison

| Mean per case | Frozen baseline v4 | Agent v2 | Agent v3 |
|---|---:|---:|---:|
| Information gap recall | 0.642 | 0.583 | 0.892 |
| Follow-up topic recall | 0.717 | 0.683 | 0.708 |
| Nutrition consideration recall | 0.500 | 0.450 | 1.000 |
| Nutrition consideration precision | 0.317 | 0.250 | 0.767 |
| Risk factor recall | 0.733 | 0.767 | 0.650 |
| Referral recall (legacy rubric) | 0.900 | 0.800 | 0.800 |
| Referral precision | 0.600 | 0.800 | 0.800 |
| Referral pathway accuracy | n/a | n/a | 1.000 |
| Unnecessary referrals | 0.30 | 0.00 | 0.00 |
| Scope proxy hits | 0.10 | 0.20 | 0.00 |
| Retry rate | n/a | 20% | 0% |
| Input tokens | 1,554.8 | 2,331.4 | 1,126.5 |
| Output tokens | 3,982.5 | 5,953.0 | 3,330.7 |
| Visible output words | 540.9 | 538.5 | 343.2 |
| Latency (ms) | 50,040.8 | 67,892.3 | 24,923.2 |
| Estimated cost (USD) | 0.00835 | 0.01249 | 0.00694 |

V3 met the development criteria for gaps, nutrition considerations, referral pathways, retries,
scope, and cost. It still trails the baseline on risk-factor recall and legacy referral recall. The
legacy referral metric counts the two prospectively labelled `clarify_first` pathways as misses;
pathway accuracy evaluates those decisions as intended.

## Interpretation boundary

The Gap Coverage Engine and supported-consideration renderer were tuned using these development
cases and their rubrics. The strong scores may therefore reflect development-set overfitting. The
original case rubrics and locked test data were not modified, and the prospective pathway overlay
was recorded before the v3 API run. Before using the locked set, qualified nutrition and medical
reviewers should inspect the new deterministic rules and pathway labels.

Detailed reports are under `all_development_vs_frozen_baseline/` and `v2_vs_v3/`.

