# Requirement: Integrate Requirement Deep-Dive into GitHub Issue Manager (devSkill)

## Background
Currently, the requirement gathering process is a standalone skill (`skill-requirement-expert`). Users often want to start development (Phase: Start) and ensure that requirements are clear before proceeding. Integrating these two processes will streamline the IDD (Issue-Driven Development) workflow.

## User Story
As a user of the `devSkill` (invoked via `dev.toml` using `skill-issue-manager`), I want the assistant to automatically offer to refine the issue's requirements before I begin implementation. This includes:
1. Fetching the issue content.
2. Identifying missing information (background, user story, success criteria, etc.).
3. Interacting with the user to fill those gaps.
4. (Optional) Skipping this step if I already have a clear plan.

## Success Criteria
- [ ] `skill-issue-manager/SKILL.md` is updated to include a requirement-gathering phase in its "Phase: Start" workflow.
- [ ] The updated instructions explicitly mention that requirement refinement can be skipped if the user confirms it's not needed.
- [ ] `skill-issue-manager` will produce or update a `requirements.md` as a result of this phase.
- [ ] The relationship between `skill-issue-manager` and `skill-requirement-expert` is documented or clarified (e.g., whether to keep both or mark one as the primary entry point).

## Constraints
- Must remain compatible with the existing `AGENTS.md` and `README.md` structure.
- Must not break the current `dev` command functionality.
- The user must explicitly approve the final requirements before moving to the Design/Task phase.
