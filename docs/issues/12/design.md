# Design: Issue #12 - Unify and Standardize Skill Management

## Proposed Structure

We will introduce a top-level `skills/` directory (or keep one of the existing ones as the primary source) to hold all shared skills.

### Directory Mapping
- **Source of Truth**: `.gemini/skills/` (since Gemini CLI has a more formal "skill" activation mechanism).
- **Secondary Access**: `.roo/skills/` will contain symlinks to `.gemini/skills/`.

### Standardization of `SKILL.md`
- Use YAML frontmatter for metadata:
  ```yaml
  ---
  name: skill-name
  description: Brief description
  ---
  ```
- Use standardized sections:
  - `# Skill: [Display Name]`
  - `## Capabilities`
  - `## Usage Guidelines` (for human/AI instructions)
  - `## CLI Usage` (for specific commands)
  - `## Resources`

### Handling Tool-Specific Logic
- Shared scripts should be in the skill's `scripts/` directory.
- If a script is tool-specific, prefix it: `gemini-update.sh`, `roo-update.sh`.
- Common logic should be extracted to `common.sh` or similar.

### Refactoring Steps
1.  Identify all skills in `.gemini/skills/` and `.roo/skills/`.
2.  Move non-duplicate skills from `.roo/skills/` to `.gemini/skills/` (if they are portable).
3.  Standardize the structure of each skill directory:
    - `SKILL.md` (Standard format)
    - `scripts/` (Scripts)
    - `references/` (Static docs)
4.  Create symlinks in `.roo/skills/` pointing to `.gemini/skills/`.
5.  Update instructions in `.roo/rules-*/` to refer to the new unified paths if necessary (though symlinks should handle this).
