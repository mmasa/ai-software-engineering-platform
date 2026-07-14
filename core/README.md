# core/

The heart of the platform: the **canonical models** and their canonical
instances. Everything else is downstream of `core/`.

- `schemas/` — JSON Schema definitions. **The source of truth.** (ADR 0002)
- `schemas/common/identifiers.schema.json` — stable ID patterns shared by all
  models. (Constitution, Article 4)
- `controls/`, `evidence/`, `risks/`, `requirements/` — canonical instances,
  authored in YAML, validated against the schemas by the test harness.

Rules:

- A concept is canonical only if it has a schema here.
- Instances declare a `kind` matching their schema and use stable IDs.
- No secrets, no business logic — data and definitions only.
