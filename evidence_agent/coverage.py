from __future__ import annotations

from evidence_agent.retrieval import EvidenceRetriever, _normalize, _tokens


def collection_has_topic_signal(retriever: EvidenceRetriever, query: str) -> bool:
    """Return whether approved source metadata explicitly covers at least one query concept."""
    query_tokens = set(_tokens(query))
    normalized_query = _normalize(query)
    for record in retriever.records:
        phrases = [*record.topics, *record.aliases]
        if any(_normalize(phrase) in normalized_query for phrase in phrases if len(_tokens(phrase)) > 1):
            return True
        metadata_tokens = set(_tokens(" ".join(phrases)))
        if query_tokens & metadata_tokens:
            return True
    return False
