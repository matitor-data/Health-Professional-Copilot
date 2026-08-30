from __future__ import annotations

from typing import Literal

from pydantic import Field

from baseline.schemas import StrictModel


class SourceRecord(StrictModel):
    source_id: str
    file: str
    status: Literal["approved", "blocked", "pending"]
    source_type: Literal["synthetic"]
    topics: list[str] = Field(default_factory=list)
    aliases: list[str] = Field(default_factory=list)


class EvidenceChunk(StrictModel):
    chunk_id: str
    source_id: str
    title: str
    section: str
    text: str
    topics: list[str] = Field(default_factory=list)
    aliases: list[str] = Field(default_factory=list)
    content_sha256: str


class RetrievalResult(StrictModel):
    chunk_id: str
    source_id: str
    title: str
    section: str
    text: str
    score: float = Field(ge=0)
    matched_terms: list[str] = Field(default_factory=list)
    retrieval_methods: list[Literal["deterministic", "embedding"]] = Field(default_factory=list)
    content_sha256: str
