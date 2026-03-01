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
