# Design: Metrics Auto-Collection and Enhanced Execution Monitoring (Issue #47)

## 1. Goal
Implement a mechanism to capture "RAW logs" (stdout/stderr) of `roo` CLI execution to ensure objective metrics collection and integrity auditing, bypassing AI-generated reports.

## 2. Architecture
### 2.1 Raw Log Shadowing
- **Wrapper Script**: Introduce `.infra/scripts/run_roo_wrapper.sh` to encapsulate the `roo` CLI execution.
- **Teeing Output**: Use `tee` or similar redirection to record stdout and stderr to `.ops/audit_logs/raw/[timestamp]_[mode].log` while still providing output to the terminal for the AI agent.
- **Command Update**: Update `.gemini/commands/run-roo.toml` to use this wrapper.

### 2.2 Metrics Extraction (Fact Extractor)
- **Script**: `.ops/scripts/extract_metrics.py` (or shell script) to parse raw logs.
- **Indicators**:
    - **Turn Count (TC)**: Count of prompt/response turns in the log.
    - **Tool Success Rate (TSR)**: Ratio of successful tool calls based on exit codes.
    - **Read-to-Write Ratio**: Ratio of read/search tool calls vs. write/replace tool calls.

### 2.3 Integrity Audit
- **Comparison**: Compare `.ops/audit_logs/raw/` data with `development_logs/` and `.ops/project_state.md`.
- **Integrity Score**: A score (0-100) reflecting the consistency between AI reports and actual execution logs.

## 3. Data Flow
1. `Gemini CLI` -> `/run-roo` command.
2. `/run-roo` -> `.infra/scripts/run_roo_wrapper.sh`.
3. `run_roo_wrapper.sh` -> executes `roo`, pipes to `.ops/audit_logs/raw/TIMESTAMP.log`.
4. `roo` output -> displayed to `Gemini CLI`.
5. Post-session: `.ops/scripts/extract_metrics.py` parses the RAW logs.

## 4. Testing Plan (PoC)
1. Run a simple task using `/run-roo`.
2. Verify that `.ops/audit_logs/raw/` contains a log file.
3. Verify that the log file contains the full stdout/stderr of the `roo` execution.
4. Manually verify if tools and their exit codes are identifiable in the raw log.
