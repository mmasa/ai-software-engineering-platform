"""Shared test fixtures for the ASEP schema validation harness.

The harness treats ``core/schemas`` as the source of truth and verifies that
(a) every schema is itself a valid JSON Schema and (b) every canonical example
document in the repository validates against the correct schema.

It performs NO business logic. Its only job is to keep the canonical models and
their examples honest.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "core" / "schemas"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def schema_dir() -> Path:
    return SCHEMA_DIR


@pytest.fixture(scope="session")
def schema_paths() -> list[Path]:
    return sorted(SCHEMA_DIR.rglob("*.schema.json"))


@pytest.fixture(scope="session")
def registry():
    """Build a referencing registry so cross-file ``$ref`` by ``$id`` resolves
    offline (no network access)."""
    from referencing import Registry, Resource

    resources = []
    for path in SCHEMA_DIR.rglob("*.schema.json"):
        schema = load_json(path)
        resources.append((schema["$id"], Resource.from_contents(schema)))
    return Registry().with_resources(resources)
