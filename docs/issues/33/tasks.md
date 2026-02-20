# Tasks: Restore `self-optimize` slash command to `my-commands` submodule

- [ ] **Phase 1: Preparation**
  - [ ] Identify the old `self-optimize.md` content from git history (already retrieved: commit `5bf58b8^:commands/self-optimize.md`).
  - [ ] Identify the current `audit.toml` format to use as a template.

- [ ] **Phase 2: Implementation (Task)**
  - [ ] Create `.roo/commands/self-optimize.toml` in the `my-commands` submodule.
  - [ ] Create `.roo/commands/self-optimize.md` as a symbolic link to `self-optimize.toml`.
  - [ ] Verify the link and the content of the TOML.

- [ ] **Phase 3: Integration (Task)**
  - [ ] Commit changes in the `my-commands` submodule (`.roo/commands/`).
  - [ ] Update the `commands` submodule reference in the `.roo` repository and commit it.
  - [ ] Update the `.roo` submodule reference in the root repository.

- [ ] **Phase 4: Verification (Review)**
  - [ ] List `.roo/commands/` to ensure files are present.
  - [ ] Call `/self-optimize` or manually check if it's interpretable as a slash command.

- [ ] **Phase 5: Finalization (End)**
  - [ ] Create a pull request or report the completion of changes.
