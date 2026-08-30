# Reproduction Guide

This guide describes how to reproduce the current Nutrition Module baseline from a clean
environment. It is a living document and must be updated whenever the model, prompt, dataset,
evaluation, or agent architecture changes.

## 1. Current reproducible scope

The repository currently includes:

- A single-prompt LLM baseline.
- A structured `BaselineBrief` validated with Pydantic.
- A locked dataset containing 20 synthetic nutrition cases.
- A separate development dataset containing 10 synthetic guardrail cases.
- Deterministic lexical evaluation metrics, structural checks, and labelled heuristic proxies.
- Unit tests and a no-cost dry-run mode.

Frozen Nutrition Reasoning Agent v3 and its deterministic gap, safety, and referral gates are
runnable. The Evidence Agent, approved knowledge base, retrieval pipeline, and Evidence Gate remain
pending, so the complete evidence-grounded workflow is not implemented yet.

## 2. Requirements

The recorded development environment uses:

| Component | Version |
|---|---:|
| Python | 3.14.6 |
| uv | 0.11.15 |
| OpenAI Python SDK | 3.6.0 |
| Pydantic | 2.13.5 or later within the lock file |
| Baseline model | `gpt-5-mini` |
| Frozen prompt | `nutrition-baseline-v4` |

Git and an OpenAI API key are also required for a real model execution.

## 3. Clone and install

```bash
git clone https://github.com/matitor-data/Health-Professional-Copilot.git
cd Health-Professional-Copilot
uv sync --locked
```

`uv sync --locked` creates the virtual environment from `pyproject.toml` and `uv.lock` without
changing the recorded dependency resolution.

## 4. Configure the API key

Create the local environment file:

```bash
cp .env.example .env
```

Edit `.env` and set:

```dotenv
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5-mini
```

Never commit `.env`. It is excluded by `.gitignore`.

## 5. Required data

The locked dataset is:

```text
data/cases/locked_test/nutrition_cases_021_040.json
```

It contains 20 synthetic cases, from `case_021` to `case_040`. Each case contains:

- A structured patient intake.
- Case type and difficulty.
- Expected information gaps.
- Expected follow-up topics.
- Expected nutrition considerations.
- Expected nutritional risk factors.
- Expected referral flags.
- Known medical context.
- Suggestions that must not be produced.

The dataset is synthetic and has not yet been clinically validated. It is treated as a locked test
set and should not be used to tune the prompt. Prompt experiments require a separate development
dataset, provided at `data/cases/development/nutrition_cases_dev.json`.

## 6. Validate the environment without API cost

Run the tests:

```bash
uv run python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 18 tests
OK
```

Validate the complete dataset and prompt construction without calling OpenAI:

```bash
uv run python -m baseline.runner --dry-run
```

Expected result:

```text
Validated 20 cases from data/cases/locked_test/nutrition_cases_021_040.json
Prompt version: nutrition-baseline-v4
```

## 7. Run the baseline

Start with one case:

```bash
uv run python -m baseline.runner \
  --prompt-version nutrition-baseline-v4 \
  --case-id case_021
```

Run all locked cases:

```bash
uv run python -m baseline.runner --prompt-version nutrition-baseline-v4
```

The baseline performs one structured LLM call per case. It has no tools, retrieval, Evidence Agent,
Evidence Gate, or autonomous loop.

## 8. Run the evaluation

Evaluation is currently integrated into the baseline runner. No second command is needed after a
successful baseline run. For each case, the runner compares the generated brief with the predefined
rubric and then aggregates the metrics.

Every real run creates:

```text
evaluation/runs/<run_id>/
├── manifest.json
├── outputs.jsonl
├── failures.jsonl
└── metrics.json
```

- `manifest.json` records the model, prompt version and hash, dataset path and hash, timestamp, and
  selected cases.
- `outputs.jsonl` contains the structured brief, usage, latency, and per-case metrics.
- Token usage separates `reasoning_tokens` from `visible_output_tokens`; `output_tokens` is their
  total and remains the value used for API cost estimation.
- `failures.jsonl` contains cases that could not be completed.
- `metrics.json` contains aggregate metrics for successful cases.

These files are ignored by Git because API response identifiers and experimental outputs should be
reviewed before publication.

Compare two compatible runs:

```bash
uv run python -m evaluation.compare \
  --baseline-run evaluation/runs/<baseline_run_id> \
  --candidate-run evaluation/runs/<candidate_run_id> \
  --output-dir evaluation/reports/<comparison_name>
```

The command creates `comparison.json` and `comparison.md` with per-case deltas for metrics, tokens,
visible brief size, latency, estimated cost, section counts, and an aggregate mean.

To reproduce the development prompt experiment, run each version against the development data with
a separate output root, then pass the resulting timestamped directories to `evaluation.compare`:

```bash
uv run python -m baseline.runner --dataset data/cases/development/nutrition_cases_dev.json \
  --prompt-version nutrition-baseline-v1 --output-root evaluation/runs/development/v1
uv run python -m baseline.runner --dataset data/cases/development/nutrition_cases_dev.json \
  --prompt-version nutrition-baseline-v2 --output-root evaluation/runs/development/v2
uv run python -m baseline.runner --dataset data/cases/development/nutrition_cases_dev.json \
  --prompt-version nutrition-baseline-v3 --output-root evaluation/runs/development/v3
```

The recorded 30-call experiment took approximately five minutes with the three runs executed in
parallel and cost an estimated USD 0.23562. Results are summarized in
`evaluation/reports/development/README.md`.

## 9. Run the complete solution

Run the implemented Nutrition Reasoning Agent on one development case:

```bash
uv run python -m nutrition_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json \
  --case-id dev_004
```

