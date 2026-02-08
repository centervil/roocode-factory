# Tasks: Issue #17 - Relocate Policies to .ops

- [x] **Phase 1: Migration**
    - [x] Create `.ops/policies/` directory.
    - [x] Move files from `.roo/policies/` to `.ops/policies/`.
    - [x] Remove empty `.roo/policies/` directory.
- [x] **Phase 2: Reference Updates**
    - [x] Update `.gemini/skills/skill-metrics-manager/scripts/check-gates.py`.
    - [x] Update `README.md` (Operational Protocols section).
    - [x] Update any other occurrences in the codebase.
- [x] **Phase 3: Verification**
    - [x] Run `bash .gemini/skills/skill-metrics-manager/scripts/run-audit.sh --check`.
- [x] **Phase 4: Cleanup & Completion**
    - [x] Record development log.
    - [x] Update project state.
    - [x] Close issue.
