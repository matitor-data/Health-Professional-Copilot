from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

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

    def test_chunk_hash_matches_content(self) -> None:
        import hashlib

        for chunk in self.retriever.chunks:
            self.assertEqual(
                chunk.content_sha256,
                hashlib.sha256(chunk.text.encode("utf-8")).hexdigest(),
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


if __name__ == "__main__":
    unittest.main()
