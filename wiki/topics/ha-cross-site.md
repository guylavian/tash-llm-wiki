---
title: High Availability & Cross-Site (Multi-Cluster) Deployments
type: topic
domain: keycloak
slug: ha-cross-site
summary: "Running RHBK across multiple clusters/sites for resilience, using external Infinispan / Red Hat Data Grid for cross-site session replication"
sources:
  - guide:high_availability_guide
  - ref:high-availability.md
provenance: needs-review
tags: [ha, concept]
status: draft
updated: 2026-06-16
---

# High Availability & Cross-Site (Multi-Cluster) Deployments

**Running RHBK across multiple clusters/sites for resilience, using external
Infinispan / Red Hat Data Grid for cross-site session replication.**

## Body
The HA Guide splits into **single-cluster** and **multi-cluster** chapters:

- **Single-cluster** — multiple RHBK pods in one OpenShift cluster, fronted by a
  shared external database. DB credentials live in a Secret
  (`keycloak-db-secret` with `username`/`password`), referenced by the
  [[rhbk-operator]] `Keycloak` CR.
- **Multi-cluster (cross-site)** — an **Active/Passive** topology across two
  sites. Each site runs RHBK + an **external Infinispan/Data Grid** cluster; the
  two Data Grid clusters form a **cross-site** connection so user sessions
  replicate. A load balancer handles failover between sites.

Operational gates (from the guide's `oc wait` steps):
```sh
oc wait --for condition=WellFormed        --timeout=300s infinispans.infinispan.org/infinispan -n keycloak
oc wait --for condition=CrossSiteViewFormed --timeout=300s infinispans.infinispan.org/infinispan -n keycloak
```

Aurora/external Postgres is the documented DB (connection pool sized via
`poolMinSize` / `poolInitialSize` / `poolMaxSize` on the CR).

For the building blocks of this topology see [[external-data-grid-operator]]
(Cross-DC sessions), [[ha-load-balancer-failover]] (AWS Global Accelerator +
fencing Lambda), [[multi-site-feature-flag]] (`/lb-check`), and
[[site-synchronization]] (split-brain recovery). For the broader single-vs-multi
decision and sizing, see [[rhbk-ha-architectures]].

## Contradictions / caveats
- **Active/Passive only** — Active/Active is not the documented supported model;
  confirm supported vs. preview in `ref:rhbk-platform-support.md` for the target
  RHBK version before committing.
- Cross-site requires **external** Infinispan; embedded Infinispan is for
  single-cluster. Check `ref:high-availability.md` for embedded-vs-external cache
  roles and session persistence.
- **Naming changed by version:** 26.0/26.2 call this "**multi-site**" deployments
  (synchronous Data Grid replication as the core building block); 26.4/26.6 rename
  the chapter to "**multi-cluster**" deployments (connecting independent clusters,
  embedded Infinispan + external Data Grid Cross-DC). The Active/Passive, two-site,
  consistency-first model is unchanged. External Data Grid requires **8.5.2+**.
- **Two sites only** — more than two sites is explicitly unsupported (latency and
  failure probability amplify). Some failure/switchover scenarios incur up to
  5 min downtime and may require manual re-sync.
- Steps are version-sensitive — verify with
  `rhbk_kb.py search "..." --guide high_availability_guide`.

## See also
- [[rhbk-ha-architectures]]
- [[external-data-grid-operator]]
- [[ha-load-balancer-failover]]
- [[multi-site-feature-flag]]
- [[site-synchronization]]
- [[session-persistence-volatile]]
- [[rhbk-db-connection-pool]]
- [[rhbk-operator]]
- [[distributed-caches]]
