# Design: Implement Logging Skill (JSON/Markdown)

## Architecture
The logging skill will be enhanced to support both JSON and Markdown formats. It will be implemented as a stateless skill within the `.roo/skills/logging/` directory.

### Components
- **Logging Skill (`.roo/skills/logging/SKILL.md`)**: Defines the procedure for logging.
- **Log Storage (`development_logs/`)**: Directory where audit logs are persisted.

## Implementation Plan
1.  **Refactor `SKILL.md`**: Update the logging skill definition to match the standard template and include instructions for JSON and Markdown output.
2.  **Stateless Procedure**: Ensure the skill remains a set of instructions without internal state.
3.  **Format Support**:
    - **Markdown**: Human-readable summary including Goal, Result, Gap, and Action.
    - **JSON**: Structured data for machine processing, including timestamps, session IDs, and categorized findings.

## Test Strategy
- **Manual Verification**: Invoke the skill from `pm` mode and verify the output in both JSON and Markdown.
- **Orchestration Test**: Use the dummy task pattern to ensure the Orchestrator can successfully dispatch to the logging skill.
- **Format Validation**: Ensure JSON output is valid and Markdown is correctly formatted.

## Interface Definition
### Input
- `session_id`: Unique identifier for the session.
- `goal`: What was intended.
- `result`: What actually happened.
- `gap`: Discrepancy between goal and result.
- `action`: Next steps for improvement.
- `format`: `markdown` | `json` | `both`

### Output
- A log file in `development_logs/` in the requested format(s).
