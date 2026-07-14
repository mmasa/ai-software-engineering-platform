# ASEP Security

Security principles for the platform and everything it generates. This is a
skeleton for Phase 1; controls grow as engines are implemented.

## Safe by default

- **No secrets.** No credentials, API keys, tokens, or passwords are stored in
  this repository — not in code, manifests, examples, or documentation.
- **No production integrations.** Phase 1 contains boundaries only. No engine
  performs live network or repository writes.
- **No destructive operations.** Any destructive or external side effect must be
  declared in an engine's manifest (`contract.sideEffects`) and is disabled
  unless explicitly enabled by a human.
- **Least authority.** Engines receive only the inputs declared in their
  contract and produce only their declared outputs.

## Handling secrets (future engines)

When engines gain real integrations, secrets MUST be supplied at runtime from a
secure secret store or environment — never committed, never logged, never
embedded in generated artifacts. This is enforced by control `CTL-AC-0001`.

## Supply chain

Dependencies are minimal and pinned by lower bound in `pyproject.toml`. CI runs
on pull requests. Secret scanning is expected in CI (see `EVD-0001`).

## Reporting

Until a formal channel exists, report suspected vulnerabilities privately to the
repository maintainers. Do not open public issues for security reports.

## Mapping to controls

Security expectations are expressed as canonical Controls under `core/controls/`
with references to ISO/IEC 27001 and NIST SSDF, and are satisfied by Evidence
under `core/evidence/`.
