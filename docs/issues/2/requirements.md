# Requirements: Implement State Management Skill

## User Story
As a project contributor, I want an automated way to update project state and task lists, so that the manual overhead of progress tracking is minimized and project transparency is maintained.

## Acceptance Criteria
- [ ] A new Gemini CLI skill is created specifically for state management.
- [ ] The skill can read the status of the current issue (title, body, and labels).
- [ ] The skill can summarize development progress based on recent changes or logs.
- [ ] The skill can automatically update `.ops/project_state.md`.
- [ ] The skill can update `docs/issues/[ID]/tasks.md` with progress status.
- [ ] The implementation follows the existing skill structure in `.gemini/skills/`.
