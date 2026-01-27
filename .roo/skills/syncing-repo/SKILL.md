---
name: syncing-repo
description: Syncs the current repository with the remote origin and shows status.
---

# Instructions

Use this skill to ensure the local repository is up to date and to review any pending changes.

1.  **Check Status**: Run `git status` to see current branch and changes.
2.  **Pull Changes**: Run `git pull origin $(git branch --show-current)` to get latest updates.
3.  **Verify**: Run `git log -n 5 --oneline` to see recent commits.
4.  **Helper Script**: You can also use the provided `scripts/git-sync.sh` for a guided sync.
