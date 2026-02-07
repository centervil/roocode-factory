# Requirements: Extend Skill-Architect for Constitution/Map Pattern

## Context
We have established a robust architectural pattern for AI Projects:
1.  **`agents.md`**: Abstract Behavioral Constitution (Portable).
2.  **`README.md`**: Concrete Project Map & Static Definitions (Project-Specific).
3.  **Skills**: Executable procedures and tools (Implementation).

## Goal
Enhance the existing `skill-architect` (or create a specialized sub-skill) to automatically generate, validate, and maintain this three-tier structure for any project.

## Acceptance Criteria
- [ ] **Scaffolding**: The skill can generate a matched pair of `agents.md` (Generic) and `README.md` (Specific) based on a project template or intent.
- [ ] **Validation**: The skill can verify that `README.md` contains all concrete definitions (Issue Tracker, Paths, Tools) referenced by the abstract `agents.md`.
- [ ] **Maintenance**: The skill provides commands to update the "Map" (`README.md`) when structure changes, without affecting the "Constitution" (`agents.md`).
- [ ] **Integration**: The enhanced functionality is integrated into the `skill-architect` workspace.