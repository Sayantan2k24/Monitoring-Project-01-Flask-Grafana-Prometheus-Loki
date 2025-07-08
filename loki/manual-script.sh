#!/bin/bash
# ubuntu:22.04 tested
apt update
apt install -y curl wget unzip

LOKI_VERSION=$(curl -s "https://api.github.com/repos/grafana/loki/releases/latest" | grep -Po '"tag_name": "v\K[0-9.]+' || echo "2.9.2")

mkdir -p /opt/loki
wget -qO /opt/loki/loki.zip "https://github.com/grafana/loki/releases/download/v${LOKI_VERSION}/loki-linux-amd64.zip"
unzip -o /opt/loki/loki.zip -d /opt/loki/
mv /opt/loki/loki-linux-amd64 /opt/loki/loki
chmod +x /opt/loki/loki
ln -s /opt/loki/loki /usr/local/bin/loki

wget -qO /opt/loki/loki-config.yaml "https://raw.githubusercontent.com/grafana/loki/v${LOKI_VERSION}/cmd/loki/loki-local-config.yaml"

sed -i '/enable_multi_variant_queries/d' /opt/loki/loki-config.yaml

loki -config.file=/opt/loki/loki-config.yaml
