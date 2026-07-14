# harness/

The AI harness is where AI-assisted development is *governed* — the boundary
between autonomous agent work and human authority. In **Phase 1 this is a
boundary only**; no orchestration code exists.

## Responsibilities (specification)

- **Task intake:** turn canonical `Task`s into agent work items.
- **Guardrails:** enforce safe-by-default and the pull-request change model
  (ADR 0004) — agents propose diffs; they never write to protected branches.
- **Evidence capture:** record what an agent did as `Evidence` linked to the
  relevant `Control`, supporting the evidence-based assurance model.
- **Auditability:** every agent action is traceable to a task and reviewable.

## Boundary rules

- The harness invokes engines through their declared contracts; it does not
  embed engine logic.
- Human governance is non-negotiable: the harness cannot merge, only propose.

Distinct from `.claude/` and `CLAUDE.md`, which configure *this* repository's
AI contributors. `harness/` concerns how ASEP governs AI work on the projects it
manages.
