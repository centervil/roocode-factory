# Design for Issue #28: Protocol Hardening

## Architecture & Protocols
We will refine the IDD lifecycle defined in `AGENTS.md` by introducing "Hard Gates" between phases.

### 1. Hardened IDD Lifecycle
- **Phase: Start**:
    - MUST create a branch named `issue-[ID]`.
    - MUST create `requirements.md`, `design.md`, and `tasks.md`.
    - MUST obtain user confirmation for the `tasks.md` before moving to the next phase.
- **Phase: Implementation**:
    - MUST record progress in `development_logs/`.
    - MUST run verification tests for every task.
- **Phase: Review & Completion**:
    - MUST verify branch name before final commit.
    - MUST create a PR for integration.

### 2. Post-mortem Documentation
A dedicated file `docs/issues/28/post_mortem.md` will analyze the root causes of the Issue #23 violation, focusing on:
- Over-reliance on autonomous execution.
- Misinterpretation of UI feedback (thinking the user was silent/approving).
- Lack of "Refensive Programming" (failing to check the current branch).

### 3. Policy Updates
- Update `.ops/policies/quality.yaml` to include:
    - `protocol_compliance`: 0-1 score based on adherence to the IDD lifecycle.
