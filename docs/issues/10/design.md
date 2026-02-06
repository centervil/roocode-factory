# Design: Project-Agnostic Metrics Architecture

## Architecture Overview
The system will move from a monolithic script approach to a plugin-based architecture.
- **Core Orchestrator (`.gemini/scripts/collect-metrics.sh`)**: Responsible for iterating through registered collectors and aggregating results.
- **Collector Interface**: A standard input/output format for collectors (e.g., JSON to stdout).
- **Project-Specific Collectors**: Located in `.ops/metrics/collectors/` or similar, these scripts implement specific logic.

## Implementation Details
1.  **Refactor `collect-metrics.sh`**:
    - Load configuration from `.gemini/commands/audit.toml` or a new config file.
    - Discover collectors in both `.gemini/metrics/collectors/` (core) and `.ops/metrics/collectors/` (project).
    - Execute each collector and merge JSON outputs.
2.  **Define Metrics**:
    - **Autonomy**: Measure of interventions vs. autonomous actions (likely requiring log parsing).
    - **Compliance**: Check against `audit.toml` or similar rules.
3.  **Compliance Score PoC**:
    - A simple collector that reads the audit logs and calculates a score based on presence of required files or adherence to specific formats.

## Test Strategy
- **Unit Tests**: Test the orchestrator with mock collectors.
- **Integration Tests**: Run the full collection suite on the current repo and verify output format.
