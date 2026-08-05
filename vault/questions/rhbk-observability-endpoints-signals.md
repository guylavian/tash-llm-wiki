---
origin: eval-cohort
title: RHBK observability endpoints and signals
type: question
domain: keycloak
slug: rhbk-observability-endpoints-signals
summary: "RHBK exposes health probes, Prometheus/OpenMetrics metrics, and OpenTelemetry traces (plus preview OTel logs/metrics) — most served on the dedicated management port 9000."
sources:
  - guide:observability_guide
  - guide:server_configuration_guide
  - kb:telemetry-
  - kb:health-
  - kb:configuration-metrics-
  - kb:event-metrics-
  - kb:tracing-
  - kb:keycloak-service-level-indicators-
  - kb:grafana-dashboards-
  - kb:exemplars-
  - kb:metrics-for-troubleshooting-
provenance_extracted: 14
provenance_inferred: 3
provenance_ambiguous: 0
question_tier: conceptual
tags: [observability]
status: draft
updated: 2026-07-12
graph_community: "RHBK observability stack — health, metrics, tracing, OpenTelemetry"
---

# RHBK observability endpoints and signals

## Endpoints

### Management interface (port 9000)

All observability endpoints are served on a **dedicated management HTTP server** on port 9000 by default, separate from the application HTTP(S) ports (`observability-stack.md:34-38`, `management-interface.md:19-21`). This lets you firewall them independently.

| Endpoint | Purpose | How to enable |
|---|---|---|
| `/health` | Aggregate health check — JSON `{"status":"UP",...}` | `kc.sh build --health-enabled=true` |
| `/health/live` | Liveness probe — 200 OK or 503 | Same |
| `/health/ready` | Readiness probe — 200 OK or 503 | Same |
| `/health/started` | Startup probe — 200 OK or 503 | Same |
| `/metrics` | Prometheus/OpenMetrics scrape endpoint | `kc.sh build --metrics-enabled=true` |

`health-endpoints.md:26-31`, `server-metrics-endpoint.md:28-34`

### OpenTelemetry OTLP export (push-based)

Not a scrape endpoint — RHBK pushes traces (and, in preview, logs/metrics) to an OTel collector via gRPC:

| Setting | Default | Purpose |
|---|---|---|
| `telemetry-endpoint` | `http://localhost:4317` | OTLP collector address |
| `telemetry-protocol` | `grpc` | Transport (also `http/protobuf`) |

`opentelemetry-centralization.md:24-31`

## Signals

### 1. Health checks

Each `/health/*` endpoint returns HTTP 200 OK with body `{"status":"UP","checks":[...]}` or 503 on failure. Checks include `Keycloak Initialized`, `Graceful Shutdown`, `Keycloak cluster health check`, and `Keycloak database connections async health check`. (`health-endpoints.md:31-31`)

### 2. Prometheus / OpenMetrics metrics

**Native scrape endpoint** (the supported metrics path). Metric families (`server-metrics-endpoint.md:38-50`):

| Family | Examples |
|---|---|
| System | `system_load_average_1m` — CPU, memory |
| JVM | `base_gc_total`, `jvm_memory_usage_after_gc_percent`, `jvm_threads_peak_threads` |
| Database | `agroal_active_count` — Agroal connection pool |
| HTTP | `http_server_requests_seconds_count` / `_bucket` — per-endpoint |
| Infinispan Caches | See [[distributed-caches]] |
| Keycloak-specific | `keycloak_user_events_total` (user-activity counters) |
| Keycloak-specific | `keycloak_credentials_password_hashing_validations_total` |

Additional knobs:
- `http-metrics-histograms-enabled=true` — percentile buckets for latency heatmaps (`server-metrics-endpoint.md:53-54`)
- `http-metrics-slos=250` — explicit SLO threshold buckets (`server-metrics-endpoint.md:54-54`)

**User event metrics** (`event-metrics.md:28-31`):
- `keycloak_user_events_total{realm,client_id,idp,event,error}` — counters for login/logout/refresh token etc.
- Enables: `--metrics-enabled=true --event-metrics-user-enabled=true`

### 3. Distributed tracing (OTLP)

RHBK records OpenTelemetry spans for the full request lifecycle (`tracing-otlp.md:22-22, 42-44`):
- **Spans for**: incoming HTTP requests, outgoing DB calls, LDAP requests, outgoing HTTP (IdP brokerage)
- **Tags**: `kc.clientId`, `kc.realmName`, `kc.sessionId`, `kc.token.id`, etc.
- **Trace IDs embedded in logs** when tracing is on (`tracing-otlp.md:47-48`)
- Sampling: ratio `[0,1]` (default `1.0`). Production recommendation: lower to `0.1` (`tracing-otlp.md:53-55`)

### 4. OTel Logs and Metrics (Technology Preview)

