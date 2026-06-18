---
title: "Active/Passive multi-site RHBK 26 — how sessions stay consistent, and what is lost on failover"
type: question
domain: keycloak
slug: active-passive-session-consistency-failover
summary: "In Active/Passive multi-site RHBK 26, the synchronously-replicated database is the durable source of truth and external Data Grid Cross-DC keeps session caches consistent between sites; a site failover loses only in-flight requests (and incurs up to ~5 min downtime), but a partial replication failure breaks the no-loss guarantee until a manual re-sync."
sources:
  - guide:high_availability_guide
  - kb:concepts-multi-site
  - kb:operate-synchronize
  - kb:deploy-infinispan-kubernetes-crossdc
provenance:
  extracted: 9
  inferred: 3
  ambiguous: 0
tags: [ha, tokens]
status: reviewed
updated: 2026-06-17
---

# Active/Passive multi-site RHBK 26 — session consistency & failover loss

**The replicated database is the durable source of truth; external Data Grid
Cross-DC keeps the session caches consistent between sites synchronously. A clean
site failover loses essentially only in-flight requests, but a *partial*
replication failure silently breaks the no-data-loss guarantee until you do a
manual re-sync.**

## How consistency is maintained

Two layers cooperate ([[ha-cross-site]], [[session-persistence-volatile]]):

1. **Database (durable, source of truth).** By default RHBK persists user
   sessions in the database and only *caches* them in Infinispan. In the
   multi-site model the DB is **synchronously replicated** across both sites
   (e.g. Aurora multi-AZ/global). Because the durable copy lives in the
   replicated DB, "no data loss on a site failure" holds even if a site is lost.

2. **External Data Grid Cross-DC (cache consistency).** Sessions are *not* held
   in embedded Infinispan — each site runs a separate **Red Hat Data Grid**
   cluster (Operator-deployed, ≥ 8.5.2), and the two clusters form a Cross-DC
   connection over **JGroups/TLS** (Gossip Router in 26.4/26.6). RHBK connects to
   it as a remote store (`cache-remote-host/-port/-username/-password` +
   `spi-connections-infinispan-quarkus-site-name` via `additionalOptions`). The
   caches replicated **synchronously** between sites are `authenticationSessions`,
   `actionTokens`, `loginFailures`, and `work` ([[external-data-grid-operator]],
   [[site-synchronization]]). Synchronous replication is what makes a request that
   lands on the passive site after failover see consistent state (inferred).

The whole multi-site path is gated by the **`multi-site` feature flag**
([[multi-site-feature-flag]]), which also exposes the `/lb-check` endpoint the
load balancer probes.

## What is lost on failover

- **In-flight requests / up to ~5 min downtime.** Failover is not instantaneous.
  The **AWS Global Accelerator** (static anycast IP, since client DNS caching
  makes DNS failover unreliable) health-checks `/lb-check` and re-routes to the
  healthy site, but requests in flight at the moment of failure will error, and
  some switchover scenarios incur **up to 5 minutes of downtime**
  ([[ha-load-balancer-failover]]).
- **No loss of established user sessions** in a clean failover — they are in the
  replicated DB and in the synchronously-replicated Data Grid caches, so users
  generally stay logged in (inferred, from the durability design).
- **The redundancy / "no data loss" guarantee itself, after a *partial* failure.**
  The model is consistency-first but **not self-healing**: if a synchronous
  cross-site request fails, the sites silently drift out of sync. This is hard to
  monitor, and until a **full manual re-sync** is completed, the no-data-loss
  guarantee does *not* hold for a *subsequent* failure ([[site-synchronization]]).
- **Everything, if you opted into volatile sessions.** If you switched sessions to
  cache-as-source-of-truth (no DB persistence) to cut DB IOPS, a full restart of
  all pods loses **all sessions** — that mode trades away the multi-site
  durability guarantee ([[session-persistence-volatile]]) (inferred).

## Recovery after a degraded failover

A split-brain or failed sync requires the manual procedure in
[[site-synchronization]]: stop RHBK on the offline site (`instances: 0`), take
cross-site replication offline toward the active site (**verify it is offline** or
the clear wipes both), `clearcache` the stale caches, bring replication back
online (triggers a full state transfer), restart RHBK, and re-add the site to the
load-balancer EndpointGroup. An AWS Lambda fenced the degraded site automatically
during the outage.

## Caveats

- **Active/Passive only, two sites only.** Active/Active is not the documented
  supported model, and more than two sites is explicitly unsupported.
- **Naming by version:** 26.0/26.2 call this "**multi-site**"; 26.4/26.6 rename
  the chapter to "**multi-cluster**". The Active/Passive, consistency-first model
  is unchanged.
- The reference blueprint is **AWS-specific** (Global Accelerator + NLB + fencing
  Lambda); on other platforms supply an equivalent static-IP failover LB that
  probes `/lb-check` and can fence a degraded site.

## See also
- [[ha-cross-site]]
- [[session-persistence-volatile]]
- [[site-synchronization]]
- [[external-data-grid-operator]]
- [[ha-load-balancer-failover]]
- [[multi-site-feature-flag]]
- [[rhbk-ha-architectures]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-2-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
- [[rhbk-26-2-operate-synchronize|Chapter 15. Synchronizing sites]]
- [[rhbk-26-2-deploy-infinispan-kubernetes-crossdc|Chapter 9. Deploying Data Grid for HA with the Data Grid Operator]]
<!-- crosslink:end -->
