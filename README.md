# hand-gesture-api
FastAPI backend for serving hand gesture predictions

Sure! Here’s a full **README** section you can add to your backend repo or project documentation explaining the 3 metrics with some setup hints:

---

# Monitoring Metrics Documentation

Monitoring the health and performance of the hand gesture classifier API is essential for maintaining a smooth user experience and reliable service. We have selected three key metrics to monitor, covering model performance, data flow, and server health:

---

## 1. Model-related Metric: **Prediction Latency**

* **Metric name:** `http_request_duration_seconds` (Histogram)
* **Description:** Measures the time taken to process each prediction request by the API.
* **Why it matters:**

  * Real-time gesture control requires fast responses.
  * Increasing latency can indicate model inefficiencies or resource constraints.
* **How it is collected:**

  * Using the `prometheus_fastapi_instrumentator` package which instruments FastAPI endpoints.
  * Exposed automatically and scraped by Prometheus.

---

## 2. Data-related Metric: **Number of Requests**

* **Metric name:** `http_requests_total` (Counter)
* **Description:** Counts total prediction requests sent to the API.
* **Why it matters:**

  * Tracks usage volume and user activity patterns.
  * Sudden drops or spikes might indicate issues with clients or changes in input data distribution.
* **How it is collected:**

  * Also instrumented via `prometheus_fastapi_instrumentator`.
  * Incremented on every API request received.

---

## 3. Server-related Metric: **CPU Usage**

* **Metric name:** `node_cpu_seconds_total` (Gauge or derived from node exporter)
* **Description:** Measures the percentage of CPU used by the server hosting the API.
* **Why it matters:**

  * Ensures server is not overloaded, preventing crashes or performance degradation.
  * Helps with capacity planning and resource scaling.
* **How it is collected:**

  * Via Prometheus node\_exporter running on the host machine or via Docker stats.
  * Visualized in Grafana dashboards.

---

## How to Set Up Monitoring

1. **Run Prometheus** configured to scrape your FastAPI app and node exporter metrics.
2. **Run Grafana** and add Prometheus as a data source.
3. **Import or create dashboards** visualizing the above metrics:

   * Prediction latency histograms and percentiles
   * Request count over time
   * CPU usage over time
4. **Use alerts** in Prometheus or Grafana to notify when latency is too high, requests drop, or CPU usage exceeds safe thresholds.

---

## Summary Table

| Metric Name                     | Type           | Reason for Monitoring                     |
| ------------------------------- | -------------- | ----------------------------------------- |
| `http_request_duration_seconds` | Model-related  | Maintain fast API response times for UX   |
| `http_requests_total`           | Data-related   | Track usage volume and detect anomalies   |
| `node_cpu_seconds_total`        | Server-related | Ensure server health and prevent overload |

---






