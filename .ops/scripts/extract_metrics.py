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
    # Parse timestamp and mode from filename: YYYYMMDD_HHMMSS_MODE.log
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

    # Turn Count (TC): Count of [reasoning] sections (starts of turns)
    # We filter out empty or very short reasoning if they are duplicates, 
    # but usually one [reasoning] = one turn.
    turn_count = len(re.findall(r'\[reasoning\]', content))

    # Tool calls: count [Tool Request] [toolName]
    # Example: [Tool Request] readFile
    tool_requests = re.findall(r'\[Tool Request\]\s+(\w+)', content)
    
    # [command request] is also a tool call in some versions/modes
    command_requests = re.findall(r'\[command request\]', content)
    
    total_tool_calls = len(tool_requests) + len(command_requests)

    # Tool Errors:
    # 1. "[ExecaTerminalProcess#run] shell execution error:"
    # 2. "[Tool Result] Error:"
    # 3. "[CLI] Error:" (usually means prompt failed or something fatal)
    error_patterns = [
        r'shell execution error:',
        r'\[Tool Result\].*?Error:',
        r'\[CLI\] Error:',
        r'\[ExecaTerminalProcess#run\].*?failed'
    ]
    tool_errors = 0
    for pattern in error_patterns:
        tool_errors += len(re.findall(pattern, content, re.DOTALL | re.IGNORECASE))

    # Success rate
    tsr = 1.0
    if total_tool_calls > 0:
        # Avoid negative TSR if errors are double counted, clamp at 0
        tsr = max(0.0, (total_tool_calls - tool_errors) / total_tool_calls)
    elif tool_errors > 0:
        # If no tool calls but errors, TSR is 0
        tsr = 0.0

    # Read vs Write categorization
    read_tools = [
        'readFile', 'read_file', 
        'listFiles', 'list_files', 
        'listCodeDefinition', 'list_code_definition',
        'searchFiles', 'search_files', 
        'read_command_output', 'executeCommand' # executeCommand is often used for 'ls', 'cat', etc.
    ]
    write_tools = [
        'newFileCreated', 'write_to_file',
        'applyDiff', 'apply_diff', 
        'editFile', 'insert_content',
        'update_todo_list', 'delete_file'
    ]
    
    read_count = len([t for t in tool_requests if t in read_tools]) + len(command_requests)
    write_count = len([t for t in tool_requests if t in write_tools])
    
    rw_ratio = 0.0
    if write_count > 0:
        rw_ratio = read_count / write_count
    else:
        rw_ratio = float(read_count)

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
        "read_to_write_ratio": round(rw_ratio, 2)
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_metrics.py <log_file>")
        sys.exit(1)

    metrics = parse_log(sys.argv[1])
    if metrics:
        print(json.dumps(metrics, indent=2))
