from __future__ import annotations

import re

from baseline.schemas import PatientIntake


REF_PATTERN = re.compile(r"^([a-z_]+)(?:\[(\d+)\])?$")


def resolve_source_ref(patient: PatientIntake, source_ref: str) -> tuple[str, str] | None:
    match = REF_PATTERN.fullmatch(source_ref)
    if not match or match.group(1) not in PatientIntake.model_fields:
        return None
    field, index_text = match.groups()
    value = getattr(patient, field)
    if index_text is not None:
        if not isinstance(value, list) or int(index_text) >= len(value):
            return None
        return field, str(value[int(index_text)])
    if value is None or value == "" or value == []:
        return None
    if isinstance(value, list):
        return None
    return field, str(value)


def resolve_refs(patient: PatientIntake, refs: list[str]) -> tuple[list[str], list[str]] | None:
    resolved = [resolve_source_ref(patient, ref) for ref in refs]
    if not refs or any(item is None for item in resolved):
        return None
    pairs = [item for item in resolved if item is not None]
    return list(dict.fromkeys(field for field, _ in pairs)), [fact for _, fact in pairs]

