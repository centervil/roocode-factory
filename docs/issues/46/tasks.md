# Tasks for Issue 46: Gemini CLI integration with Roo Code CLI (/run-roo)

## Phase: Start (Done)
- [x] Create issue workspace `docs/issues/46/`
- [x] Create `design.md`
- [x] Create `tasks.md`

## Phase: Task (Implementation)
- [x] Install `roo` CLI.
  - [x] Create `.infra/scripts/setup_roo.sh` for automated installation.
  - [x] Use `curl` to fetch the installation script.
  - [x] Ensure `roo` is available in the shell PATH.
  - [x] Verify installation with `roo --version`.
- [x] Define the `/run-roo` command.
  - [x] Create `.gemini/commands/run-roo.toml`.
  - [x] Add the command description and prompt to map Gemini inputs to `roo` CLI flags.
- [x] Set up environment variables.
  - [x] Check if `OPENROUTER_API_KEY` is present.
  - [x] Ensure `roo` can access the necessary API keys.
- [x] Test the `/run-roo` command.
  - [x] Execute a test task (e.g., `/run-roo --mode "ask" "What is the version of this project?"`).
  - [x] Verify that the task is completed successfully and output is captured.

## Phase: Review
- [x] Self-review of the implementation.
- [x] Ensure all Success Criteria are met.

## Phase: End
- [ ] Create a Pull Request.
- [ ] Merge and sync.
