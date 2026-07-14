# ADR 0006 — Profile-Driven Architecture

- **Status:** accepted
- **Date:** 2026-07-15
- **Deciders:** Chief Software Architect, Principal Security Architect

## Context
Different projects need different governance, security, and engineering
standards (e.g. an ISO/IEC 27001 baseline, a secure backend service, a data
product). These bundles of policy must be reusable, composable, and independent
of any single project or engine.

## Decision
We will make policy **profile-driven**. A `Profile` bundles controls,
requirements, default locales, and opaque engine settings. Profiles compose via
single inheritance (`extends`), with child values overriding parent values. A
`ProjectManifest` references profiles in precedence order; engines read the
resolved profile set to decide behavior.

## Consequences
- Standards are defined once and reused across projects.
- Composition (`extends`) enables baselines plus specializations.
- Engines depend on the *resolved* profile, not on project-specific code.
- Requires a well-defined resolution/override order (documented in
  `profiles/README.md`).

## Alternatives considered
- *Per-project bespoke configuration:* rejected — no reuse, high drift.
- *Multiple inheritance of profiles:* deferred — single inheritance keeps
  resolution deterministic and simple; revisit if real needs emerge.
