FROM ubuntu:22.04

# Set working directory
WORKDIR /opt/alertmanager

# Install wget, curl, and other required tools
RUN apt-get update && \
    apt-get install -y wget curl ca-certificates && \
    apt-get clean

# Set Alertmanager version
ENV ALERTMANAGER_VERSION=0.27.0

# Download and extract Alertmanager
RUN wget https://github.com/prometheus/alertmanager/releases/download/v${ALERTMANAGER_VERSION}/alertmanager-${ALERTMANAGER_VERSION}.linux-amd64.tar.gz && \
    tar -xvf alertmanager-${ALERTMANAGER_VERSION}.linux-amd64.tar.gz --strip-components=1 && \
    rm alertmanager-${ALERTMANAGER_VERSION}.linux-amd64.tar.gz

# Expose the Alertmanager port
EXPOSE 9093

# Copy the configuration file (You must mount this in Docker Compose)
# COPY alertmanager.yml /etc/alertmanager/alertmanager.yml

# Run Alertmanager
CMD ["./alertmanager", "--config.file=/etc/alertmanager/alertmanager.yml"]
