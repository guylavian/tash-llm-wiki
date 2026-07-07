---
title: Management interface — health & metrics
type: entity
domain: keycloak
slug: management-interface
summary: "Health (`/health`) and metrics (`/metrics`) are served on a separate management HTTP server (default port 9000) so they can be kept off the public-facing port."
sources:
  - guide:server_configuration_guide
provenance_extracted: 10
provenance_inferred: 0
provenance_ambiguous: 0
tags: [server-config]
status: draft
updated: 2026-07-02
---

# Management interface (health & metrics)

**Health (`/health`) and metrics (`/metrics`) are served on a separate management HTTP server (default port 9000) so they can be kept off the public-facing port.**

> Scope note: this page covers the management interface from the **server-configuration** angle (enabling, relative path, TLS scheme, deprecation). For the observability-guide treatment of the port and its endpoints see [[management-port]], [[health-endpoints]], and [[server-metrics-endpoint]].

The management interface turns on automatically when something is exposed on it — currently only health checks and metrics, gated by their build-time options.

## Health checks

- Build-time enable: `kc.sh build --health-enabled=true`. By default no checks are returned.
- Endpoints: `/health/live`, `/health/ready`, `/health/started`, `/health`. Respond `200 OK` (`{"status":"UP",...}`) or `503 Service Unavailable`.
- Monitor via external HTTP (e.g. `curl --head -fsS http://localhost:9000/health/ready`). The container image strips `curl`, so run checks from outside the container; in Kubernetes use an HTTP probe, not a liveness command.

## Metrics

- Build-time enable: `kc.sh build --metrics-enabled=true`. Exposed at `/metrics` on the management interface (Micrometer/Prometheus format).
- User-event metrics are an additional opt-in feature (`user-event-metrics:v1`).

## Interface options

- `http-management-port` — default `9000`.
- `http-management-relative-path` — prefix (defaults to `http-relative-path` if set; e.g. `/auth` → `/auth/health`).
- TLS: inherits the main server's TLS by default; the management server is HTTP **or** HTTPS, not both. Force HTTP with `http-management-scheme=http`; tune TLS separately with `https-management-*`.
- `legacy-observability-interface=true` — moves health/metrics back onto the main server. **Deprecated** (will be removed); exposing health/metrics on the main server is discouraged for security.

Do not proxy port 9000 — keep health/metrics internal (see [[reverse-proxy-configuration]] exposed-path table, which lists `/metrics` and `/health` as "not exposed").

## Contradictions / caveats
- In RHBK **26.0** the docs split this across separate "Health checks" (ch.19) and "Metrics" (ch.20) chapters; from **26.4** they are unified under "Configuring the Management Interface" (ch.18) plus the dedicated health/metrics chapters. Endpoints and `health-enabled`/`metrics-enabled` options are unchanged.
- `legacy-observability-interface` exists only as a deprecated migration aid — do not rely on it long-term.

## See also
- [[server-configuration]]
- [[management-port]]
- [[health-endpoints]]
- [[server-metrics-endpoint]]
- [[observability-stack]]
- [[reverse-proxy-configuration]]
- [[tls-configuration]]
- [[build-vs-runtime-options]]
- [[production-checklist]]
- [[rhbk-operator]]
