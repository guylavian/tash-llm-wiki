---
title: "Active-Passive site failover with external Data Grid — why users got kicked out and had to re-login"
type: question
question_tier: support-kb
domain: keycloak
slug: active-passive-failover-sessions-lost
summary: "In an RHBK Active-Passive multi-site setup with external Data Grid, sessions lost on failover means one of the critical durability layers is missing or misconfigured: the `sessions` cache is NOT cross-site replicated, so session survival depends entirely on DB persistence + synchronous DB replication. The most common causes are (1) `multi-site` feature flag not enabled, (2) volatile sessions (`persistent-user-sessions` disabled), (3) database not synchronously replicated, or (4) a single Data Grid cluster instead of two with Cross-DC."
sources:
  - guide:high_availability_guide
  - kb:concepts-multi-site
  - kb:multi-cluster-introduction
  - kb:caching
  - ref:high-availability.md
source_notes:
  - "[[rhbk-26-2-concepts-multi-site]]"
  - "[[rhbk-26-6-multi-cluster-introduction]]"
provenance_extracted: 12
provenance_inferred: 4
provenance_ambiguous: 0
tags: [ha, tokens]
status: reviewed
updated: 2026-06-22
---

# Active-Passive site failover with external Data Grid — why users got kicked out and had to re-login

**Your users were forced to re-authenticate because the user sessions created on the primary site were unavailable on the passive site after failover. This should NOT happen in a correctly configured multi-cluster deployment — sessions are designed to survive a site failure — but there is a critical architectural constraint you may have missed: the `sessions` cache is NOT cross-site replicated, so session durability depends entirely on a chain of prerequisites, any one of which being broken causes total session loss.**

---

## The architectural truth: the `sessions` cache is not cross-site replicated

This is the single most important fact about session persistence in the multi-cluster Active-Passive model.

In the documented external Data Grid blueprint, exactly **four** caches are synchronously replicated between the two sites via Data Grid Cross-DC (rhbk-26-2-deploy-infinispan-kubernetes-crossdc):

| Cache | Cross-site? | Purpose |
|-------|------------|---------|
| `authenticationSessions` | **Yes** — `strategy: "SYNC"` | In-flight login state (not DB-persistent) |
| `actionTokens` | **Yes** — `strategy: "SYNC"` | Forgot-password / email-verification tokens (not DB-persistent) |
| `loginFailures` | **Yes** — `strategy: "SYNC"` | Brute-force tracking data |
| `work` | **Yes** — `strategy: "SYNC"` | Cross-site invalidation messages |

**`sessions`, `clientSessions`, `offlineSessions`, and `offlineClientSessions` — the caches holding your users' actual SSO sessions — are NOT cross-site replicated.** They are managed as **local caches** within each site's RHBK pods, loaded on demand from the database (rhbk-26-4-multi-cluster-introduction, §3.7.2; [[distributed-caches]]).

This means session survival across a site failure relies on **this chain**, not on the Data Grid:

```
Sessions created on primary site
  → persisted to database by persistent-user-sessions
    → database replicates synchronously to passive site's DB
      → passive site RHBK loads session from DB into local cache on first request
```

Break any link, and users get kicked out.

---

## Root cause analysis — which link broke?

### Cause 1 (most likely): The `multi-site` feature flag was NOT enabled on the Keycloak CR

Without `spec.features.enabled: [multi-site]` on the `Keycloak` CR, RHBK does **not** enter multi-cluster operating mode. Consequences:

- The `/lb-check` health probe endpoint is **not exposed** — the load balancer cannot health-check the passive site properly, which may cause traffic misrouting or fail-open to a degraded site.
- `persistent-user-sessions` **can be disabled** (it is forced ON when `multi-site` is enabled — line 105-107, rhbk-26-4-caching: "Disabling persistent-user-sessions is not possible when multi-site feature is enabled"). If you or an earlier team member disabled it to reduce DB load, sessions were **volatile** — in-memory only, lost when the primary site died.
- Cross-site `work` cache invalidation may not function correctly without the RHBK server knowing it is in a multi-cluster topology.

