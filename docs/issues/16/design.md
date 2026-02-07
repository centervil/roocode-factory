# Design: Operational Protocols in README.md

## New Section: Operational Protocols
A new section "4. Operational Protocols" will be added to `README.md`. This section will serve as the bridge between the abstract `agents.md` and the concrete project structure.

### 4.1. Source of Truth
- Specify GitHub Issues as the authoritative source for tasking and status.
- Instruct agents to use `skill-issue-manager` (or `gh` commands as a fallback) to synchronize state.

### 4.2. Concrete Mapping (The "Map")
A table to translate abstract concepts from `agents.md` into concrete paths.

| Abstract Concept (from agents.md) | Concrete Path / Entity |
| :--- | :--- |
| **Common Infrastructure** | `.gemini/` (Gemini CLI), `.roo/` (Roo Code) |
| **Project Operations** | `.ops/` |
| **Issue Workspace** | `docs/issues/[ID]/` |
| **Development Log** | `development_logs/` |
| **Common Skills** | `.gemini/skills/`, `.roo/skills/` |

### 4.3. Authorized Tooling
- **Issue/Tasking**: `gh` (GitHub CLI)
- **State Tracking**: `skill-state-manager`
- **Audit/Metrics**: `skill-metrics-manager`
