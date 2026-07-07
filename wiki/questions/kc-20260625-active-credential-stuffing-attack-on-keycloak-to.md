---
title: KC-20260625: Active Credential Stuffing Attack on Keycloak Token Endpoint
type: question
domain: keycloak
slug: kc-20260625-active-credential-stuffing-attack-on-keycloak-to
summary: Post-mortem — Active credential stuffing attack targeting POST /realms/{realm}/protocol/{protocol}/token on keycloak:9000. An external
sources:
  - rhbk-26-4-mitigating-security-threats
  - rhbk-26-4-assembly-managing-clients-server-administration-guide
provenance:
  extracted: 2
  inferred: 1
  ambiguous: 0
tags: [users]
status: draft
updated: 2026-06-25
---

# KC-20260625: Active Credential Stuffing Attack on Keycloak Token Endpoint

**Root cause.** Active credential stuffing attack targeting POST /realms/{realm}/protocol/{protocol}/token on keycloak:9000. An external actor is submitting a high and accelerating volume of token grant requests with invalid credentials. This is NOT a misconfiguration: the 401 rate is accelerating (1m rate 1.08 req/s vs 5m rate 0.49 req/s — a 3× spike), the token endpoint has a 100% 401 rate with zero successful grants, and every other endpoint is idle. Brute-force detection is not enabled (default Keycloak state), so the attack is unchecked.

## Evidence
1. ALERT (17:27:43 UTC): KeycloakHighAuthFailureRate fired — sum(rate(http_server_requests_seconds_count{job="keycloak",status="401"}[1m])) > 0.1

2. URI BREAKDOWN (query_metrics, by uri+status, 1m window):
   - POST /realms/{realm}/protocol/{protocol}/token  status=401 → 1.08 req/s  ← ONLY active auth traffic
   - POST /realms/{realm}/protocol/{protocol}/token  status=200 → 0 req/s      ← ZERO successful grants
   - All other auth URIs → 0 req/s
   - /health/ready 200 → 0.04 req/s (scrape only)
   - /metrics 200 → 0.10 req/s (scrape only)

3. RATE ACCELERATION (credential stuffing signature, not flat misconfiguration):
   - 5m 401 rate: 0.49 req/s
   - 1m 401 rate: 1.08–1.48 req/s  (3× higher than 5m, still climbing)

4. SUCCESS RATIO: 14.5% overall — but that 14.5% is entirely health/metrics scraping; effective auth success rate = 0%.

5. SINGLE INSTANCE: All 401s on keycloak:9000 — no multi-node distribution that would suggest a routing problem.

6. BRUTE FORCE DETECTION: Disabled by default per RHBK 26.4 docs (rhbk-26-4-mitigating-security-threats §16.3). No account lockout or Quick Login Check is in effect, so the attack continues unthrottled.

Ruling out misconfigured client: a single bad client would produce a flat, low, steady 401 rate — not an accelerating rate with 100% failure across the entire token endpoint. Ruling out network/interface fault: no CRC/input errors, no BGP/OSPF events, health snapshot showed no interface telemetry anomalies.

## See also
- [[brute-force-detection]] — RHBK's built-in lockout defense against this attack
- [[security-hardening-checklist]] — realm hardening that blunts credential stuffing
- [[keycloak-keycloakhighauthfailurerate]] — the Prometheus alert that fires during this attack
- [[rhbk-26-4-mitigating-security-threats]]
- [[rhbk-26-4-assembly-managing-clients-server-administration-guide]]
