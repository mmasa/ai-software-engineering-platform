# AI Software Engineering Platform (ASEP)

An AI-native, human-governed platform for generating, upgrading, converting,
assessing, and governing software engineering projects.

> ASEP is **not** a trading system. The Adaptive Trading Platform is the first
> project ASEP is intended to *generate* — see `examples/`.

## Principles

- **English is canonical.** Logic and identifiers are English; other languages
  are generated artifacts.
- **Schemas are the source of truth.** Canonical models live in `core/schemas/`.
- **Manifest- and profile-driven.** Behavior is configured by data, not code.
- **Evidence-based and human-governed.** Change flows through pull requests.
- **Safe by default.** No secrets, no implicit destructive or external actions.

## Layout

| Path | Purpose |
| --- | --- |
| `core/` | Canonical models (schemas) and instances — the source of truth |
| `profiles/` | Reusable policy bundles |
| `engines/` | Engine boundary manifests (boundary-only in Phase 1) |
| `templates/` `harness/` `cli/` | Capability boundaries (boundary-only) |
| `locales/` `glossary/` | Localization (generated) and canonical terms |
| `docs/` | Constitution, governance, security, architecture, ADRs |
| `examples/` | Schema-validated example projects |
| `tests/` | Schema-validation harness |

## Getting started

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[test]"
.venv/bin/python -m pytest
```

## Learn more

- [CLAUDE.md](CLAUDE.md) — operating rules for AI and human contributors
- [Architecture overview](docs/architecture/overview.md)
- [Architecture Decision Records](docs/architecture/adr/README.md)
- [Constitution](docs/constitution/CONSTITUTION.md) ·
  [Governance](docs/governance/GOVERNANCE.md) ·
  [Security](docs/security/SECURITY.md)

## Status

**Phase 1 — architectural foundation.** Boundaries, schemas, and governance
only; engine business logic is intentionally not implemented.
