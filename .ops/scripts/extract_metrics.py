#!/usr/bin/env python3
import sys
import re
import os
import json
from datetime import datetime

def parse_log(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    filename = os.path.basename(file_path)
    timestamp_str = "unknown"
    mode = "unknown"
    match = re.match(r'(\d{8}_\d{6})_(\w+)\.log', filename)
    if match:
        ts_raw = match.group(1)
        mode = match.group(2)
        try:
            timestamp_str = datetime.strptime(ts_raw, '%Y%m%d_%H%M%S').isoformat() + "Z"
        except ValueError:
            pass

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    turn_count = len(re.findall(r'\[reasoning\]', content))
    tool_requests = re.findall(r'\[Tool Request\]\s+(\w+)', content)
    command_requests = re.findall(r'\[command request\]', content)
    total_tool_calls = len(tool_requests) + len(command_requests)

    error_patterns = [
        r'shell execution error:',
        r'\[Tool Result\].*?Error:',
        r'\[CLI\] Error:',
        r'\[ExecaTerminalProcess#run\].*?failed'
    ]
    tool_errors = 0
    for pattern in error_patterns:
        tool_errors += len(re.findall(pattern, content, re.DOTALL | re.IGNORECASE))

    tsr = 1.0
    if total_tool_calls > 0:
        tsr = max(0.0, (total_tool_calls - tool_errors) / total_tool_calls)
    elif tool_errors > 0:
        tsr = 0.0

    read_tools = ['readFile', 'read_file', 'listFiles', 'list_files', 'list_code_definition', 'search_files', 'executeCommand']
    write_tools = ['write_to_file', 'apply_diff', 'editFile', 'insert_content', 'update_todo_list', 'delete_file']
    
    read_count = len([t for t in tool_requests if t in read_tools]) + len(command_requests)
    write_count = len([t for t in tool_requests if t in write_tools])
    rw_ratio = read_count / write_count if write_count > 0 else float(read_count)

    # --- Heuristic Integrity Calculation ---
    # Protocol Fidelity: Based on balanced tool usage and TSR
    protocol_fidelity = round(tsr * 100, 1)
    
    # Behavioral Alignment: Based on Turn Count vs Work Done (Efficiency)
    # If a lot of turns but little work, score decreases.
    efficiency = 100
    if turn_count > 0:
        efficiency = min(100.0, (total_tool_calls / (turn_count * 2.0)) * 100.0)
    behavioral_alignment = round(efficiency, 1)
    
    # Overall Score (Integrity)
    integrity_score = round((protocol_fidelity + behavioral_alignment) / 2.0, 1)

    return {
        "session_id": filename.replace(".log", ""),
        "timestamp": timestamp_str,
        "mode": mode,
        "turn_count": turn_count,
        "total_tool_calls": total_tool_calls,
        "tool_errors": tool_errors,
        "tool_success_rate": round(tsr, 2),
        "read_count": read_count,
        "write_count": write_count,
        "read_to_write_ratio": round(rw_ratio, 2),
        "integrity": {
            "score": integrity_score,
            "protocol_fidelity": protocol_fidelity,
            "behavioral_alignment": behavioral_alignment
        }
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_metrics.py <log_file>")
        sys.exit(1)

    metrics = parse_log(sys.argv[1])
    if metrics:
        print(json.dumps(metrics, indent=2))
