#!/bin/bash
# Wrapper script for Roo Code CLI (roo) to capture RAW logs for auditing.

set -e

# Configuration
RAW_LOG_DIR="/home/coder/project/.ops/audit_logs/raw"
ROO_BIN="/home/coder/.local/bin/roo"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Ensure log directory exists
mkdir -p "$RAW_LOG_DIR"

# Parse arguments
MODE="code"
PROMPT=""
# Simple argument parsing (could be improved)
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --mode) MODE="$2"; shift ;;
        --print) PROMPT="$2"; shift ;;
        *) PROMPT="$1" ;; # Default to prompt if not a recognized flag
    esac
    shift
done

LOG_FILE="$RAW_LOG_DIR/${TIMESTAMP}_${MODE}.log"

# Load environment variables if .env exists
if [ -f "/home/coder/project/.env" ]; then
    # Filter out comments and empty lines
    export $(grep -v '^#' /home/coder/project/.env | xargs)
fi

# Use ROO_MODEL from .env if available
MODEL="${ROO_MODEL:-gemini-2.0-flash-001}"

echo "--- [ROO WRAPPER] Starting Roo Code CLI (Mode: $MODE, Model: $MODEL) ---"
echo "--- [ROO WRAPPER] Logging to $LOG_FILE ---"

# Execute roo and capture stdout/stderr to log file while showing it in terminal
"$ROO_BIN" --mode "$MODE" --model "$MODEL" --print "$PROMPT" 2>&1 | tee "$LOG_FILE"

EXIT_CODE=${PIPESTATUS[0]}

echo "--- [ROO WRAPPER] Roo Code CLI finished with exit code $EXIT_CODE ---"

# --- Automation Pipeline: Metrics Extraction & Aggregation ---
echo "--- [ROO WRAPPER] Starting metrics analysis for $LOG_FILE ---"

EXTRACT_SCRIPT="/home/coder/project/.ops/scripts/extract_metrics.py"
AGGREGATE_SCRIPT="/home/coder/project/.ops/scripts/aggregate_metrics.py"
MD_UPDATE_SCRIPT="/home/coder/project/.ops/scripts/update_metrics_markdown.py"
STATE_UPDATE_SCRIPT="/home/coder/project/.ops/scripts/update_state_metrics.sh"

if [ -f "$EXTRACT_SCRIPT" ]; then
    METRICS_JSON=$("$EXTRACT_SCRIPT" "$LOG_FILE")
    if [ $? -eq 0 ] && [ -n "$METRICS_JSON" ]; then
        if [ -f "$AGGREGATE_SCRIPT" ]; then
            python3 "$AGGREGATE_SCRIPT" "$METRICS_JSON"
        fi
    fi
fi

if [ -f "$MD_UPDATE_SCRIPT" ]; then
    python3 "$MD_UPDATE_SCRIPT"
fi

if [ -f "$STATE_UPDATE_SCRIPT" ]; then
    bash "$STATE_UPDATE_SCRIPT"
fi

echo "--- [ROO WRAPPER] Metrics updated successfully ---"

exit $EXIT_CODE
