# Observability — OpenTelemetry, Metrics, Health, Tracing — RHBK 26.6 (Offline Reference)

Centralized telemetry (OTel logs/metrics/traces), health probes, Micrometer/Prometheus metrics, SLIs, tracing, and dashboards/exemplars for Red Hat build of Keycloak 26.6 — with air-gap notes.

## 1. OpenTelemetry centralization

OTel is the unified path for Logs, Metrics, and Traces. The `opentelemetry` feature is **enabled by default**; at least one component (e.g. Traces) must be turned on for export to occur. Disable the `opentelemetry` feature to disable all OTel components.

Global `telemetry-*` options configure a single shared collector for all components.

| Option | Purpose | Default |
|---|---|---|
| `telemetry-endpoint` | Shared collector endpoint (all components) | `http://localhost:4317` |
| `telemetry-service-name` | Service name identifying the exporter; precedes `service.name` in resource attrs | `keycloak` |
| `telemetry-protocol` | Transport: `grpc` or `http/protobuf` | `grpc` |
| `telemetry-resource-attributes` | Resource attributes (List) | — |
| `telemetry-header-<header>` | Custom request header for all components | — |

```bash
bin/kc.[sh|bat] start \
  --telemetry-endpoint=http://otel-collector.example.internal:4317 \
  --telemetry-service-name=my-keycloak-iam \
  --telemetry-protocol=http/protobuf \
  --telemetry-header-Authorization='Bearer ***'
```

Component-specific headers (`telemetry-logs-header-*`, `telemetry-metrics-header-*`) take precedence over general `telemetry-header-*` for their component.

> **Air-gap:** The default endpoint `http://localhost:4317` assumes a co-located/internal collector. Always repoint `telemetry-endpoint` to an internal collector (e.g. `otel-collector.example.internal:4317`) or keep all OTel components off. A disconnected server with an enabled exporter pointed at an unreachable external endpoint will fail/stall on export. Inject auth tokens via `telemetry-header-Authorization='Bearer ***'`.

### Keycloak CR (Operator) — `spec.telemetry`

```yaml
apiVersion: k8s.keycloak.org/v2beta1
kind: Keycloak
metadata:
  name: example-kc
spec:
  telemetry:
    endpoint: http://otel-collector.example.internal:4317  # default 'http://localhost:4317'
    serviceName: my-best-keycloak-telemetry                # default 'keycloak'
    protocol: http/protobuf                                # default 'grpc'
    resourceAttributes:
      service.namespace: keycloak-namespace-telemetry
```

CR `telemetry.*` fields map 1:1 to `telemetry-*` server options.

### Enable all OTel components (Logs + Metrics + Traces)

OTel **Logs and Metrics are preview/experimental** — not for production.

```yaml
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
  name: example-kc
spec:
  features:
    enabled:
      - opentelemetry-logs
      - opentelemetry-metrics
  telemetry:
    endpoint: http://otel-collector.example.internal:4317
    serviceName: my-best-keycloak-telemetry
    protocol: grpc
  tracing:
    enabled: true
  additionalOptions:
    - name: telemetry-logs-enabled
      value: "true"
    - name: telemetry-metrics-enabled
      value: "true"
    - name: metrics-enabled
      value: "true"
```

### OTel Logs (Technology Preview, disabled by default)

```bash
bin/kc.[sh|bat] start --features=opentelemetry-logs --telemetry-logs-enabled=true
```

- `telemetry-logs-level` filters which already-generated logs are exported. It does **not** generate logs below the `log-level` threshold — setting `telemetry-logs-level=DEBUG` exports nothing if `log-level=WARN`.
- `telemetry-logs-header-<header>` sets log-export headers.

### OTel Metrics (experimental, not for production)

Requires `metrics-enabled=true` and the `opentelemetry` feature on. Uses the Micrometer-to-OpenTelemetry bridge.

```bash
bin/kc.[sh|bat] start --features=opentelemetry-metrics --telemetry-metrics-enabled=true --metrics-enabled=true
```

