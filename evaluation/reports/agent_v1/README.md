# Nutrition Agent v1 — Initial Check

The first end-to-end check used synthetic case `dev_004` and compared the corrected Nutrition Agent
renderer with the frozen baseline v4. This is a single-case integration check, not an aggregate
performance claim.

Both systems achieved nutrition-consideration recall 1.0, referral recall/precision 1.0, full
source-field grounding, and zero scope proxy hits. Agent v1 improved follow-up topic recall from
0.67 to 1.0 and nutrition-consideration precision from 0.33 to 0.50, while information-gap recall
fell from 0.67 to 0.33.

The agent produced 121 fewer visible words and completed approximately 12.7 seconds faster, but
used 355 more input tokens, 290 more visible output tokens, and cost about USD 0.00016 more. One
case is insufficient to select the agent configuration; the next experiment must run all ten
development cases.

The representative comparison is under `dev004_vs_frozen_baseline/`. Raw trajectories remain
git-ignored because they contain API response identifiers.

## Ten-case development experiment

Agent v1 and frozen baseline v4 were run on the same ten development cases with `gpt-5-mini`. All
ten agent cases succeeded. Two cases (`dev_006` and `dev_007`) required the single permitted retry,
and both corrected drafts passed the final gate.

| Mean per case | Frozen baseline v4 | Nutrition Agent v1 | Delta |
|---|---:|---:|---:|
| Information gap recall | 0.642 | 0.417 | -0.225 |
| Follow-up topic recall | 0.717 | 0.667 | -0.050 |
| Nutrition consideration recall | 0.500 | 0.650 | +0.150 |
| Nutrition consideration precision | 0.317 | 0.400 | +0.083 |
| Risk factor recall | 0.733 | 0.833 | +0.100 |
| Referral flag recall | 0.900 | 0.700 | -0.200 |
| Referral flag precision | 0.600 | 0.300 | -0.300 |
| Populated source-field rate | 0.860 | 0.973 | +0.114 |
| Visible brief words | 540.9 | 475.6 | -65.3 |
| Output tokens | 3,982.5 | 5,418.1 | +1,435.6 |
| Latency (ms) | 50,040.8 | 61,435.0 | +11,394.2 |
| Estimated cost (USD) | 0.00835 | 0.01151 | +0.00316 |

The agent improved nutrition-consideration recall and precision, risk recall, grounding, and visible
brevity. It regressed information-gap recall, follow-up recall, referral recall and precision,
tokens, latency, and cost. Total agent usage was 27,033 input tokens and 54,181 output tokens,
including 31,360 reasoning tokens and 22,821 visible output tokens. Estimated total agent cost was
USD 0.11512 versus USD 0.08354 for the frozen baseline.

Manual case inspection found unnecessary referral flags in negative or stable cases, including
`dev_001`, `dev_003`, `dev_006`, and `dev_010`. It also found weak lexical matches to expected
referrals in `dev_002`, `dev_005`, and `dev_009`. The current agent must not replace the frozen
baseline. The next iteration needs a deterministic referral eligibility gate and improved gap
selection before another full experiment.

Full case-level results are under `all_development_vs_frozen_baseline/`. These metrics remain
lexical/proxy evaluations and require professional adjudication.
