"""Every canonical document in the repository must validate against its schema.

Documents are discovered by scanning for YAML/JSON files that declare a ``kind``.
The ``kind`` selects the schema. Any document whose ``kind`` is unknown fails the
suite, so a typo or an undocumented model is caught immediately.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

from conftest import REPO_ROOT, load_json

# Canonical `kind` -> schema `$id`.
KIND_TO_SCHEMA = {
    "ProjectManifest": "https://asep.dev/schemas/project-manifest.schema.json",
    "Profile": "https://asep.dev/schemas/profile.schema.json",
    "Control": "https://asep.dev/schemas/control.schema.json",
    "Evidence": "https://asep.dev/schemas/evidence.schema.json",
    "Risk": "https://asep.dev/schemas/risk.schema.json",
    "Requirement": "https://asep.dev/schemas/requirement.schema.json",
    "Task": "https://asep.dev/schemas/task.schema.json",
    "EngineManifest": "https://asep.dev/schemas/engine-manifest.schema.json",
    "LocalizationBundle": "https://asep.dev/schemas/localization.schema.json",
    "Glossary": "https://asep.dev/schemas/glossary.schema.json",
}

# Directories that hold documents but never canonical instances.
_EXCLUDE = {".git", ".venv", "node_modules", "core/schemas", "tests"}


def _document_paths() -> list[Path]:
    paths: list[Path] = []
    for pattern in ("*.yaml", "*.yml", "*.json"):
        for path in REPO_ROOT.rglob(pattern):
            rel = path.relative_to(REPO_ROOT).as_posix()
            if any(rel == e or rel.startswith(e + "/") for e in _EXCLUDE):
                continue
            paths.append(path)
    return sorted(paths)


def _load_doc(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    data = load_json(path) if path.suffix == ".json" else yaml.safe_load(text)
    if isinstance(data, dict) and "kind" in data:
        return data
    return None


def _discovered_kinds() -> set[str]:
    kinds = set()
    for path in _document_paths():
        doc = _load_doc(path)
        if doc is not None:
            kinds.add(doc["kind"])
    return kinds


@pytest.mark.parametrize("kind", sorted(KIND_TO_SCHEMA), ids=lambda k: k)
def test_every_canonical_kind_has_an_example(kind: str) -> None:
    """The repo's schema-plus-example rule: every schema must be exercised by at
    least one example document, so CI catches regressions in that model."""
    assert kind in _discovered_kinds(), (
        f"No example document found for kind '{kind}'. "
        f"Add a validating instance so {KIND_TO_SCHEMA[kind]} is exercised."
    )


@pytest.mark.parametrize("doc_path", _document_paths(), ids=lambda p: p.relative_to(REPO_ROOT).as_posix())
def test_document_validates_against_schema(doc_path: Path, registry) -> None:
    doc = _load_doc(doc_path)
    if doc is None:
        pytest.skip("not a canonical document (no 'kind')")

    kind = doc["kind"]
    assert kind in KIND_TO_SCHEMA, f"Unknown kind '{kind}' in {doc_path.name}"

    schema = registry.get_or_retrieve(KIND_TO_SCHEMA[kind]).value.contents
    validator = Draft202012Validator(schema, registry=registry)
    errors = sorted(validator.iter_errors(doc), key=lambda e: e.path)
    assert not errors, "\n".join(f"  - {e.message} at {list(e.path)}" for e in errors)
