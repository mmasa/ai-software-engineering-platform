# ADR 0004 — Pull Request Change Model

- **Status:** accepted
- **Date:** 2026-07-15
- **Deciders:** AI Governance Architect, Principal Platform Engineer

## Context
ASEP is AI-native but human-governed. AI agents will propose substantial change,
including to repositories the platform manages. Change must be reviewable,
auditable, and reversible, and humans must retain authority.

## Decision
We will require that **all change flows through pull requests**. No agent or
engine writes directly to a protected branch. Engines that mutate repositories
declare `creates-pull-request` in their manifest `sideEffects` and produce
proposals, never direct commits to protected branches.

## Consequences
- Every change has a review surface and an audit trail.
- Humans hold the merge decision.
- Engines are designed around *proposing* diffs, not applying them silently.
- Requires branch protection and CI as enforcement (out of scope for Phase 1
  beyond the CI skeleton).

## Alternatives considered
- *Direct commits by trusted automation:* rejected — removes human authority and
  auditability, violating the Constitution.
