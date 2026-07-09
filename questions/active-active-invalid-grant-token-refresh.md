---
title: "RHBK 26 cross-site Active-Active — intermittent 'invalid_grant' on token refresh with sticky sessions ON"
type: question
question_tier: support-kb
domain: keycloak
slug: active-active-invalid-grant-token-refresh
summary: "Running RHBK 26 in a two-site Active-Active topology with a shared external Data Grid and round-robin + sticky sessions produces intermittent 'invalid_grant' on token refresh — not primarily a stickiness, replication-lag, or clock problem, but an architecture mismatch: the documented model is Active/Passive, and the Active-Active round-robin causes session-cache churn across sites (local caches are cold for sessions from the other site, triggering DB round-trips under load), plus potential 'work' cache deadlocks (explicitly warned against in the guide for active-active setups). Sticky sessions help but cannot eliminate cross-site routing under load, and a single shared Data Grid cluster (instead of two with Cross-DC) adds latency and split-brain risk."
sources:
  - guide:high_availability_guide
  - kb:multi-cluster-introduction
  - kb:concepts-multi-site
  - kb:deploy-infinispan-kubernetes-crossdc
  - kb:deploy-keycloak-kubernetes
  - kb:deploy-aws-accelerator-loadbalancer
  - ref:high-availability.md
provenance:
  extracted: 12
  inferred: 5
  ambiguous: 0
symptoms:
  - "invalid_grant on POST /realms/<realm>/protocol/openid-connect/token with grant_type=refresh_token"
  - "intermittent user logout / 'Session not active' errors"
  - "symptoms intensify under load (more concurrent users)"
  - "sticky sessions enabled at the load balancer — no help"
tags: [tokens]
status: reviewed
updated: 2026-06-22
---

# RHBK 26 cross-site Active-Active — intermittent 'invalid_grant' on token refresh

**The short answer: none of the three hypotheses is the root cause in isolation. The real problem is running an Active-Active topology that the product does not document or test as Active-Active — the supported model is Active/Passive. The Active-Active round-robin causes session-cache churn across sites that spikes DB connections under load, and the guide explicitly warns that deadlocks may occur in active-active setups.**

---

## The three hypotheses — evaluated

### H1: Load-balancer stickiness problem — partial contributor, not root cause

Sticky sessions (source-IP affinity) are ON. They should keep a given user pinned to the same RHBK pod within its site. Under load, however:

- **Sticky session table overflow.** Some LBs (especially L4 NLBs) have finite session tables. Under high concurrent-user counts, older entries get evicted and the fallback is round-robin. The user's next refresh lands on a different pod, possibly in the other site.
- **Pod restart under load.** If an RHBK pod is OOMKilled or restarted, the user pinned to it is re-routed — the LB picks a random healthy backend, potentially on the other site.
- **Even with perfect stickiness**, pods within a site are behind a Service, and the in-site routing among pods of a StatefulSet is also governed by the LB's session affinity.

When a refresh hits Site B's RHBK for a session created on Site A, the session is NOT in Site B's pod local cache. The `sessions` cache is NOT cross-site replicated — it's a **local cache** loaded on demand from the database ([[active-passive-failover-sessions-lost]], [[distributed-caches]]). If `persistent-user-sessions` is ON (default in RHBK 26, forced ON by `multi-site` feature flag), Site B loads the session from the DB — which requires a synchronous DB round-trip. Under load, DB connection pool exhaustion causes timeouts → `invalid_grant`.

> **Verdict:** Stickiness helps but is not sufficient. It masks the underlying architecture tension; under load the mask slips.

### H2: Infinispan replication-lag problem — not the cause for sessions

The Infinispan/Data Grid layer in the multi-cluster topology has a critical design constraint that most troubleshooting overlooks:

