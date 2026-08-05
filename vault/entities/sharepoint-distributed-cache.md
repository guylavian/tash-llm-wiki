---
title: SharePoint Distributed Cache Service
type: entity
domain: sharepoint
slug: sharepoint-distributed-cache
summary: The Distributed Cache service (built on AppFabric Caching) powers newsfeeds and other social features; it does not replicate data between cache hosts, so a host failure loses that host's cached data unless a graceful shutdown (Stop-SPDistributedCacheServiceInstance -Graceful) drains it first, and it's capped at 16 cache hosts per cluster / 16 GB per host.
sources:
  - kb:what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition
  - kb:install-planning-for-a-minrole-server-deployment-in-sharepoint-server
  - kb:install-software-boundaries-limits-2019
  - kb:technical-reference-cached-objects-have-been-evicted
  - kb:technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down
  - kb:technical-reference-firewall-client-settings-on-the-cache-host-are-incorrect
  - kb:administration-manage-the-distributed-cache-service
  - kb:administration-plan-for-feeds-and-the-distributed-cache-service
  - kb:upgrade-and-update-install-a-software-update
provenance_extracted: 13
provenance_inferred: 1
provenance_ambiguous: 1
symptoms:
  - "Cached objects have been evicted"
  - "One of the cache hosts in the cluster is down"
  - "Firewall client settings on the cache host are incorrect"
  - "AppFabric Caching Service"
tags: [sp-farm, troubleshooting, concept]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# SharePoint Distributed Cache Service

**A farm-wide in-memory cache (built on AppFabric Caching) that backs newsfeeds and
other social/collaborative features; unlike other SharePoint HA services, it does not
replicate cached data between hosts — losing a host loses that host's cache.**

## Body

### Role and non-replication

Distributed Cache is one of the dedicated MinRole server roles (see
[[sharepoint-farm-topology]]). Per the MinRole role table: "Distributed Cache doesn't
support High Availability the way that other services do. While you can have multiple
Distributed Cache servers in your SharePoint farm to help distribute the load, the data
cached on each Distributed Cache server is not replicated to the other Distributed
Cache servers. If a Distributed Cache server unexpectedly goes down, the data cached
in that server will be lost"
(`install-planning-for-a-minrole-server-deployment-in-sharepoint-server.md:35`).

### Graceful shutdown to avoid data loss

`Stop-SPDistributedCacheServiceInstance -Graceful` transfers a cache host's data to
another instance before it shuts down, instead of dropping it. `-Timeout <seconds>`
bounds how long the drain may take (default **900 seconds / 5 minutes**); `-Force`
shuts the instance down anyway if the graceful drain can't finish in time
(`what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition.md:504-506`).

### Cmdlet surface

`New-SPCache`, `Get-SPCache`, `Get-SPCacheStatistics`, `Get-SPCacheHost`,
`Start-SPCacheCluster`, `Stop-SPCacheCluster`, `Import-SPCacheClusterConfig`,
`Export-SPCacheClusterConfig`, `Get-SPCacheClusterHealth` (SharePoint-native
equivalents of the standalone AppFabric cmdlets)
(`administration-manage-the-distributed-cache-service.md:37-49`). Farm-role management uses
`Add-SPDistributedCacheServiceInstance` / `Remove-SPDistributedCacheServiceInstance`
(`administration-manage-the-distributed-cache-service.md:210,220`). Cache size is tuned once with
`Update-SPDistributedCacheSize -CacheSizeInMB <n>` — hard ceiling **16 GB** per cache
host regardless of source (`ambiguous` on the default percentage, see Contradictions
below): the install-time default is documented as **10%** of total physical memory,
reserving 2 GB for other services on the host
(`administration-plan-for-feeds-and-the-distributed-cache-service.md:118`), while the
"Cached objects have been evicted" Health Analyzer remediation documents the
`-CacheSizeInMB` default as **5%**, capped at 40%
(`technical-reference-cached-objects-have-been-evicted.md:71`).

### Limits

`install-software-boundaries-limits-2019.md:688-692`: **400,000** followable entities (users,
documents, sites, hashtags) per cache host with 16 GB RAM assigned; **16** cache hosts
maximum per cluster; **16 GB** maximum memory dedicated to the service per host.

