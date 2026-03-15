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

    # 1. TSR Line Chart (Last 10 sessions)
    # Use index + mode as label to avoid duplication
    recent = sessions[-10:]
    labels = []
    for i, s in enumerate(recent):
        short_id = s["session_id"].split('_')[1] if '_' in s["session_id"] else s["session_id"][-4:]
        labels.append(f"\"{i+1}:{s['mode']}\"")
    
    tsr_chart = "```mermaid\nxychart-beta\n    title \"Tool Success Rate (TSR) Trend (Last 10 Sessions)\"\n    x-axis ["
    tsr_chart += ", ".join(labels)
    tsr_chart += "]\n    y-axis \"Success Rate (%)\" 0 --> 100\n    line ["
    tsr_chart += ", ".join([str(int(s.get("tool_success_rate", 0) * 100)) for s in recent])
    tsr_chart += "]\n```"

    # 2. Read/Write Ratio Pie Chart (Last session)
    last = sessions[-1]
    read = last.get('read_count', 0)
    write = last.get('write_count', 0)
    # Handle case where both are zero
    if read == 0 and write == 0:
        pie_chart = "> No tool usage in the last session."
    else:
        pie_chart = f"```mermaid\npie title \"Tool Usage (Read vs Write) - Session: {last['session_id']}\"\n    \"Read Tools\" : {read}\n    \"Write Tools\" : {write}\n```"

    # 3. Autonomy Level (Pie chart: Autonomous vs Manual intervention)
    # Mermaid requirementDiagram was failing. Using Pie chart for clarity.
    auto_rate = metrics.get('autonomy', {}).get('rate', 0)
    manual_rate = max(0, 100.0 - auto_rate)
    autonomy_chart = f"```mermaid\npie title \"System Autonomy Rate ({auto_rate}%)\"\n    \"Autonomous\" : {auto_rate}\n    \"Intervention Needed\" : {manual_rate}\n```"

    return f"""## 📊 Visual Metrics Dashboard

### 📈 Tool Success Rate (TSR) Trend
{tsr_chart}

### 🍕 Tool Usage (Last Session)
{pie_chart}

### 🤖 Autonomy Level
{autonomy_chart}
"""

def update_dashboard():
    if not os.path.exists(METRICS_FILE):
        return

    with open(METRICS_FILE, 'r') as f:
        data = json.load(f)

    charts = generate_mermaid_charts(data)
    
    content = f"""# 🚀 Project Dashboard: Roocode Factory

*Last Updated: {datetime.now().isoformat()}*

{charts}

---
## ℹ️ How to read
- **TSR Trend**: Indicates the stability of tool executions. Higher is better.
- **Tool Usage**: Shows the balance between investigation (Read) and implementation (Write).
- **Autonomy**: High autonomy means the agent is completing more tasks without needing manual intervention.

---
[← Back to METRICS.md](../.ops/metrics/METRICS.md) | [Home](../README.md)
"""

    with open(DASHBOARD_FILE, 'w') as f:
        f.write(content)

    print(f"Dashboard updated: {DASHBOARD_FILE}")

if __name__ == "__main__":
    update_dashboard()
