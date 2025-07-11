# traffic_simulator/Dockerfile

FROM ubuntu:22.04

LABEL maintainer="sayantan2k21"

# Install curl and bash (if needed)
RUN apt-get update && \
    apt-get install -y curl bash && \
    apt-get clean

# Set workdir
WORKDIR /app

# Copy scripts
COPY simulate_traffic.sh script.sh ./

# Make scripts executable
RUN chmod +x simulate_traffic.sh script.sh

# Set entrypoint (runs the load script)
CMD ["./script.sh"]