**Verify:** Check the `Keycloak` CR — does `spec.features.enabled` contain `multi-site`? If not, fix and re-deploy (this requires a build+restart since feature flags are build-time options baked into your image, unless using `--features` at runtime).

```yaml
spec:
  features:
    enabled:
      - multi-site
```

Also confirm the companion settings are present:
```yaml
additionalOptions:
  - name: cache-remote-host              # points to Data Grid service
  - name: cache-remote-port              # 11222
  - name: cache-remote-username          # from remote-store-secret
  - name: cache-remote-password          # from remote-store-secret
  - name: spi-connections-infinispan-quarkus-site-name  # e.g. "keycloak"
```

([[multi-site-feature-flag]], [[external-data-grid-operator]], rhbk-26-2-deploy-keycloak-kubernetes)

### Cause 2: Volatile sessions (persistent-user-sessions disabled)

If `persistent-user-sessions` was explicitly disabled (`--features-disabled=persistent-user-sessions`), user sessions lived **only in the Infinispan cache** — never written to the database. Since the `sessions` cache is **not** cross-site replicated, the passive site had no copy. When the primary site died, every session was destroyed.

Symptoms of this misconfiguration:
- `OFFLINE` sessions survive failover (these ARE stored in the DB even without `persistent-user-sessions` — [[tokens-and-sessions]])
- Online SSO sessions do NOT survive
- If you check the `user_session` table in the DB after a primary site failure, it has no entries for online sessions

The guide is explicit about the trade-off (rhbk-26-4-caching, §10.2.2):
> "Losing sessions when all Red Hat build of Keycloak nodes restart."

But in a multi-site setup this is fatal, which is why the `multi-site` feature flag prevents it.

**Verify:** Check your server config or build command for `--features-disabled=persistent-user-sessions`. If found and `multi-site` is also enabled, the server should have rejected this at startup — check logs for an error about the conflict. If `multi-site` was NOT enabled, you may have been running volatile sessions unknowingly.

### Cause 3: Database is NOT synchronously replicated across sites

The entire durability model of the multi-cluster topology assumes a **synchronously replicated database** across both sites (rhbk-26-4-multi-cluster-introduction, §3.7.6):

> "A synchronously replicated database ensures that data written in one site is always available in the other site after site failures and no data is lost."

If your DB uses asynchronous replication (e.g., standard Aurora Read Replicas, standard PostgreSQL streaming replication with `synchronous_standby_names` not configured), session data written to the primary site's DB may **not have arrived** at the passive site's DB at the moment of failure. The passive site's RHBK loads the session from its local DB copy → not found → user is unknown → must re-authenticate.

Additionally, if the DB failover itself was not automatic (manual promotion of a standby), the passive site may have been unable to connect to a writable DB at all during the failover window.

**Verify:** Check your DB configuration. Aurora must use **multi-AZ** with synchronous replication. PostgreSQL (or CloudNativePG) must have quorum-based synchronous replication configured. See the tested configuration in the HA guide: "High availability with a primary DB instance in one availability zone, and a synchronously replicated reader in the second availability zone."

### Cause 4: Single Data Grid cluster instead of two with Cross-DC

The phrase "external Infinispan" is ambiguous. The blueprint requires **two** independent Data Grid clusters (one per site) connected via Data Grid Cross-DC with the **Gossip Router** (rhbk-26-4-multi-cluster-introduction, §3.8.5). If you instead deployed:

- **One** Data Grid cluster shared across both sites (via network): when the primary site goes down, the Data Grid goes with it.
- Two Data Grid clusters but **without Cross-DC replication** configured: the passive site's Data Grid has no session data from the primary site.

Both scenarios leave the passive site with empty session caches.

### Cause 5: Prior degradation — the silent time bomb

The "no data loss" guarantee has a critical footnote in the HA guide (rhbk-26-4-multi-cluster-introduction, §3.7.4, table footnote 3):

> "The statement 'No data loss' depends on the setup not being degraded from previous failures, which includes completing any pending manual operations to resynchronize the state between the sites."

