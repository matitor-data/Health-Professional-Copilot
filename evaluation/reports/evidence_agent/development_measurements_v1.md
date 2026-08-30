# Evidence Agent development measurements

This report compares the two complete ten-case development runs produced with the same agent and
retrieval configuration. The JSON report contains all per-run values and aligned consideration
pairs.

## Per-run results

| Metric | `20260830T052956Z` | `20260830T053131Z` |
|---|---:|---:|
| Assessments | 22 | 20 |
| Gate acceptance | 1.000 | 1.000 |
| Retrieval coverage | 0.864 | 0.850 |
| Evidence support coverage | 0.818 | 0.700 |
| Full support rate | 0.545 | 0.500 |
| Unresolved rate | 0.182 | 0.300 |
| Citation validity | 1.000 | 1.000 |
| Cited assessment rate | 0.818 | 0.850 |
| Single-citation proxy | 0.778 | 0.941 |
| Limitation coverage | 1.000 | 1.000 |
| Eligible render fidelity | 1.000 | 1.000 |
| Ineligible exclusion fidelity | 1.000 | 1.000 |
| References | 22 | 18 |

Citation validity checks that every reference was among the chunks retrieved for that exact
consideration. It does not prove semantic support. The single-citation proxy measures citation
count only and does not prove that a citation was necessary.

## Run-to-run stability

| Metric | Value |
|---|---:|
| Assessment count difference | 2 |
| Lexically aligned assessments | 13 |
| Consideration alignment F1 | 0.619 |
| Exact-match rate among aligned items | 1.000 |
| Support-status agreement among aligned items | 0.846 |
| Citation-set agreement among aligned items | 0.846 |

The alignment is a declared lexical proxy using greedy Jaccard matching at `>= 0.35`. It aligned 13
exactly repeated considerations; semantically similar but substantially reworded considerations
were not counted as stable.

Two exact considerations changed evidence interpretation:

- `dev_001`: `supported` versus `partially_supported`.
- `dev_005`: `outside_source_scope` versus `unsupported`.

## Conclusion

Deterministic safety behavior is stable: both runs have perfect gate acceptance, citation validity,
limitation coverage, and renderer fidelity. Content generation and evidence interpretation remain
variable. The Evidence Agent should not be frozen until consideration stability and status
agreement improve or the accepted variability is explicitly bounded by a reviewed rubric.
