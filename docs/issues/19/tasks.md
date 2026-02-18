# Tasks: Issue #19 Refactor External Dependencies

## Phase 1: Audit (Investigation)
- [ ] **T1.1**: Run a global search across `work/my-skills/` for hardcoded absolute paths (e.g., `/home/`).
- [ ] **T1.2**: Search for hardcoded references to project-specific files (`AGENTS.md`, `.ops/`, `README.md`).
- [ ] **T1.3**: Document all found dependencies in a temporary audit log.

## Phase 2: Implementation (Refactoring)
- [ ] **T2.1**: Refactor Shell Scripts: Replace absolute paths with relative ones or dynamic discovery logic.
- [ ] **T2.2**: Update `SKILL.md` files: Generalize instructions to remove specific project names or fixed file paths.
- [ ] **T2.3**: Implement/Verify a "Root Discovery" pattern in at least one complex skill (e.g., `skill-project-and-skill-architect`).

## Phase 3: Verification (Portability Test)
- [ ] **T3.1**: Run `grep` to ensure no absolute paths or specific user references remain in `work/my-skills/`.
- [ ] **T3.2**: Copy `my-skills` to a temporary directory outside the current project and verify that a non-destructive skill (like `skill-research`) can still be "activated" or its instructions understood without path errors.
- [ ] **T3.3**: Verify error handling when `AGENTS.md` is missing.

## Phase 4: Finalization
- [ ] **T4.1**: Remove the temporary audit log.
- [ ] **T4.2**: Record progress in the development log.
