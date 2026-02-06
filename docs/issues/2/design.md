# Design: Implement State Management Skill

## Architecture
The state management skill will be implemented as a new skill directory in `.gemini/skills/skill-state-manager/`. It will leverage the `gh` CLI for issue metadata and file system tools to update project documentation.

## Implementation Strategy
1. **Skill Structure**:
    - `.gemini/skills/skill-state-manager/SKILL.md`: Instructions for the skill.
    - `.gemini/skills/skill-state-manager/scripts/update-state.sh`: Script to handle markdown updates.
2. **Logic Flow**:
    - Fetch current issue context.
    - Analyze `development_logs/` for the current issue.
    - Parse `.ops/project_state.md`.
    - Generate updated markdown content.
    - Apply updates to `.ops/project_state.md` and `docs/issues/[ID]/tasks.md`.

## Test Strategy
- **Unit Tests**: Verify the parsing logic for markdown files.
- **Integration Tests**: Run the skill in a controlled environment to ensure it updates mock state files correctly.
- **Manual Verification**: Run the skill against this current issue (ID: 2) to see if it updates the state.
