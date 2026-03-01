#!/bin/bash

# Modify coder user UID/GID if PUID/PGID are provided
if [ -n "$PUID" ]; then
    echo "Updating coder UID to $PUID"
    sudo usermod -u "$PUID" coder
fi
if [ -n "$PGID" ]; then
    echo "Updating coder GID to $PGID"
    sudo groupmod -g "$PGID" coder
fi

# Ensure /var/lib/tailscale is owned by root (as required by tailscaled)
# But since we use a named volume, it might have wrong permissions.
# sudo chown -R root:root /var/lib/tailscale

# Ensure code-server, gh, and gemini config directories are owned by coder
echo "Setting permissions for config directories..."
sudo chown -R coder:coder /home/coder/.local/share/code-server
sudo chown -R coder:coder /home/coder/.config
sudo chown -R coder:coder /home/coder/.gemini
sudo chown -R coder:coder /home/coder/project

# Start sshd
echo "Starting sshd..."
sudo service ssh start

# Start tailscaled in background
echo "Starting tailscaled..."
sudo tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/run/tailscale/tailscaled.sock &

# Optional: if an auth key is provided, try to authenticate
if [ -n "$TAILSCALE_AUTH_KEY" ]; then
    echo "Authenticating Tailscale..."
    sudo tailscale up --authkey=$TAILSCALE_AUTH_KEY --hostname=roo-orchestrator --accept-routes --ssh
fi

# Start code-server
echo "Starting code-server..."
# Using exec to replace the shell process with code-server
exec code-server --bind-addr 0.0.0.0:8080 --auth password /home/coder/project
