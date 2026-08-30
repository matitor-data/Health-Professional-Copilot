# Complete Prototype Demonstration — `dev_003`

Recorded run: `20260830T153611Z`

Data: synthetic development case and synthetic approved evidence sources

Result: one successful case, zero failures, zero gate violations

## Patient context

The consultation goal is nutrition support for physician-diagnosed prediabetes. The intake reports
daily sugar-sweetened beverages and few vegetables. The module does not infer a new diagnosis.

## Nutrition Agent output

The agent produced three grounded considerations:

1. Reduce frequent sugar-sweetened beverages.
2. Increase fiber-rich foods and overall dietary quality.
3. Integrate the known prediabetes context with the reported beverage pattern when planning the
   consultation.

It produced no referral flag for this case. Deterministic gates preserved the reported diagnosis as
context and did not introduce medication changes, new tests, or diagnostic claims.

## Retrieval and Evidence Agent output

Hybrid retrieval searched the approved synthetic collection separately for each consideration. The
Evidence Agent returned:

| Consideration | Support state | Cited source chunk |
|---|---|---|
| Sugar-sweetened beverages | Supported | `synthetic_prediabetes_fiber_v1:evidence-statements` |
| Fiber-rich foods | Supported | `synthetic_prediabetes_fiber_v1:evidence-statements` |
| Integrated behavior-change planning | Partially supported | `synthetic_prediabetes_fiber_v1:consultation-implications` |

The Evidence Gate accepted all assessments. Every citation was present in the corresponding
retrieval packet, and the final renderer preserved all pre-evidence nutrition sections.

## Usage

| Stage | Input | Output | Reasoning | Visible | Latency |
|---|---:|---:|---:|---:|---:|
| Nutrition Agent | 1,070 | 3,400 | 2,624 | 776 | 42.605 s |
| Evidence embeddings | 84 | — | — | — | included below |
| Evidence Agent | 1,263 | 1,768 | 1,280 | 488 | 18.193 s |

## Interpretation

This trajectory demonstrates the intended mechanics: grounded consultation preparation, per-claim
retrieval, traceable citations, explicit partial support, and deterministic citation validation. It
does not demonstrate clinical effectiveness. The case, evidence, and evaluation are synthetic, and
the module is not intended for production or patient-care decisions.
