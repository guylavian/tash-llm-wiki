---
title: Site Links and Replication Schedule
type: entity
domain: active-directory
slug: site-links-and-replication-schedule
summary: AD DS site link objects define inter-site replication paths via three tunable properties — cost, interval, and schedule — that together control when and how frequently the KCC builds connections between bridgehead servers across sites.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Setting-Site-Link-Properties (Microsoft Learn — Setting Site Link Properties, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-a-Site-Link-Design (Microsoft Learn — Creating a Site Link Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Determining-the-Cost (Microsoft Learn — Determining the Cost, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Determining-the-Interval (Microsoft Learn — Determining the Interval, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Determining-the-Schedule (Microsoft Learn — Determining the Schedule, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-a-Site-Link-Bridge-Design (Microsoft Learn — Creating a Site Link Bridge Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/Active-Directory-Replication-Concepts (Microsoft Learn — Active Directory Replication Concepts, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 3
provenance_ambiguous: 0
tags: [replication, sites-topology, concept]
status: draft
updated: 2026-06-18
---

# Site Links and Replication Schedule

**A site link is an AD DS object that models a WAN path between two or more sites and exposes three properties — cost, interval, and schedule — that the KCC uses to generate and time inter-site replication connections.**

## Body

### What a site link is

Site links live in the **Inter-Site Transports** container (IP sub-container for RPC-over-IP; SMTP sub-container is deprecated and not supported for domain partitions). A site link represents a set of sites that can communicate at uniform cost over a single transport. Every site must appear in at least one site link, or the KCC logs a topology-not-connected error in the Directory Service event log.

When two sites are joined by a site link, the KCC picks **bridgehead servers** — one writable DC per domain partition per site — and creates connection objects between them. In Windows Server 2008 and later, the selection is randomized across all candidate bridgehead DCs to distribute workload; the randomization happens once when connection objects are first added.

### Cost

Cost is an administrator-assigned integer (lower = preferred). It should reflect bandwidth, latency, reliability, and monetary expense of the link — not bandwidth alone. The reference formula `cost = 1024 / log(bandwidth_kbps)` gives a relative baseline: a 512 Kbps link yields cost 378; a 1,024 Kbps link yields 340. Failure-prone links should carry an artificially high cost to force the KCC toward more reliable alternatives for normal replication.

Cost is also used by **DC Locator** and **DFSN** to route clients to the nearest resource when their home site has no local DC.

### Interval

The interval controls how frequently replication fires **within the schedule window**. Default is 180 minutes (3 hours); minimum is 15 minutes. A shorter interval reduces convergence latency but increases WAN traffic. For domain partitions, lower latency is generally preferred (inferred — combining the interval and schedule guidance).

### Schedule

The schedule constrains which hours inter-site replication is permitted. Times are stored in UTC but displayed in local time on each DC. When a path spans multiple site links, the KCC takes the **intersection** of schedules — if any link is closed, the whole path is unavailable. Blocking replication during business-hours peak traffic increases latency; the default (100% available) is recommended unless WAN contention is a real operational concern.

### Site link bridges and transitivity

By default, **Bridge all site links** is enabled for the IP transport, making every site link transitive. The KCC can then sum costs across multiple links to find the least-expensive route to a remote site, even if the sites are not directly linked. Disable **Bridge all site links** only when:

- The IP network is **not fully routed** (physical connectivity gaps exist), or
- You need to **isolate replication flow** — e.g., hub-and-spoke where satellite sites must not replicate directly with each other if the hub goes down, or replication must pass through a firewall.

When **Bridge all site links** is disabled, create explicit **site link bridge** objects to model which groups of site links share transitive connectivity. The KCC treats each bridge as an isolated routing domain (inferred — combining bridge-design and replication-concepts notes). The cost of a bridged path is the **sum** of its constituent site link costs.

SMTP replication is deprecated and will not be supported in future versions of AD DS; new site links should always use the IP container.

## Contradictions / caveats

- Site link cost does not reflect actual TCP/IP routing — packets may traverse a completely different physical path. Redundant site links are unnecessary to improve AD replication efficiency; cost just directs the KCC's logical topology.
- Removing a site link bridge does not immediately break replication — replication continues until the KCC next removes the now-unjustified connection objects (inferred — from bridge-design note).
- If a site is left in `Default-First-Site-Link` after being added to a new site link, the KCC makes routing decisions based on both memberships, potentially producing incorrect routes.

## Reference notes
- [[ad-ds-setting-site-link-properties]]
- [[ad-ds-creating-a-site-link-design]]
- [[ad-ds-determining-the-cost]]
- [[ad-ds-determining-the-interval]]
- [[ad-ds-determining-the-schedule]]
- [[ad-ds-creating-a-site-link-bridge-design]]
- [[ad-ds-active-directory-replication-concepts]]

## See also
- [[ad-replication]]
- [[knowledge-consistency-checker]]
- [[site-topology-design]]
- [[dc-locator]]
