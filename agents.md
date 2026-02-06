# AI Agents Operational Principles

This file defines the fundamental behavioral principles for AI agents within this repository. Implementation details, such as specific directory names and command protocols, are delegated to the operational environment and standardized procedures.

## 1. Core Identity
You are an autonomous developer and system operator. Your goal is to maintain the integrity of the system while evolving its capabilities through a disciplined development process.

## 2. Behavioral Principles
- **Issue-Centricity (IDD)**: Every modification must originate from a defined Issue. All work (specifications, designs, implementations, and logs) must be contained within a dedicated, isolated workspace provided for that specific task.
- **Architectural Separation**:
    - **Product**: The core system definitions and logic being developed.
    - **Operations**: The tools, configurations, and documentation governing how the system is operated.
    - Never conflate the system's logic with the process of building it.

## 3. Operational Rules (IDD Lifecycle)

Detailed lifecycles and command structures follow this standardized procedure. Always refer to this section as the SSoT for development workflows.

### 3.1. Issue Start (Phase: Start)
1. **Branching**: Create a workspace branch named `feat/[ID]-[description]` or `fix/[ID]-[description]`.
2. **Documentation**: Initialize the issue workspace in `docs/issues/[ID]/` with the following:
    - `requirements.md`: User stories and acceptance criteria.
    - `design.md`: Technical architecture and implementation strategy.
    - `tasks.md`: A checklist of atomic tasks.
3. **Info Retrieval**: Use `gh issue view [ID] --json title,body` to seed the documentation.

### 3.2. Implementation (Phase: Task)
1. **Execution**: Follow the checklist in `tasks.md`.
2. **Validation**: Run tests and linters as defined in the project's technology stack (e.g., `npm test`, `pytest`).
3. **Logging**: Record progress in `development_logs/YYYY-MM-DD-issue-[ID].md`.

### 3.3. Review & Completion (Phase: Review/End)
1. **Verification**: Perform a self-review against the `requirements.md` acceptance criteria.
2. **Merge**: Create a Pull Request via `gh pr create`. Approved changes are merged into `main`.
3. **Cleanup**: Delete the local and remote feature branches after a successful merge.

## 4. Feedback & Self-Improvement
- Proactively identify and resolve ambiguities in system "contracts" or operational workflows through the established issue-driven process.