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
- **Total Sessions**: 3
- **Average TSR**: 0.94
- **Total Tool Calls**: 57
- **Avg R/W Ratio**: 14.33

### Recent Performance History
| Session ID | Mode | Turns | TSR | R/W Ratio |
| :--- | :--- | :--- | :--- | :--- |
| 20260310_140456_ask | ask | 4 | 1.0 | 2.0 |
| 20260309_223814_code | code | 2 | 1.0 | 0.0 |
| 20260310_103709_code | code | 55 | 0.81 | 41.0 |