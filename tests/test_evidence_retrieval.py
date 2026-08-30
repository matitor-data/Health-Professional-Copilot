from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from evidence_agent.evaluate import evaluate_retrieval
from evidence_agent.embedding_retrieval import EmbeddingRetriever, _cosine_similarity
from evidence_agent.hybrid_retrieval import HybridRetriever
from evidence_agent.retrieval import EvidenceRetriever


SOURCE_DIR = Path("data/nutrition_evidence_sources_v1")


class EvidenceRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.retriever = EvidenceRetriever(SOURCE_DIR)

    def test_loads_only_registered_approved_sources(self) -> None:
        self.assertEqual(len(self.retriever.records), 4)
        self.assertTrue(self.retriever.chunks)
        self.assertEqual(
            {chunk.source_id for chunk in self.retriever.chunks},
            {record.source_id for record in self.retriever.records},
        )

    def test_iron_query_returns_iron_source_first(self) -> None:
        results = self.retriever.search("vegetarian iron sources and vitamin C", top_k=3)
        self.assertTrue(results)
        self.assertEqual(results[0].source_id, "synthetic_iron_vegetarian_v1")
        self.assertIn("iron", results[0].matched_terms)

    def test_spanish_query_is_accent_insensitive(self) -> None:
        results = self.retriever.search("evaluación de sodio y potasio en CKD")
        self.assertTrue(results)
        self.assertEqual(results[0].source_id, "synthetic_ckd_sodium_v1")

    def test_unknown_query_can_return_empty_list(self) -> None:
        self.assertEqual(self.retriever.search("xylophone nebula zirconium"), [])

    def test_order_is_deterministic(self) -> None:
        first = self.retriever.search("nutrition assessment", top_k=10)
        second = self.retriever.search("nutrition assessment", top_k=10)
        self.assertEqual(first, second)

    def test_chunk_fingerprint_is_stable(self) -> None:
        reloaded = EvidenceRetriever(SOURCE_DIR)
        self.assertEqual(
            [chunk.content_sha256 for chunk in self.retriever.chunks],
            [chunk.content_sha256 for chunk in reloaded.chunks],
        )
        self.assertTrue(all(len(chunk.content_sha256) == 64 for chunk in reloaded.chunks))

    def test_registry_provides_bilingual_aliases(self) -> None:
        self.assertTrue(all(record.aliases for record in self.retriever.records))
        self.assertEqual(
            self.retriever.search("gaseosa con azúcar")[0].source_id,
            "synthetic_prediabetes_fiber_v1",
        )

    def test_rejects_source_path_outside_collection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = {
                "sources": [{
                    "source_id": "outside",
                    "file": "../outside.md",
                    "status": "approved",
                    "source_type": "synthetic",
                    "topics": [],
                }]
            }
            (root / "source_registry.json").write_text(json.dumps(registry), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "escapes evidence directory"):
                EvidenceRetriever(root)

    def test_fixed_benchmark_produces_bounded_metrics(self) -> None:
        report = evaluate_retrieval(self.retriever)
        self.assertEqual(report["metrics"]["query_count"], 36)
        for name in ("recall@1", "recall@3", "precision@1", "precision@3", "no_answer_accuracy"):
            self.assertGreaterEqual(report["metrics"][name], 0.0)
            self.assertLessEqual(report["metrics"][name], 1.0)

    def test_locked_benchmark_contract_and_hash(self) -> None:
        path = Path("data/evaluations/locked/evidence_retrieval_locked_v1.json")
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["status"], "locked")
        self.assertEqual(len(payload["queries"]), 48)
        self.assertEqual(len({item["query_id"] for item in payload["queries"]}), 48)
        self.assertEqual(
            hashlib.sha256(path.read_bytes()).hexdigest(),
            "49137514e595da147c9f3c11048dc63d5481bd4e8a76fbbad65b9f88ae6732c6",
        )

    def test_cosine_similarity(self) -> None:
        self.assertAlmostEqual(_cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0)
        self.assertAlmostEqual(_cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0)

    def test_embedding_retriever_rejects_incomplete_index(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not match"):
            EmbeddingRetriever(self.retriever, {}, dimensions=2, client=object())

    def test_hybrid_rejects_weak_single_term_lexical_match(self) -> None:
        class StubEmbeddings:
            def search_many(self, queries: list[str], top_k: int) -> list[list[object]]:
                return [[] for _ in queries]

        hybrid = HybridRetriever(self.retriever, StubEmbeddings())
        self.assertEqual(hybrid.search("food allergy elimination protocol"), [])
        self.assertEqual(hybrid.search("dieta sin gluten para celiaquía"), [])

    def test_hybrid_keeps_strong_lexical_fallback(self) -> None:
        class StubEmbeddings:
            def search_many(self, queries: list[str], top_k: int) -> list[list[object]]:
                return [[] for _ in queries]

        hybrid = HybridRetriever(self.retriever, StubEmbeddings())
        results = hybrid.search("packaged meals restaurant foods and renal diet")
        self.assertEqual(results[0].source_id, "synthetic_ckd_sodium_v1")
        self.assertEqual(results[0].retrieval_methods, ["deterministic"])


if __name__ == "__main__":
    unittest.main()
