---
title: RHBK High-Availability Architectures (Single-cluster vs Multi-cluster)
type: topic
domain: keycloak
slug: rhbk-ha-architectures
summary: "RHBK ships two documented HA shapes: a single OpenShift cluster (optionally spread across availability zones) using embedded Infinispan, and a two-site Active/Passive deployment using an external Red Hat Data Grid with synchronous replication. The guide prioritizes consistency over availability"
sources:
  - guide:high_availability_guide
  - kb:multi-cluster-introduction
  - kb:single-cluster-introduction
  - kb:concepts-multi-site
source_notes:
  - "[[rhbk-26-6-multi-cluster-introduction]]"
  - "[[rhbk-26-6-single-cluster-introduction]]"
  - "[[rhbk-26-2-concepts-multi-site]]"
provenance_extracted: 16
provenance_inferred: 0
provenance_ambiguous: 1
tags: [ha, concept]
status: draft
updated: 2026-07-02
---

# RHBK High-Availability Architectures (Single-cluster vs Multi-cluster)

**RHBK ships two documented HA shapes: a single OpenShift cluster (optionally
spread across availability zones) using embedded Infinispan, and a two-site
Active/Passive deployment using an external Red Hat Data Grid with synchronous
replication. The guide prioritizes consistency over availability.**

## The two shapes

### Single-cluster
- Multiple RHBK pods in **one** OpenShift cluster behind a shared external
  database. Use when the network is **transparent** (one cluster) and all healthy
  pods should serve traffic.
- Pods cluster via **embedded Infinispan** ([[distributed-caches]]); the operator
  applies default `topologySpreadConstraints` to spread pods across nodes and
  zones (`maxSkew: 1` on `topology.kubernetes.io/zone` and `kubernetes.io/hostname`,
  `whenUnsatisfiable: ScheduleAnyway`).
- Can span **up to three availability zones** in one region if OpenShift supports
  it and the DB can tolerate zone failures. Requires **< 10 ms** round-trip
  latency between RHBK instances.
- Tested config: ROSA HCP across 3 AZs, Aurora PostgreSQL 17.5 (primary +
  synchronous readers), OpenShift 4.17+.
- Survives: RHBK pod loss, OpenShift node loss, intra-cluster connectivity loss —
  each **< 30 s** recovery, no data loss. Does **not** survive whole-cluster
  failure or a region outage; upgrades still cause downtime.

### Multi-cluster (a.k.a. multi-site)
- **Two independent** RHBK deployments in two separate OpenShift clusters/sites,
  connected over a low-latency link, fronted by a load balancer.
  See [[ha-cross-site]].
- Adds components to bridge **non-transparent** networks: a synchronously
  replicated database across both sites, an **external Data Grid** with Cross-DC
  replication ([[external-data-grid-operator]]), and a failover load balancer
  ([[ha-load-balancer-failover]]).
- Requires **< 5 ms suggested / < 10 ms required** round-trip latency between
  sites; suggested as two AWS AZs in one region (not two regions).
- Tested/supported only with **exactly two sites** — more sites amplify latency
  and failure probability and are unsupported.
- RPO: no data loss (when not already degraded). RTO: site failover **< 2 min**;
  some failure/switchover scenarios incur **up to 5 min** downtime and may need
  manual re-synchronization ([[site-synchronization]]).

## Embedded vs external Infinispan — the dividing line
- **Single-cluster → embedded** Infinispan inside each RHBK JVM; pods discover
  each other and share distributed caches directly.
- **Multi-cluster → external** Data Grid. RHBK connects to it as a **remote
  store** via `cache-remote-host`/`cache-remote-port`/`cache-remote-username`/
  `cache-remote-password`; the two Data Grid clusters replicate cross-site. In
  this topology RHBK's own caches behave as **local** caches and writes broadcast
  an invalidation through the `work` cache.

## What changed across versions (naming)
- **26.0 / 26.2** call this "**multi-site** deployments" with **synchronous Data
  Grid** replication as the core building block.
- **26.4 / 26.6** rename the chapter to "**multi-cluster** deployments" and frame
  it as connecting independent clusters that can use embedded Infinispan plus the
  external Data Grid Cross-DC building block; the underlying Active/Passive,
  two-site, consistency-first model is the same.

## Sizing quick reference (from the guide)
- Base: ~1250 MB RAM per pod for realm caches + 10,000 sessions; ~70% of the
  memory limit is heap, plus ~300 MB non-heap.
- ~1 vCPU per **15** password logins/s, per **120** client-credential grants/s,
  per **120** refresh-token requests/s; leave **150%** CPU head-room for spikes
  and failover.
- DB-backed sessions: budget ~1400 write IOPS and 0.35–0.7 vCPU per 100
  login/logout/refresh requests/s on Aurora multi-AZ.

## Contradictions / caveats
- **Active/Passive only.** Active/Active is not the documented supported model;
  the guide deliberately trades availability for consistency (synchronous
  replication). Verify support state per RHBK version.
- The `multi-site` **feature flag** must be enabled on the CR for multi-cluster
  (adds the `/lb-check` probe) — see [[multi-site-feature-flag]]. It is not used
  for single-cluster.
- External Data Grid requires **Data Grid 8.5.2+** for supported external
  deployments (ambiguous — `rhbk-26-6-multi-cluster-introduction` states
  **8.5.3+**; treat 8.5.3 as the source of record until confirmed otherwise).
- Naming differs by version (multi-site vs multi-cluster); when searching the KB
  use the term matching your version: `--guide high_availability_guide`.

## See also
- [[ha-cross-site]]
- [[distributed-caches]]
- [[external-data-grid-operator]]
- [[ha-load-balancer-failover]]
- [[session-persistence-volatile]]
- [[rhbk-db-connection-pool]]
- [[multi-site-feature-flag]]
- [[site-synchronization]]
- [[rhbk-operator]]
- [[tokens-and-sessions]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-high_availability_guide|keycloak reference — high_availability_guide]]
- [[rhbk-26-6-multi-cluster-introduction|Chapter 3. Multi-cluster deployments]]
- [[rhbk-26-6-single-cluster-introduction|Chapter 2. Single-cluster deployments]]
- [[rhbk-26-2-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
<!-- crosslink:end -->
