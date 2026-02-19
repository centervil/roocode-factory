# Design for Issue #18: Organize duplicates in my-skills repository

## 1. Analysis of Current Duplicates
- **Templates**: `work/my-skills/skill-template.md` (English) and `work/my-skills/skill-project-and-skill-architect/templates/skill-definition.md` (Japanese) serve the same purpose.
- **Location**: Having a template at the root of `my-skills/` is inconsistent if `skill-project-and-skill-architect` is the designated skill for creating new skills.
- **Consistency**: The root `skill-template.md` is more detailed and follows English, which aligns with Global portability goals.

## 2. Proposed Changes
- **Template Consolidation**:
    - Move `work/my-skills/skill-template.md` to `work/my-skills/skill-project-and-skill-architect/templates/skill-template.md`.
    - Delete `work/my-skills/skill-project-and-skill-architect/templates/skill-definition.md`.
    - Ensure the unified `skill-template.md` covers all necessary aspects (Overview, Capabilities, Usage, CLI, Resources, Output Contract).
- **Cleanup**:
    - Remove `work/my-skills/skill-template.md` after the move.
- **Audit for further duplicates**:
    - Final scan for any other redundant template files (e.g., `collector-template.sh` if any other exists).
    - Ensure no empty or redundant `references/` or `scripts/` exist.

## 3. Implementation Plan
1. Move and merge templates.
2. Remove redundant files.
3. Validate by checking if the new template structure is logical and ready for use by `skill-project-and-skill-architect`.

## 4. Verification Plan
- Run `ls -R work/my-skills/` to confirm the new structure.
- Verify that `skill-template.md` contains the best of both previous templates.
- Confirm no broken links or references.
