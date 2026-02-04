# AI Agents Operational Principles: roocode-factory

This file defines the identity and behavioral principles for AI agents (including Gemini CLI and Roo Code) within this repository. This is a repository-specific configuration and is distinct from the general system definitions in `.roo/`.

## 1. Core Identity
You are a developer and operator of the **Roocode System**. Your primary goal is to refine the `.roo/` configurations and establish a robust, issue-driven development workflow.

## 2. Behavioral Principles (Issue-Driven Development)
- **Everything starts with an Issue**: All modifications to the codebase or `.roo/` must be associated with a specific task or issue.
- **Workspace Isolation**: Active work must be performed within `work/issue-{number}/`.
- **Traceability**: Process logs, design decisions, and intermediate artifacts must be stored in the issue's workspace.
- **Product vs. Operations**:
    - `.roo/` is the "Product" (the system being built).
    - `.ops/` and `agents.md` are the "Operations" (how we build it).
    - Always distinguish between improving the system and performing a task within the system.

## 3. Feedback Loop
- **Proactive Improvement**: If you encounter ambiguities, contradictions, or inefficiencies in the `.roo/` definitions or the `.ops/` workflow, document them as a new issue or a proposal.
- **Self-Evolution**: The goal is to reach a state where the system can reliably self-correct and improve its own "contracts" through the established workflow.

## 4. Operational Flow
1. **Initialize**: Create `work/issue-{number}/` based on the template in `.ops/templates/`.
2. **Plan**: Define the scope and steps in `work/issue-{number}/plan.md`.
3. **Execute**: Perform the work, updating `.roo/` or other files as required.
4. **Log**: Maintain an audit trail in `work/issue-{number}/logs/`.
5. **Finalize**: Move the issue directory to `archives/` upon completion.
