---
title: KeycloakHighServerErrorRate — DB Connection Pool Exhaustion via Slow Queries (2026-06-28)
type: question
question_tier: scenarios
domain: keycloak
slug: keycloak-keycloakhighservererrorrate
summary: Post-mortem — The backing PostgreSQL database began returning extremely slow queries (p99 = 9.52 s, ~100× above healthy baseline). Slo
sources:
  - rhbk-26-4-db
  - rhbk-26-6-single-cluster-introduction
provenance:
  extracted: 2
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-06-28
---

# KeycloakHighServerErrorRate — DB Connection Pool Exhaustion via Slow Queries (2026-06-28)

> ⚠️ Out of corpus coverage — `keycloak` holds `conceptual, support-kb` only; this is a `scenarios` question and that tier is not ingested; verify against the primary source.

**Root cause.** The backing PostgreSQL database began returning extremely slow queries (p99 = 9.52 s, ~100× above healthy baseline). Slow queries held Agroal JDBC connections for much longer than normal, driving the pool to its hard ceiling of 100 active connections (agroal_active_count=100, agroal_available_count=0). With no free connections, 37 inbound /token threads queued (agroal_awaiting_count=37), each waiting an average of 8,021 ms before timing out. Those timeouts propagated as HTTP 500 responses, producing the observed 10.4% 5xx error rate. The Keycloak JVM (up=1) and CPU (0.6 load avg) were healthy — the fault was entirely in the database layer driving pool starvation.

## Evidence
Metric chain (all job="keycloak", instant query at incident time 2026-06-28):

1. ERROR RATE
   http_requests_total{status="500"} = 1.4 req/s
   http_requests_total{status="200"} = 12.0 req/s
   → 1.4 / (1.4+12.0) = 10.4% 5xx rate on /token

2. DB QUERY LATENCY (primary fault)
   keycloak_database_query_duration_seconds{quantile="0.99"} = 9.52 s
   → p99 DB query time ~10× what it should be; queries holding connections far too long

3. CONNECTION POOL EXHAUSTION (cascade)
   agroal_active_count    = 100  (pool at hard ceiling)
   agroal_max_used_count  = 100  (confirmed ceiling = 100)
   agroal_available_count = 0    (zero connections free)
   agroal_awaiting_count  = 37   (37 threads blocked waiting)
   agroal_blocking_time_average_milliseconds = 8,021 ms (avg wait > 8 s → timeout → 5xx)

4. RULED OUT
   up{job="keycloak"} = 1                  → process alive, not a crash
   system_cpu_load_average_1m = 0.6        → CPU not saturated
   iface_input_errors / crc_errors = []    → no layer-1/2 fault
   bgp_peer_state / ospf_neighbor_state = [] → no routing-protocol fault

Root-cause chain:
  Slow DB queries (p99 9.52 s)
  → connections held longer than normal
  → Agroal pool exhausted (100/100 active, 0 available)
  → 37 /token threads blocked (avg 8 s wait)
  → thread wait exceeds Keycloak's acquisition timeout
  → HTTP 500 returned to clients

## See also
- [[rhbk-26-4-db]]
- [[rhbk-26-6-single-cluster-introduction]]

## Occurrences
- 2026-06-28 — The backing PostgreSQL database began returning extremely slow queries (p99 = 9.52 s, ~100× above healthy baseline). Slow queries held Agroal JDBC connections for much longer than normal, driving the 