- **`sessions`, `clientSessions`, `offlineSessions`, and `offlineClientSessions` are NOT cross-site replicated.** Only four caches are synchronously replicated via Data Grid Cross-DC: `authenticationSessions`, `actionTokens`, `loginFailures`, and `work` ([[active-passive-failover-sessions-lost]], rhbk-26-2-deploy-infinispan-kubernetes-crossdc).
- Sessions live in the **synchronously replicated database** as the source of truth. The local RHBK caches are just that — caches of DB data. So "Data Grid replication lag" for sessions is a category error: sessions don't travel through Data Grid across sites.
- The `work` cache (replicated, cross-site) carries **invalidation messages**, not session data. If cross-site `work` replication fails, sites silently drift — but this causes stale-cache issues (e.g. a revoked session appearing active), not `invalid_grant` on refresh.

However, with a **single shared Data Grid cluster** (as described: "both backed by a shared external Infinispan cluster") instead of **two clusters with Cross-DC** (the documented blueprint), there is no Data Grid cross-site replication at all. The single cluster must span the WAN link between sites, which adds latency and partition risk to the `work` cache operations — making invalidation failures and deadlock conditions more likely.

> **Verdict:** Not the cause for session-based `invalid_grant` — sessions don't depend on Data Grid for cross-site replication. But a single shared Data Grid cluster (vs. two with Cross-DC) introduces latency and network-partition risks to the `work` cache that can cause write failures and deadlocks (inferred).

### H3: Token/clock problem across sites — not the primary cause

RHBK 26.6 increased the default clock-skew tolerance for JWT `iat` (issued-at) checks from 0 to 10 seconds (rhbk-26-6-migration-changes, §2.2.10). This was a fix for token-validation failures on nodes with slightly unsynchronized clocks.

However:

- Clock skew issues affect **all** requests deterministically, not intermittently or under load. An `invalid_grant` caused by clock skew would be reproducible for every affected user.
- The refresh-token grant (`grant_type=refresh_token`) validates the refresh token against the user session's expiry in the DB — it does not gate on `iat` clock skew the way signed JWT assertions do.
- The gated KB solution `_gated-kb-index.md` line 2614 documents "Private Key JWT authentication fails with 'token is not active' when clock skew exceeds 15 seconds" — but that's JWT client assertions, not refresh-token grants.

> **Verdict:** Not the primary cause. If clock skew were the issue, it would be deterministic, not load-sensitive.

---

## The real root cause

### The documented model is Active/Passive — you are running Active/Active

The RHBK High-Availability Guide explicitly documents a **two-site Active/Passive** topology ([[rhbk-ha-architectures]], [[ha-cross-site]]). The load balancer in the AWS blueprint sends equal weight-128 traffic to both sites when both are healthy (rhbk-26-6-multi-cluster-introduction, line 841), which looks like "active-active" at the network layer — but the **data model is Active/Passive**:

1. **Sessions are local caches** — Each site's RHBK pods cache sessions as local (not distributed) caches loaded from the DB. There is no cross-site session replication.
2. **The `work` cache is the cross-site coherency bus** — Invalidation messages flow cross-site via Data Grid Cross-DC. The HA guide explicitly warns (rhbk-26-6-multi-cluster-introduction, line 670): > **"Deadlocks may occur in an active-active setup as entries are modified concurrently in both sites."**
3. **The 4 cross-site caches use `NON_DURABLE_XA` + `FAIL` failure policy** — When a deadlock occurs, the transaction rolls back and RHBK retries. Under high load (many concurrent refresh requests modifying session state), this retry storm amplifies response times and can produce `invalid_grant` errors.

### Three specific failure modes from Active/Active with round-robin

#### Mode 1: Session-cache churn across sites (primary cause of `invalid_grant`)

User authenticates → session created on Site A → session stored in Site A's local cache AND in the DB (replicated to Site B's DB). On refresh:

- **If the refresh hits Site A** (perfect stickiness): session found in local cache → refresh succeeds with no DB round-trip.
- **If the refresh hits Site B** (stickiness fails under load, pod restart, or sticky-table overflow): Site B's RHBK checks its local cache → miss → must load the session from the DB.

