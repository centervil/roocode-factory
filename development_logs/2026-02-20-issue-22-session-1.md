# Development Log: Issue #22 - Slash Command Policy

## Session 1 (2026-02-20)
### Accomplishments
- Created `docs/policies/slash-commands.md` defining naming, directory, and schema standards for slash commands.
- Audited and updated existing `.gemini/commands/` (e.g., added `name` to `next-issue.toml`).
- Integrated policy into project's source of truth:
    - Updated `README.md` (Operational Protocols) to include Slash Command Policy mapping.
    - Updated `AGENTS.md` (Operational Integrity) to include interface consistency requirement.
- Verified standard directory roles: `.gemini/` (CLI/TOML) vs `.roo/` (VS Code/MD).

### Technical Details
- Modified: `docs/policies/slash-commands.md`, `.gemini/commands/next-issue.toml`, `README.md`, `AGENTS.md`.
- Verified: Manual check of TOML and Markdown command definitions against the new policy.
- Branch: `issue-22`.

### Process Corrections
- Identified that `.roo/commands/` uses Markdown custom instructions while `.gemini/commands/` uses TOML. Standardized both within the policy.
