# Task List - Issue #35: Optimize IDD workflow

- [ ] **Task 1: Research & Setup**
    - [ ] Analyze `skill-issue-manager` scripts in `.gemini/skills/skill-issue-manager/scripts/`.
    - [ ] Analyze existing `dev` and `requirements` command logic.
- [ ] **Task 2: Update IDD Operational Rules**
    - [ ] Update `SKILL.md` of `skill-issue-manager` to reflect the new autonomous flow (Start -> Execute -> PR).
- [ ] **Task 3: Refine `dev` and `requirements` Commands**
    - [ ] Modify `dev` command logic to remove redundant approvals between Task phases.
    - [ ] Ensure `requirements` command effectively feeds into the `dev` workflow.
- [ ] **Task 4: Implement Post-Merge Automation**
    - [ ] Develop logic for automatic branch deletion and submodule synchronization after PR merge.
- [ ] **Task 5: Validation & Dogfooding**
    - [ ] Verify the optimized workflow by simulating a small development task.
    - [ ] Confirm that post-merge cleanup works correctly.
- [ ] **Task 6: PR Creation and Completion**
    - [ ] Review all changes and create the PR.
