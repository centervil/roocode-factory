# 🚀 Project Dashboard: Roocode Factory

*Last Updated: 2026-03-18T22:30:36.032636*

## 📊 Visual Metrics Dashboard

### 📈 Tool Success Rate (TSR) Trend
```mermaid
xychart-beta
    title "Tool Success Rate (TSR) Trend (Last 10 Sessions)"
    x-axis ["1:code", "2:code", "3:code", "4:code", "5:ask", "6:ask"]
    y-axis "Success Rate (%)" 0 --> 100
    line [100, 100, 0, 81, 100, 100]
```

### 🍕 Tool Usage (Last Session)
```mermaid
pie title "Tool Usage (Read vs Write) - Session: 20260309_223635_ask"
    "Read Tools" : 1
    "Write Tools" : 0
```

### 🤖 Autonomy Level
```mermaid
pie title "System Autonomy Rate (58.6%)"
    "Autonomous" : 58.6
    "Intervention Needed" : 41.4
```

### ⚖️ Architectural Compliance (Behavioral Alignment)
```mermaid
xychart-beta
    title "Architectural Compliance (Behavioral Alignment) Trend"
    x-axis ["1:code", "2:code", "3:code", "4:code", "5:ask", "6:ask"]
    y-axis "Compliance Score (0-100)" 0 --> 100
    line [0, 25, 100, 49, 25, 100]
```


---
## ℹ️ How to read
- **TSR Trend**: Indicates the stability of tool executions. Higher is better.
- **Tool Usage**: Shows the balance between investigation (Read) and implementation (Write).
- **Autonomy**: High autonomy means the agent is completing more tasks without needing manual intervention.
- **Architectural Compliance**: Measures how well the agent follows its Mode-specific rules (Must/Must Not). Evaluated by LLM-as-a-Judge.

---
[← Back to METRICS.md](../.ops/metrics/METRICS.md) | [Home](../README.md)
