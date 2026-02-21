# Design Document - Issue #35: Optimize IDD workflow

## Background
The current IDD workflow has redundant task approval steps and an incomplete lifecycle, leading to manual synchronization overhead. We need to streamline the process from design to PR and automate the post-merge cleanup.

## Goals
- Eliminate redundant manual approvals during the implementation phase.
- Automate the end-to-end development cycle: Design -> Implementation -> Review -> PR creation.
- Automate post-merge synchronization (branch deletion, submodule sync, local env update).
- Refine `dev` and `requirements` commands for better IDD DX.

## Proposed Changes

### 1. `skill-issue-manager` Optimization
- **Operational Rule Update**: Once the initial design and task list are approved, the agent should proceed autonomously until the PR is created.
- **Post-Merge Logic**: Add logic to handle branch cleanup and submodule synchronization after a PR is merged.

### 2. `dev` and `requirements` Command Refinement
- **Integration**: Ensure `dev` and `requirements` work together seamlessly.
- **Automation**: Update scripts in `.gemini/skills/skill-issue-manager/scripts/` to support the new autonomous flow.

### 3. Workflow Stages
- **Start**: Requirements retrieval, branch creation, design/task generation, and **User Approval (Critical Gate)**.
- **Execute**: Implementation, Testing, Review, and PR creation (Autonomous).
- **Finalize**: User review of PR, Merge (User-triggered or semi-auto), and Post-merge cleanup (Autonomous).

## Success Criteria
- Immediate progression from approval to PR creation.
- PR stage is the only major manual review point after task approval.
- `main` branch is fully synchronized automatically upon completion.
