# Design for Issue #24: Issue Granularity and Splitting Protocol

## 1. Documentation Strategy (README.md)
Add a section under "Operational Protocols" defining "Standard Issue Granularity".

### Splitting Criteria (Draft)
- **Layer Crossing**: If a task requires changes in both "Common Infrastructure" (.gemini, .roo) and "Project Operations" (.ops), consider splitting.
- **Complexity**: If a task involves more than 3 distinct implementation steps or is expected to exceed 3 development sessions.
- **Independency**: If a sub-feature can be tested and verified independently of the rest of the issue.

## 2. Skill Integration (skill-issue-manager)
Update the `Start` phase instructions to include a "Granularity Assessment" step.

- **Action**: Before creating `requirements.md`, the agent must analyze the issue's scope against the project's `README.md` standards.
- **Outcome**: If the scope is too broad, the agent should propose a split to the user before proceeding.
