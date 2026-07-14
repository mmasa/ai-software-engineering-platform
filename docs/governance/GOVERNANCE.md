# ASEP Governance

Governance describes *how decisions are made and enforced*. It operationalizes
the [Constitution](../constitution/CONSTITUTION.md).

## Roles

Roles are responsibilities, not individuals, and never carry credentials.

| Role | Accountable for |
| --- | --- |
| Chief Software Architect | Overall architecture and ADRs |
| Principal Security Architect | Security posture and controls |
| Principal Platform Engineer | Engines, harness, CLI boundaries |
| AI Governance Architect | AI operating rules, evidence, auditability |

## Decision records

Architecturally significant decisions are captured as ADRs under
`docs/architecture/adr/`. An ADR is immutable once accepted; it is superseded
by a new ADR rather than edited.

## Change model

All change flows through pull requests (see ADR 0004). A change is mergeable
only when:

1. The schema test harness passes.
2. Any new canonical model has a schema and at least one validating example.
3. Security constraints are respected (no secrets, safe by default).
4. Architecturally significant decisions have an accompanying ADR.

## Traceability

Governance is traceable through stable identifiers:

```
Requirement (REQ) ──satisfiedBy──▶ Control (CTL) ──evidence──▶ Evidence (EVD)
        ▲                               │
        └───────── Task (TSK) ─────────┘  Control ──mitigates──▶ Risk (RSK)
```

Every link uses stable IDs so traceability survives regeneration.

## Compliance alignment

The platform aligns generated projects with ISO/IEC 27001 and NIST SSDF via
Controls that carry `frameworkReferences`. Alignment is asserted only where
Evidence exists.
