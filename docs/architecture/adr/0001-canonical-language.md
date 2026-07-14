# ADR 0001 — Canonical Language

- **Status:** accepted
- **Date:** 2026-07-15
- **Deciders:** Chief Software Architect, AI Governance Architect

## Context
ASEP must support English, Japanese, Vietnamese, Korean, and future languages,
while remaining stable and maintainable for many years. Multilingual systems
that treat translated strings as semantically significant become impossible to
reason about: logic branches on localized text, and identity drifts per locale.

## Decision
We will treat **English as the single canonical semantic language**. All program
logic, schema keys, enums, and stable identifiers are English. Localized content
is a **generated artifact** keyed by stable, language-independent keys, and is
never read by program logic.

## Consequences
- Logic is deterministic and locale-independent.
- Translations can be regenerated or corrected without touching logic.
- Drift is detectable via `sourceHash` on localization entries.
- Contributors must resist the temptation to branch on localized text.

## Alternatives considered
- *Locale-neutral symbolic keys with no canonical language:* rejected — humans
  still need a readable source of truth; English serves that role.
- *Full per-locale models:* rejected — multiplies maintenance and invites
  semantic divergence between languages.
