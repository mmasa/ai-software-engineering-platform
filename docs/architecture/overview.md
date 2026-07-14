# ASEP Architecture Overview

This document is the map. It explains how the pieces fit; the authoritative
detail lives in the schemas (`core/schemas/`) and the ADRs (`adr/`).

## Layers

```
                    ┌─────────────────────────────────────────┐
   Humans / AI ───▶ │                  CLI                     │  cli/
                    └───────────────────┬─────────────────────┘
                                        │ invokes
                    ┌───────────────────▼─────────────────────┐
                    │                Engines                    │  engines/
                    │  generate · convert · upgrade · assess ·  │  (boundary-only
                    │            integrate                      │   in Phase 1)
                    └───────────────────┬─────────────────────┘
                        reads / writes  │  canonical models only
                    ┌───────────────────▼─────────────────────┐
                    │            Core canonical models          │  core/schemas/
                    │  Manifest · Profile · Control · Evidence · │
                    │  Risk · Requirement · Task · Localization  │
                    └───────────────────────────────────────────┘
             cross-cutting: Profiles · Templates · Locales · Glossary · Harness
```

## Key relationships

- A **ProjectManifest** references **Profiles**; profiles bundle **Controls** and
  **Requirements**.
- **Requirements** are satisfied by **Controls**; **Controls** are demonstrated
  by **Evidence** and mitigate **Risks**.
- **Tasks** implement requirements/controls and become GitHub Projects items via
  the integration engine.
- **Engines** never import each other; they exchange canonical models declared
  in their **EngineManifest** `contract`, and their dependencies form a DAG.

## Coupling rules

- Depend on **canonical models**, not on other engines' internals.
- Depend on the **resolved profile**, not on project-specific code.
- Localized text and generated docs are **downstream** of canonical models and
  never inputs to logic.

## Extensibility

New capability is added by (1) adding/extending a schema, (2) adding a profile
or manifest, and (3) — when logic is needed — adding an engine that honors a
declared contract. This keeps the platform open for extension and closed for
disruptive modification, and is the basis for future plugin support.
