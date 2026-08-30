from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv

from baseline.runner import load_dataset, sha256
from evidence_agent.agent import OpenAIEvidenceAgent
from evidence_agent.embedding_retrieval import DEFAULT_INDEX_PATH, EmbeddingRetriever
from evidence_agent.hybrid_retrieval import HybridRetriever
from evidence_agent.prompt import PROMPT_VERSION, SYSTEM_PROMPT
from evidence_agent.retrieval import DEFAULT_SOURCE_DIR, EvidenceRetriever
from nutrition_agent.client import OpenAINutritionAgent


DEFAULT_DATASET = Path("data/cases/development/nutrition_cases_dev.json")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Nutrition Agent followed by Evidence Agent.")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--case-id", action="append")
    parser.add_argument("--nutrition-model", default=os.getenv("OPENAI_MODEL", "gpt-5-mini"))
    parser.add_argument("--evidence-model", default=os.getenv("OPENAI_MODEL", "gpt-5-mini"))
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--embedding-index", type=Path, default=DEFAULT_INDEX_PATH)
    parser.add_argument("--output-root", type=Path, default=Path("evaluation/evidence_agent_runs"))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = parse_args(argv)
    dataset = load_dataset(args.dataset)
    selected = [case for case in dataset.cases if not args.case_id or case.case_id in args.case_id]
    if args.case_id and len(selected) != len(set(args.case_id)):
        available = {case.case_id for case in dataset.cases}
        raise SystemExit(f"Unknown case IDs: {', '.join(sorted(set(args.case_id) - available))}")
    if args.dry_run:
        EvidenceRetriever(args.source_dir)
        EmbeddingRetriever.load(args.embedding_index, source_dir=args.source_dir, client=object())
        print(f"Validated {len(selected)} cases, approved sources, and embedding index.")
        return 0

    deterministic = EvidenceRetriever(args.source_dir)
    embeddings = EmbeddingRetriever.load(args.embedding_index, source_dir=args.source_dir)
    hybrid = HybridRetriever(deterministic, embeddings)
    nutrition_agent = OpenAINutritionAgent(args.nutrition_model)
    evidence_agent = OpenAIEvidenceAgent(args.evidence_model, hybrid)
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    rows: list[dict[str, object]] = []
    failures: list[dict[str, str]] = []

    for case in selected:
        try:
            nutrition = nutrition_agent.generate(case.patient_intake)
            evidence = evidence_agent.generate(nutrition.brief)
            rows.append({
                "case_id": case.case_id,
                "brief_before_evidence": nutrition.brief.model_dump(mode="json"),
                "brief": evidence.brief.model_dump(mode="json"),
                "nutrition_agent": {
                    "response_ids": nutrition.response_ids,
                    "input_tokens": nutrition.input_tokens,
                    "output_tokens": nutrition.output_tokens,
                    "reasoning_tokens": nutrition.reasoning_tokens,
                    "visible_output_tokens": nutrition.visible_output_tokens,
                    "latency_ms": nutrition.latency_ms,
                },
                "evidence_agent": {
                    "trajectory": [item.model_dump(mode="json") for item in evidence.evidence.trajectory],
                    "draft": evidence.draft.model_dump(mode="json") if evidence.draft else None,
                    "assessments": [
                        item.model_dump(mode="json") for item in evidence.evidence.assessments
                    ],
                    "gate_report": evidence.evidence.gate_report.model_dump(mode="json"),
                    "response_id": evidence.response_id,
                    "embedding_input_tokens": evidence.embedding_input_tokens,
                    "model_input_tokens": evidence.model_input_tokens,
                    "model_output_tokens": evidence.model_output_tokens,
                    "reasoning_tokens": evidence.reasoning_tokens,
                    "visible_output_tokens": evidence.visible_output_tokens,
                    "latency_ms": evidence.latency_ms,
                },
            })
            print(f"Completed {case.case_id}", flush=True)
        except Exception as exc:
            failures.append({"case_id": case.case_id, "error": f"{type(exc).__name__}: {exc}"})
            print(f"Failed {case.case_id}: {type(exc).__name__}", flush=True)

    manifest = {
        "run_id": run_id,
        "created_at": datetime.now(UTC).isoformat(),
        "nutrition_model": args.nutrition_model,
        "evidence_model": args.evidence_model,
        "evidence_prompt_version": PROMPT_VERSION,
        "evidence_prompt_sha256": hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest(),
        "dataset": str(args.dataset),
        "dataset_sha256": sha256(args.dataset),
        "source_registry_sha256": sha256(args.source_dir / "source_registry.json"),
        "embedding_index": str(args.embedding_index),
        "embedding_index_sha256": sha256(args.embedding_index),
        "selected_cases": [case.case_id for case in selected],
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "outputs.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
    )
    (run_dir / "failures.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in failures), encoding="utf-8"
    )
    print(f"Evidence Agent run written to {run_dir}: {len(rows)} succeeded, {len(failures)} failed")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
