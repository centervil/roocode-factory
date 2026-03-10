#!/usr/bin/env python3
import json
import os
import re

METRICS_FILE = ".ops/audit_logs/metrics.json"
MD_FILE = ".ops/metrics/METRICS.md"

def update_md():
    if not os.path.exists(METRICS_FILE):
        return

    with open(METRICS_FILE, 'r') as f:
        data = json.load(f)

    summary = data.get('summary', {})
    sessions = data.get('sessions', [])
    
    # Take last 5 sessions for history
    recent_sessions = sessions[-5:] if sessions else []
    
    history_table = "| Session ID | Mode | Turns | TSR | R/W Ratio |\n| :--- | :--- | :--- | :--- | :--- |\n"
    if not recent_sessions:
        history_table += "| N/A | N/A | N/A | N/A | N/A |\n"
    for s in reversed(recent_sessions):
        history_table += f"| {s.get('session_id')} | {s.get('mode')} | {s.get('turn_count')} | {s.get('tool_success_rate')} | {s.get('read_to_write_ratio')} |\n"

    performance_section = f"""## 3. Performance Summary (Automated)
- **Total Sessions**: {summary.get('total_sessions', 0)}
- **Average TSR**: {summary.get('avg_tsr', 0)}
- **Total Tool Calls**: {summary.get('total_tool_calls', 0)}
- **Avg R/W Ratio**: {summary.get('avg_rw_ratio', 0)}

### Recent Performance History
{history_table}
"""

    if not os.path.exists(MD_FILE):
        content = performance_section
    else:
        with open(MD_FILE, 'r') as f:
            content = f.read()

    # Check if section exists, if not append
    header = "## 3. Performance Summary (Automated)"
    if header in content:
        # Use a more robust pattern to match until the next level-2 header or end of string
        pattern = re.escape(header) + r".*?(?=\n## |\Z)"
        content = re.sub(pattern, performance_section.strip(), content, flags=re.DOTALL)
    else:
        content = content.strip() + "\n\n" + performance_section

    with open(MD_FILE, 'w') as f:
        f.write(content)

    print("METRICS.md updated with latest statistics.")

if __name__ == "__main__":
    update_md()
