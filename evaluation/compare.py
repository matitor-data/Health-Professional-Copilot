from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_INPUT_PRICE_PER_MILLION = 0.25
DEFAULT_OUTPUT_PRICE_PER_MILLION = 2.00

COUNT_FIELDS = (
    "information_to_clarify",
    "suggested_questions",
    "nutrition_considerations",
    "nutritional_risk_factors",
    "referral_escalation_flags",
    "potential_blind_spots",
)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            rows[row["case_id"]] = row
    return rows


def _cost(row: dict[str, Any], input_price: float, output_price: float) -> float:
    input_tokens = row.get("input_tokens") or 0
    output_tokens = row.get("output_tokens") or 0
    return (input_tokens * input_price + output_tokens * output_price) / 1_000_000


def _counts(row: dict[str, Any]) -> dict[str, int]:
    brief = row.get("brief", {})
    return {field: len(brief.get(field, [])) for field in COUNT_FIELDS}


def _visible_size(row: dict[str, Any]) -> dict[str, int]:
    serialized = json.dumps(row.get("brief", {}), ensure_ascii=False, separators=(",", ":"))
    return {"characters": len(serialized), "words": len(serialized.split())}


def compare_runs(
    baseline_dir: Path,
    candidate_dir: Path,
    input_price: float = DEFAULT_INPUT_PRICE_PER_MILLION,
    output_price: float = DEFAULT_OUTPUT_PRICE_PER_MILLION,
) -> dict[str, Any]:
    baseline_manifest = _read_json(baseline_dir / "manifest.json")
    candidate_manifest = _read_json(candidate_dir / "manifest.json")
    baseline_rows = _read_jsonl(baseline_dir / "outputs.jsonl")
    candidate_rows = _read_jsonl(candidate_dir / "outputs.jsonl")
    shared_cases = sorted(set(baseline_rows) & set(candidate_rows))
    if not shared_cases:
        raise ValueError("The runs do not contain any shared successful cases")

    cases: list[dict[str, Any]] = []
    for case_id in shared_cases:
        before, after = baseline_rows[case_id], candidate_rows[case_id]
        metric_names = sorted(set(before.get("metrics", {})) & set(after.get("metrics", {})))
        before_cost = _cost(before, input_price, output_price)
        after_cost = _cost(after, input_price, output_price)
        cases.append(
            {
                "case_id": case_id,
                "baseline": {
                    "input_tokens": before.get("input_tokens"),
                    "output_tokens": before.get("output_tokens"),
                    "latency_ms": before.get("latency_ms"),
                    "estimated_cost_usd": before_cost,
                    "visible_output": _visible_size(before),
                    "counts": _counts(before),
                    "metrics": before.get("metrics", {}),
                },
                "candidate": {
                    "input_tokens": after.get("input_tokens"),
                    "output_tokens": after.get("output_tokens"),
                    "latency_ms": after.get("latency_ms"),
                    "estimated_cost_usd": after_cost,
                    "visible_output": _visible_size(after),
                    "counts": _counts(after),
                    "metrics": after.get("metrics", {}),
                },
                "delta": {
                    "input_tokens": (after.get("input_tokens") or 0) - (before.get("input_tokens") or 0),
                    "output_tokens": (after.get("output_tokens") or 0) - (before.get("output_tokens") or 0),
                    "latency_ms": (after.get("latency_ms") or 0) - (before.get("latency_ms") or 0),
                    "estimated_cost_usd": after_cost - before_cost,
                    "visible_output": {
                        name: _visible_size(after)[name] - _visible_size(before)[name]
                        for name in ("characters", "words")
                    },
                    "counts": {
                        field: _counts(after)[field] - _counts(before)[field] for field in COUNT_FIELDS
                    },
                    "metrics": {
                        name: float(after["metrics"][name]) - float(before["metrics"][name])
                        for name in metric_names
                    },
                },
            }
        )

    return {
        "baseline_run": baseline_manifest,
        "candidate_run": candidate_manifest,
        "pricing": {
            "input_usd_per_million_tokens": input_price,
            "output_usd_per_million_tokens": output_price,
        },
        "shared_cases": shared_cases,
        "cases": cases,
    }


