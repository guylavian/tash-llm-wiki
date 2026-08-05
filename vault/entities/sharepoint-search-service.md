---
title: SharePoint Search Service Application
type: entity
domain: sharepoint
slug: sharepoint-search-service
summary: The Search service application pipelines content through six components (Crawl, Content Processing, Analytics Processing, Index, Query Processing, Search Administration) backed by four databases (Crawl, Link, Analytics Reporting, Search Administration), and supports an RPO/RTO of one week via Backup-SPFarm/Restore-SPFarm.
sources:
  - kb:search-search-architecture-overview
  - kb:technical-reference-database-types-and-descriptions
  - kb:search-best-practices-of-disaster-recovery-for-search
  - kb:technical-reference-search-in-sharepoint-server
  - kb:install-software-boundaries-limits-2019
provenance_extracted: 9
provenance_inferred: 1
provenance_ambiguous: 0
symptoms:
  - "Index: Lost Generations"
  - "Index: Missing partition"
  - "Index component down"
  - "Index: Indexing Blocked"
tags: [sp-search, troubleshooting, concept]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# SharePoint Search Service Application

**Search is a pipeline service application: content is crawled, processed, indexed, and
served through six cooperating components on top of four databases.**

## Body

### Components (`search-search-architecture-overview.md:35-42`)

| Component | Role |
|---|---|
| Crawl | Crawls content sources (file shares, SharePoint content, LOB apps), passes crawled items to Content Processing |
| Content Processing | Transforms crawled items, maps crawled properties to managed properties, sends them to Index |
| Analytics Processing | Runs search + usage analytics |
| Index | Writes processed items to the search index; serves incoming queries against that index |
| Query Processing | Analyzes incoming queries (precision/recall/relevance) before sending to Index |
| Search Administration | Runs search's system processes; adds/initializes new component instances |

### Databases (`technical-reference-database-types-and-descriptions.md:243-249`)

Crawl database (crawl history, last-crawl time/ID, add/update/delete tracking), Link
database (unprocessed content-processing output + search-click data for analytics),
Analytics Reporting database (usage-analysis results), Search Administration database
(search configuration).

### Scaling limit

Index components are capped at **60 per Search service application / 4 per server**,
and index partitions at **25 per Search service application**
(`install-software-boundaries-limits-2019.md:343-344`); see [[sharepoint-farm-topology]]
for the MinRole Search server role that hosts these components.

### Backup, restore, RPO/RTO

Search service applications back up and restore through `Backup-SPFarm` /
`Restore-SPFarm` (see [[sharepoint-backup-restore]] for cmdlet syntax). SharePoint
supports an **RPO and RTO of one week** for the search service application — a
restored search environment's configuration, analytics, and freshness can be up to a
week stale. Because search content is fluid/transient, only one or two full backups
need to be retained (unlike content backups, which need longer retention)
(`search-best-practices-of-disaster-recovery-for-search.md:199`). Search is offline during an overwrite-mode
restore; running a parallel new service application and cutting over after a fresh crawl
avoids the outage at roughly double the index/database footprint
(`search-best-practices-of-disaster-recovery-for-search.md:296-298`).

### Troubleshooting: search alert catalog

`technical-reference-search-in-sharepoint-server.md` documents named search health alerts —
selected ones relevant to indexing outages:

| Alert | Cause | Resolution | Note |
|---|---|---|---|
| Index: Lost Generations | Failures exceeded fault-tolerance; acknowledged-indexed data permanently lost | Full re-crawl required | `technical-reference-search-in-sharepoint-server.md:497-511` |
| Index: Missing partition | Missing injection from index component; lost network connectivity; index component down | Lookup Service auto-restarts; check index component and connectivity | `technical-reference-search-in-sharepoint-server.md:517-543` |
| Index: Indexing Blocked | Indexer starved of resources, or content arriving faster than it can be consumed | Investigate index-component resource usage; adjust topology to lower feed rate | `technical-reference-search-in-sharepoint-server.md:547-561` |
| Index: Journal IO Exception (Read/Write) | Disk-level: file lock, external file change, physical disk problem | Release lock / revert change / fix disk; may require deleting and refeeding the Journal | `technical-reference-search-in-sharepoint-server.md:571-633` |
| Index Lookup: Missing partition | Index component down; missing injection; lost network connectivity | Auto-restart; check index component and communication | `technical-reference-search-in-sharepoint-server.md:655-681` |

## Contradictions / caveats

None noted — the search architecture description is consistent across the corpus
chunks (component table matches the databases described in the search backup/restore
material).

## See also
- [[sharepoint-farm-topology]]
- [[sharepoint-distributed-cache]]
- [[sharepoint-backup-restore]]
- [[sharepoint-implementation-review]]
- [[sharepoint-overview]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[search-search-architecture-overview|Overview of search architecture in SharePoint Server]]
- [[technical-reference-database-types-and-descriptions|Database types and descriptions in SharePoint Server]]
- [[search-best-practices-of-disaster-recovery-for-search|Disaster recovery best practices and strategies for SharePoint 2016 search]]
- [[technical-reference-search-in-sharepoint-server|Search in SharePoint Server knowledge articles]]
- [[install-software-boundaries-limits-2019|Software boundaries and limits for SharePoint Servers 2016 and 2019]]
<!-- crosslink:end -->
