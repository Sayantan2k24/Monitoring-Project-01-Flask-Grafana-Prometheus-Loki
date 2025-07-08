FROM ubuntu:22.04

# Install required tools
RUN apt-get update && apt-get install -y wget curl unzip ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV LOKI_VERSION=2.9.2

# Create a user and working directories
RUN useradd --no-create-home --shell /bin/false loki && \
    mkdir -p /etc/loki /data/loki

# Download Loki binary and move to /usr/local/bin
RUN wget https://github.com/grafana/loki/releases/download/v${LOKI_VERSION}/loki-linux-amd64.zip && \
    unzip loki-linux-amd64.zip && \
    mv loki-linux-amd64 /usr/local/bin/loki && \
    chmod +x /usr/local/bin/loki && \
    rm loki-linux-amd64.zip

# Copy default config (you can override this via volume)
COPY loki-config.yaml /etc/loki/config.yaml

# Set ownership
RUN chown -R loki:loki /etc/loki /data/loki

# Expose Loki port
EXPOSE 3100

# Run as non-root
USER loki

# Start Loki
ENTRYPOINT ["/usr/local/bin/loki", "-config.file=/etc/loki/config.yaml"]
