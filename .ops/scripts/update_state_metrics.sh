#!/bin/bash

# Update project_state.md with latest metrics from metrics.json

METRICS_FILE=".ops/audit_logs/metrics.json"
STATE_FILE=".ops/project_state.md"

if [ ! -f "$METRICS_FILE" ]; then
    echo "Metrics file not found."
    exit 1
fi

# Extract values using python for reliability
VALUES=$(python3 - <<EOF
import json
import os
with open('$METRICS_FILE') as f:
    data = json.load(f)
    m = data.get('metrics', {})
    sum = data.get('summary', {})
    
    comp = m.get('compliance', {})
    auto = m.get('autonomy', {})
    
    score = comp.get('score', 0)
    fidelity = comp.get('protocol_fidelity', 0)
    alignment = comp.get('behavioral_alignment', 0)
    rate = auto.get('rate', 0)
    
    # Summary (avg_tsr is 0.0-1.0 in extract_metrics, so needs * 100)
    tsr = sum.get('avg_tsr', 0)
    sessions = sum.get('total_sessions', 0)
    
    print(f"{score}|{fidelity}|{alignment}|{rate}|{tsr}|{sessions}")
EOF
)

IFS='|' read -r SCORE FIDELITY ALIGNMENT AUTO_RATE TSR TOTAL_SESSIONS <<< "$VALUES"

export SCORE FIDELITY ALIGNMENT AUTO_RATE TSR TOTAL_SESSIONS

python3 - <<EOF
import re
import os

with open('$STATE_FILE', 'r') as f:
    content = f.read()

score = os.environ['SCORE']
# Fidelity, Alignment, Auto_Rate are already % (0-100)
fidelity = float(os.environ['FIDELITY'])
alignment = float(os.environ['ALIGNMENT'])
auto_rate = float(os.environ['AUTO_RATE'])
# TSR is 0.0-1.0, so needs * 100
tsr = float(os.environ['TSR']) * 100
sessions = os.environ['TOTAL_SESSIONS']

metrics_section = f"""## Metrics (Snapshot)
- **System Integrity (Dynamic)**:
    - Protocol Fidelity: {fidelity:.1f}%
    - Behavioral Alignment: {alignment:.1f}%
    - Overall Compliance Score: {score}
- **Autonomy Rate**: {auto_rate:.1f}%
- **AI Performance (Automated)**:
    - Average TSR: {tsr:.1f}%
    - Total Sessions Analyzed: {sessions}
"""

# Replace existing metrics section or append if not found
if "## Metrics" in content:
    # Match from header to next header or end
    new_content = re.sub(r"## Metrics \(Snapshot\).*?(?=\n## |\Z)", metrics_section.strip() + "\n", content, flags=re.DOTALL)
else:
    new_content = content.strip() + "\n\n" + metrics_section

with open('$STATE_FILE', 'w') as f:
    f.write(new_content)
EOF

# Update dashboards and METRICS.md
python3 .ops/scripts/generate_dashboard.py
python3 .ops/scripts/update_metrics_markdown.py

echo "project_state.md and dashboards updated with latest metrics."
