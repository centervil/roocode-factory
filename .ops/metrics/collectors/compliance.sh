#!/bin/bash

SCORE=0

# Check for audit.toml
if [ -f ".gemini/commands/audit.toml" ]; then
    SCORE=$((SCORE + 50))
fi

# Check for README.md
if [ -f ".roo/README.md" ]; then
    SCORE=$((SCORE + 50))
fi

cat <<JSON
{
  "compliance": {
    "score": $SCORE,
    "max_score": 100
  }
}
JSON
