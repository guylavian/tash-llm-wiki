---
title: Phantom incident from double-encoded Alertmanager webhook obscures real Keycloak token-endpoint 401 surge (2026-06-25)
type: question
domain: keycloak
slug: phantom-incident-from-double-encoded-alertmanager-webhook-ob
summary: Post-mortem — The network-blocking root cause is an escalating Keycloak token-endpoint failure: POST /realms/{realm}/protocol/{protoco
sources:
  - rhbk-26-6-metrics-for-troubleshooting
provenance:
  extracted: 1
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-06-25
---

# Phantom incident from double-encoded Alertmanager webhook obscures real Keycloak token-endpoint 401 surge (2026-06-25)

**Root cause.** The network-blocking root cause is an escalating Keycloak token-endpoint failure: POST /realms/{realm}/protocol/{protocol}/token is returning HTTP 401 (315 responses, growing during investigation), denying OAuth2/OIDC token issuance to clients. Services that depend on bearer-token authentication for cross-service network calls are blocked at the authentication layer. This condition was not alerted on because: (1) the Alertmanager webhook receiver has a JSON double-serialization bug that produced a phantom malformed incident (alerts[] empty, payload key is the literal string '{"alerts":[]}' rather than a parsed body), and (2) no PrometheusRule covers a sustained 401 rate on the token endpoint. A third contributing structural gap is that Prometheus has zero network telemetry scrape targets (no SNMP/BGP/node exporters), making all L2/L3 faults invisible to the monitoring stack.

## Evidence
1. Incident payload: {'{\"alerts\":[]}':''} — Alertmanager webhook body was JSON-stringified and used as an object key instead of being parsed; alerts array is empty, confirming no real Alertmanager rule fired (phantom incident). 2. Prometheus up targets: only keycloak:9000 (value=1). Zero network device exporters registered; get_service_health returned all-empty arrays for bgp_peer_state, ospf_neighbor_state, iface_input_errors, iface_crc_errors, p99_latency_ms, error_rate. 3. vendor_cluster_size=1, vendor_cache_container_stats_required_minimum_number_of_nodes=1 — single-node Keycloak, intended topology, not a split-brain. 4. http_server_requests_seconds_count{status='401', uri='/realms/{realm}/protocol/{protocol}/token'} = 315 and growing (was 261 at investigation start) — active escalating auth failures on token issuance endpoint. 5. ALERTS{alertstate='firing'} = empty — no alert rule covers this 401 rate. 6. All other HTTP endpoints returning 200/302 (health, admin, OIDC discovery, resource serving). Docs consulted: rhbk-26-6-metrics-for-troubleshooting (clustering metrics §6.7, HTTP metrics §6.5, embedded Infinispan §6.8).

## See also
- [[keycloak-keycloakhighauthfailurerate]] — the real auth-failure alert this phantom mimicked
- [[event-metrics]] — the metric pipeline the double-encoding corrupted
- [[rhbk-26-6-metrics-for-troubleshooting]]
