# Requirements: Issue #12 - Unify and Standardize Skill Management

## Context
Currently, skills are duplicated or split between `.gemini/skills/` and `.roo/skills/`. This makes it difficult to maintain shared logic (like state management or metrics) across both tools.

## Goals
- Establish a single source of truth for shared skills.
- Allow tool-specific skills to exist where necessary (e.g., UI-specific commands for Roo, or CLI-specific ones for Gemini).
- Standardize the `SKILL.md` format so it's compatible with both tools.
- Ensure easy discoverability and activation for both tools.

## Acceptance Criteria
- [ ] A unified directory structure for shared skills is established.
- [ ] Existing core skills (State Management, Metrics, Issue Manager) are moved to the shared structure.
- [ ] Both Gemini CLI and Roo Code can access these shared skills.
- [ ] Standardization documentation (template) is updated.
- [ ] No regression in skill functionality for either tool.