`telemetry-metrics-header-<header>` sets metrics-export headers. Note API/semantic-convention differences between Micrometer and OTel metrics; verify required metrics are exported.

## 2. Health checks

Exposed on the **management port `9000`** by default. Four endpoints:

| Endpoint | Purpose |
|---|---|
| `/health/started` | Startup probe (initial startup before liveness takes over). |
| `/health/live` | Liveness — if it fails, terminate and restart the app. |
| `/health/ready` | Readiness — only route traffic once it succeeds. |
| `/health` | Accumulates all health-check procedures. |

Responses: HTTP `200 OK` on success, `503 Service Unavailable` on failure, JSON body `{"status":"UP","checks":[...]}`.

### Enabling (build time)

```bash
bin/kc.[sh|bat] build --health-enabled=true
bin/kc.[sh|bat] build --health-enabled=true --metrics-enabled=true   # for checks requiring metrics
```

When health endpoints are enabled, async server bootstrap is also enabled by default (HTTP ports open while bootstrapping).

### Available checks

| Check | Description | Requires Metrics |
|---|---|---|
| Database | Status of DB connection pool. | Yes |
| Cluster | Status of cluster (network partitions). | No |
| Graceful shutdown | Returns `DOWN` once pre-shutdown phase starts. | No |
| Keycloak Initialized | Server initialization status. | No |

Cluster health check is available only for clustered setups using cache transport stacks `jdbc-ping` or `jdbc-ping-udp`.

### Port / interface behavior

- `http-management-health-enabled=false` → health endpoints stay on the main HTTP(S) ports; block external `/health` traffic at the proxy.
- TLS on the main interface propagates to the management interface. For plain-HTTP health checks: set `http-management-scheme=http`, or set `http-management-health-enabled=false` with `http-enabled=true` (then block external traffic to the HTTP port — default `8080` — and `/health`).
- With `https-client-auth=required`, the management interface inherits mTLS; set `https-management-client-auth` to `request` or `none` so probes do not need a client cert.
- Container images strip `curl`/HTTP clients — run checks from outside the container or use a custom image.

```bash
curl --head -fsS http://localhost:9000/health/ready    # status 0 == ready
```

Containerfile HEALTHCHECK without an HTTP client (BASH TCP redirect):

```bash
{ printf 'HEAD /health/ready HTTP/1.0\r\n\r\n' >&0; grep 'HTTP/1.0 200'; } 0<>/dev/tcp/localhost/9000
```

Path/port depend on `http-relative-path` / `http-management-relative-path` / `http-management-port`. In Kubernetes, define an HTTP Probe — do not use a liveness command.

> **Air-gap:** Use Kubernetes HTTP probes against `:9000` internally; no external dependency. Build the health-enabled image in a connected build env, push to the internal registry, then deploy disconnected.

## 3. Metrics

Enable at build/start time:

```bash
bin/kc.[sh|bat] start --metrics-enabled=true
```

Exposed at `/metrics` on the management interface. Content type `application/openmetrics-text` (Prometheus/OpenMetrics text format). Sample families: `base_gc_total`, `jvm_memory_usage_after_gc_percent`, `jvm_threads_peak_threads`, `agroal_active_count`, `base_memory_maxHeap_bytes`, `process_start_time_seconds`, `system_load_average_1m`.

### Key metric families

**JVM**

| Area | Metric (prefix) | Description |
|---|---|---|
| Info | JVM info | Version, runtime, vendor. |
| Heap committed | committed-memory gauge | Memory the JVM committed for use. |
| Heap used | used-memory gauge | Actual memory consumed. |
| GC pause max | GC max-duration | Max GC pause duration (s) by cause. |
| GC pause total | GC total-time | Cumulative GC pause time. |
| GC pause count | GC count | Total GC pause events. |
| GC overhead | GC CPU % | % of CPU time spent on GC. |
| Container CPU | container CPU core-seconds | Cumulative CPU time (Kubernetes). |

**Database connection pool (agroal)** — fixed-size pool recommended.

