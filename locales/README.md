# locales/

Generated localization bundles, one subtree per locale. **These are generated
artifacts** (ADR 0001): they are produced from canonical English sources and are
**never** read by program logic — logic keys on the stable `key`, not the value.

## Layout

`locales/<locale>/*.localization.yaml`, validated against
`core/schemas/localization.schema.json`.

Planned locales: `en` (canonical source), `ja`, `vi`, `ko`, and future
languages. Adding a language is additive — a new subtree — and touches no logic.

## Drift

Each entry may carry a `sourceHash` of its English source. When the source
changes, the hash mismatches and the entry is marked `stale` for regeneration.
