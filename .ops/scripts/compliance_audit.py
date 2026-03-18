#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import re

def call_llm(prompt):
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return {"error": "OPENROUTER_API_KEY not found"}

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/centervil/roocode-factory", # Optional
    }
    
    data = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {"role": "system", "content": "You are a professional auditor for AI agent behavioral compliance. Your task is to compare raw execution logs with defined rules (Must/Must Not/Forbidden) and determine if the agent complied with the design intent."},
            {"role": "user", "content": prompt}
        ],
        "response_format": { "type": "json_object" }
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return json.loads(res_data["choices"][0]["message"]["content"])
    except Exception as e:
        return {"error": str(e)}

def extract_mode_from_filename(filename):
    # Example: 20260309_223707_code.log -> code
    match = re.search(r'_([a-z]+)\.log$', filename)
    if match:
        return match.group(1)
    return "unknown"

def main():
    if len(sys.argv) < 2:
        print("Usage: compliance_audit.py <raw_log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    if not os.path.exists(log_file):
        print(f"File not found: {log_file}")
        sys.exit(1)

    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()

    # Get rules
    script_dir = os.path.dirname(os.path.abspath(__file__))
    extractor_path = os.path.join(script_dir, "extract_rules.py")
    
    import subprocess
    result = subprocess.run([sys.executable, extractor_path], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error extracting rules")
        sys.exit(1)
    
    all_rules = json.loads(result.stdout)
    mode = extract_mode_from_filename(log_file)
    
    relevant_rules = all_rules.get(mode, [])
    # Also include general rules or skills if needed
    # For now, focus on the mode rules
    
    prompt = f"""
Audit the following Roo Code execution log for the mode '{mode}'.
Check if the agent followed these rules:

RULES:
{json.dumps(relevant_rules, indent=2, ensure_ascii=False)}

RAW LOG:
---START LOG---
{log_content[-10000:]} # Last 10000 chars to avoid context limit
---END LOG---

Instructions:
1. Evaluate compliance score (0-100).
2. Identify any violations.
3. Provide evidence (quotes from the log).
4. Output JSON format:
{{
  "compliance_score": number,
  "summary": "...",
  "violations": [
    {{
      "rule": "...",
      "severity": "high/medium/low",
      "reason": "...",
      "evidence": "..."
    }}
  ]
}}
"""

    audit_result = call_llm(prompt)
    
    output = {
        "log_file": os.path.basename(log_file),
        "mode": mode,
        "audit": audit_result
    }
    
    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
