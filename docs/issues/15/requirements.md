# Requirements: Refactor agents.md for absolute project-agnosticism

## Context
To achieve the goal of a portable 'AI Constitution', `agents.md` must not contain project-specific folder names or idiosyncratic definitions.

## Goal
- Remove references to specific directories like `.gemini`, `.roo`, or `.ops` from `agents.md`.
- Replace them with abstract behavioral mandates (e.g., 'Respect the structural definitions provided in README.md', 'Maintain separation between shared infrastructure and project-specific operations').

## Acceptance Criteria
- [ ] `agents.md` contains zero references to `.gemini`, `.roo`, or `.ops`.
- [ ] `agents.md` uses abstract terms like "Common Infrastructure" and "Project-Specific Operations".
- [ ] `agents.md` remains effective and provides clear guidance for AI agents regardless of the specific folder naming convention.
