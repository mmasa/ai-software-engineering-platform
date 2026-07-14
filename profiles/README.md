# profiles/

Profiles are reusable, composable bundles of policy — controls, requirements,
default locales, and opaque engine settings — that drive platform behavior
(ADR 0006). Each profile validates against `core/schemas/profile.schema.json`.

## Layout

One directory per profile, containing `profile.yaml`.

- `iso27001-baseline/` — `PRF-ISO27001-BASELINE`, the shared baseline.
- `secure-backend/` — `PRF-SECURE-BACKEND`, extends the baseline.

## Composition and resolution

- A profile may `extends` exactly one parent (single inheritance).
- A `ProjectManifest` lists profiles in **precedence order**; later profiles
  override earlier ones.
- Resolution order for a value: project manifest ▶ last profile … ▶ first
  profile ▶ parent profiles (child over parent).

Engines consume the **resolved** profile set, never a specific profile file.
