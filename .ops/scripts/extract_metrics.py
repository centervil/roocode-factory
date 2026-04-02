#!/usr/bin/env python3
import sys
import re
import os
import json
from datetime import datetime

# Current tool names used in the project
READ_TOOLS = [
    'read_file', 'list_directory', 'grep_search', 'glob', 'list_pages', 'take_snapshot', 
    'list_network_requests', 'get_network_request', 'list_console_messages', 'get_console_message'
]
WRITE_TOOLS = [
    'write_file', 'replace', 'run_shell_command', 'click', 'type_text', 'fill', 'fill_form', 
    'drag', 'hover', 'press_key', 'upload_file', 'handle_dialog', 'navigate_page', 'new_page'
]

def parse_log(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    filename = os.path.basename(file_path)
    timestamp_str = "unknown"
    mode = "unknown"
    match = re.match(r'(\d{4}-\d{2}-\d{2}_\d{6})_(\w+)\.log|(\d{8}_\d{6})_(\w+)\.log', filename)
    if match:
        ts_raw = match.group(1) or match.group(3)
        mode = match.group(2) or match.group(4)
        try:
            if '-' in ts_raw:
                timestamp_str = datetime.strptime(ts_raw, '%Y-%m-%d_%H%M%S').isoformat() + "Z"
            else:
                timestamp_str = datetime.strptime(ts_raw, '%Y%m%d_%H%M%S').isoformat() + "Z"
        except ValueError:
            pass

    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Turn count: Look for reasoning blocks or user messages
    # In RAW logs, turns are often delimited by specific patterns.
    # We use [reasoning] or "Turn:" if available, or just general structure.
    turn_count = len(re.findall(r'\[reasoning\]', content))
    if turn_count == 0:
        # Fallback for logs without [reasoning] tag
        turn_count = content.count('--- User Message ---') + 1

    # Tool requests: Capture tool name from [Tool Request]
    tool_requests = re.findall(r'\[Tool Request\]\s+(\w+)', content)
    # Command requests: Capture from [command request]
    command_requests = re.findall(r'\[command request\]', content)
    total_tool_calls = len(tool_requests) + len(command_requests)

    # Errors
    error_patterns = [
        r'shell execution error:',
        r'\[Tool Result\].*?Error:',
        r'\[CLI\] Error:',
        r'\[ExecaTerminalProcess#run\].*?failed',
        r'Exit Code: [1-9]\d*'
    ]
    tool_errors = 0
    for pattern in error_patterns:
        tool_errors += len(re.findall(pattern, content, re.DOTALL | re.IGNORECASE))

    # TSR Calculation
    tsr = 1.0
    if total_tool_calls > 0:
        tsr = max(0.0, (total_tool_calls - tool_errors) / total_tool_calls)
    elif tool_errors > 0:
        tsr = 0.0

    # Read/Write Analysis
    read_count = len([t for t in tool_requests if t in READ_TOOLS]) + len(command_requests)
    write_count = len([t for t in tool_requests if t in WRITE_TOOLS])
    
    # Heuristic for R/W: Most command requests are "read" like cat, ls, gh list, etc.
    # But some might be "write". For simplicity, we count them as "read" unless specified.
    
    rw_ratio = 1.0
    if write_count > 0:
        rw_ratio = read_count / write_count
    else:
        rw_ratio = float(read_count) if read_count > 0 else 1.0

    # --- Integrity Calculation ---
    protocol_fidelity = round(tsr * 100, 1)
    
    # Efficiency: tool calls per turn. Ideal is 2-4.
    efficiency = 0
    if turn_count > 0:
        tool_per_turn = total_tool_calls / turn_count
        # Normalized score: 3 tools/turn = 100%
        efficiency = min(100.0, (tool_per_turn / 3.0) * 100.0)
    
    behavioral_alignment = round(efficiency, 1) if efficiency > 0 else 50.0 # Default to 50 if data is thin
    
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
