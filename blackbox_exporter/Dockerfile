FROM ubuntu:22.04

# Install dependencies
RUN apt update && apt install -y wget unzip curl

# Set working directory
WORKDIR /opt/blackbox

# Download and extract blackbox_exporter
RUN wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.24.0/blackbox_exporter-0.24.0.linux-amd64.tar.gz && \
    tar -xzf blackbox_exporter-0.24.0.linux-amd64.tar.gz --strip-components=1


# mount this config file as a volume while launching
# Copy config file into container
# COPY blackbox.yml /etc/blackbox_exporter/blackbox.yml

# Expose port
EXPOSE 9115

# Start blackbox_exporter with config
CMD ["./blackbox_exporter", "--config.file=/etc/blackbox_exporter/blackbox.yml"]
