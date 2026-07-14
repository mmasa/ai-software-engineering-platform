# CLAUDE.md — Operating Guide for AI Contributors

This file governs how AI agents (and humans) work in this repository. It is
binding. Read it before making changes.

## What this repository is

The **AI Software Engineering Platform (ASEP)** — an AI-native, human-governed
platform for generating, upgrading, converting, assessing, and governing
software engineering projects.

ASEP is **not** a trading system. The Adaptive Trading Platform is only the
first project ASEP is intended to *generate*; it lives under `examples/` as a
schema-validated illustration, not as an implementation.

## Non-negotiable principles

1. **English is the canonical semantic language.** All logic, identifiers, and
   schema keys are English. Localized text is a *generated artifact* and MUST
   NEVER drive program logic. (See `docs/architecture/adr/0001-canonical-language.md`.)
2. **Schemas are the source of truth.** Canonical models live in
   `core/schemas/` as JSON Schema. Documentation and other artifacts are
   generated *from* canonical models wherever possible — not hand-authored in
   parallel. (See ADR 0002.)
3. **Everything important has a stable identifier.** Controls, risks, tasks,
   profiles, evidence, requirements, projects, engines, and glossary terms all
   use the ID patterns in `core/schemas/common/identifiers.schema.json`.
   IDs are stable across regeneration.
4. **Manifest-driven and profile-driven.** Behavior is configured by manifests
   and profiles (data), not by branching code. (See ADRs 0005, 0006.)
5. **Safe by default.** No secrets, credentials, API keys, or production
   integrations. Destructive or external side effects must be *declared* in an
   engine manifest and are off unless explicitly enabled. (See `docs/security/`.)
6. **Change flows through pull requests.** No direct writes to protected
   branches; every change is reviewable. (See ADR 0004.)

## Architecture at a glance

| Area | Location | Status |
| --- | --- | --- |
| Canonical models (schemas) | `core/schemas/` | source of truth |
| Canonical instances | `core/controls`, `core/risks`, … | examples |
| Profiles | `profiles/` | data |
| Engines (boundaries only) | `engines/` | boundary-only |
| Localization | `locales/`, `glossary/` | generated |
| AI harness | `harness/` | boundary-only |
| CLI | `cli/` | boundary-only |
| Docs & governance | `docs/` | authored |
| Test harness | `tests/` | active |

Modules are **loosely coupled**. Engines communicate only through the canonical
models declared in their manifest `contract`. Do not create direct imports
between engines.

## Working in this repo

- **Add or change a model:** edit the schema in `core/schemas/`, then update or
  add an example, then run the tests. A model without a schema is not canonical.
- **Add an example/instance:** give it a `kind` matching a schema; the test
  harness validates it automatically.
- **Keep the README lightweight.** Do not over-document. Documentation grows
  from the canonical architecture.
- **Every file must earn its place.** No placeholder code without architectural
  value.

## Verifying your change

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[test]"
.venv/bin/python -m pytest
```

The suite validates that every schema is a valid JSON Schema and that every
canonical document validates against its schema. CI runs the same checks.

## Scope discipline

This is **Phase 1: architectural foundation**. Do not implement engine business
logic (generation, conversion, upgrade, audit, GitHub automation). Create and
respect *boundaries* only.
