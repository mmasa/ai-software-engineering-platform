# tests/

The **schema-validation harness**. It contains no business logic; its only job
is to keep the canonical models and their examples honest.

- `test_schemas_valid.py` — every `*.schema.json` is a valid Draft 2020-12
  schema, has a unique `$id`, and has a title.
- `test_examples_validate.py` — every document in the repo that declares a
  `kind` validates against the matching schema. An unknown `kind` fails the
  suite, so typos and undocumented models are caught.
- `conftest.py` — builds an offline `referencing` registry so cross-file
  `$ref` by `$id` resolves without network access.

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[test]"
.venv/bin/python -m pytest
```

CI runs the same checks on every pull request.