Under load, **every cross-site refresh incurs a synchronous DB read**. If the DB connection pool (`poolMaxSize`) is not sized for the additional cross-site load (each site must serve both its own sessions AND sessions created on the other site), connections queue up and time out. The token endpoint returns `invalid_grant` because the session lookup failed.

The guide recommends setting `poolMinSize`, `poolInitialSize`, and `poolMaxSize` to equal values ([[rhbk-db-connection-pool]]) — but in an Active/Active setup, each site effectively needs double the usual pool to handle the imported session lookups.

#### Mode 2: `work` cache deadlocks under concurrent cross-site writes

The `work` cache carries invalidation messages between sites when session/cache data is modified. In a true Active-Active setup where **both sites serve and modify sessions concurrently**, the pessimistic locking + `NON_DURABLE_XA` mode (rhbk-26-6-multi-cluster-introduction, lines 660-683) can produce deadlocks:

> "Deadlocks may occur in an active-active setup as entries are modified concurrently in both sites. The `transaction.mode: NON_DURABLE_XA` ensures that the transaction is rolled back keeping the data consistent if this occurs."

Each deadlock → rollback → RHBK retry. Under high load, the retry rate compounds → some requests exceed their retry budget → `invalid_grant`. This is the product's own documentation telling you not to do what you are doing.

#### Mode 3: Single shared Data Grid cluster (not two with Cross-DC)

The documented blueprint requires **two** Data Grid clusters (one per site) connected via Cross-DC with the Gossip Router ([[external-data-grid-operator]], rhbk-26-2-deploy-infinispan-kubernetes-crossdc). A **single shared Data Grid cluster** across both sites:

- Requires the Data Grid cluster to span the WAN link, which introduces latency on every cache operation.
- Creates a single point of failure for the entire session/cache layer.
- Lacks the Cross-DC failure-isolation properties; a network partition can cause split-brain in the Data Grid itself.
- The `work` cache (replicated, cross-site) doesn't function correctly without Data Grid Cross-DC, because a single Data Grid cluster can't distinguish "sites" for site-level offline/online operations.

---

## Verification checklist

### 1. Confirm the architecture mismatch (most important)

Check whether your setup matches the documented blueprint:

| Aspect | Documented blueprint (Active/Passive) | Your setup (Active-Active) |
|--------|--------------------------------------|---------------------------|
| Load balancer traffic | Weight 128 to both sites, failover on health | Round-robin, both sites serve |
| Site roles | One active, one standby (or both receiving but session affinity expected to keep users on their home site) | Both sites fully active |
| Data Grid | **Two** clusters with Cross-DC + Gossip Router | **One** shared cluster |
| Feature flag | `multi-site` enabled | `multi-site` enabled |
| Session persistence | `persistent-user-sessions` forced ON by `multi-site` | Should be ON |

### 2. Check the `multi-site` feature flag

Without `spec.features.enabled: [multi-site]` on the `Keycloak` CR:
- `/lb-check` is not exposed → LB health-checking may be incorrect
- `persistent-user-sessions` can be disabled → sessions may be volatile ([[multi-site-feature-flag]], [[active-passive-failover-sessions-lost]])

### 3. Check DB connection pool sizing

```
oc get keycloak/<name> -o yaml | grep -A5 pool
```
The guide recommends equal `poolMinSize`, `poolInitialSize`, and `poolMaxSize` for HA ([[rhbk-db-connection-pool]]). In an Active-Active setup, multiply the recommended size by 2 to account for cross-site session loads.

### 4. Check for `work` cache deadlock symptoms

Search RHBK logs for:
- Transaction rollback or deadlock errors
- Synchronous replication timeout messages
- Data Grid `FAIL` failure policy messages

### 5. Check Data Grid deployment topology

```sh
oc get infinispan -n keycloak -o yaml | grep -A10 spec.sites
```
If you see only one `Infinispan` CR (a single cluster) instead of two (one per site, each with `spec.sites.local.name` and `spec.sites.locations` for the remote site), you are running a single-cluster topology, not the two-cluster Cross-DC blueprint required for multi-site ([[external-data-grid-operator]]).