| Metric | Description |
|---|---|
| `agroal_active_count` | Active connections in use. |
| (idle) | Idle DB connections. |
| (active/in-tx) | Connections in ongoing transactions. |
| (awaiting) | Threads waiting for a connection. |

If many threads wait: reduce `http-pool-max-threads` to match available DB connections rather than blindly enlarging the pool; or enlarge `users`/`realms` caches.

**HTTP** — tags: `method`, `outcome`, `status`, `uri`.

| Metric | Description |
|---|---|
| `http_server_requests_seconds_count` | Total requests processed. |
| `http_server_requests_seconds_sum`/bucket | Total duration / buckets. |
| (active requests) | Current active requests. |
| (responses/bytes sent, requests/bytes received) | Bandwidth. |

Enable histograms with `http-metrics-histograms-enabled=true`; add SLO buckets with `http-metrics-slos`.

**Local caching** — global tag `cache=<name>`.

| Metric | Description |
|---|---|
| `cache_gets_total` | Total cache lookups (tag `result=hit\|miss`). |
| (size) | Number of cached entries. |
| (evictions) | Times the cache evicted. |

Hit ratio: `cache_gets_total{result="hit"} / cache_gets_total`.

**Embedded Infinispan** (`vendor_*`) — tag `cache=<name>`: `vendor_statistics_hit_times_seconds_count`, `vendor_statistics_miss_times_seconds_count`, `vendor_statistics_remove_*`, `vendor_statistics_store_times_seconds_count`, eviction, locking, transactions (prepare/rollback/commit), state transfer, replication (`vendor_rpc_manager_replication_count`, `vendor_rpc_manager_replication_failures`).

**Clustering / JGroups** — `vendor_jgroups_*` are debug-only and may change between releases; do **not** use in dashboards or alerting. Covers response time, bandwidth (per transport protocol, default TCP), thread pool (default max `200`; unavailable with virtual threads, default on OpenJDK 21+), flow control (UFC/MFC), retransmissions/RED, cluster size, network-partition merge events, and (external Data Grid) cross-site status (`1`=online, `0`=offline, `2`=unknown).

### Event metrics (user activity)

Counters per instance, reset on restart; aggregate across cluster nodes for a cluster view. Separate metric per realm by default.

```bash
bin/kc.[sh|bat] start --metrics-enabled=true --event-metrics-user-enabled=true
bin/kc.[sh|bat] start ... --event-metrics-user-tags=realm,idp,clientId
bin/kc.[sh|bat] start ... --event-metrics-user-events=login,logout
```

| Option | Purpose |
|---|---|
| `event-metrics-user-enabled` | Enable user-event metrics (feature `user-event-metrics` + metrics). |
| `event-metrics-user-tags` | Dimensions: `realm`, `idp`, `clientId`. High-cardinality risk. |
| `event-metrics-user-events` | Limit collected events, e.g. `login,logout`. |

Metric `keycloak_user_events_total` (counter) — tags `realm`, `client_id`, `idp` (`client_id`/`idp` off by default for cardinality), `event`, `error`.

```
keycloak_user_events_total{client_id="security-admin-console",error="",event="login",idp="",realm="master",} 1.0
keycloak_user_events_total{client_id="security-admin-console",error="invalid_user_credentials",event="login",idp="",realm="master",} 1.0
```

**Password hashing** — `keycloak_credentials_password_hashing_validations_total` (counter); tags `realm`, `algorithm` (e.g. `argon2`), `hashing_strength` (e.g. `Argon2id-1.3[m=7168,t=5,p=1]`), `outcome` (`valid`/`invalid`/`error`). Configure tags via `spi-credential--keycloak-password--validations-counter-tags` (all enabled by default).

## 4. Service Level Indicators (SLIs)

Prereqs: metrics enabled, `http-metrics-slos` set to the latency target (ms), and a Prometheus-compatible system (PromQL).

