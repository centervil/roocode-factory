# Design Document - Issue #39: Implement Metrics Collection MVP

## Goals
- Reorganize logging structure to separate human-readable context from machine-readable audit evidence.
- Implement dynamic metrics (Protocol Fidelity, Behavioral Alignment) based on execution logs.
- Automate the collection and visualization of these metrics.

## Proposed Changes

### 1. Logging Infrastructure
- **`skill-logging` Upgrade**:
    - Update logic to write Markdown files to `development_logs/`.
    - Update logic to write JSON files to `.ops/audit_logs/sessions/`.
    - Ensure JSON logs include `source_mode` and `protocol_fidelity` markers.

### 2. Log Reorganization & Cleanup
- Create `.ops/audit_logs/sessions/` directory.
- Move existing JSON files from `development_logs/` to `.ops/audit_logs/sessions/`.
- Clean up or archive inconsistent files in `.ops/audit_logs/`.

### 3. Dynamic Collectors
- **`compliance.sh`**: Analyze JSON files in `.ops/audit_logs/sessions/` for protocol patterns and gap keywords.
- **`autonomy.sh`**: Sum up interactions and total actions from the same JSON files.

### 4. Integration
- A script or command to trigger collection and update `project_state.md`.

## Verification Plan
- Run `skill-logging` and verify split output.
- Run collectors and verify `metrics.json` content.
- Check if `project_state.md` reflects the new metrics.
