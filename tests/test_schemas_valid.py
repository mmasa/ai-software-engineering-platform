"""Every canonical schema must itself be a valid Draft 2020-12 JSON Schema."""

from __future__ import annotations

from pathlib import Path

import pytest
from jsonschema.validators import Draft202012Validator

from conftest import load_json


def _schema_files() -> list[Path]:
    from conftest import SCHEMA_DIR

    return sorted(SCHEMA_DIR.rglob("*.schema.json"))


@pytest.mark.parametrize("schema_path", _schema_files(), ids=lambda p: p.name)
def test_schema_is_valid_metaschema(schema_path: Path) -> None:
    schema = load_json(schema_path)
    # Raises SchemaError if the schema is not valid against the metaschema.
    Draft202012Validator.check_schema(schema)


@pytest.mark.parametrize("schema_path", _schema_files(), ids=lambda p: p.name)
def test_schema_has_id_and_title(schema_path: Path) -> None:
    schema = load_json(schema_path)
    assert schema.get("$id"), f"{schema_path.name} is missing a canonical $id"
    assert schema.get("title"), f"{schema_path.name} is missing a title"


def test_schema_ids_are_unique() -> None:
    ids = [load_json(p)["$id"] for p in _schema_files()]
    assert len(ids) == len(set(ids)), "Duplicate $id values found across schemas"
