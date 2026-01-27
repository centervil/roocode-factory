#!/bin/bash
# Simple git sync script

echo "Checking git status..."
git status

echo "Fetching from origin..."
git fetch origin

CURRENT_BRANCH=$(git branch --show-current)

echo "Pulling changes for $CURRENT_BRANCH..."
git pull origin "$CURRENT_BRANCH"

echo "Sync complete."
