# Design: Integrate Requirement Deep-Dive into GitHub Issue Manager

## Architectural Concept
The goal is to merge the expert knowledge of `skill-requirement-expert` into the standard workflow of `skill-issue-manager`. This makes the "Requirement Definition" phase an integral part of the "Phase: Start" of the IDD lifecycle.

## Changes

### 1. `.gemini/skills/skill-issue-manager/SKILL.md`
- **New Section**: Add `0. Requirement Deep-Dive` under `A. 開発開始 (Phase: Start)`.
- **Integration Logic**: 
    - Instruct the agent to fetch the issue details.
    - Instruct the agent to analyze the four pillars (Background, Scenarios, Requirements, Definition of Done).
    - Instruct the agent to perform an iterative interview (one question at a time).
    - **Skip Clause**: Explicitly state that the agent MUST ask the user if they want to skip this process if the context seems sufficient.
- **Workflow Update**: The output of this stage should update the GitHub Issue itself and be reflected in the local `requirements.md`.

### 2. Relationship with `skill-requirement-expert`
- `skill-requirement-expert` will remain as a specialized tool for more complex requirement gathering tasks or when a user wants to start *before* an issue is even created (though `skill-issue-manager` could handle that too).
- We will update `skill-requirement-expert`'s `SKILL.md` to mention it is also integrated into the standard `dev` flow.

### 3. Verification Plan
- Simulate a `Phase: Start` flow.
- Verify that the agent proposes to deepen requirements.
- Verify that it provides a skip option.
- Verify that it proceeds to create/update `requirements.md`.