| Characteristic | SLI | Example SLO | Source |
|---|---|---|---|
| Availability | % of time RHBK answers requests | 99.9%/month (~44 min/month) | `up` metric |
| Latency | Response time for auth HTTP requests | 95% < 250 ms over 30 days | `http_server_requests_seconds_bucket` (`http-metrics-slos=250`) |
| Errors | Failed auth requests due to server problems | < 0.1% over 30 days | `http_server_requests_seconds_count{outcome="SERVER_ERROR"}` |

```promql
# Latency SLI (fraction faster than 0.25s)
sum(rate(http_server_requests_seconds_bucket{
  uri=~"/realms/{realm}/protocol/{protocol}.*|/realms/{realm}/login-actions.*",
  le="0.25", container="keycloak", namespace="$namespace"}[30d]
)) without (le,uri,status,outcome,method,pod,instance)
/
sum(rate(http_server_requests_seconds_count{
  uri=~"/realms/{realm}/protocol/{protocol}.*|/realms/{realm}/login-actions.*",
  container="keycloak", namespace="$namespace"}[30d]
)) without (le,uri,status,outcome,method,pod,instance)
```

Availability uses `count_over_time(sum(up{container="keycloak",namespace="$namespace"} > 0)[30d:15s]) / count_over_time(vector(1)[30d:15s])`. In Grafana, swap `30d`/`30d:15s` for `$__range`/`$range:$interval`. Use recording rules in production. Set `http-metrics-histograms-enabled=true` for extra latency-troubleshooting buckets.

## 5. Troubleshooting via metrics

"What if SLOs aren't met?" — correlate symptoms to metrics:

- **Latency SLO breached** + DB pool exhausted (threads queuing) + low `users` cache hit ratio (~5%) → increase `users` cache size (`cache-embedded-users-max-count`), and/or increase DB pool connections (verify against DB metrics, possibly add processors).
- **Rapid eviction + high DB CPU** → `users`/`realms` cache too small; raise `cache-embedded-users-max-count` / `cache-embedded-realms-max-count`.
- Always confirm any change with a comparative performance test. DB-internal troubleshooting is out of scope.

## 6. Tracing (OTLP)

Enable at build time (`opentelemetry` feature must be on — default):

```bash
bin/kc.[sh|bat] start --tracing-enabled=true
```

Defaults: batched export over **gRPC** to **`http://localhost:4317`**, sampler `traceidratio`, ratio `1.0`, service name `keycloak`.

| Option | Purpose | Default |
|---|---|---|
| `tracing-enabled` | Enable tracing (build time). | — |
| `tracing-sampler-type` | `always_on`, `always_off`, `traceidratio`, `parentbased_always_on`, `parentbased_always_off`, `parentbased_traceidratio` | `traceidratio` |
| `tracing-sampler-ratio` | Sampling ratio `[0,1]` (Double). `0.0` disables at runtime. | `1.0` |
| `tracing-service-name` | **DEPRECATED** — use `telemetry-service-name`. | `keycloak` |
| `tracing-resource-attributes` | **DEPRECATED** — use `telemetry-resource-attributes` (List). | — |
| `log-<handler>-include-trace` | Include trace info in a log handler (e.g. `log-console-include-trace`). | — |

Endpoint/protocol are taken from the global `telemetry-*` options (override the global collector via Tracing options to export traces elsewhere).

**Spans** are created for: incoming HTTP requests; outgoing DB (incl. acquiring a connection — JDBC tracing); outgoing LDAP (incl. connect); outgoing HTTP (incl. IdP brokerage). **Tags** are prefixed `kc.` (`kc.clientId`, `kc.realmName`, `kc.sessionId`, `kc.token.id`, `kc.token.issuer`, `kc.token.sid`, `kc.authenticationSessionId`, `kc.authenticationTabId`). Sampled traces embed user events (`LOGIN`, `LOGOUT`, `REFRESH_TOKEN`) and LDAP errors as logs.

### Sampling

Default `traceidratio` makes per-span decisions independent of parent. `parentbased_traceidratio` keeps parent/child consistent but external callers can manipulate trace headers (esp. `tracestate`) → DoS risk; filter headers and assess caller trust. Production: lower `tracing-sampler-ratio` (e.g. `0.1` = 10%) to cut storage/overhead.

