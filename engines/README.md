# engines/

Engines are the platform's units of capability. In **Phase 1 they are
boundaries only** — each engine is declared by an `EngineManifest`
(`core/schemas/engine-manifest.schema.json`) with `status: boundary-only`. No
engine contains business logic yet.

| Engine | ID | Capability |
| --- | --- | --- |
| Generator | `ENG-GENERATOR` | generate a new project |
| Converter | `ENG-CONVERTER` | convert a legacy repository |
| Upgrade | `ENG-UPGRADE` | upgrade a managed repository |
| Audit | `ENG-AUDIT` | assess quality / gap analysis (read-only) |
| GitHub | `ENG-GITHUB` | project tasks & PR-based change |

## Boundary rules

- An engine interacts with the world **only** through the `inputs`/`outputs`
  declared in its manifest `contract` — all of which are canonical models.
- Engines **must not** import or call each other directly. Ordering is expressed
  by `dependsOn`, which must form a DAG.
- Every destructive or external side effect is declared in
  `contract.sideEffects` and is **off by default** (safe by default).

Adding an engine = adding a manifest that honors these rules, then (later) an
implementation behind that contract. This is the seam for future plugins.
