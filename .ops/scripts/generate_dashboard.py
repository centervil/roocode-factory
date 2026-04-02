#!/usr/bin/env python3
import json
import os
import sys

METRICS_FILE = ".ops/audit_logs/metrics.json"

def generate_mermaid_charts(data):
    charts = []

    # 1. Pie Chart: Autonomy Rate
    rate = data.get('metrics', {}).get('autonomy', {}).get('rate', 0)
    charts.append("### Autonomy Rate (AI vs Human)")
    charts.append("```mermaid\npie title Autonomy vs Intervention\n    \"Autonomous Actions\" : " + str(rate) + "\n    \"Manual Interventions\" : " + str(round(100 - rate, 1)) + "\n```")

    # 2. XY Chart: TSR Trend (Last 10 sessions)
    sessions = data.get('sessions', [])[-10:]
    if sessions:
        charts.append("### Tool Success Rate (TSR) Trend")
        charts.append("```mermaid\nxychart-beta\n    title \"TSR per Session (Last 10)\"\n    x-axis [" + ", ".join(['"' + s.get('session_id', '')[-6:] + '"' for s in sessions]) + "]\n    y-axis \"Success Rate\" 0 --> 1\n    line [" + ", ".join([str(s.get('tool_success_rate', 0)) for s in sessions]) + "]\n```")

    # 3. Radar Chart: System Integrity (Using Mermaid's quadrant or polar chart if available, but radar is often simulated)
    # Since Mermaid's native radar is limited, we use a simple table-based visualization or requirement diagram as a fallback,
    # or just use a bar chart for integrity components.
    compliance = data.get('metrics', {}).get('compliance', {})
    charts.append("### System Integrity Profile")
    charts.append("```mermaid\nrequirementDiagram\n\n    requirement Integrity_Score {\n    id: 1\n    text: Overall Score\n    risk: low\n    verifymethod: analysis\n    }\n\n    requirement Protocol_Fidelity {\n    id: 2\n    text: " + str(compliance.get('protocol_fidelity', 0)) + "%\n    risk: low\n    verifymethod: test\n    }\n\n    requirement Behavioral_Alignment {\n    id: 3\n    text: " + str(compliance.get('behavioral_alignment', 0)) + "%\n    risk: low\n    verifymethod: inspection\n    }\n\n    Integrity_Score - satisfies -> Protocol_Fidelity\n    Integrity_Score - satisfies -> Behavioral_Alignment\n```")

    return "\n\n".join(charts)

def main():
    if not os.path.exists(METRICS_FILE):
        print("Metrics file not found.")
        return

    with open(METRICS_FILE, 'r') as f:
        data = json.load(f)

    mermaid_content = generate_mermaid_charts(data)
    
    # Update docs/dashboard.md
    dashboard_path = "docs/dashboard.md"
    template = f"""# Metrics Dashboard

This dashboard visualizes the health and performance of the Roocode Factory system based on session logs.

{mermaid_content}

---
*Last Updated: {data.get('last_updated', 'Unknown')}*
"""
    
    with open(dashboard_path, 'w') as f:
        f.write(template)
    
    print(f"Successfully generated dashboard: {dashboard_path}")

if __name__ == "__main__":
    main()
