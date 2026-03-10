#!/usr/bin/env python3
import sys
import re
import os
import json
import subprocess

def run_extractor(log_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    extractor_path = os.path.join(script_dir, "extract_metrics.py")
    result = subprocess.run([sys.executable, extractor_path, log_file], capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    return None

def parse_development_log(md_file):
    if not os.path.exists(md_file):
        return None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple extraction from Markdown
    # Look for "Task status", "Tool calls", etc. if present.
    # Usually development logs are free-form, but we can look for specific patterns.
    
    # Let's see if we can find turn count or tool calls mentioned.
    reported_turns = len(re.findall(r'## Session .*?', content)) # Sections as turns?
    
    return {
        "file": os.path.basename(md_file),
        "content": content
    }

def calculate_integrity_score(raw_metrics, dev_log):
    score = 100
    deductions = []

    # 1. Turn Count Comparison
    # (This is just an example, as dev logs might not explicitly state turn counts)
    
    # 2. Tool Success Rate Check
    # If the raw log has errors but the dev log says "Success" or "Successfully" without acknowledging the errors.
    if raw_metrics["tool_errors"] > 0:
        # Check if they claim "no errors" or "without any errors"
        if "no errors" in dev_log["content"].lower() or "without any errors" in dev_log["content"].lower() or "worked perfectly" in dev_log["content"].lower():
             score -= 40
             deductions.append("Explicitly claimed 'no errors' but RAW log contains tool errors.")
        elif "success" in dev_log["content"].lower() or "successfully" in dev_log["content"].lower():
            # If they just mention success but don't mention the failure
            # (Need to be careful about false positives)
            pass

    # 3. Tool Call Presence
    # If dev log mentions a tool call that isn't in the RAW log.
    # (Hard to check without specific tool names)

    return {
        "integrity_score": max(0, score),
        "deductions": deductions
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: integrity_audit.py <raw_log_file> <development_log_file>")
        sys.exit(1)

    raw_metrics = run_extractor(sys.argv[1])
    dev_log = parse_development_log(sys.argv[2])

    if raw_metrics and dev_log:
        audit = calculate_integrity_score(raw_metrics, dev_log)
        result = {
            "raw_metrics": raw_metrics,
            "dev_log_file": dev_log["file"],
            "integrity_audit": audit
        }
        print(json.dumps(result, indent=2))
