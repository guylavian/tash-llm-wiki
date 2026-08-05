---
title: SharePoint Server — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: sharepoint
slug: sharepoint-implementation-review
summary: The evaluation lens and Map of Content for the sharepoint brain — a rule → anti-pattern → symptom checklist across farm topology/MinRole, Distributed Cache, content databases, authentication, search, and backup/management-shell health areas, plus a symptom → likely-cause reverse index (mostly SharePoint Health Analyzer rule names) the SRE agent uses to turn an alert into a cause page.
sources:
  - kb:technical-reference-some-content-databases-are-growing-too-large
  - kb:technical-reference-cached-objects-have-been-evicted
  - kb:technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down
  - kb:technical-reference-firewall-client-settings-on-the-cache-host-are-incorrect
  - kb:technical-reference-content-databases-contain-orphaned-apps
  - kb:technical-reference-one-or-more-web-applications-are-configured-to-use-windows-classic-authenticatio
  - kb:technical-reference-content-databases-contain-orphaned-items
  - kb:technical-reference-search-in-sharepoint-server
  - kb:install-planning-for-a-minrole-server-deployment-in-sharepoint-server
provenance_extracted: 0
provenance_inferred: 32
provenance_ambiguous: 0
tags: [sp-farm, sp-content, sp-search, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# SharePoint Server — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `sharepoint` domain.** It indexes
SharePoint health pages into a forward checklist (rule → anti-pattern → symptom) and
a reverse index (symptom → likely cause) so a Health Analyzer alert or an operator
ticket can be turned into a cause page. This is the SharePoint analogue of
[[active-directory-implementation-review]] / [[sso-implementation-review]]; grow it as
pages land via INGEST.

---

## How to use this page

Read each row left to right: the **Rule** column states what a healthy farm must do;
the **Anti-pattern** column states the common misconfiguration; the **Symptom** column
names the observable fault it produces — almost always a named **Health Analyzer
rule** or search/cache alert in this corpus; the **Page** column links the cause page.
To diagnose from an alert, jump to the
[Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist (SharePoint Server)

### Farm topology and MinRole (sp-farm)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Assign every server a MinRole role that matches the services it should run; let the nightly self-healing scan enforce compliance | Manually starting/stopping service instances on a MinRole-managed server, fighting the nightly compliance scan | Health report: `Server role configuration isn't correct` — MinRole auto-repairs or reports the drifted server | [[sharepoint-farm-topology]] |
| Deploy shared roles ("Front-end with Distributed Cache", "Application with Search") only on farms with the November 2016 PU (Feature Pack 1) or later | Trying to select a shared role on a pre-Feature-Pack-1 farm | Shared role missing from the server-role picker; role conversion blocked | [[sharepoint-farm-topology]] |
| Keep a Single-Server Farm role farm at exactly one SharePoint server | Adding a second SharePoint server to a farm provisioned with the Single-Server Farm role | Farm/role validation rejects the additional server join | [[sharepoint-farm-topology]] |
| Publish a service application's proxy into the proxy group(s) of every web application that should consume it | Standing up a service application but leaving its proxy out of a consuming web app's proxy group | Feature/service unexpectedly unavailable on a specific web app despite the service application existing farm-wide | [[sharepoint-farm-topology]], [[sharepoint-overview]] |

### Distributed Cache (sp-farm)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Drain a Distributed Cache host with `Stop-SPDistributedCacheServiceInstance -Graceful` before maintenance/reboot | Stopping or rebooting a cache host without `-Graceful`, or forcing past the default 900s (5-min) drain timeout | Newsfeed/social data missing after the host comes back; cache eviction alert | [[sharepoint-distributed-cache]] |
| Keep the cluster under its hard ceilings: 16 cache hosts, 16 GB memory/host, 400,000 followable entities/host | Undersizing cache-host RAM, or growing past 16 hosts without redesigning the cluster | `Cached objects have been evicted` (memory-pressure eviction) | [[sharepoint-distributed-cache]] |
| Keep the AppFabric Caching Windows service and its inbound/outbound firewall rules enabled on every cache host | AppFabric Caching Service stopped, or its firewall rule (TCP-In/TCP-Out) disabled | `One of the cache hosts in the cluster is down`; `Firewall client settings on the cache host are incorrect` | [[sharepoint-distributed-cache]] |

### Content databases and site collections (sp-content)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Keep content databases at or under the 200 GB sizing recommendation; treat 100 GB as the availability-risk alert line | Letting a content database grow unchecked past 100 GB / 200 GB without splitting site collections into a new database | `Some content databases are growing too large` | [[sharepoint-content-databases]] |
| Never leave a content database set to SQL Server read-only outside a deliberate, short maintenance/DR step | A database left `Read-Only=True` (backup tooling, DR failover) into normal operation | Content database `set to read only`; upgrade/PSConfig fails against it | [[sharepoint-content-databases]] |
| Resolve orphaned objects promptly instead of letting them accumulate across upgrade cycles | Ignoring Health Analyzer's orphan warnings; upgrading a farm with known orphans | `Content databases contain orphaned Apps`; `orphaned items` | [[sharepoint-content-databases]] |
| Migrate any remaining Windows Classic-mode web applications to claims-based authentication | Leaving a legacy web app on Windows Classic mode (only creatable via `New-SPWebApplication`; no Central Administration UI path) | `One or more web applications are configured to use Windows Classic authentication` | [[sharepoint-authentication]] |

### Search (sp-search)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Budget Search DR around a one-week RPO/RTO; consider a parallel new Search service application + cutover to avoid the overwrite-restore outage | Assuming Search restores as fast/fresh as a content database restore, or restoring `Overwrite`-mode into a live production farm without planning for the outage | Search offline during restore; configuration/analytics/index up to a week stale afterward | [[sharepoint-search-service]], [[sharepoint-backup-restore]] |
| Investigate index component health/network connectivity immediately on a missing-partition alert, before it becomes unrecoverable | Ignoring index component alerts until data loss forces a full re-crawl | `Index: Missing partition`; `Index component down` | [[sharepoint-search-service]] |
| Watch index-component resource usage and feed rate on high-volume crawls | Feeding content faster than the index component(s) can consume it | `Index: Indexing Blocked` | [[sharepoint-search-service]] |
| Treat `Index: Lost Generations` as unrecoverable data loss, not a transient alert | Waiting/retrying instead of accepting the loss and re-crawling | `Index: Lost Generations` — acknowledged-indexed data permanently lost, full re-crawl required | [[sharepoint-search-service]] |

### Backup, restore, and management shell (sp-farm)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Check `spbrtoc.xml` / `Get-SPBackupHistory` for the actual backup ID before restoring, rather than assuming "the last backup" | Running `Restore-SPFarm` without `-BackupId` when multiple recent backups exist for different components | Wrong component/version restored | [[sharepoint-backup-restore]] |
| Run on-prem SharePoint Server cmdlets only from Windows PowerShell — the module (Subscription Edition+) or `Add-PSSnapin Microsoft.SharePoint.PowerShell` (older) | Running SharePoint Server cmdlets from PowerShell 7.x/Core, or forgetting `Add-PSSnapin` on pre-Subscription-Edition farms | Cmdlet not recognized; module/snap-in fails to load | [[sharepoint-management-shell]] |
| Launch the SharePoint Management Shell elevated whenever a cmdlet needs an elevated token | Running non-elevated; UAC silently withholds the elevated token | Cmdlet fails with a permission error despite the account holding the right group memberships | [[sharepoint-management-shell]] |
| Grant cmdlet-only access with `Add-SPShellAdmin` instead of adding operators to `securityadmin`/`db_owner`/local Administrators | Adding an operator to SQL `securityadmin` + `db_owner` + local Administrators just so they can run one cmdlet | Over-privileged accounts flagged in a security review | [[sharepoint-management-shell]] |

---

## Reverse index — symptom → likely cause

Each signature is drawn from the `symptoms:` frontmatter of the referenced page (SharePoint Health Analyzer rule names and search/cache alert names, quoted verbatim from the corpus).

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| `Server role configuration isn't correct` | A service instance on a MinRole-managed server drifted from its role's expected set; the nightly scan auto-repairs unless disabled | [[sharepoint-farm-topology]] |
| `Cached objects have been evicted` | Distributed Cache cluster memory pressure (low/high watermark eviction) | [[sharepoint-distributed-cache]] |
| `One of the cache hosts in the cluster is down` | AppFabric Caching Windows service stopped on that host | [[sharepoint-distributed-cache]] |
| `Firewall client settings on the cache host are incorrect` | AppFabric Caching TCP-In/TCP-Out firewall rules disabled | [[sharepoint-distributed-cache]] |
| Newsfeed/social data missing after a cache host reboot | `Stop-SPDistributedCacheServiceInstance` run without `-Graceful`, or `-Force`d past the drain timeout | [[sharepoint-distributed-cache]] |
| `Some content databases are growing too large` | Content database exceeded the 100 GB Health Analyzer alert threshold | [[sharepoint-content-databases]] |
| `databases...set to read only` / upgrade fails | Content database left `Read-Only=True` in SQL Server | [[sharepoint-content-databases]] |
| `orphaned Apps` / `orphaned items` | Corrupted content database; objects inaccessible but still consuming resources/licenses | [[sharepoint-content-databases]] |
| `configured to use Windows Classic authentication` | Legacy web application never migrated off Windows Classic mode | [[sharepoint-authentication]] |
| `Index: Lost Generations` | Failures exceeded fault-tolerance; acknowledged-indexed data permanently lost | [[sharepoint-search-service]] |
| `Index: Missing partition` / `Index component down` | Lost network connectivity to an index component, or the component itself is down | [[sharepoint-search-service]] |
| `Index: Indexing Blocked` | Indexer starved of resources, or content arriving faster than it can be consumed | [[sharepoint-search-service]] |
| Search results/analytics stale after a DR restore | Search's documented one-week RPO/RTO; restore froze configuration/analytics at the last backup | [[sharepoint-search-service]], [[sharepoint-backup-restore]] |
| SharePoint Server cmdlet not recognized in a PowerShell session | Session is PowerShell 7.x/Core (unsupported), or the snap-in was never loaded with `Add-PSSnapin` | [[sharepoint-management-shell]] |

---

## Domain map — pages by health area

### Farm topology and services
- [[sharepoint-overview]] — farm/MinRole/service-application spine
- [[sharepoint-farm-topology]] — three-tier vs. MinRole, server roles, proxy groups
- [[sharepoint-distributed-cache]] — AppFabric-based social cache, non-replication
- [[sharepoint-management-shell]] — on-prem cmdlet surface, module vs. snap-in

### Content
- [[sharepoint-web-applications]] — IIS boundary, zones, site collections
- [[sharepoint-content-databases]] — sizing limits, Health Analyzer rules
- [[sharepoint-authentication]] — claims-based auth, SAML, deprecated Classic mode

### Search
- [[sharepoint-search-service]] — six-component pipeline, four databases, alert catalog

### Backup and DR
- [[sharepoint-backup-restore]] — `Backup-SPFarm`/`Restore-SPFarm`, `spbrtoc.xml`, Search RPO/RTO

## See also
- [[sharepoint-overview]]
- [[active-directory-implementation-review]] — the shape this MOC follows
- [[sso-implementation-review]] — Keycloak/SSO domain equivalent of this MOC

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[technical-reference-some-content-databases-are-growing-too-large|Some content databases are growing too large (SharePoint Server)]]
- [[technical-reference-cached-objects-have-been-evicted|Cached objects have been evicted (SharePoint Server)]]
- [[technical-reference-one-of-the-cache-hosts-in-the-cluster-is-down|One of the cache hosts in the cluster is down (SharePoint Server)]]
- [[technical-reference-firewall-client-settings-on-the-cache-host-are-incorrect|Firewall client settings on the cache host are incorrect (SharePoint Server)]]
- [[technical-reference-content-databases-contain-orphaned-apps|Content databases contain orphaned Apps (SharePoint Server)]]
- [[technical-reference-one-or-more-web-applications-are-configured-to-use-windows-classic-authenticatio|One or more web applications are configured to use Windows Classic authentication (SharePoint Server)]]
- [[technical-reference-content-databases-contain-orphaned-items|Content databases contain orphaned items (SharePoint Server)]]
- [[technical-reference-search-in-sharepoint-server|Search in SharePoint Server knowledge articles]]
- [[install-planning-for-a-minrole-server-deployment-in-sharepoint-server|Planning for a MinRole server deployment in SharePoint Servers 2016, 2019, and Subscription Edition]]
<!-- crosslink:end -->
