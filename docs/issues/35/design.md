# Design: Optimize IDD workflow for increased autonomy and lifecycle completion

## Overview
Improve the efficiency and completeness of the Issue-Driven Development (IDD) workflow by reducing redundant human-in-the-loop steps and extending the lifecycle beyond PR creation to include merging and environment synchronization.

## Architecture
- **Skill Update**: Modify `skill-issue-manager` in `.gemini/skills/` and `.roo/skills/`.
- **Workflow Flow**:
  1.  **Start**: Requirement definition (via `skill-requirement-expert` or detailed Issue Body).
  2.  **Autonomous Task (NEW)**: Generate `design.md` and `tasks.md`, then immediately proceed to `Task` phase without waiting for approval IF requirements are clear.
  3.  **Autonomous Task -> Review -> End**: Execute implementation, self-review, and create a Pull Request without stopping.
  4.  **Human Review (Wait)**: User reviews the PR content and approves merging.
  5.  **Autonomous Conclusion (NEW)**: After PR approval, the agent:
      -   Merges the PR and deletes the branch.
      -   Pushes submodule changes (if any).
      -   Updates the local `main` branch (git pull, submodule update).

## Implementation Details

### 1. `skill-issue-manager/SKILL.md` (Common Skill)
- **Phase A (Start)**: Update to allow skipping `tasks.md` approval if requirements are established.
- **Phase B/C/D**: Clarify that these phases should be executed autonomously once `Task` begins.
- **Phase D (End)**: Redefine to include PR creation, followed by a "Wait for PR Approval" gate.
- **Phase E (Merge/Sync)**: Add a new phase for autonomous merging and environment synchronization.

### 2. Submodule Synchronization
- Ensure that if submodules are modified, they are pushed before merging the parent PR (or as part of the merging process if the parent PR includes the submodule update).
- Standardize the `git push` command for submodules.

### 3. Session Termination Logic
- The session should only be considered "closed" once the local `main` branch is updated and synchronized.

## Considerations
- **Safety**: Human review of the PR remains a critical safety gate before any code is merged into `main`.
- **Flexibility**: If requirements are NOT clear, the agent should still stop at the `Start` phase and ask for clarification.