### 6. Monitor site drift

Check the four cross-site Data Grid caches for synchronization status:
```sh
oc exec -it pods/infinispan-0 -- ./bin/cli.sh --trustall \
  --connect https://127.0.0.1:11222 -c "site push-site-status --cache=work"
```
Each cache should return `"OK"` for the remote site. Diverging entry counts between sites indicate drift ([[site-synchronization]], [[active-passive-failover-sessions-lost]]).

---

## Recommended fixes (in priority order)

### 1. Switch to the documented Active/Passive topology

Configure the load balancer to send traffic to one site only, with the other on standby. This is the supported model. The AWS Global Accelerator blueprint ships with equal weight-128 for both sites, but that's for **health-checked failover** — when both sites are healthy the traffic splits, but the model is still *consistency-first* and the expectation is that most sessions are served by the site that owns them ([[ha-load-balancer-failover]]).

For true load distribution, ensure sticky sessions work reliably and consider that cross-site session loads are expensive (DB round-trip for every request that lands on the wrong site).

### 2. If you must run both sites serving traffic, maximize stickiness

- Verify the LB sticky session mechanism works under your peak load (test with sustained traffic at the expected peak).
- Ensure the LB sticky table size accommodates your concurrent user count × 2 headroom.
- Set the RHBK `instances` count high enough that individual pod restarts don't cause widespread re-routing.
- Monitor the cross-site request ratio: if >10% of requests cross sites, your stickiness is not working.

### 3. Size the DB connection pool for cross-site load

Each site must handle sessions from both sites. Set:
```yaml
additionalOptions:
  - name: poolMinSize
    value: "20"    # double the usual per-site sizing
  - name: poolInitialSize
    value: "20"
  - name: poolMaxSize
    value: "20"    # equal to min/initial for HA
```

### 4. Deploy two Data Grid clusters with Cross-DC

Replace the single shared Data Grid cluster with two clusters (one per site) connected via Data Grid Cross-DC. Follow the blueprint verbatim from [[external-data-grid-operator]] and rhbk-26-2-deploy-infinispan-kubernetes-crossdc. This gives you:
- Proper cross-site cache replication for `authenticationSessions`, `actionTokens`, `loginFailures`, `work`
- Site-level failure isolation
- The Gossip Router for cross-site discovery
- The ability to take a site offline/online for re-sync

### 5. Monitor and plan for manual re-sync after degradation

The "no data loss" guarantee only holds in a non-degraded state. After any cross-site replication failure, manual re-sync is required ([[site-synchronization]]). Without it, a subsequent failure can lose sessions silently.

---

## Summary

