---
title: RHBK observability stack — health, metrics, tracing, OpenTelemetry
type: topic
domain: keycloak
slug: observability-stack
summary: "RHBK exposes built-in health probes, Prometheus/OpenMetrics metrics, and OpenTelemetry traces (plus preview OTel logs/metrics), most of it served on the dedicated management port `9000`, so a single deployment feeds a centralized observability stack with no extra sidecars."
sources:
  - guide:observability_guide
  - kb:telemetry-
  - kb:health-
  - kb:configuration-metrics-
  - kb:tracing-
source_notes:
  - "[[rhbk-26-6-telemetry]]"
  - "[[rhbk-26-6-health]]"
  - "[[rhbk-26-6-configuration-metrics]]"
  - "[[rhbk-26-6-tracing]]"
provenance_extracted: 13
provenance_inferred: 1
provenance_ambiguous: 0
tags: [observability, concept]
status: draft
updated: 2026-07-02
---

# RHBK observability stack — health, metrics, tracing, OpenTelemetry

**RHBK exposes built-in health probes, Prometheus/OpenMetrics metrics, and OpenTelemetry traces (plus preview OTel logs/metrics), most of it served on the dedicated management port `9000`, so a single deployment feeds a centralized observability stack with no extra sidecars.**

## The three signals and where they live

RHBK 26.x produces all three observability signals natively:

- **Health** — startup/liveness/readiness probes at `/health/*` on the management port. See [[health-endpoints]].
- **Metrics** — a Prometheus/OpenMetrics scrape endpoint `/metrics` on the management port. See [[server-metrics-endpoint]], plus aggregated user-activity counters in [[event-metrics]].
- **Traces** — OpenTelemetry (OTLP) spans for the request lifecycle. See [[tracing-otlp]].

By default health and metrics are served on the **management interface (port 9000)**, kept off the main HTTP(S) ports so you can firewall them separately. The `/metrics` and `/health/*` paths only appear there once their respective enable options are set.

## Centralization with OpenTelemetry

Beyond the native Prometheus endpoint, RHBK can push all three signals to a single **OpenTelemetry collector** using global `telemetry-*` options (endpoint, service name, protocol, headers, resource attributes). This lets one OTLP collector receive Logs, Metrics, and Traces with no added deployment overhead (inferred — a synthesis across the telemetry/health/metrics/tracing chapters, not a single stated conclusion). The OTel feature is **enabled by default**, but at least one component (e.g. Traces) must be turned on for anything to be exported. See [[opentelemetry-centralization]].

Note the maturity split:
- **Traces** via OTLP are the mature, fully-described path (Tech Preview in 26.0, GA-grade by 26.4+).
- **OTel Logs** (`opentelemetry-logs`) and **OTel Metrics** (`opentelemetry-metrics`) are **Technology Preview / experimental**, disabled by default, and not for production. The native `/metrics` scrape endpoint remains the supported metrics path.

## Putting it to use

- **SLIs/SLOs** — derive availability, latency and error SLIs from `up` and `http_server_requests_seconds_*` via PromQL. See [[service-level-indicators]].
- **Dashboards** — import the official Grafana dashboards (troubleshooting, capacity planning). See [[grafana-dashboards]].
- **Exemplars** — link a metric data point to the trace that produced it, bridging [[server-metrics-endpoint]] and [[tracing-otlp]]. See [[metrics-exemplars]].

## Air-gap notes

- The native `/metrics` and `/health` endpoints need no internet — scrape them with Prometheus inside the cluster.
- The **Grafana dashboard JSON** lives in the external GitHub repo `keycloak/keycloak-grafana-dashboard`; in a disconnected environment you must mirror/clone the right branch (see [[grafana-dashboards]] for the version-to-branch table) beforehand.
- **Exemplars** depend on a Prometheus build with the exemplar-storage preview feature and `OpenMetricsText1.0.0` scraping — verify your mirrored Prometheus supports it.
- The RHBK container image **strips `curl`** and similar tools, so in-container HTTPS health probes are not possible; probe from outside or use a BASH `/dev/tcp` trick (see [[health-endpoints]]).

## Contradictions / caveats

- **Tracing maturity**: in RHBK **26.0** (Server Configuration Guide ch.21) tracing is explicitly **preview** and requires `--features=opentelemetry` alongside `--tracing-enabled=true`. By **26.4/26.6** (Observability Guide) the `opentelemetry` feature is on by default, so `--tracing-enabled=true` alone suffices, and the trace ratio range is documented as `[0,1]` (26.4+) vs `(0,1]` (26.0) — 26.4+ allows `0.0` to disable sampling at runtime.
- **OTel Logs/Metrics** are Tech Preview/experimental across 26.x — do not rely on them in production; use the native `/metrics` endpoint instead.
- **Operator config**: 26.6 adds a first-class `spec.telemetry` stanza in the Keycloak CR; earlier versions required `additionalOptions` for tracing/telemetry. See [[opentelemetry-centralization]] and [[rhbk-operator]].

## See also
- [[opentelemetry-centralization]]
- [[health-endpoints]]
- [[server-metrics-endpoint]]
- [[event-metrics]]
- [[tracing-otlp]]
- [[service-level-indicators]]
- [[grafana-dashboards]]
- [[metrics-exemplars]]
- [[rhbk-operator]]
- [[distributed-caches]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-telemetry|Chapter 1. Centralize your observability stack with OpenTelemetry]]
- [[rhbk-26-6-health|Chapter 2. Tracking instance status with health checks]]
- [[rhbk-26-6-configuration-metrics|Chapter 3. Gaining insights with metrics]]
- [[rhbk-26-6-tracing|Chapter 7. Root cause analysis with tracing]]
<!-- crosslink:end -->
