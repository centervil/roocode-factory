#!/bin/bash
# Script to automate Roo Code CLI installation and setup

set -e

ROO_BIN_DIR="$HOME/.local/bin"
ROO_BIN="$ROO_BIN_DIR/roo"

echo "Checking for Roo Code CLI..."

if ! command -v "$ROO_BIN" &> /dev/null; then
    echo "Roo Code CLI not found. Installing..."
    curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
else
    echo "Roo Code CLI is already installed at $ROO_BIN."
fi

# Ensure $HOME/.local/bin is in PATH for the current session and future ones
if [[ ":$PATH:" != *":$ROO_BIN_DIR:"* ]]; then
    echo "Adding $ROO_BIN_DIR to PATH..."
    export PATH="$ROO_BIN_DIR:$PATH"
    
    # Update shell profile if needed (for user's convenience)
    PROFILE_FILE=""
    if [ -f "$HOME/.bashrc" ]; then
        PROFILE_FILE="$HOME/.bashrc"
    elif [ -f "$HOME/.zshrc" ]; then
        PROFILE_FILE="$HOME/.zshrc"
    fi
    
    if [ -n "$PROFILE_FILE" ]; then
        if ! grep -q "$ROO_BIN_DIR" "$PROFILE_FILE"; then
            echo "export PATH="$ROO_BIN_DIR:\$PATH"" >> "$PROFILE_FILE"
            echo "Updated $PROFILE_FILE."
        fi
    fi
fi

echo "Verifying installation..."
"$ROO_BIN" --version
echo "Roo Code CLI setup complete."
