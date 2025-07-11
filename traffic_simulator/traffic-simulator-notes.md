### 📄 `traffic-simulator-notes.md`

````markdown
# 🧪 Traffic Simulator (script.sh + simulate_traffic.sh)

# 🧪 Traffic Simulator: Why It’s Kept Separate

## 📌 Purpose of the Traffic Simulator

The `traffic_simulator` component is a **dedicated tool to generate artificial traffic** (HTTP requests) to the Flask microservice. It mimics real user behavior, hitting endpoints like `/` and `/slow` repeatedly, which helps in:

- Simulating realistic load
- Testing alert conditions (latency, availability)
- Visualizing metrics and logs in Grafana
- Validating Prometheus scraping and Alertmanager notifications

---

## 🔍 Why Is It Kept Separate from the Monitoring Stack?

### ✅ 1. Avoid Auto-Triggering During Startup
We want **Prometheus, Loki, Alertmanager, and Grafana to fully initialize** before traffic is simulated. Starting the simulator too early may:
- Cause misleading alerts (e.g., service down when it hasn’t even started)
- Populate dashboards with partial or incorrect data
- Stress the app before it's ready

> 🧠 Monitoring should observe a stable environment, not race with the simulator.

---

### ✅ 2. Flexibility in Traffic Pattern Control
By launching it separately, we can:
- Tune traffic intensity dynamically (e.g., 10 → 15 → 20 parallel requests)
- Start/stop simulation for specific tests
- Use different versions of traffic scripts

---

### ✅ 3. It’s a Test Utility, Not a Core Component
- The core stack is: **Flask App + Prometheus + Loki + Grafana + Alertmanager**
- The simulator is just a **developer/test utility**, not a production service
- It’s purposefully decoupled to **keep the core clean and focused**

---

## 🚀 When Should You Start the Simulator?

After verifying that all core services are up and running:

1. Prometheus targets are healthy
2. Loki logs are visible
3. Alertmanager is configured
4. Grafana dashboards are set

Then you can:
```bash
docker compose up -d
```

## Components
- `simulate_traffic.sh`: Randomly hits endpoints with varied delays.
- `script.sh`: Controls the load — starts 10 parallel instances, runs them for 30s, kills them, then pauses for 2 minutes.

## Why Two Scripts?
- Separation of concern:
  - `simulate_traffic.sh` handles request logic
  - `script.sh` simulates *controlled bursts of load* for testing alerts

## Why Sleep for 2 Minutes?
The alert rule for high latency uses a 2-minute window:
```yaml
rate(sum)[2m] / rate(count)[2m]
````
So sleeping allows Prometheus to *cleanly detect dips between bursts*.
