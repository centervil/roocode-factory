FROM codercom/code-server:latest

USER root

# OS update and common tools
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    software-properties-common \
    sudo \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Install Tailscale
RUN curl -fsSL https://tailscale.com/install.sh | sh

# Install GitHub CLI
RUN type -p curl >/dev/null || (apt-get update && apt-get install curl -y) \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install gh -y

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Install Playwright dependencies
RUN npx playwright install-deps

# Switch back to coder user for NPM installs
USER coder

# Install Playwright browsers (in coder user space)
RUN npx playwright install

# Install playwright npm package globally and set NODE_PATH
USER root
RUN npm install -g playwright
ENV NODE_PATH=/usr/lib/node_modules
USER coder

# Create workspace directory
RUN mkdir -p /home/coder/project

WORKDIR /home/coder/project

# Copy entrypoint script
COPY --chown=coder:coder scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
