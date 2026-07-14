# ADR 0003 — Repository Layout

- **Status:** accepted
- **Date:** 2026-07-15
- **Deciders:** Chief Software Architect

## Context
A platform maintained for many years needs a predictable topology that separates
concerns cleanly and admits future engines, profiles, and languages without
reorganization.

## Decision
We will adopt a domain-oriented top-level layout:

```
core/       Canonical models (schemas) and canonical instances
profiles/   Profile definitions (data)
templates/  Generation templates (boundary in Phase 1)
engines/    Engine boundary manifests (generate/convert/upgrade/assess/integrate)
locales/    Generated localization bundles
glossary/   Canonical glossary (English source of truth)
harness/    AI harness boundary
cli/        CLI boundary and command surface
tests/      Schema-validation harness
docs/       Constitution, governance, security, architecture, ADRs
examples/   Schema-validated example projects (incl. Adaptive Trading Platform)
.github/    CI and change templates
```

Each area is loosely coupled; cross-area interaction happens through canonical
models, not direct imports.

## Consequences
- Newcomers can locate concerns by name.
- New engines/profiles/locales are additive, not disruptive.
- The boundary between "source of truth" (`core/`) and "generated"
  (`locales/`, generated docs) is explicit.

## Alternatives considered
- *Layered layout (models/services/ui):* rejected — hides the domain and
  couples poorly to a plugin/engine model.
- *Single flat package:* rejected — does not scale to many engines/languages.
