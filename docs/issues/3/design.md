# Design - Issue 3: Implement Metrics Collection Base

## Architecture
The metrics collection base will consist of a shell script or TypeScript script that aggregates data from various sources (Git, Test Runner, Lint) and formats it into a single report.

### Components
1. **Metrics Collector**: A script located at `.gemini/scripts/collect-metrics.sh`.
2. **Data Sources**:
    - `git log`: To calculate code churn.
    - `npm test` (or equivalent): To capture test results.
3. **Storage**: `.roo/audit_logs/metrics.json`.

## Implementation Strategy
- **Code Churn**: Measure the number of commits and lines changed in the last 7 days using `git log --since="7 days ago" --stats`.
- **Test Results**: Run the test suite and capture the exit code and summary.
- **Automation**: Add a command to `.gemini/commands/audit.toml` or create a new `metrics.toml` to trigger the collection.

## Test Strategy
- **Manual Verification**: Run the script and check if `metrics.json` is generated with correct fields.
- **Integration**: Ensure the script handles cases where tests fail or there are no recent commits.
