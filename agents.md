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
Follow the standardized procedure defined in the project's root `README.md` and the specific issue documents.

### 3.1. Phase: Start
- Initialize the issue workspace (typically containing requirements, design, and task checklists) as defined in the project's directory structure.
- Use available CLI tools (e.g., `gh issue view`) to seed the documentation.

### 3.2. Phase: Implementation (Task)
- Adhere strictly to the `tasks.md` (or equivalent) in the issue workspace.
- Record daily progress in the designated development log directory (e.g., `development_logs/`).

### 3.3. Phase: Review & Completion
- Perform self-review against acceptance criteria.
- Follow the project's integration workflow (e.g., Pull Requests) and perform cleanup.

## 4. Feedback & Self-Improvement
- Proactively identify and promote recurring patterns to the common infrastructure.
- Suggest improvements to operational templates to streamline project management.
