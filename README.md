# Read Detailed Blog:
https://sayantansamanta098.medium.com/flask-server-monitoring-with-custom-prometheus-grafana-and-loki-docker-environment-239356759f6e


## Dashboard will Look like this.
<img width="1100" height="618" alt="image" src="https://github.com/user-attachments/assets/4b178d74-0817-49a0-ab91-f2edc992a6c5" />

## Project Architecture
```
+--------------------------+
| Traffic Simulator        |
| (simulate_traffic.sh)    |
+------------+-------------+
             |
             v
+--------------------------+           +----------------------------+
|   Flask Microservice     |  ----->   |     Prometheus             |
|   (app.py w/ custom      |  <--scrape-- metrics endpoint          |
|   metrics)               |           +------------+---------------+
+------------+-------------+                        |
             |                                      |
             v                                      v
   Probed via Blackbox Exporter         +-------------------------+
   for availability checks              |    Alertmanager         |
                                        |    (email alerts)       |
                                        +-------------------------+
                                                 |
                                                 v
                                        +--------------------------+
                                        |     Email (SMTP)         |
                                        +--------------------------+

             +------------------------------------+
             |             Loki                  |
             |     (collects logs from Flask)    |
             +------------------+----------------+
                                |      
                                v
                         +-------------+
                         |   Grafana   |
                         | Dashboards  |
                         |             |
                         | - Data Source: Prometheus (metrics)
                         | - Data Source: Loki (logs)
                         +-------------+

```
## Directory Structure

```
Monitoring-Project-01/
├── alertmanager/                             # ⚠️ Handles alert delivery (email, etc.)
│   ├── alertmanager.yml                      # Main config for alert routing & receivers
│   ├── alertmanager.yml.template             # Template version for customization
│   ├── docker-compose.yml                    # Compose file to run Alertmanager separately
│   └── Dockerfile                            # Dockerfile to build Alertmanager container
├── app-README.md                             # 📘 Project overview or documentation draft
├── blackbox_exporter/                        # 🔍 Performs external probe checks (HTTP, TCP)
│   ├── blackbox.yml                          # Config defining how to probe targets
│   ├── docker-compose.yml                    # Standalone compose for testing blackbox
│   └── Dockerfile                            # Dockerfile to build blackbox container
├── docker-compose.yml                        # 🔗 Central compose file to launch all services
├── grafana/                                  # 📊 Visualizes metrics (Prometheus) and logs (Loki)
│   ├── cmd.txt                               # Dev/testing reference commands for Grafana
│   ├── docker-compose.yml                    # Standalone Grafana runner (optional)
│   └── Dockerfile                            # Dockerfile for Grafana image
├── loki/                                     # 📄 Centralized log aggregation service
│   ├── docker-compose.yml                    # Standalone Loki compose file
│   ├── Dockerfile                            # Loki container definition
│   └── manual-script.sh                      # Manual script to test Loki setup/log scraping
├── microservice/                             # 🧩 Flask app exposing custom metrics & logs
│   ├── app.py                                # Flask app with `/`, `/slow`, `/metrics`, `/health`
│   ├── app.py.old                            # Backup of an older app version
│   ├── command.txt                           # Dev notes or curl commands
│   ├── docker-compose.yml                    # Isolated runner (optional)
│   ├── Dockerfile                            # Flask app Dockerfile
│   ├── entrypoint.sh                         # Wait-for script to delay startup until deps are ready
│   ├── requirements.txt                      # Python dependencies for the Flask app
│   └── util.py                               # Utility functions used in app.py
├── prometheus/                               # 📈 Core metrics collection & alert evaluation
│   ├── alert_rules.yml                       # Alerting rules (latency, container down, probe fail)
│   ├── command.txt                           # Notes or sample CLI commands
│   ├── docker-compose.yml                    # Standalone Prometheus runner (optional)
│   ├── Dockerfile                            # Prometheus image with custom config
│   ├── prometheus.yml                        # Scrape configs + alerting setup
│   └── prometheus.yml.template               # Editable version of the main config
└── traffic_simulator/                        # 🧪 Load generator to simulate traffic on endpoints
    ├── script.sh                             # Orchestrator: launches multiple simulate_traffic loops
    └── simulate_traffic.sh                   # Randomly hits `/` or `/slow` to mimic real usage

```
