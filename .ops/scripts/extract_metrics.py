#!/usr/bin/env python3
import sys
import re
import os
import json

def parse_log(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Turn Count (TC): Count of [reasoning] sections
    # Each turn typically starts with [reasoning] or [assistant]
    # We'll use [reasoning] as a proxy for a turn start.
    turn_count = len(re.findall(r'\[reasoning\]', content))

    # Tool calls: count [Tool Request] and [command request]
    tool_requests = re.findall(r'\[Tool Request\]\s+(\w+)', content)
    command_requests = re.findall(r'\[command request\]', content)
    
    total_tool_calls = len(tool_requests) + len(command_requests)

    # Tool Errors: count "shell execution error:" or "Error:"
    # This might be simplistic.
    tool_errors = len(re.findall(r'shell execution error:', content)) + len(re.findall(r'\[Tool Result\].*?Error:', content, re.DOTALL | re.IGNORECASE))

    # Success rate
    tsr = 1.0
    if total_tool_calls > 0:
        tsr = (total_tool_calls - tool_errors) / total_tool_calls

    # Read vs Write
    # Categorize tool_requests
    read_tools = ['readFile', 'listFiles', 'listCodeDefinition', 'searchFiles', 'read_file', 'list_files', 'search_files', 'read_command_output']
    write_tools = ['newFileCreated', 'applyDiff', 'editFile', 'write_to_file', 'apply_diff', 'update_todo_list']
    
    read_count = len([t for t in tool_requests if t in read_tools]) + len(command_requests) # command_requests are usually for investigation in this context
    write_count = len([t for t in tool_requests if t in write_tools])
    
    # Actually, command_requests can be writes too.
    # We'll refine this later. For now, simplistic.
    rw_ratio = 0.0
    if write_count > 0:
        rw_ratio = read_count / write_count
    else:
        rw_ratio = float(read_count) # Infinite if no writes but some reads

    return {
        "file": os.path.basename(file_path),
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
