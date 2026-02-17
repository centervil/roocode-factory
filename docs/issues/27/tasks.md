# Tasks: Integrate Requirement Deep-Dive into GitHub Issue Manager

## Phase 1: Implementation
- [x] Update `.gemini/skills/skill-issue-manager/SKILL.md` to include requirement gathering in its `Phase: Start` workflow.
- [x] Add the "skip" instruction to the requirement gathering section.
- [x] Update `.gemini/skills/skill-requirement-expert/SKILL.md` to note its integration with `skill-issue-manager`.
- [x] Ensure `requirements.md` generation is mentioned as a key output of the Start phase.

## Phase 2: Verification
- [x] Perform a self-review of the updated instructions.
- [x] Simulate the "Phase: Start" process for a dummy issue (e.g., #27 itself, or a new test issue).
- [x] Confirm that the agent proposes requirement deep-dive.
- [x] Confirm that the agent offers a skip option.
- [x] Verify that `requirements.md` is updated/created correctly.

## Phase 3: Documentation & Cleanup
- [x] Finalize the task checklist.
- [x] (Optional) Update `README.md` if the entry point for requirements has changed significantly (likely not needed as `dev` is the main command).
