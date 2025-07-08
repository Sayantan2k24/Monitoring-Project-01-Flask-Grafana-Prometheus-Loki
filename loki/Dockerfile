# ✅ Use official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables
ENV LOKI_DIR=/opt/loki \
    LOKI_CONFIG=/opt/loki/loki-config.yaml

# Create working directory
WORKDIR /opt/loki

# 🧰 Install necessary packages: curl, wget, unzip
RUN apt update && \
    apt install -y curl wget unzip && \
    rm -rf /var/lib/apt/lists/*

# Fetch latest Loki version
RUN LOKI_VERSION=$(curl -s "https://api.github.com/repos/grafana/loki/releases/latest" | grep -Po '"tag_name": "v\K[0-9.]+' || echo "2.9.2") && \
    wget -qO loki.zip "https://github.com/grafana/loki/releases/download/v${LOKI_VERSION}/loki-linux-amd64.zip" && \
    unzip -o loki.zip && \
    mv loki-linux-amd64 loki && \
    chmod +x loki && \
    ln -s /opt/loki/loki /usr/local/bin/loki && \
    # download the loki config file
    wget -qO loki-config.yaml "https://raw.githubusercontent.com/grafana/loki/v${LOKI_VERSION}/cmd/loki/loki-local-config.yaml" && \
    # Remove deprecated config key (may cause crash on newer versions)
    sed -i '/enable_multi_variant_queries/d' loki-config.yaml && \
    rm -f loki.zip

# Expose Loki port
EXPOSE 3100

# Start Loki with config
CMD ["loki", "-config.file=/opt/loki/loki-config.yaml"]