### Health Analyzer rules

(`technical-reference-cached-objects-have-been-evicted.md`,
`technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down.md`,
`technical-reference-firewall-client-settings-on-the-cache-host-are-incorrect.md`,
`administration-manage-the-distributed-cache-service.md:768,770`)

| Rule | Cause | Resolution |
|---|---|---|
| Cached objects have been evicted | Cache cluster memory pressure (low/high watermark eviction) | Add RAM, or raise the allocation via graceful stop + `Update-SPDistributedCacheSize` + restart |
| Distributed cache service is not configured on server(s) | Server has the Distributed Cache MinRole role but the host was never registered | `Add-SPDistributedCacheServiceInstance` on the failing server |
| Distributed cache service is not enabled in this deployment | Service manually stopped | `Add-SPDistributedCacheServiceInstance`, verify Started in Central Administration |
| Distributed cache service is unexpectedly configured on server(s) | Service running on a server role that shouldn't host it | `Remove-SPDistributedCacheServiceInstance` on the failing server |
| More cache hosts running than registered with SharePoint | SharePoint fails to identify a running cache host | Stop the unregistered host's AppFabric Caching Service manually |
| One of the cache hosts in the cluster is down | AppFabric Caching service stopped | Start the AppFabric Caching Windows service (rule supports auto-repair) |
| Firewall client settings on the cache host are incorrect | AppFabric Caching firewall rules (TCP-In/TCP-Out) disabled | Enable the AppFabric Caching Service inbound/outbound firewall rules (rule supports auto-repair) |

## Contradictions / caveats

**(ambiguous) Default cache-size percentage**: the corpus itself gives two different
numbers for the `-CacheSizeInMB` default depending on context — the install-time
default is documented as 10% of total physical memory
(`administration-plan-for-feeds-and-the-distributed-cache-service.md:118`), while the
Health Analyzer "Cached objects have been evicted" remediation article documents the
same parameter's default as 5%, capped at 40%
(`technical-reference-cached-objects-have-been-evicted.md:71`). Both are extracted
verbatim from the current live docset (not a version-drift artifact this page can
resolve) — quote whichever context matches the question (fresh install vs. post-alert
resize) rather than picking one as "the" default.

**Version-specific `-Graceful` caveat**: per the software-update guidance, "Do not use
`Stop-SPDistributedCacheServiceInstance -Graceful` for SharePoint Server 2013,
SharePoint Server 2016, and SharePoint Server 2019 as this will terminate Distributed
Cache prior to the cache being transferred to another server in the farm. But
`Stop-SPDistributedCacheServiceInstance -Graceful` can be used for SharePoint Server
Subscription Edition" (`upgrade-and-update-install-a-software-update.md:542`). The
`-Graceful` recommendation above is accurate for **Subscription Edition**; on 2013/2016/2019
during a software-update drain specifically, follow that article's version-specific
guidance instead.

## See also
- [[sharepoint-farm-topology]]
- [[sharepoint-management-shell]]
- [[sharepoint-search-service]]
- [[sharepoint-implementation-review]]
- [[sharepoint-overview]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition|New and improved features in SharePoint Server Subscription Edition]]
- [[install-planning-for-a-minrole-server-deployment-in-sharepoint-server|Planning for a MinRole server deployment in SharePoint Servers 2016, 2019, and Subscription Edition]]
- [[install-software-boundaries-limits-2019|Software boundaries and limits for SharePoint Servers 2016 and 2019]]
- [[technical-reference-cached-objects-have-been-evicted|Cached objects have been evicted (SharePoint Server)]]
- [[technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down|One of the cache hosts in the cluster is down (SharePoint Server)]]
- [[technical-reference-firewall-client-settings-on-the-cache-host-are-incorrect|Firewall client settings on the cache host are incorrect (SharePoint Server)]]
- [[administration-manage-the-distributed-cache-service|Manage the Distributed Cache service in SharePoint Server]]
- [[administration-plan-for-feeds-and-the-distributed-cache-service|Plan for feeds and the Distributed Cache service in SharePoint Server]]
- [[upgrade-and-update-install-a-software-update|Install a software update for SharePoint Server]]
<!-- crosslink:end -->
