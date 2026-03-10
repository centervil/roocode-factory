#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime

METRICS_FILE = ".ops/audit_logs/metrics.json"

def aggregate(new_metrics_json):
    if not os.path.exists(METRICS_FILE):
        data = {
            "last_updated": "",
            "summary": {
                "total_sessions": 0,
                "avg_tsr": 0.0,
                "total_turns": 0,
                "total_tool_calls": 0,
                "avg_rw_ratio": 0.0
            },
            "metrics": {
                "compliance": {"score": 0, "protocol_fidelity": 0, "behavioral_alignment": 0, "sessions_analyzed": 0},
                "autonomy": {"total_actions": 0, "interventions": 0, "rate": 0}
            },
            "sessions": []
        }
    else:
        with open(METRICS_FILE, 'r') as f:
            data = json.load(f)

    new_metrics = json.loads(new_metrics_json)
    
    # Check for duplicate session_id
    if any(s.get('session_id') == new_metrics['session_id'] for s in data.get('sessions', [])):
        print(f"Session {new_metrics['session_id']} already aggregated. Skipping.")
        return

    # Add to sessions list
    if 'sessions' not in data:
        data['sessions'] = []
    data['sessions'].append(new_metrics)

    # Keep only last 50 sessions to avoid file bloating
    if len(data['sessions']) > 50:
        data['sessions'] = data['sessions'][-50:]

    # Update summary
    sessions = data['sessions']
    count = len(sessions)
    total_tsr = sum(s.get('tool_success_rate', 0) for s in sessions)
    total_turns = sum(s.get('turn_count', 0) for s in sessions)
    total_tool_calls = sum(s.get('total_tool_calls', 0) for s in sessions)
    total_rw_ratio = sum(s.get('read_to_write_ratio', 0) for s in sessions)

    data['summary'] = {
        "total_sessions": count,
        "avg_tsr": round(total_tsr / count, 2) if count > 0 else 0,
        "total_turns": total_turns,
        "total_tool_calls": total_tool_calls,
        "avg_rw_ratio": round(total_rw_ratio / count, 2) if count > 0 else 0
    }
    
    data['last_updated'] = datetime.utcnow().isoformat() + "Z"

    with open(METRICS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Successfully aggregated session {new_metrics['session_id']}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: aggregate_metrics.py '<json_string>'")
        sys.exit(1)
    
    aggregate(sys.argv[1])
