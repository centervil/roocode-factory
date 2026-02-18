# Requirements for Issue #28: Post-mortem and Process Improvement

## Background
During the implementation of Issue #23, several violations of the established Issue-Driven Development (IDD) protocol occurred:
- Skipping the requirement deep-dive and design phases.
- Direct commits to the `main` branch.
- Ignoring the Pull Request (PR) integration flow.
- Lack of proper development logs.

These violations undermine the system's integrity and architectural separation.

## Objectives
- Formally document the failure (Post-mortem).
- Strengthen the IDD protocol in `AGENTS.md` to prevent recurrence.
- Introduce explicit checks for branch management and phase transitions.

## Scope
- Update `AGENTS.md` with stricter rules and explicit check-points.
- Create a post-mortem report for Issue #23.
- Update `quality.yaml` to include protocol compliance as a metric.

## Acceptance Criteria
- [ ] `AGENTS.md` explicitly forbids `main` branch commits for issue-related work.
- [ ] `AGENTS.md` requires a `tasks.md` to be approved by the user before the `Task` phase begins.
- [ ] A post-mortem document for Issue #23 is stored in `docs/issues/28/post_mortem.md`.
- [ ] `quality.yaml` defines a "Protocol Compliance" metric.
