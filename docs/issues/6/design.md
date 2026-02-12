# Design: Issue #6 - Dogfooding: Refactor a Skill

## Architecture Overview
The `skill-state-manager` belongs to the **Common Infrastructure** (`.gemini/`). It interacts with **Project Operations** (`.ops/`) and **Issue Workspaces** (`docs/issues/`).

## Proposed Improvements for `update-state.sh`

### 1. Dynamic Entry Identification
Instead of hardcoding "Implement State Management Skill", the script should:
- Read `docs/issues/[ID]/requirements.md` (or use `gh issue view [ID]`) to get the Issue Title.
- Search for the Issue Title or Issue ID pattern in `.ops/project_state.md`.

### 2. Robust Markdown Editing
- Use `sed` or `awk` with more specific patterns to avoid accidental replacements.
- Ensure that marking an issue as `completed` updates both the Roadmap section in `project_state.md` and the "Current Focus" section if applicable.

### 3. Task List Synchronization
- Improve the logic that marks tasks in `tasks.md`.
- Perhaps allow specific task IDs to be checked instead of "everything".

## Interface
- Input: `ISSUE_ID` (Required), `STATUS` (Optional), `TASK_ID` (Optional)
- Behavior:
    - If only `ISSUE_ID` and `STATUS` are provided: Update project state and possibly mark all tasks (if status is `completed`).
    - If `TASK_ID` is provided: Mark only that specific task in `tasks.md`.
