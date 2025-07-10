#!/bin/bash
# entrypoint.sh

# Wait for Prometheus /status endpoint
until curl -sSf http://prometheus-server:9090/-/ready > /dev/null; do
  echo "Waiting for Prometheus..."
  sleep 2
done

# Wait for Loki
until curl -sSf http://loki-server:3100/ready > /dev/null; do
  echo "Waiting for Loki..."
  sleep 2
done

# Wait for Blackbox Exporter (basic check)
until curl -sSf http://blackbox-exporter:9115 > /dev/null; do
  echo "Waiting for Blackbox Exporter..."
  sleep 2
done

# Wait for Grafana
until curl -sSf http://grafana-server:3000/api/health; do
  echo "Waiting for Grafana..."
  sleep 2
done


# Now run the Flask app
python app.py
