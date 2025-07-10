#!/bin/bash

# entrypoint.sh
./wait-for-it.sh prometheus-server:9090 -- 
./wait-for-it.sh loki-server:3100 -- 
./wait-for-it.sh blackbox-exporter:9115 -- 
python app.py