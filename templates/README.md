# templates/

Templates are the raw material the Generator (`ENG-GENERATOR`) turns into
project artifacts. In **Phase 1 this is a boundary only** — no templates ship
yet.

## Principles (specification)

- Templates are **data**, not logic. They are parameterized by canonical models
  (manifest + resolved profile), never by hard-coded project specifics.
- Human-facing text in templates is authored in the **canonical language** and
  localized downstream via stable keys (ADR 0001).
- Templates **must not** contain secrets, credentials, or live endpoints.
- A template declares which model fields it consumes so generation is
  inspectable and testable.

The template format and engine are deliberately unfixed in Phase 1.