def _fmt(value: float | int | None, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, int):
        return f"{value:,}"
    return f"{value:.{digits}f}"


def render_markdown(report: dict[str, Any]) -> str:
    baseline = report["baseline_run"]
    candidate = report["candidate_run"]
    lines = [
        "# Baseline Comparison Report",
        "",
        f"- Baseline run: `{baseline['run_id']}` (`{baseline['prompt_version']}`)",
        f"- Candidate run: `{candidate['run_id']}` (`{candidate['prompt_version']}`)",
        f"- Model: `{candidate['model']}`",
        f"- Shared successful cases: {len(report['shared_cases'])}",
        "",
    ]

    for case in report["cases"]:
        before, after, delta = case["baseline"], case["candidate"], case["delta"]
        lines.extend(
            [
                f"## {case['case_id']}",
                "",
                "| Efficiency | Baseline | Candidate | Delta |",
                "|---|---:|---:|---:|",
                f"| Input tokens | {_fmt(before['input_tokens'])} | {_fmt(after['input_tokens'])} | {_fmt(delta['input_tokens'])} |",
                f"| Output tokens | {_fmt(before['output_tokens'])} | {_fmt(after['output_tokens'])} | {_fmt(delta['output_tokens'])} |",
                f"| Visible brief characters | {_fmt(before['visible_output']['characters'])} | {_fmt(after['visible_output']['characters'])} | {_fmt(delta['visible_output']['characters'])} |",
                f"| Visible brief words | {_fmt(before['visible_output']['words'])} | {_fmt(after['visible_output']['words'])} | {_fmt(delta['visible_output']['words'])} |",
                f"| Latency (s) | {_fmt(before['latency_ms'] / 1000)} | {_fmt(after['latency_ms'] / 1000)} | {_fmt(delta['latency_ms'] / 1000)} |",
                f"| Estimated cost (USD) | {_fmt(before['estimated_cost_usd'], 5)} | {_fmt(after['estimated_cost_usd'], 5)} | {_fmt(delta['estimated_cost_usd'], 5)} |",
                "",
                "| Brief section | Baseline | Candidate | Delta |",
                "|---|---:|---:|---:|",
            ]
        )
        for field in COUNT_FIELDS:
            lines.append(
                f"| `{field}` | {before['counts'][field]} | {after['counts'][field]} | {delta['counts'][field]:+d} |"
            )
        lines.extend(["", "| Metric | Baseline | Candidate | Delta |", "|---|---:|---:|---:|"])
        for name in sorted(delta["metrics"]):
            lines.append(
                f"| `{name}` | {_fmt(before['metrics'][name])} | {_fmt(after['metrics'][name])} | {_fmt(delta['metrics'][name])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Interpretation notes",
            "",
            "- Negative token, latency, and cost deltas indicate improvement.",
            "- Metric deltas use the current deterministic lexical evaluator and require manual review.",
            "- Cost is estimated from the token prices passed to the comparison command.",
            "- A shorter output is not automatically better if referral safety or relevant recall decreases.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare two baseline run directories")
    parser.add_argument("--baseline-run", type=Path, required=True)
    parser.add_argument("--candidate-run", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--input-price", type=float, default=DEFAULT_INPUT_PRICE_PER_MILLION)
    parser.add_argument("--output-price", type=float, default=DEFAULT_OUTPUT_PRICE_PER_MILLION)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = compare_runs(
        args.baseline_run,
        args.candidate_run,
        input_price=args.input_price,
        output_price=args.output_price,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "comparison.json"
    markdown_path = args.output_dir / "comparison.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    print(f"Comparison written to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
