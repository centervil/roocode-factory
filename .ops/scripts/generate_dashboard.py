#!/usr/bin/env python3
import json
import os
from datetime import datetime

METRICS_FILE = ".ops/audit_logs/metrics.json"
DASHBOARD_FILE = "docs/dashboard.md"

def generate_mermaid_charts(data):
    sessions = data.get('sessions', [])
    summary = data.get('summary', {})
    metrics = data.get('metrics', {})
    
    if not sessions:
        return "No session data available."

    # 1. TSR Line Chart (Last 5-10 sessions)
    recent = sessions[-10:]
    tsr_chart = "```mermaid\nxychart-beta\n    title \"Tool Success Rate (TSR) History\"\n    x-axis ["
    tsr_chart += ", ".join([f'"{s["session_id"][-6:]}"' for s in recent])
    tsr_chart += "]\n    y-axis \"Success Rate (%)\" 0 --> 100\n    line ["
    tsr_chart += ", ".join([str(int(s.get("tool_success_rate", 0) * 100)) for s in recent])
    tsr_chart += "]\n```"

    # 2. Read/Write Ratio Pie Chart (Last session)
    last = sessions[-1]
    read = last.get('read_count', 0)
    write = last.get('write_count', 0)
    pie_chart = f"```mermaid\npie title \"Tool Usage Distribution (Last Session: {last['session_id'][-6:]})\"\n    \"Read Tools\" : {read}\n    \"Write Tools\" : {write}\n```"

    # 3. Autonomy vs Interventions (Summary)
    # Using a simple gauge or progress bar representation using Mermaid state diagram or just text
    # Mermaid doesn't have a native "gauge", so we use a stylized block
    autonomy_rate = metrics.get('autonomy', {}).get('rate', 0)
    autonomy_display = f"```mermaid\nrequirementDiagram\n    requirement \"System Autonomy\"\n    id: 1\n    text: \"{autonomy_rate}%\"\n    severity: critical\n```"

    return f"""## 📊 Visual Metrics Dashboard

### 📈 Tool Success Rate (TSR) Trend
{tsr_chart}

### 🍕 Tool Usage (Read vs Write)
{pie_chart}

### 🤖 Autonomy Level
{autonomy_display}
"""

def update_dashboard():
    if not os.path.exists(METRICS_FILE):
        return

    with open(METRICS_FILE, 'r') as f:
        data = json.load(f)

    charts = generate_mermaid_charts(data)
    
    content = f"""# 🚀 Project Dashboard: Roocode Factory

*Last Updated: {data.get('last_updated', datetime.utcnow().isoformat())}*

{charts}

---
[← Back to METRICS.md](../.ops/metrics/METRICS.md) | [Home](../README.md)
"""

    with open(DASHBOARD_FILE, 'w') as f:
        f.write(content)

    print(f"Dashboard updated: {DASHBOARD_FILE}")

if __name__ == "__main__":
    update_dashboard()
