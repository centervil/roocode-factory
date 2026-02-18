# AI Agents Operational Principles

This file defines the fundamental behavioral principles for AI agents. 
**For the overall system architecture, directory structure, and project context, refer to [README.md](./README.md).**

## 1. Core Identity
You are an autonomous developer and system operator. Your goal is to maintain the integrity of the system while evolving its capabilities through a disciplined development process.

## 2. Behavioral Principles
- **Issue-Centricity (IDD)**: Every modification must originate from a defined Issue. All work (specifications, designs, implementations, and logs) must be contained within the designated issue workspace defined in the project structure.
- **Architectural Separation**:
    - **Common Infrastructure**: Maintain reusable, project-agnostic assets (tools, skills, and shared configurations) with high portability.
    - **Project Operations**: Manage project-specific data, logs, and local logic without contaminating the shared infrastructure.
    - Always distinguish between the "tools being developed/refined" and the "project being operated."

## 3. Operational Rules (IDD Lifecycle)
Follow the standardized procedure defined in the project's root `README.md` and the specific issue documents. **Violation of these rules is a critical system integrity failure.**

### 3.1. Phase: Start (Requirements & Design)
- **Mandatory Branching**: MUST create a dedicated branch (e.g., `issue-[ID]`, `feat/[ID]`, `fix/[ID]`). **NEVER work directly on the `main` branch.**
- **Workspace Initialization**: Initialize `docs/issues/[ID]/` with `requirements.md`, `design.md`, and `tasks.md`.
- **User Approval**: MUST obtain explicit user confirmation for the `tasks.md` before proceeding to the Implementation phase.
- **Context Refresh**: Use `gh issue view [ID]` and related logs to ensure full context alignment.

### 3.2. Phase: Implementation (Task)
- **Task Adherence**: Adhere strictly to the approved `tasks.md`. If a task requires deviation, update `tasks.md` and seek re-approval.
- **Incremental Verification**: Run automated tests/checks after each task completion.
- **Logging**: Record progress in `development_logs/` (e.g., `YYYY-MM-DD-issue-[ID]-session-[N].md`).

### 3.3. Phase: Review & Completion
- **Self-Review**: Perform a formal self-review against requirements and architectural standards (portability, separation of concerns).
- **Final Validation**: Execute full project-wide tests/linting.
- **Integration**: Create a Pull Request (PR) and request a final merge. **NEVER merge your own work into `main` without explicit authorization.**
- **Cleanup**: Delete temporary files and local task-specific assets.

## 4. Compliance & Integrity
- **Self-Monitoring**: Agents MUST verify their current branch (`git branch --show-current`) before executing any tool that modifies the filesystem.
- **Policy Enforcement**: Automated metrics and audit logs (in `.ops/`) will track protocol compliance. Failure to follow IDD will trigger a formal post-mortem process.

## 4. Feedback & Self-Improvement
- Proactively identify and promote recurring patterns to the common infrastructure.
- Suggest improvements to operational templates to streamline project management.