| Signal | Feature flag | Status |
|---|---|---|
| OTel Logs | `opentelemetry-logs` | Technology Preview, disabled by default |
| OTel Metrics | `opentelemetry-metrics` | Experimental, not for production |

`opentelemetry-centralization.md:45-47`

These are **not production-ready** — use the native `/metrics` endpoint and normal log pipeline instead.

### 5. Exemplars (metrics ↔ traces bridge)

Three metric families support exemplars attaching the last trace ID to a data point (`metrics-exemplars.md:26-28`):
- `http_server_requests_seconds_count`
- `keycloak_credentials_password_hashing_validations_total`
- `keycloak_user_events_total`

Requires Prometheus exemplar-storage preview feature + `OpenMetricsText1.0.0` scrape protocol (`metrics-exemplars.md:32-39`).

### 6. SLIs / SLOs (PromQL)

Example SLIs derived from the metrics endpoint (`service-level-indicators.md:29-31`):

| SLI | Target | Source metric |
|---|---|---|
| Availability | 99.9% / month | `up` |
| Latency | 95% < 250ms over 30d | `http_server_requests_seconds_bucket{le="0.25"}` |
| Errors | SERVER_ERROR < 0.1% over 30d | `http_server_requests_seconds_count{outcome="SERVER_ERROR"}` |

### 7. Grafana dashboards

Official dashboard JSON in `keycloak/keycloak-grafana-dashboard` repo (`grafana-dashboards.md:24-27`):
- **Troubleshooting dashboard** — SLI graphs + drill-down
- **Capacity planning dashboard** — requires [[event-metrics]]

## Key architectural points

- Health and metrics are on the **management port** by default, not the main HTTPS port — do not proxy port 9000 publicly (`management-interface.md:42-43`)
- `health-enabled` and `metrics-enabled` are **build-time** options — changing them requires `kc.sh build` (`health-endpoints.md:35-39`, `server-metrics-endpoint.md:28-32`)
- The container image strips `curl` — probe from outside or use `/dev/tcp` BASH trick (`health-endpoints.md:47-48`)
- Tracing is GA-grade by 26.4+; in 26.0 it required `--features=opentelemetry` explicitly (`tracing-otlp.md:32-36`)
- The `spec.telemetry` CR stanza is a **26.6 addition**; earlier versions use `additionalOptions` (`opentelemetry-centralization.md:51-63`)
- OTel Logs/Metrics are Tech Preview — the native `kc.sh build --metrics-enabled=true` + `/metrics` scrape is the supported path (`opentelemetry-centralization.md:45-47`)

## References

**RH ground-truth:**
- `guide:observability_guide` — Observability Guide (health, metrics, tracing, telemetry, SLIs, dashboards, exemplars)
- `guide:server_configuration_guide` — Management Interface configuration
- `kb:telemetry-` — Centralized observability with OpenTelemetry
- `kb:health-` — Health check endpoints
- `kb:configuration-metrics-` — Metrics configuration and families
- `kb:event-metrics-` — User event metrics
- `kb:tracing-` — Distributed tracing via OTLP
- `kb:keycloak-service-level-indicators-` — PromQL SLIs
- `kb:grafana-dashboards-` — Official Grafana dashboards
- `kb:exemplars-` — Metrics-to-traces exemplars
- `kb:metrics-for-troubleshooting-` — Troubleshooting with metrics

**Wiki pages:**
- [[observability-stack]]
- [[health-endpoints]]
- [[management-port]]
- [[management-interface]]
- [[server-metrics-endpoint]]
- [[event-metrics]]
- [[tracing-otlp]]
- [[opentelemetry-centralization]]
- [[service-level-indicators]]
- [[grafana-dashboards]]
- [[metrics-exemplars]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-observability_guide|keycloak reference — observability_guide]]
- [[_ref-keycloak-server_configuration_guide|keycloak reference — server_configuration_guide]]
- [[rhbk-26-6-telemetry|Chapter 1. Centralize your observability stack with OpenTelemetry]]
- [[rhbk-26-6-health|Chapter 2. Tracking instance status with health checks]]
- [[rhbk-26-6-configuration-metrics|Chapter 3. Gaining insights with metrics]]
- [[rhbk-26-6-event-metrics|Chapter 4. Monitoring user activities with event metrics]]
- [[rhbk-26-6-tracing|Chapter 7. Root cause analysis with tracing]]
- [[rhbk-26-6-keycloak-service-level-indicators|Chapter 5. Monitoring performance with Service Level Indicators]]
- [[rhbk-26-6-grafana-dashboards|Chapter 8. Visualizing activities in dashboards]]
- [[rhbk-26-6-exemplars|Chapter 9. Analyzing outliers and errors with exemplars]]
- [[rhbk-26-6-metrics-for-troubleshooting|Chapter 6. Troubleshooting using metrics]]
<!-- crosslink:end -->
