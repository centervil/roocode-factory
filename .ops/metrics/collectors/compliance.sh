#!/bin/bash

# Dynamic Compliance Analyzer
# Analyzes session logs in .ops/audit_logs/sessions/ for Protocol Fidelity and Behavioral Alignment.

SESSIONS_DIR=".ops/audit_logs/sessions"
TOTAL_SESSIONS=$(ls $SESSIONS_DIR/*.json 2>/dev/null | wc -l)

if [ "$TOTAL_SESSIONS" -eq 0 ]; then
    echo '{"compliance": {"protocol_fidelity": 0, "behavioral_alignment": 0, "score": 0}}'
    exit 0
fi

# Function to format float with leading zero
format_float() {
    printf "%.2f" "$1" | sed 's/^\./0./'
}

# 1. Protocol Fidelity: Count sessions where protocol_fidelity is true
FIDELITY_COUNT=$(grep -l '"protocol_fidelity": true' $SESSIONS_DIR/*.json 2>/dev/null | wc -l)
FIDELITY_RATE=$(echo "scale=2; $FIDELITY_COUNT / $TOTAL_SESSIONS" | bc | sed 's/^\./0./')

# 2. Behavioral Alignment: Count sessions with NO critical gap keywords
NON_ALIGNED_COUNT=$(grep -ilE "violation|unexpected|diverged|failure" $SESSIONS_DIR/*.json 2>/dev/null | wc -l)
ALIGNED_COUNT=$((TOTAL_SESSIONS - NON_ALIGNED_COUNT))
ALIGNMENT_RATE=$(echo "scale=2; $ALIGNED_COUNT / $TOTAL_SESSIONS" | bc | sed 's/^\./0./')

# Calculate overall compliance score (average of the two, 0-100)
SCORE=$(echo "scale=2; ($FIDELITY_RATE + $ALIGNMENT_RATE) * 50" | bc | sed 's/^\./0./')

cat <<JSON
{
  "compliance": {
    "protocol_fidelity": $FIDELITY_RATE,
    "behavioral_alignment": $ALIGNMENT_RATE,
    "score": $SCORE,
    "sessions_analyzed": $TOTAL_SESSIONS
  }
}
JSON
