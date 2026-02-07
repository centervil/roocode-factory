# Requirements: Define Project-Specific Source of Truth and Protocols in README.md

## Context
Following the refactoring of `agents.md` to be project-agnostic (Issue #15), we must now explicitly define the concrete operational realities in `README.md`.

## Goal
Establish `README.md` as the absolute "Map" that translates abstract mandates into concrete actions for this specific project.

## Acceptance Criteria
- [ ] **Source of Truth Definition**:
    - Explicitly state that **GitHub Issues** are the single source of truth for task management.
    - Mandate that Agents must execute specific skills (e.g., `skill-issue-manager`) to sync context at the start of any session.
- [ ] **Concrete Path Mapping**:
    - Create a mapping table linking `agents.md` abstract terms to concrete paths:
        - Common Infrastructure -> `.gemini/`, `.roo/`
        - Project Operations -> `.ops/`
        - Issue Workspace -> `docs/issues/[ID]/`
        - Development Log -> `development_logs/`
- [ ] **Tool Specification**:
    - Specify that `gh` (GitHub CLI) is the authorized tool for interaction.
- [ ] **Deliverables**:
    - Updated `README.md` with a new "Operational Protocols" section.