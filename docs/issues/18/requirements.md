# Requirements for Issue #18: Organize duplicates in my-skills repository

## 1. Objective
Identify and remove redundant skill templates and duplicate files within the `my-skills` repository (located at `work/my-skills/`) to improve maintainability and ensure a single source of truth for skill creation.

## 2. Context
- The `my-skills` repository contains several skill implementations and templates.
- Currently, a `skill-template.md` exists at the root of `my-skills/`.
- Another template, `skill-definition.md`, exists in `skill-project-and-skill-architect/templates/`.
- The project's IDD workflow requires clean and standardized skill assets.

## 3. Scope
- Review all files within `work/my-skills/`.
- Identify duplicate or redundant templates.
- Identify identical or near-identical logic/files across different skill folders.
- Propose and execute a consolidation plan.

## 4. Acceptance Criteria
- [ ] Redundant `skill-template.md` files are consolidated or removed.
- [ ] Template for skill creation is unified and located in its most logical place (`skill-project-and-skill-architect/templates/`).
- [ ] No duplicate files (excluding mandatory `SKILL.md`) exist within `my-skills`.
- [ ] All remaining skills function correctly after the cleanup.
- [ ] Documentation reflects the new organization.
