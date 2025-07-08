import logging
from logging_loki import LokiHandler
from flask import Flask, jsonify, Response
from util import do_some_heavy_task
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import os
import time


# Loki URL (adjust host & port as per your Loki setup)
LOKI_URL = "http://loki-server:3100/loki/api/v1/push"

# Set up a logger
logger = logging.getLogger("flask-loki-logger")
logger.setLevel(logging.INFO)

# Loki handler with tags (like `app=flask-metrics-logger`)
loki_handler = LokiHandler(
    url=LOKI_URL,
    tags={"app": "flask-metrics-logger"},
    version="1",
)

# Add Loki handler to logger
logger.addHandler(loki_handler)


# Create Flask app
app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))

# Constant label to identify metrics source
APP_LABEL = {"app": "flask-metrics-logger"}

# Counter: Tracks total number of requests by method, endpoint, status, and app
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'http_status', 'app']
)

# Histogram: Measures latency per endpoint, with custom buckets in seconds
# Converted from ms: [1,50,100,200,400,500,800,1000,2000] → [0.001, ..., 2.0]
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Latency of HTTP requests in seconds',
    ['endpoint', 'app'],
    buckets=[0.001, 0.05, 0.1, 0.2, 0.4, 0.5, 0.8, 1.0, 2.0]
)

@app.route("/")
def home():
    start_time = time.time()
    status = 200
    try:
        logger.info("Received request at /")
        return "Hello from Flask!"
    finally:
        duration = time.time() - start_time
        logger.info(f"Handled / in {duration:.3f} sec")
        REQUEST_LATENCY.labels(endpoint="/", app="flask-metrics-logger").observe(duration)
        REQUEST_COUNT.labels(method="GET", endpoint="/", http_status=status, app="flask-metrics-logger").inc()


@app.route("/slow")
def slow():
    start_time = time.time()
    try:
        logger.info("Heavy task started at /slow")
        time_taken = do_some_heavy_task()
        logger.info(f"Heavy task finished in {time_taken}ms")
        response = jsonify({
            "status": "Success",
            "message": f"Heavy task completed in {time_taken}ms"
        })
        status = 200
    except Exception as e:
        logger.error(f"Error in /slow: {e}")
        response = jsonify({
            "status": "Error",
            "error": "Internal Server Error"
        })
        status = 500
    finally:
        duration = time.time() - start_time
        logger.info(f"Handled /slow in {duration:.3f} sec with status {status}")
        REQUEST_LATENCY.labels(endpoint="/slow", app="flask-metrics-logger").observe(duration)
        REQUEST_COUNT.labels(method="GET", endpoint="/slow", http_status=status, app="flask-metrics-logger").inc()
    return response, status

# Prometheus scrape endpoint - returns latest metrics
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


# Run app
if __name__ == "__main__":
    # threaded=True allows handling multiple requests at once
    app.run(host="0.0.0.0", port=PORT, debug=True, threaded=True)
