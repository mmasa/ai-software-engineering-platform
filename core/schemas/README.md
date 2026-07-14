# core/schemas/

Canonical models as **JSON Schema (Draft 2020-12)**. These are the source of
truth (ADR 0002). Each schema has a stable `$id` under `https://asep.dev/schemas/`
used for cross-file `$ref` resolution; the identifier is a namespace, not a live
endpoint.

| Schema | Model | `kind` |
| --- | --- | --- |
| `project-manifest.schema.json` | Managed project | `ProjectManifest` |
| `profile.schema.json` | Reusable policy bundle | `Profile` |
| `control.schema.json` | Governance/security control | `Control` |
| `evidence.schema.json` | Assurance evidence | `Evidence` |
| `risk.schema.json` | Tracked risk | `Risk` |
| `requirement.schema.json` | Normative requirement | `Requirement` |
| `task.schema.json` | Unit of work | `Task` |
| `engine-manifest.schema.json` | Engine boundary contract | `EngineManifest` |
| `localization.schema.json` | Generated locale strings | `LocalizationBundle` |
| `glossary.schema.json` | Canonical terms | `Glossary` |
| `common/identifiers.schema.json` | Shared stable-ID patterns | — |

## Conventions

- `apiVersion` is `asep.dev/v1alpha1`. Breaking changes bump the version.
- `additionalProperties: false` on structural objects keeps documents honest;
  open annotation is confined to explicit `metadata`/`engineSettings` objects.
- Identifiers are referenced from `common/identifiers.schema.json`, never
  redefined per schema.

## Validation

`tests/` validates that every schema is a valid metaschema and that every
document declaring a matching `kind` conforms. Run `pytest`.
