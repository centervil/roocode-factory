# Project-Specific Metric Definitions

## 1. AI Autonomy
**Definition**: Measures the ratio of autonomous actions performed by the agent versus human interventions.
**Calculation**: `(Total Actions - Interventions) / Total Actions`
- **Data Source**: Audit logs (e.g., `.ops/audit_logs/roocode_tasklog.txt.md`).
- **Collector**: `.ops/metrics/collectors/autonomy.sh`

## 2. Protocol Compliance
**Definition**: A score representing how well the project adheres to the established operational protocols and file structures.
**Calculation**: Sum of points for each satisfied check.
- **Checks (PoC)**:
    - `audit.toml` exists: 50 points
    - `README.md` exists: 50 points
    - **Total**: 100 points
- **Collector**: `.ops/metrics/collectors/compliance.sh`

## 3. Performance Summary (Automated)
- **Total Sessions**: 16
- **Average TSR**: 0.74
- **Total Tool Calls**: 636
- **Avg R/W Ratio**: 3.38

### Recent Performance History
| Session ID | Mode | Turns | TSR | R/W Ratio |
| :--- | :--- | :--- | :--- | :--- |
| 20260320_084149_pm | pm | 1 | 0.0 | 1.0 |
| 20260320_084229_pm | pm | 1 | 0.0 | 1.0 |
| 20260320_084249_pm | pm | 1 | 1.0 | 1.0 |
| 20260320_084311_pm | pm | 1 | 1.0 | 1.0 |
| 20260320_084339_pm | pm | 3 | 1.0 | 1.0 |