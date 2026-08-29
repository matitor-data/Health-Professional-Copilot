# Video Script

Working script for a video of no more than five minutes. This version covers the problem, the simple
baseline, one recorded execution, and the prompt change introduced to reduce token use. Replace
provisional sections as the complete agentic solution is implemented.

## 0:00-0:35 - The problem

**On screen:** Project title, followed by a compact patient intake form.

**Narration:**

> Nutrition professionals prepare for consultations by combining dietary patterns, symptoms,
> established medical diagnoses, medications, supplements, lifestyle factors, and existing lab
> results. The challenge is not simply finding medical information. It is connecting the specific
> patient context with the right questions, nutrition considerations, risk factors, and possible
> referral needs under limited time and attention.
>
> A static intake form collects information, but it cannot identify what is still missing or what
> may deserve further exploration. Health Professional Copilot is designed to provide a second
> layer of attention while remaining within the nutritionist's scope of practice.

## 0:35-1:10 - Scope and baseline

**On screen:** Diagram: `Patient Intake -> One Prompt -> One LLM Call -> Structured Brief`.

**Narration:**

> I started with the simplest measurable baseline. It takes one structured patient intake, sends
> one versioned prompt to GPT-5 mini, and validates the response against a Pydantic schema.
>
> The baseline has no tools, no retrieval, no evidence agent, and no agent loop. Medical diagnoses
> can only be copied from the input. It cannot infer a diagnosis, modify medication, recommend new
> laboratory tests, or invent supporting evidence. It can flag that medical assessment may be
> required without claiming what the diagnosis is.

## 1:10-1:35 - Reproducible data and evaluation

**On screen:** Open `data/cases/locked_test/nutrition_cases_021_040.json`, then
`evaluation/metrics.py`.

**Narration:**

> The current dataset contains twenty synthetic cases with predefined expectations for information
> gaps, follow-up topics, nutrition considerations, nutritional risk factors, referral flags, and
> prohibited suggestions. The same cases will later be used to compare the baseline with the
> two-agent solution.
>
> The current evaluator is deliberately simple and deterministic. It provides reproducible lexical
> metrics, but it will later be complemented with semantic evaluation and professional review.

## 1:35-2:30 - Run one case from start to finish

**On screen:** Terminal and the `case_021` patient intake.

**Narration:**

> First, I validate the environment without making an API call.

**On screen:** Run:

```bash
uv run python -m unittest discover -s tests -v
uv run python -m baseline.runner --dry-run
```

**Narration:**

> The five tests pass, and all twenty cases validate. Now I run one realistic case: a vegetarian
> patient with physician-diagnosed iron deficiency anemia, prescribed iron supplementation, and
> persistent fatigue.

**On screen:** Run:

```bash
uv run python -m baseline.runner --case-id case_021
```

**Narration:**

> The runner validates the intake, builds the versioned prompt, requests a structured response,
> validates the brief, compares it with the rubric, and writes a manifest, outputs, failures, and
> aggregate metrics.

## 2:30-3:15 - Inspect the result

**On screen:** Show the generated brief and then `metrics.json`.

**Narration:**

> The response remained within the main safety boundaries. It did not create a new diagnosis, did
> not recommend changing the prescribed supplement, did not invent evidence, and correctly raised
> a prompt medical follow-up flag for persistent fatigue.
>
> On this first run, referral recall and precision were both one hundred percent, information-gap
> recall was seventy-five percent, and there were zero prohibited suggestions. Nutrition
> consideration recall was fifty percent and measured precision was forty percent. Some of these
> lower scores reflect the limits of lexical matching, but the output also reveals a real baseline
> weakness: it generates too much material.

## 3:15-4:05 - The prompt problem and the implemented change

**On screen:** Display: `1,219 input tokens`, `3,959 output tokens`, `44.1 seconds`, `~$0.0082`.

**Narration:**

> The first case used one thousand two hundred nineteen input tokens and three thousand nine hundred
> fifty-nine output tokens. It took about forty-four seconds and cost approximately eight-tenths of
> one cent at the recorded GPT-5 mini prices.
>
> The main problem is not the input. It is the amount of output encouraged by the prompt and schema.
> The model produced six clarification topics, six questions, five nutrition considerations, four
> risk factors, and four blind spots, each with long rationales. This increases latency, cost, and
> the risk of overwhelming the professional.
>
> The new prompt version introduces explicit budgets: up to five gaps, three to five questions,
> up to three nutrition considerations, up to four risk factors, up to two referral flags, and up to
> three blind spots. Rationales will be limited to one concise sentence, and secondary
> considerations require at least two case-specific facts. It also prevents generic risk expansion
> from dietary patterns, distinguishes unreported facts from actual absence, avoids assumptions
> about treatment adherence or response, and requires referral flags to describe only what the
> intake actually reports.

## 4:05-4:35 - Changelog and comparison plan

**On screen:** Open `CHANGELOG.md`, then show
`evaluation/reports/v1_vs_v3_case021/comparison.md`.

**Narration:**

> The changelog records the baseline, the locked dataset, the first real execution, and the current
> limitations. Output budgeting contributed most to visible concision: the brief fell from about
> ten thousand six hundred to six thousand eight hundred characters, and nutrition-consideration
> precision increased from forty to sixty-seven percent. However, total output tokens increased,
> so the token-cost objective has not yet been achieved and needs a separate experiment.
>
> One approach intentionally excluded from the baseline is retrieval. Adding evidence now would make
> it impossible to know whether later improvements come from agent reasoning or from the knowledge
> system. Retrieval belongs in the evidence agent and will be measured as a separate iteration.

## 4:35-5:00 - Close

**On screen:** Diagram showing baseline on the left and future two-agent solution on the right.

**Narration:**

> The baseline is now reproducible, measurable, and intentionally limited. The next step is to test
> the shorter prompt on a representative development set, reduce reasoning-token cost, freeze the
> reference results, and then compare it with the
> Nutrition Reasoning Agent, the Evidence Agent, and deterministic safety and evidence gates on the
> exact same cases.

## Recording checklist

- Keep the final recording below five minutes.
- Do not display `.env`, the API key, full response IDs, or account information.
- Use one pre-recorded successful run to avoid waiting through model latency.
- Show the exact commit hash used for the recording.
- Replace provisional comparisons once the complete solution exists.
- Mention that cases are synthetic and not yet clinically validated.
