# Tasks for Issue #18: Organize duplicates in my-skills repository

## 1. Research & Analysis
- [x] Analyze current `my-skills` structure and identify duplicates.
- [x] Compare root `skill-template.md` and `skill-project-and-skill-architect/templates/skill-definition.md`.

## 2. Consolidation & Cleanup
- [ ] **Consolidate Templates**:
    - Merge `skill-template.md` (root) and `skill-definition.md` (skill-project-and-skill-architect/templates/) into a single, comprehensive `skill-template.md`.
    - Choose English as the primary language for consistency with global portability goals.
- [ ] **Move & Rename**:
    - Place the consolidated `skill-template.md` into `work/my-skills/skill-project-and-skill-architect/templates/`.
- [ ] **Remove Redundancies**:
    - Delete the root `work/my-skills/skill-template.md`.
    - Delete the old `work/my-skills/skill-project-and-skill-architect/templates/skill-definition.md`.
- [ ] **Final Audit**:
    - Scan for any other redundant template files or empty directories within `work/my-skills/`.
    - Verify that no other skills have redundant `references/` or `scripts/` that could be unified.

## 3. Documentation & Verification
- [ ] Verify the new structure with `ls -R work/my-skills/`.
- [ ] Record the changes in a development log: `development_logs/2026-02-19-issue-18.md`.
- [ ] Review the `my-skills` repository to ensure it is clean and ready for RC release.
