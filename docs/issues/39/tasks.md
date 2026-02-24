# Tasks - Issue #39: Implement Metrics Collection MVP

## Phase 1: Infrastructure & Cleanup
- [x] Create `.ops/audit_logs/sessions/` directory. <!-- id: 0 -->
- [x] Migrate existing JSON logs from `development_logs/` to `.ops/audit_logs/sessions/`. <!-- id: 1 -->
- [x] Update `.gemini/skills/skill-logging/SKILL.md` to support split output. <!-- id: 2 -->

## Phase 2: Collector Upgrade
- [x] Implement new logic in `.ops/metrics/collectors/compliance.sh` (Dynamic analysis). <!-- id: 3 -->
- [x] Implement new logic in `.ops/metrics/collectors/autonomy.sh` (JSON-based aggregation). <!-- id: 4 -->

## Phase 3: Integration & Visualization
- [x] Create a script to aggregate metrics and update `.ops/audit_logs/metrics.json`. <!-- id: 5 -->
- [x] Implement automatic update logic for `project_state.md`. <!-- id: 6 -->

## Phase 4: Validation
- [x] Verify metrics with real/mock session data. <!-- id: 7 -->
