# Requirements: Issue #6 - Dogfooding: Refactor a Skill

## Context
As part of Phase 3 (Validation), we need to verify the IDD workflow by refactoring an existing skill. The `State Management Skill` is a prime candidate for improvement as its current implementation is a Proof of Concept with hardcoded logic.

## Goals
1. **Workflow Validation**: Successfully execute the full IDD cycle (Start, Task, Review, End).
2. **Skill Refinement**: Refactor `skill-state-manager` to move beyond PoC and support dynamic updates.

## Acceptance Criteria
- [ ] `update-state.sh` can dynamically identify the issue entry in `.ops/project_state.md` based on Issue ID.
- [ ] `update-state.sh` can update task completion status in `docs/issues/[ID]/tasks.md` reliably.
- [ ] The refactored skill is used to update the status of this Issue (#6) in `project_state.md`.
- [ ] All code adheres to the project's architectural separation (Common Infra vs. Project Ops).

## Target Skill
- **Path**: `.gemini/skills/skill-state-manager/`
- **Main Script**: `scripts/update-state.sh`
