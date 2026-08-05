---
title: How do I take a SharePoint Distributed Cache host down for maintenance without losing newsfeed data?
type: question
domain: sharepoint
slug: sharepoint-distributed-cache-maintenance
summary: Drain the host first with Stop-SPDistributedCacheServiceInstance -Graceful (default 900s/5-min timeout) — Distributed Cache does not replicate data between hosts, so an ungraceful stop or reboot loses whatever that host was caching; if the host still shows down afterward, the Health Analyzer "One of the cache hosts in the cluster is down" rule points at a stopped AppFabric Caching Windows service.
sources:
  - kb:what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition
  - kb:install-planning-for-a-minrole-server-deployment-in-sharepoint-server
  - kb:technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down
  - kb:install-software-boundaries-limits-2019
  - kb:upgrade-and-update-install-a-software-update
provenance_extracted: 9
provenance_inferred: 1
provenance_ambiguous: 1
question_tier: conceptual
tags: [sp-farm, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# How do I take a SharePoint Distributed Cache host down for maintenance without losing newsfeed data?

**Run `Stop-SPDistributedCacheServiceInstance -Graceful` on the host before taking it
down — never just stop the service or reboot the box — because Distributed Cache does
not replicate cached data between hosts, so an ungraceful stop drops that host's cache
outright.**

## Answer

### Why an ungraceful stop loses data

The MinRole "Distributed Cache" server-role description is explicit: "Distributed Cache
doesn't support High Availability the way that other services do. While you can have
multiple Distributed Cache servers in your SharePoint farm to help distribute the load,
the data cached on each Distributed Cache server is not replicated to the other
Distributed Cache servers. If a Distributed [Cache server unexpectedly goes down, the
data cached in that server will be lost]"
(`reference/sharepoint/install-planning-for-a-minrole-server-deployment-in-sharepoint-server.md:35`,
extracted). This is what makes graceful shutdown mandatory before any planned
maintenance, patching, or reboot of a cache host — unlike most other SharePoint
services, there's no automatic failover copy to fall back to.

### The graceful shutdown procedure

"The `Stop-SPDistributedCacheServiceInstance` cmdlet is improved to better support
graceful shutdowns. You can specify the `-Graceful` switch parameter with the cmdlet
to ensure that the cached data in a Distributed Cache service instance is transferred to
another Distributed Cache service instance before the first service instance shuts
down." The transfer is time-bounded: "If the `-Timeout` parameter isn't specified, the
default is 900 seconds (5 minutes)." `-Force` shuts the instance down anyway if the
graceful drain can't finish before the timeout
(`reference/sharepoint/what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition.md:504-506`, extracted).
In practice:

```
Stop-SPDistributedCacheServiceInstance -Graceful
```

run on the host being taken down (add `-Timeout <seconds>` to give a large cache more
time to drain, or `-Force` only if you've accepted the data loss risk to meet a
maintenance window). This same command is also the documented first step of the
Health Analyzer remediation for a farm running low on cache memory: stop every cache
host gracefully, resize with `Update-SPDistributedCacheSize -CacheSizeInMB CacheSize`
— this remediation article documents the default as "5 percent of total system RAM...
should not be more than 40 percent of total system RAM with a maximum limit of 16
gigabytes (GB)"
(`reference/sharepoint/technical-reference-cached-objects-have-been-evicted.md:71`,
extracted) — on any one host, then restart the
service on all hosts
(`reference/sharepoint/technical-reference-cached-objects-have-been-evicted.md:59-73`, extracted).
(`(ambiguous)`: a separate planning article documents the install-time default as 10% of
total physical memory instead — see [[sharepoint-distributed-cache]] Contradictions.)

### If the host still shows down afterward

Central Administration's Health Analyzer carries a dedicated rule for this: "**One of
the cache hosts in the cluster is down**" — "Cause: The AppFabric Caching service is
stopped" — "Resolution: Start the AppFabric Caching service" (via Server Manager →
Tools → Services, confirm `AppFabric Caching Service` is `Started`)
(`reference/sharepoint/technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down.md:23-29`, extracted).
This rule has automatic repair enabled by default, so a transient stop often self-heals
before anyone notices — but a host that stays flagged after maintenance usually means
the Windows service didn't come back up cleanly, not a deeper cache-cluster problem.

