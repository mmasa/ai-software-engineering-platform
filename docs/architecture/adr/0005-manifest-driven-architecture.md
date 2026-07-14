# ADR 0005 — Manifest-Driven Architecture

- **Status:** accepted
- **Date:** 2026-07-15
- **Deciders:** Chief Software Architect, Principal Platform Engineer

## Context
The platform must operate over arbitrary projects and languages without
hard-coding project specifics into engine logic. Behavior should be described by
data, not by branching code, so it can be generated, diffed, and audited.

## Decision
We will make the platform **manifest-driven**. A `ProjectManifest` is the
single source of truth for a managed project; engine boundaries are described by
`EngineManifest`s. Engines consume and produce the canonical models declared in
their manifest `contract`. Adding capability means adding data (manifests,
profiles) and, where necessary, an engine that honors a declared contract.

## Consequences
- Project behavior is inspectable and reviewable as data.
- Engines stay generic; project specifics live in manifests.
- Contracts make coupling explicit and testable.
- Requires disciplined `apiVersion` evolution of manifest schemas.

## Alternatives considered
- *Configuration embedded in code:* rejected — not portable, not auditable,
  couples engines to specific projects.