If a previous connectivity blip caused a synchronous Data Grid request to fail, the two sites silently drifted out of sync. This is **difficult to monitor** and goes undetected (same section, §3.7.5: "The sites can become out of sync when a synchronous Data Grid request fails. This situation is currently difficult to monitor."). When the primary site then failed, the re-sync had never been done — the guarantee was already void.

**Verify:** Check `site push-site-status --cache=actionTokens` (and the other 3 cross-site caches) to see if both sites report `"OK"`. Compare cache entry counts between sites. Check RHBK logs for synchronous replication timeout errors.

### Cause 6: Session cookie / hostname mismatch

If the two sites have different `--hostname` settings or if the load balancer presents a different URL to the passive site, the user's browser may not send the `KEYCLOAK_IDENTITY` session cookie (different domain, different cookie path). This looks exactly like "got kicked out" but is actually a routing/cookie-persistence issue, not a data-loss issue.

**Verify:** Check `spec.hostname` on both sites' `Keycloak` CRs. They should use the same load-balanced URL. Cookie domain must match.

---

## What to configure differently — the checklist

### 1. Enable the `multi-site` feature flag

```yaml
spec:
  features:
    enabled:
      - multi-site
```

This forces `persistent-user-sessions` ON, exposes `/lb-check`, and activates multi-cluster session handling. Add the companion `additionalOptions` for the remote store connection ([[multi-site-feature-flag]], [[external-data-grid-operator]]).

### 2. Ensure DB-persistent sessions

With `multi-site` enabled, `persistent-user-sessions` is forced on — you cannot disable it. Verify no one has overridden this at build time.

On RHBK 26.x, `persistent-user-sessions` is enabled by default. It stores both online and offline user sessions in the database (rhbk-26-0-release_notes: "stores online user sessions and online client sessions in both memory and the database. As a result, a user can stay logged in even if all instances of Red Hat build of Keycloak are restarted").

### 3. Synchronously replicated database

Configure your database for synchronous replication across both sites. The tested config is Aurora PostgreSQL multi-AZ with a primary writer in one AZ and a synchronous reader in the other. For CloudNativePG, configure quorum-based synchronous replication.

All DB connection pool sizes (`poolMinSize`, `poolInitialSize`, `poolMaxSize`) should be equal to avoid connection-creation overhead during failover spikes ([[rhbk-db-connection-pool]]).

### 4. Two Data Grid clusters with Cross-DC, one per site

Deploy the Data Grid Operator in **both** clusters. Create an `Infinispan` CR in each with:
- `spec.service.type: DataGrid`
- `spec.sites.local.name: site-a` (or `site-b`)
- Cross-site locations pointing to the other site
- TLS encryption for JGroups sockets

Then create **four** `Cache` CRs per site — one each for `actionTokens`, `authenticationSessions`, `loginFailures`, `work` — all with `backups: site-x: backup: strategy: "SYNC" failurePolicy: "FAIL"`.

(RHBK requires exactly these four caches to be present in Data Grid — [[external-data-grid-operator]], rhbk-26-2-deploy-infinispan-kubernetes-crossdc)

### 5. Monitor for degradation (this is critical)

The model is consistency-first but **not self-healing**. After any replication blip, manual re-sync is required. Proactively monitor:

- Data Grid cross-site push status: `site push-site-status --cache=actionTokens` — all caches should return `"OK"` for the remote site
- Cache entry counts on both sites — significant divergence = drift
- RHBK logs for synchronous replication timeouts
- The observability guide provides Data Grid cache metrics for this: `vendor_cache_manager_X_site_status` (rhbk-26-4-observability_guide, §5.10.3)

### 6. Enable sticky sessions at the load balancer

Keep OpenShift's default source-IP sticky sessions enabled. After failover, the passive site's local sessions cache is cold. Every first request per user will hit the DB to load their session. Sticky sessions keep each user pinned to one pod, avoiding cross-pod "thrashing" as each pod independently loads the same session from the DB. You can disable sticky sessions for load tests, but re-enable for production.

### 7. Use a static-IP load balancer, not DNS failover

The blueprint uses AWS Global Accelerator (static anycast IP) because client DNS caching makes DNS-based failover unreliable ([[ha-load-balancer-failover]]). The LB must health-check `/lb-check` (only available with `multi-site` flag). On non-AWS platforms, provide an equivalent static-IP failover LB.

