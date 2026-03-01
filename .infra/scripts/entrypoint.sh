#!/bin/bash

# Ensure /var/lib/tailscale is owned by root (as required by tailscaled)
# But since we use a named volume, it might have wrong permissions.
# sudo chown -R root:root /var/lib/tailscale

# Ensure code-server data directory is owned by coder
echo "Setting permissions for code-server data directory..."
sudo chown -R coder:coder /home/coder/.local/share/code-server

# Start tailscaled in background
echo "Starting tailscaled..."
sudo tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/run/tailscale/tailscaled.sock &

# Optional: if an auth key is provided, try to authenticate
if [ -n "$TAILSCALE_AUTH_KEY" ]; then
    echo "Authenticating Tailscale..."
    sudo tailscale up --authkey=$TAILSCALE_AUTH_KEY --hostname=roo-orchestrator --accept-routes
fi

# Start code-server
echo "Starting code-server..."
# Using exec to replace the shell process with code-server
exec code-server --bind-addr 0.0.0.0:8080 --auth password /home/coder/project
