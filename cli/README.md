# cli/

The CLI is the primary human/AI entry point to the platform. In **Phase 1 this
is a boundary only** — the command surface is specified here; no implementation
exists.

## Architecture

- The CLI is a **thin dispatcher**. It parses input, resolves manifests and
  profiles, and invokes an engine through its declared contract. It holds no
  business logic of its own.
- Commands map one-to-one onto engine capabilities, keeping the surface small
  and predictable.
- All human-facing output is localizable via stable keys (ADR 0001); logic and
  exit codes never depend on localized text.
- Safe by default: commands with declared side effects require an explicit
  opt-in flag before any write, network, or PR action.

## Intended command surface (specification, not implementation)

| Command | Engine | Side effects |
| --- | --- | --- |
| `asep generate` | `ENG-GENERATOR` | writes files (opt-in) |
| `asep convert` | `ENG-CONVERTER` | reads repository |
| `asep upgrade` | `ENG-UPGRADE` | proposes PR (opt-in) |
| `asep assess` | `ENG-AUDIT` | read-only |
| `asep sync` | `ENG-GITHUB` | network, PR (opt-in) |
| `asep validate` | — | read-only (schema validation) |

The concrete CLI framework and language are deliberately unfixed in Phase 1 to
avoid premature coupling.
