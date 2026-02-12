# Tasks: Issue #12 - Unify and Standardize Skill Management

## Phase 1: Start (Preparation)
- [x] Create issue workspace `docs/issues/12/` <!-- id: 0 -->
- [x] Define requirements and design <!-- id: 1 -->

## Phase 2: Task (Implementation)
- [x] List all current skills in `.gemini/skills/` and `.roo/skills/` <!-- id: 2 -->
- [x] Merge `.roo/skills/` into `.gemini/skills/` where appropriate <!-- id: 3 -->
- [x] Standardize all `SKILL.md` files to the new template <!-- id: 4 -->
- [x] Establish symlinks in `.roo/skills/` to `.gemini/skills/` <!-- id: 5 -->
- [x] Update `skill-template.md` to reflect the standard <!-- id: 6 -->

## Phase 3: Review (Verification)
- [x] Verify Gemini CLI can still list and activate all skills <!-- id: 7 -->
- [x] Verify Roo Code (simulated) can access skills via symlinks <!-- id: 8 -->
- [x] Ensure `skill-state-manager` and `skill-issue-manager` work correctly after move <!-- id: 9 -->

## Phase 4: End (Completion)
- [x] Record development log in `development_logs/2026-02-10-issue-12.md` <!-- id: 10 -->
- [x] Update project state to "completed" <!-- id: 11 -->
