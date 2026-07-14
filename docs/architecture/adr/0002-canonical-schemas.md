# ADR 0002 — Canonical Schemas as Source of Truth

- **Status:** accepted
- **Date:** 2026-07-15
- **Deciders:** Chief Software Architect, Principal Platform Engineer

## Context
The platform manipulates many structured concepts (manifests, controls,
evidence, profiles, risks, requirements, tasks, engine boundaries). These must
be validated, versioned, tool-agnostic, and language-independent. If the
authoritative definition lives in code, it becomes coupled to one language and
hard to reuse across engines and generated projects.

## Decision
We will define every canonical model as a **JSON Schema (Draft 2020-12)** under
`core/schemas/`. Schemas are the source of truth. Instances may be authored in
YAML or JSON. Human-facing documentation is generated from canonical models
wherever possible. A test harness validates that every schema is valid and that
every canonical document validates against its schema.

## Consequences
- Models are language-independent and reusable by any engine or generated repo.
- Validation is automatic and enforced in CI.
- Adding a model means adding a schema plus a validating example — not code.
- Schema evolution requires a versioning discipline (`apiVersion`).

## Alternatives considered
- *Code-first models (e.g. Pydantic/TypeScript types):* rejected — couples the
  source of truth to one language, contradicting language independence.
- *Prose specifications only:* rejected — not machine-validatable.