### Trace IDs in logs / templates

When tracing is on, log lines include `traceId`, `parentId`, `spanId`, `sampled` (across all enabled handlers). Disable per-handler with `log-<handler>-include-trace=false` (no effect if the handler's log format is explicitly overridden). The login theme exposes a `traceId` Freemarker variable (default in `error.ftl`).

### Kubernetes

With the Operator, tracing config propagates to containers. The Operator auto-sets `KC_TRACING_SERVICE_NAME` and `KC_TRACING_RESOURCE_ATTRIBUTES` per container; `KC_TRACING_RESOURCE_ATTRIBUTES` always carries `k8s.namespace.name` unless overridden. Filter traces by `service.name` (deployment), `k8s.namespace.name`, `host.name` (pod).

> **Air-gap:** Tracing defaults to gRPC `http://localhost:4317` — an unreachable external collector on a disconnected server will error/stall. Options: (a) keep `tracing-enabled=false`; (b) set `tracing-sampler-ratio=0.0` (no traces sent at runtime); or (c) repoint the global `telemetry-endpoint` to an internal collector, e.g. `otel-collector.example.internal:4317`, optionally `--telemetry-protocol=http/protobuf` with `--telemetry-header-Authorization='Bearer ***'`. Dev-only Jaeger-all-in-one (`jaegertracing/all-in-one`, ports 16686/4317/4318) must be mirrored to the internal registry first.

## 7. Dashboards & exemplars

Grafana dashboards (JSON) live in `keycloak/keycloak-grafana-dashboard`. Branch/tag: `26.1–26.2` → `26.2.0`; `>= 26.3` → `main`.

```bash
git clone -b main https://github.com/keycloak/keycloak-grafana-dashboard.git
# dashboards in keycloak-grafana-dashboard/dashboards
```

- `keycloak-troubleshooting-dashboard.json` — SLI graphs + troubleshooting.
- `keycloak-capacity-planning-dashboard.json` — load/password-validations/login flows; **requires event metrics enabled**.

Heatmaps need `http-metrics-histograms-enabled=true`. Import via Dashboards → New → Import → upload JSON → pick Prometheus datasource. For bare-metal (no Kubernetes labels) add labels in the scrape config:

```yaml
scrape_configs:
  - job_name: "keycloak-service"
    static_configs:
      - targets: ["localhost:9000", "localhost:9001", "localhost:9002"]
        labels:
          namespace: 'keycloak'
          container: 'keycloak'
    relabel_configs:
      - source_labels: [__address__]
        target_label: pod
```

### Exemplars (link metric → trace)

Supported on `http_server_requests_seconds_count` (incl. histograms), `keycloak_credentials_password_hashing_validations_total`, `keycloak_user_events_total`. Setup: enable metrics + tracing; enable exemplar storage in the monitoring system; scrape with `OpenMetricsText1.0.0`; configure datasource trace links; enable the Exemplars toggle per query.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
spec:
  scrapeProtocols:
    - OpenMetricsText1.0.0
```

Without the `OpenMetricsText1.0.0` protocol, Prometheus falls back to PrometheusText and no exemplars appear. Browser access to `/metrics` negotiates PrometheusText (no exemplars). For Grafana+Prometheus set `exemplarTraceIdDestinations` pointing at the tracing datasource (Jaeger/Tempo). Verify:

```bash
curl -s http://localhost:9000/metrics \
  -H 'Accept: application/openmetrics-text; version=1.0.0; charset=utf-8' \
  | grep "#.*trace_id"
```

> **Air-gap:** Clone the dashboard repo and mirror Grafana/Prometheus/Jaeger/Tempo images into the internal registry from a connected host; import dashboards offline. Exemplar trace links must point at an internal tracing datasource (`*.example.internal`).

_Source: Red Hat build of Keycloak 26.6 Observability Guide (docs.redhat.com), distilled offline._
