# Metrics Dashboard

This dashboard visualizes the health and performance of the Roocode Factory system based on session logs.

### Autonomy Rate (AI vs Human)

```mermaid
pie title Autonomy vs Intervention
    "Autonomous Actions" : 100.0
    "Manual Interventions" : 0.0
```

### Tool Success Rate (TSR) Trend

```mermaid
xychart-beta
    title "TSR per Session (Last 10)"
    x-axis ["742_pm", "938_pm", "701_pm", "719_pm", "504_pm", "339_pm", "311_pm", "249_pm", "229_pm", "149_pm"]
    y-axis "Success Rate" 0 --> 1
    line [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0]
```

### System Integrity Profile

```mermaid
requirementDiagram

    requirement Integrity_Score {
    id: 1
    text: Overall Score
    risk: low
    verifymethod: analysis
    }

    requirement Protocol_Fidelity {
    id: 2
    text: 73.8%
    risk: low
    verifymethod: test
    }

    requirement Behavioral_Alignment {
    id: 3
    text: 37.8%
    risk: low
    verifymethod: inspection
    }

    Integrity_Score - satisfies -> Protocol_Fidelity
    Integrity_Score - satisfies -> Behavioral_Alignment
```

---
*Last Updated: 2026-04-02T03:12:56.856416Z*