### 8. Be ready for the ~5-min downtime window

The HA guide documents that some failure/switchover scenarios incur up to 5 minutes of downtime ([[rhbk-ha-architectures]]). Users whose requests arrive during this window will get errors, which they may interpret as "got kicked out." After the window, they should be able to use their existing session. If they had to log in again after the 5-min window, one of the causes above is the real culprit.

---

## Summary: the session survival chain

```
multi-site feature flag ON
  → persistent-user-sessions forced ON
    → sessions written to DB
      → DB synchronously replicated across sites
        → passive site RHBK can load sessions from DB on failover
          → users stay logged in ✓
```

Missing the feature flag, using volatile sessions, async DB replication, or a single Data Grid cluster breaks the chain and sessions are lost. The `sessions` cache not being cross-site replicated is by design — it's the DB that carries the durability guarantee, not the cache.

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **kb:multi-cluster-introduction** (rhbk-26-4-multi-cluster-introduction) — Chapter 3. Multi-cluster deployments, RHBK 26.4 HA Guide: deployment architecture, data storage patterns (sessions in DB + local caches), synchronous replication requirements, failure modes, conditional "no data loss" guarantee, out-of-sync monitoring gap
- **kb:concepts-multi-site** (rhbk-26-2-concepts-multi-site) — Chapter 2. Concepts for multi-site deployments, RHBK 26.2 HA Guide: same architecture, synchronous Data Grid + DB replication rationale, consistency-over-availability trade-off
- **kb:caching** (rhbk-26-4-caching) — Chapter 10. Configuring distributed caches, RHBK 26.4 Server Configuration Guide: volatile sessions vs persistent sessions, "Disabling persistent-user-sessions is not possible when multi-site feature is enabled" (lines 105-107), 4 caches that cannot have max-count set
- **kb:deploy-infinispan-kubernetes-crossdc** (rhbk-26-2-deploy-infinispan-kubernetes-crossdc) — Chapter 9. Deploying Data Grid for HA: the exact 4 caches created with cross-site SYNC replication (`actionTokens`, `authenticationSessions`, `loginFailures`, `work`)
- **kb:deploy-keycloak-kubernetes** (rhbk-26-2-deploy-keycloak-kubernetes) — Chapter 10. Deploying RHBK for HA with the Operator: CR settings including `multi-site` flag, `cache-remote-*` options, `spi-connections-infinispan-quarkus-site-name`
- **rhbk-26-0-release_notes** — §1.14.6: persistent-user-sessions default-on behavior: "stores online user sessions and online client sessions in both memory and the database"
- **doc-7135882** — gated KB: volatile sessions = all users logged out on full restart, async cleanup behavior

### Wiki (cross-linked synthesis pages)

- [[ha-cross-site]] — Multi-cluster / cross-site Active-Passive HA topology overview
- [[rhbk-ha-architectures]] — The two HA shapes (single-cluster vs multi-cluster), decision criteria
- [[distributed-caches]] — Cache types (sessions/clientSessions/authenticationSessions/etc.) and their replication scope
- [[session-persistence-volatile]] — DB-backed vs volatile sessions, the trade-off explained
- [[external-data-grid-operator]] — External Data Grid deployment with the Data Grid Operator
- [[multi-site-feature-flag]] — The feature flag that gates multi-cluster mode
- [[ha-load-balancer-failover]] — Static-IP failover LB with `/lb-check` health probing
- [[site-synchronization]] — Manual re-sync procedure after a degradation
- [[active-passive-session-consistency-failover]] — Prior Q&A on what is lost on failover
- [[rhbk-db-connection-pool]] — Equal min/initial/max pool sizing for HA

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-high_availability_guide|keycloak reference — high_availability_guide]]
- [[rhbk-26-2-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
- [[rhbk-26-6-multi-cluster-introduction|Chapter 3. Multi-cluster deployments]]
- [[rhbk-26-4-caching|Chapter 10. Configuring distributed caches]]
- [[references/high-availability|Red Hat build of Keycloak 26.6 — High Availability & Clustering]]
<!-- crosslink:end -->