Run all development cases:

```bash
uv run python -m nutrition_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json
```

The command writes trajectories to `evaluation/agent_runs/<run_id>/`, including normalized patient
state, the reasoning draft, deterministic safety feedback, retry count, final brief, tokens, and
metrics. Agent v3 performs exactly one model call per case; unsupported optional items are removed
locally instead of triggering a correction call.

Agent v3 performs exactly one call per case and supports deterministic replay after gate or renderer
changes:

```bash
uv run python -m nutrition_agent.replay \
  --source-run evaluation/agent_runs/<agent_v3_run_id> \
  --output-root evaluation/agent_runs/replayed
```

Replay reuses the stored compact drafts and recorded token usage; it does not call the API.

Run the Nutrition Agent followed by the Evidence Agent on one development case:

```bash
uv run python -m evidence_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json \
  --case-id dev_003
```

The command writes `manifest.json`, `outputs.jsonl`, and `failures.jsonl` under
`evaluation/evidence_agent_runs/<run_id>/`. Each output includes the brief before and after
evidence, retrieval queries and chunks, the structured draft, Evidence Gate feedback, final
assessments, response IDs, separate token counts, and stage latency.

Validate the cases, approved source collection, and cached embedding index without API calls:

```bash
uv run python -m evidence_agent.runner \
  --dataset data/cases/development/nutrition_cases_dev.json \
  --case-id dev_003 \
  --dry-run
```

The retrieval layer can already be reproduced independently. Run the deterministic benchmark:

```bash
uv run python -m evidence_agent.evaluate \
  --output results/evidence_retrieval/deterministic_v1.json
```

Build the cached semantic index using the configured `OPENAI_API_KEY`:

```bash
uv run python -m evidence_agent.embedding_retrieval --build
```

Compare both retrieval systems on the same fixed benchmark:

```bash
uv run python -m evidence_agent.compare_retrieval
```

This command compares deterministic, embedding, and hybrid retrieval. The hybrid uses source-level
reciprocal rank fusion and admits a lexical fallback only with at least two matched terms and a
lexical score of at least 4. The comparison is written to
`results/evidence_retrieval/comparison_v1.json`. The recorded run used
`text-embedding-3-small`, 512 dimensions, a cosine-similarity threshold of 0.45, 3,278 input tokens
to build the 24-chunk index, and 301 input tokens for all 36 benchmark queries.

Run one hybrid query directly:

```bash
uv run python -m evidence_agent.hybrid_retrieval \
  "hydration based on sweat losses and hot environment" \
  --top-k 3
```

The held-out benchmark is frozen at
`data/evaluations/locked/evidence_retrieval_locked_v1.json`. Its only recorded execution is stored
in `results/evidence_retrieval/locked_comparison_v1.json`, with hashes and the unchanged retrieval
configuration in `results/evidence_retrieval/locked_run_v1_manifest.json`. Do not rerun this locked
set for tuning; create a new versioned benchmark for any future confirmation run.

## 10. Recorded reference execution

A real execution of `case_021` was recorded on 2026-08-29:

The historical execution used `nutrition-baseline-v1`. A second execution used
`nutrition-baseline-v3` on the same case and model.

| Field | Recorded value |
|---|---:|
| Model | `gpt-5-mini` |
| Prompt | `nutrition-baseline-v1` |
| Input tokens | 1,219 |
| Output tokens | 3,959 |
| End-to-end model latency | 44.111 seconds |
| Successful cases | 1 |
| Failed cases | 0 |
| Approximate API cost | USD 0.0082 |

The v3 candidate produced:

| Field | Recorded value |
|---|---:|
| Run | `20260829T224616Z` |
| Input tokens | 1,495 |
| Output tokens | 4,849 |
| Visible brief characters | 6,851 |
| End-to-end model latency | 36.044 seconds |
| Approximate API cost | USD 0.0101 |

Compared with v1, v3 reduced the visible brief by 3,807 characters (35.7%) and latency by 8.067
seconds, while total output tokens increased by 890 and estimated cost increased by about USD
0.00185. The token increase may include additional reasoning tokens; the recorded run did not store
reasoning-token details, so this explanation remains an inference.

The approximate cost uses GPT-5 mini prices available on 2026-08-29: USD 0.25 per one million input
tokens and USD 2.00 per one million output tokens. Pricing source:
[official OpenAI GPT-5 mini documentation](https://developers.openai.com/api/docs/models/gpt-5-mini).

Calculation:

```text
(1,219 × 0.25 / 1,000,000) + (3,959 × 2.00 / 1,000,000) = USD 0.00822
```

If all 20 cases consumed the same number of tokens, the estimated total would be approximately USD
0.16 and about 15 minutes of sequential model time. Actual time and cost will vary with case
complexity, output length, model availability, caching, retries, and pricing changes.

## 11. Current evaluation caveat

The current evaluator uses deterministic lexical overlap. This makes runs easy to reproduce, but it
can underestimate semantically correct answers that use different wording. The results must not be
treated as clinically validated performance.

Future reports should preserve the deterministic metrics and add semantic evaluation plus qualified
nutrition and medical review.

## 12. Reproduction checklist

- [ ] Clone the recorded commit.
- [ ] Run `uv sync --locked`.
- [ ] Configure `.env` without committing it.
- [ ] Run all thirty-six tests.
- [ ] Run the dry-run and validate 20 cases.
- [ ] Run at least one baseline case.
- [ ] Confirm that four run files were created.
- [ ] Record model, prompt hash, dataset hash, tokens, latency, and cost.
- [ ] Confirm that `supporting_evidence` is empty for the baseline.
- [ ] Confirm that no unreported medical diagnosis or new laboratory recommendation appears.
