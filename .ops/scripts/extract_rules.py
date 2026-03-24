#!/usr/bin/env python3
import os
import re
import json
import glob

def extract_rules_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    rules = []
    # Section patterns that usually contain rules/constraints
    target_sections = [
        r'##\s*(?:3\.\s*)?特殊な制約',
        r'##\s*Forbidden Actions',
        r'##\s*Instructions',
        r'##\s*Operational Guidelines',
        r'##\s*Responsibilities',
        r'##\s*Non-Responsibilities'
    ]

    for section_pattern in target_sections:
        # Find the start of the section
        match = re.search(section_pattern, content, re.IGNORECASE)
        if match:
            start_pos = match.end()
            # Find the end of the section (next header or end of file)
            end_match = re.search(r'\n##\s+', content[start_pos:])
            if end_match:
                section_content = content[start_pos:start_pos + end_match.start()].strip()
            else:
                section_content = content[start_pos:].strip()
            
            # Extract bullet points or sentences as individual rules
            lines = section_content.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('- ') or line.startswith('* ') or re.match(r'\d+\.', line):
                    rules.append({
                        "source_section": re.sub(r'##\s*', '', match.group()),
                        "rule": re.sub(r'^[-*]\s+|\d+\.\s*', '', line)
                    })
                elif line:
                    # Keep non-bullet lines if they look like rules
                    rules.append({
                        "source_section": re.sub(r'##\s*', '', match.group()),
                        "rule": line
                    })

    return rules

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    rules_data = {}

    # 1. Roo Rules
    roo_rules_dir = os.path.join(base_dir, ".roo")
    for rule_file in glob.glob(os.path.join(roo_rules_dir, "rules-*", "*.md")):
        mode_name = os.path.basename(os.path.dirname(rule_file)).replace("rules-", "")
        if mode_name not in rules_data:
            rules_data[mode_name] = []
        rules_data[mode_name].extend(extract_rules_from_file(rule_file))

    # 2. Gemini Skills
    gemini_skills_dir = os.path.join(base_dir, ".gemini", "skills")
    for skill_file in glob.glob(os.path.join(gemini_skills_dir, "*", "*.md")):
        skill_name = os.path.basename(os.path.dirname(skill_file))
        if skill_name not in rules_data:
            rules_data[skill_name] = []
        rules_data[skill_name].extend(extract_rules_from_file(skill_file))

    print(json.dumps(rules_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
