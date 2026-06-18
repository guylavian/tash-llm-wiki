---
title: Distributed Caches (Infinispan) in RHBK
type: entity
domain: keycloak
slug: distributed-caches
summary: "RHBK's clustering/session layer is an in-memory Infinispan data grid. Caches live either embedded in each RHBK pod (single cluster) or in an external Data Grid cluster (cross-site)"
sources:
  - guide:server_configuration_guide
  - guide:high_availability_guide
  - ref:high-availability.md
  - ref:server-configuration.md
provenance: needs-review
tags: [ha]
status: draft
updated: 2026-06-16
---

# Distributed Caches (Infinispan) in RHBK

**RHBK's clustering/session layer is an in-memory Infinispan data grid. Caches
live either embedded in each RHBK pod (single cluster) or in an external Data
Grid cluster (cross-site).**

## Two deployment shapes
- **Embedded** (default) — Infinispan runs inside each RHBK JVM/pod; pods
  discover each other and share caches. Enabled in production via `start`
  (`--cache=ispn`). `start-dev` forces `--cache=local` (not shared — dev only).
  Config: `conf/cache-ispn.xml`. On Kubernetes use a **TCP / `jdbc-ping`**
  discovery stack — the default UDP multicast usually isn't available in pods.
- **External (Red Hat Data Grid)** — a separate Data Grid cluster (Data Grid
  Operator) holds the caches and replicates them cross-site (Cross-DC). Required
  for multi-site — embedded cannot span sites. See [[ha-cross-site]].

## Caches and their types
| Cache | Type | Holds |
|---|---|---|
| realms | Local | persisted realm data (clients, roles, groups) |
| users | Local | persisted user data |
| authorization | Local | resources, permissions, policies |
| keys | Local | external public keys (≤1000, ~1h expiry) |
| work | Replicated | cache-invalidation messages between pods |
| authenticationSessions | Distributed | in-flight login state |
| sessions / clientSessions | Distributed | active user/client SSO sessions |
| offlineSessions / offlineClientSessions | Distributed | offline-token sessions |
| loginFailures | Distributed | brute-force/fraud tracking |
| actionTokens | Distributed | action tokens |

- **Local** — per-pod copy from DB; the **replicated** `work` cache broadcasts
  invalidations so other pods drop stale entries on a write.
- **Distributed** — entries spread across pods with limited owners (sessions
  default to **single owner**, 10,000 entries/pod), so any pod can serve any user.

## Caveats / gotchas
- **Session affinity:** distributed caches allow any pod to serve any user, but a
  sticky LB to the originating pod avoids cross-pod state transfer (CPU/mem/net).
- **Volatile sessions:** by default sessions persist in the **database** and load
  on-demand; you can make the cache the source of truth (lower DB load) but must
  set ≥2 owners + unlimited entries, and **all sessions are lost if every pod
  restarts**.
- Flush via kcadm: `clear-realm-cache` / `clear-user-cache` / `clear-keys-cache`.
- Cache wording is stable 26.0→26.6; cross-DC blueprint detail varies by version
  (`rhbk_kb.py show caching-`, or `--guide high_availability_guide`).

For the external-cache deployment mechanics (Operator, Cross-DC, remote-store CR
options) see [[external-data-grid-operator]]. For making the cache the source of
truth vs DB-backed sessions, see [[session-persistence-volatile]].

## See also
- [[ha-cross-site]]
- [[rhbk-ha-architectures]]
- [[external-data-grid-operator]]
- [[session-persistence-volatile]]
- [[site-synchronization]]
- [[rhbk-operator]]
- [[tokens-and-sessions]]
