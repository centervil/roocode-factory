# Meta-Maker Rule Set

When acting as the Meta-Maker, you must follow these rules:

1.  **Strict File Structure**: 
    - Always place mode definitions in `.roomodes` at the root.
    - Always place skill definitions in `.roo/skills/{skill-name}/SKILL.md`.
    - Always place mode-specific rules in `.roo/rules-{mode-slug}/`.

2.  **Mode Definition Standard**:
    - `slug` must be lowercase and hyphenated.
    - `groups` should be minimal but sufficient. For Meta-Maker, `["read", "edit", "command", "browser", "mcp"]` is allowed.

3.  **Skill Package Standard**:
    - Skill names must be in the gerund form (e.g., `managing-tasks`).
    - `SKILL.md` must contain:
      ```markdown
      ---
      name: {skill-name}
      description: {short-description}
      ---
      # Instructions
      {detailed-instructions}
      ```
    - Scripts should be POSIX compliant and placed in `scripts/`.

4.  **Self-Evolution**:
    - When the user asks for a new functionality, first determine if it's a new Mode, a new Skill, or a new Rule for an existing Mode.
    - Propose the change and wait for approval before writing.
