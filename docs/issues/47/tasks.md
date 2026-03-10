# Tasks for Issue 47: Metrics Auto-Collection and Enhanced Execution Monitoring

- [x] **Phase 1: PoC (Raw Log Capture)**
    - [x] Create `.infra/scripts/run_roo_wrapper.sh`.
    - [x] Implement output redirection and timestamped logging to `.ops/audit_logs/raw/`.
    - [x] Update `.gemini/commands/run-roo.toml` to use the wrapper.
    - [x] Test with a simple `roo` command and verify log generation.

- [x] **Phase 2: Fact Extractor Implementation**
    - [x] Create `.ops/scripts/extract_metrics.py` to parse raw logs.
    - [x] Implement extraction logic for:
        - Turn Count (TC).
        - Tool Success Rate (TSR).
        - Read-to-Write Ratio.
    - [x] Test the extractor on a sample raw log.

- [x] **Phase 3: Integrity Audit System**
    - [x] Create `.ops/scripts/integrity_audit.py` to compare reports and RAW logs.
    - [x] Define the formula for "Integrity Score".
    - [x] Update `.ops/project_state.md` and `development_logs/` if necessary.

- [x] **Phase 4: Final Validation**
    - [x] Execute a full `roo` session and verify the entire pipeline (Capture -> Extract -> Audit).
    - [x] Verify all Success Criteria of Issue #47 are met.