| Hypothesis | Role | Why |
|------------|------|-----|
| **Stickiness problem** | Partial contributor | Sticky sessions mask the architecture tension but fail under load (table overflow, pod restart) |
| **Data Grid replication lag** | Not the cause for sessions | `sessions` cache is NOT cross-site replicated — sessions come from the DB. A single shared cluster (vs two with Cross-DC) adds latency and partition risk to the `work` cache, amplifying the deadlock problem |
| **Clock skew** | Not the cause | Clock problems are deterministic, not load-sensitive |
| **Architecture mismatch** | **Root cause** | The documented model is Active/Passive. Active-Active with round-robin causes session-cache churn (cold local caches → DB spikes under load) and `work` cache deadlocks (warned in the guide) |

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **kb:multi-cluster-introduction** (rhbk-26-6-multi-cluster-introduction) — Chapter 3. Multi-cluster deployments, RHBK 26.6 HA Guide: "Deadlocks may occur in an active-active setup" (line 670), deployment data storage pattern (line 72: "data is also cached in the Red Hat build of Keycloak Infinispan caches as local caches"), failure tables
- **kb:concepts-multi-site** (rhbk-26-2-concepts-multi-site) — Chapter 2. Concepts for multi-site deployments, RHBK 26.2 HA Guide: synchronous Data Grid + DB replication rationale, out-of-sync monitoring gap
- **kb:deploy-infinispan-kubernetes-crossdc** (rhbk-26-2-deploy-infinispan-kubernetes-crossdc) — Chapter 9. Deploying Data Grid for HA: the 4 cross-site caches (`actionTokens`, `authenticationSessions`, `loginFailures`, `work`) with SYNC backup strategy, `NON_DURABLE_XA`, `FAIL` failure policy, and deadlock warning
- **kb:deploy-keycloak-kubernetes** (rhbk-26-2-deploy-keycloak-kubernetes) — Chapter 10. Deploying RHBK for HA with the Operator: `multi-site` feature flag, `cache-remote-*` options, remote store connection
- **kb:deploy-aws-accelerator-loadbalancer** (rhbk-26-2-deploy-aws-accelerator-loadbalancer) — Chapter 11. AWS Global Accelerator load balancer blueprint: weight 128 to both sites, `/lb-check` health probe
- **kb:operate-synchronize** (rhbk-26-2-operate-synchronize) — Chapter 15. Synchronizing sites: manual re-sync procedure
- **rhbk-26-6-migration-changes** (rhbk-26-6-migration-changes) — §2.2.10: default clock-skew increased to 10 seconds for JWT `iat` checks
- **kb:caching** (rhbk-26-4-caching) — Chapter 10. Configuring distributed caches: `persistent-user-sessions` forced ON when `multi-site` enabled; sessions cache type
- **doc-7135882** — gated KB: volatile sessions behavior and cleanup

### Wiki (cross-linked synthesis pages)

- [[active-passive-failover-sessions-lost]] — Prior Q&A: sessions NOT cross-site replicated; DB is the source of truth; failure chain analysis
- [[active-passive-session-consistency-failover]] — Prior Q&A: how sessions stay consistent across sites, what degrades the guarantee
- [[ha-cross-site]] — Multi-cluster/cross-site HA topology overview
- [[rhbk-ha-architectures]] — The two HA shapes (single-cluster vs multi-cluster); Active/Passive only constraint
- [[distributed-caches]] — Cache types and their replication scope; sessions as local caches in multi-cluster
- [[session-persistence-volatile]] — DB-backed vs volatile sessions; impact on multi-site durability
- [[external-data-grid-operator]] — External Data Grid with Cross-DC; two-cluster requirement
- [[multi-site-feature-flag]] — Feature flag that gates multi-cluster mode and forces `persistent-user-sessions`
- [[ha-load-balancer-failover]] — LB blueprint with sticky sessions, `/lb-check`, failover behavior
- [[site-synchronization]] — Manual re-sync procedure after site drift
- [[rhbk-db-connection-pool]] — Equal pool sizing for HA; cross-site load multiplier
- [[tokens-and-sessions]] — Token lifespans, refresh token rotation, session idle/max timeouts
- [[oidc-client-best-practices]] — Refresh token handling: single-flight, atomic rotation storage, `invalid_grant` → re-auth
- [[troubleshooting-index]] — Triage map (HA/infinispan section)

### Upstream

- **RFC 9700** — OAuth 2.0 Security BCP: refresh token rotation, sender-constrained tokens, minimizing token lifetimes (cited in [[oidc-client-best-practices]])

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-multi-cluster-introduction|Chapter 3. Multi-cluster deployments]]
- [[rhbk-26-2-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
- [[rhbk-26-2-deploy-infinispan-kubernetes-crossdc|Chapter 9. Deploying Data Grid for HA with the Data Grid Operator]]
- [[rhbk-26-2-deploy-keycloak-kubernetes|Chapter 10. Deploying Red Hat build of Keycloak for HA with the Operator]]
- [[rhbk-26-2-deploy-aws-accelerator-loadbalancer|Chapter 11. Deploying an AWS Global Accelerator load balancer]]
<!-- crosslink:end -->