### Sizing the cluster so a single host's loss is tolerable

The practical mitigation for the no-replication design is capacity headroom: the
distributed cache cluster caps out at **16 cache hosts** and **16 GB** memory dedicated
to the service per host, supporting **400,000** followable entities (users, documents,
sites, hashtags) per host at 16 GB assigned
(`reference/sharepoint/install-software-boundaries-limits-2019.md:688-692`,
extracted). Running multiple cache hosts distributes load and reduces the blast radius
of losing one, but does not itself prevent data loss on that host — only a graceful
drain (or accepting the newsfeed gap until data repopulates from source) does that
(inferred — direct implication of "not replicated" plus the multi-host load-distribution
framing in the same role description).

## Contradictions / caveats

**(ambiguous) Default cache-size percentage**: the install-time planning article
documents the `-CacheSizeInMB` default as 10% of total physical memory
(`reference/sharepoint/administration-plan-for-feeds-and-the-distributed-cache-service.md:118`),
while the Health Analyzer remediation article used above documents the same
parameter's default as 5%, capped at 40%
(`reference/sharepoint/technical-reference-cached-objects-have-been-evicted.md:71`).
Both are verbatim from the current live docset; quote the one matching context
(fresh install vs. post-alert resize).

**Version-specific `-Graceful` caveat**: "Do not use
`Stop-SPDistributedCacheServiceInstance -Graceful` for SharePoint Server 2013,
SharePoint Server 2016, and SharePoint Server 2019 as this will terminate Distributed
Cache prior to the cache being transferred to another server in the farm. But
`Stop-SPDistributedCacheServiceInstance -Graceful` can be used for SharePoint Server
Subscription Edition"
(`reference/sharepoint/upgrade-and-update-install-a-software-update.md:542`,
extracted) — during a **software-update** drain specifically on 2013/2016/2019, follow
that article's version-specific guidance instead of the general `-Graceful` procedure
above.

## See also
- [[sharepoint-distributed-cache]]
- [[sharepoint-farm-topology]]
- [[sharepoint-management-shell]]
- [[sharepoint-implementation-review]]
- [[sharepoint-overview]]

## References

**RH ground-truth (kb:)**
- `install-planning-for-a-minrole-server-deployment-in-sharepoint-server` — Planning for a MinRole server deployment in SharePoint Server (MinRole server-role table; Distributed Cache non-replication)
- `what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition` — New and improved features in SharePoint Server Subscription Edition (`Stop-SPDistributedCacheServiceInstance -Graceful`/`-Timeout`/`-Force`)
- `technical-reference-cached-objects-have-been-evicted` — Cached objects have been evicted (SharePoint Server) (Health Analyzer rule + remediation)
- `technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down` — One of the cache hosts in the cluster is down (SharePoint Server) (Health Analyzer rule)
- `install-software-boundaries-limits-2019` — Software boundaries and limits for SharePoint Servers 2016 and 2019 (distributed cache service limits table)
- `upgrade-and-update-install-a-software-update` — Install a software update (SharePoint Server) (version-specific `-Graceful` caveat)

**Wiki**
- [[sharepoint-distributed-cache]]
- [[sharepoint-farm-topology]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition|New and improved features in SharePoint Server Subscription Edition]]
- [[install-planning-for-a-minrole-server-deployment-in-sharepoint-server|Planning for a MinRole server deployment in SharePoint Servers 2016, 2019, and Subscription Edition]]
- [[technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down|One of the cache hosts in the cluster is down (SharePoint Server)]]
- [[install-software-boundaries-limits-2019|Software boundaries and limits for SharePoint Servers 2016 and 2019]]
- [[upgrade-and-update-install-a-software-update|Install a software update for SharePoint Server]]
<!-- crosslink:end -->
