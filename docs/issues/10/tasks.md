# Tasks: Issue #10

- [ ] Refactor `.gemini/scripts/collect-metrics.sh` to support dynamic collector discovery.
- [ ] Define the "Collector Interface" (JSON schema for output).
- [ ] Create directory structure for project-specific collectors (`.ops/metrics/collectors/`).
- [ ] Implement "AI Autonomy" metric definition (documentation/spec).
- [ ] Implement "Protocol Compliance" metric definition (documentation/spec).
- [ ] Create a PoC collector for "Compliance Score".
- [ ] Verify separation: Ensure no project-specific logic remains in `.gemini` core scripts.
- [x] Test the new architecture with a sample run.

## Review Feedback
- [x] Fix `test_status.sh` JSON schema to maintain backward compatibility (flatten `test_status` and `test_exit_code`).