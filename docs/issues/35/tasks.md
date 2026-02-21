# Tasks: Optimize IDD workflow for increased autonomy and lifecycle completion

- [ ] **Phase 1: Skill Modification (Common Skill)**
  - [ ] Update `.gemini/skills/skill-issue-manager/SKILL.md` to skip approval for `tasks.md` if requirements are clear.
  - [ ] Update `.gemini/skills/skill-issue-manager/SKILL.md` to include "Autonomous Conclusion" (Merge/Sync) phase after PR approval.
  - [ ] Update `.roo/skills/skill-issue-manager/SKILL.md` to match the new workflow for Roo Code consistency.
  - [ ] Update `skill-requirement-expert/SKILL.md` if needed to ensure requirements are marked as "clear" for the next step. (Check current content first)

- [ ] **Phase 2: Operational Procedure Integration**
  - [ ] Update `AGENTS.md` (if needed) to reflect the new IDD workflow for increased autonomy and lifecycle completion.
  - [ ] Ensure that `skill-issue-manager` instructions are consistent across both `.gemini/` and `.roo/` infrastructures.

- [ ] **Phase 3: Verification (Review)**
  - [ ] Self-review the changes to `skill-issue-manager/SKILL.md`.
  - [ ] Verify that the new workflow includes PR creation, wait for approval, merge, and local sync.
  - [ ] Check if submodule push logic is correctly integrated into the "End" phase description.

- [ ] **Phase 4: Finalization (End)**
  - [ ] Create a pull request for the changes in `skill-issue-manager` and `AGENTS.md`.
  - [ ] Wait for user approval of the PR content.
  - [ ] **(Autonomous Conclusion)** After approval, merge the PR, delete the `issue-35` branch, push any submodules, and update the local `main` branch.

## Success Criteria
- [ ] No more manual approval for `tasks.md` after requirements are settled.
- [ ] Workflow proceeds autonomously from `Task` to PR creation.
- [ ] Session ends with a synchronized local `main` branch after merging.
