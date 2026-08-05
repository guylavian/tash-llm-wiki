---
title: KeycloakHighAuthFailureRate — Keys cache flushed + DB pool starvation → cascade 401s
type: question
question_tier: support-kb
domain: keycloak
slug: keycloak-keycloakhighauthfailurerate
summary: Post-mortem — The Infinispan `keys` cache was flushed (0 entries, 0 stores, 0 hits, 0 misses over a 57-minute stats window) while the 
sources:
  - rhbk-26-6-metrics-for-troubleshooting
  - rhbk-26-6-single-cluster-introduction
  - rhbk-26-6-multi-cluster-introduction
provenance:
  extracted: 3
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-06-25
graph_community: "RHBK observability stack — health, metrics, tracing, OpenTelemetry"
---

# KeycloakHighAuthFailureRate — Keys cache flushed + DB pool starvation → cascade 401s

**Root cause.** The Infinispan `keys` cache was flushed (0 entries, 0 stores, 0 hits, 0 misses over a 57-minute stats window) while the Agroal DB connection pool was configured with a hard ceiling of ~3 connections (agroal_max_used_count=3, agroal_available_count=1 at idle) — far below the RHBK-recommended minimum of 30. With the keys cache empty, every token-endpoint request requiring a realm signing key lookup was forced to the DB. The 3-connection pool was immediately exhausted under concurrent load, causing DB acquisition timeouts. Keycloak could not complete token signing or validation, producing a cascade of HTTP 401 responses on /realms/{realm}/protocol/{protocol}/token. The cache could not self-heal because every re-population attempt competed for the same exhausted pool.

## Evidence
1. vendor_statistics_number_of_entries{cache="keys"} = 0 — keys cache completely empty.\n2. vendor_statistics_stores{cache="keys"} = 0, hits = 0, misses = 0 over a 3450-second (57-min) stats window — cache was never written to or read from; not an eviction issue.\n3. vendor_statistics_evictions{cache="keys"} = 0 — confirms entries were not evicted; they were never stored (likely an admin cache-clear event).\n4. agroal_max_used_count = 3, agroal_available_count = 1, agroal_creation_count_total = 9, agroal_acquire_count_total = 53 — pool hard ceiling ~3 connections, vs. RHBK-recommended 30.\n5. Other caches healthy: realms=67 entries/0.99 hit ratio, users=2 entries/0.998 hit ratio — DB is reachable but pool is too small for the keys-cache-miss storm.\n6. vendor_cluster_size = 1 — single-node deployment, no split-brain or replication failure.\n7. http_server_requests_seconds_count{status="401", uri="/realms/{realm}/protocol/{protocol}/token"} — alert-triggering metric confirmed on keycloak:9000.

## See also
- [[kc-20260625-active-credential-stuffing-attack-on-keycloak-to]] — the attack scenario that trips this alert
- [[event-metrics]] — the login-failure event metrics this alert thresholds on
- [[server-metrics-endpoint]] — where the auth-failure counters are exposed
- [[rhbk-26-6-metrics-for-troubleshooting]]
- [[rhbk-26-6-single-cluster-introduction]]
- [[rhbk-26-6-multi-cluster-introduction]]

## Occurrences
- 2026-06-25 — The Infinispan `keys` cache was flushed (0 entries, 0 stores, 0 hits, 0 misses over a 57-minute stats window) while the Agroal DB connection pool was configured with a hard ceiling of ~3 connections (
