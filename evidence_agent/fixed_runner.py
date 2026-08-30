from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv

from baseline.schemas import BaselineBrief
from baseline.runner import sha256
from evidence_agent.agent import OpenAIEvidenceAgent
from evidence_agent.embedding_retrieval import DEFAULT_INDEX_PATH, EmbeddingRetriever
from evidence_agent.hybrid_retrieval import HybridRetriever
from evidence_agent.prompt import PROMPT_VERSION, SYSTEM_PROMPT
from evidence_agent.retrieval import DEFAULT_SOURCE_DIR, EvidenceRetriever
from evidence_agent.rubric import DEFAULT_RUBRIC


DEFAULT_SOURCE_RUN = Path("evaluation/evidence_agent_runs/20260830T053131Z")


def _load_fixed_briefs(source_run: Path) -> list[dict[str, object]]:
    rows = [
        json.loads(line)
        for line in (source_run / "outputs.jsonl").read_text(encoding="utf-8").splitlines()
        if line
    ]
    return [{"case_id": row["case_id"], "brief": row["brief_before_evidence"]} for row in rows]


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Repeat Evidence Agent with fixed Nutrition briefs.")
    parser.add_argument("--source-run", type=Path, default=DEFAULT_SOURCE_RUN)
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-5-mini"))
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--embedding-index", type=Path, default=DEFAULT_INDEX_PATH)
    parser.add_argument("--output-root", type=Path, default=Path("evaluation/evidence_fixed_runs"))
    parser.add_argument("--rubric", type=Path, default=DEFAULT_RUBRIC)
    args = parser.parse_args(argv)

    fixed = _load_fixed_briefs(args.source_run)
    deterministic = EvidenceRetriever(args.source_dir)
    embeddings = EmbeddingRetriever.load(args.embedding_index, source_dir=args.source_dir)
    agent = OpenAIEvidenceAgent(args.model, HybridRetriever(deterministic, embeddings))
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    rows: list[dict[str, object]] = []
    failures: list[dict[str, str]] = []

    for item in fixed:
        case_id = str(item["case_id"])
        try:
            brief = BaselineBrief.model_validate(item["brief"])
            result = agent.generate(brief)
            rows.append({
                "case_id": case_id,
                "brief_before_evidence": brief.model_dump(mode="json"),
                "brief": result.brief.model_dump(mode="json"),
                "evidence_agent": {
                    "trajectory": [entry.model_dump(mode="json") for entry in result.evidence.trajectory],
                    "draft": result.draft.model_dump(mode="json") if result.draft else None,
                    "assessments": [entry.model_dump(mode="json") for entry in result.evidence.assessments],
                    "gate_report": result.evidence.gate_report.model_dump(mode="json"),
                    "response_id": result.response_id,
                    "embedding_input_tokens": result.embedding_input_tokens,
                    "model_input_tokens": result.model_input_tokens,
                    "model_output_tokens": result.model_output_tokens,
                    "reasoning_tokens": result.reasoning_tokens,
                    "visible_output_tokens": result.visible_output_tokens,
                    "latency_ms": result.latency_ms,
                },
            })
            print(f"Completed {case_id}", flush=True)
        except Exception as exc:
            failures.append({"case_id": case_id, "error": f"{type(exc).__name__}: {exc}"})
            print(f"Failed {case_id}: {type(exc).__name__}", flush=True)

    manifest = {
        "run_id": run_id,
        "created_at": datetime.now(UTC).isoformat(),
        "mode": "fixed_nutrition_briefs",
        "source_run": str(args.source_run),
        "source_outputs_sha256": sha256(args.source_run / "outputs.jsonl"),
        "model": args.model,
        "prompt_version": PROMPT_VERSION,
        "prompt_sha256": hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest(),
        "source_registry_sha256": sha256(args.source_dir / "source_registry.json"),
        "embedding_index_sha256": sha256(args.embedding_index),
        "rubric": str(args.rubric),
        "rubric_sha256": sha256(args.rubric),
        "case_ids": [item["case_id"] for item in fixed],
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "outputs.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
    )
    (run_dir / "failures.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in failures), encoding="utf-8"
    )
    print(f"Fixed Evidence run written to {run_dir}: {len(rows)} succeeded, {len(failures)} failed")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
