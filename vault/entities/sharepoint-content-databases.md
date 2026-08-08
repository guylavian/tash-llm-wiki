---
title: SharePoint Content Databases
type: entity
domain: sharepoint
slug: sharepoint-content-databases
summary: Content databases store all site content for a web application; SharePoint recommends capping them at 200 GB (4 TB supported with extra IOPS/HA planning, unlimited for document-archive scenarios) and 5,000 site collections (10,000 supported), with a Health Analyzer rule flagging databases over 100 GB and set-to-read-only or orphaned-object states that block upgrade.
sources:
  - kb:install-software-boundaries-limits-2019
  - kb:administration-attach-or-detach-content-databases
  - kb:upgrade-and-update-upgrade-content-databases
  - kb:technical-reference-some-content-databases-are-growing-too-large
  - kb:technical-reference-content-databases-contain-orphaned-apps
  - kb:technical-reference-content-databases-contain-orphaned-items
  - kb:technical-reference-databases-within-this-farm-are-set-to-read-only-and-will-fail-to-upgrade-unless
provenance_extracted: 10
provenance_inferred: 1
provenance_ambiguous: 0
symptoms:
  - "orphaned Apps"
  - "orphaned items"
  - "databases.*set to read only"
tags: [sp-content, troubleshooting, concept]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# SharePoint Content Databases

**The SQL Server database that stores all site content — documents, list items, and
site structure — for a web application; a web application can have many, and their
size/count are the main site-collection-growth throttles.**

## Body

The content database stores all site content for a farm; this is not supported for
direct SQL manipulation — content databases are attached to a web application via
`Mount-SPContentDatabase`: "You must use the Mount-SPContentDatabase cmdlet to
attach a content database to a web application. Using the SharePoint Central
Administration pages to attach a content database is not supported for upgrading."
(`upgrade-and-update-upgrade-content-databases.md:190`).

### Size and count limits (supported vs. recommended)

`install-software-boundaries-limits-2019.md:154-177` gives these guidelines:

| Limit | Value | Type |
|---|---|---|
| Content databases per farm | 500 | Supported |
| Content database size (general usage) | 200 GB recommended | Supported |
| Content database size (all usage scenarios) | 4 TB | Supported, requires 0.25–2 IOPS/GB and HA/DR/capacity planning |
| Content database size (document-archive scenario) | No explicit limit | Supported, requires Document Center/Records Center templates, <5% content accessed/month, no alerts/workflows/item-level security |
| Items per content database | 60 million tested max | Supported |
| Site collections per content database | 5,000 recommended, 10,000 supported (max 2,500 non-Personal) | Supported |

At 200 GB × 500 databases, a farm supports up to 100 TB of data. Native SharePoint
backup for content databases over 200 GB may not meet backup/restore requirements
— alternative backup solutions should be evaluated for larger databases
(`install-software-boundaries-limits-2019.md:158-163`).

### Health Analyzer: databases growing too large

The **"Some content databases are growing too large"** rule fires once a content
database exceeds **100 GB** (a lower, availability-focused threshold than the 200 GB
sizing recommendation above): large databases are harder to back up/restore and more
likely to hang the farm during whole-database operations. The default remediation
edits the rule to stop new sites landing in the oversized database and moves some
site collections to other databases
(`technical-reference-some-content-databases-are-growing-too-large.md:25-43`).

### Health Analyzer: orphaned objects and read-only state

- **Orphaned Apps** — a corrupted content database can contain orphaned apps that
  are inaccessible but still consume resources/licenses and can break upgrade; fix by
  removing the orphaned apps from the affected site collection
  (`technical-reference-content-databases-contain-orphaned-apps.md`).
- **Orphaned items** — a related rule for orphaned list/library items
  (`technical-reference-content-databases-contain-orphaned-items.md`).
- **Databases set to read-only** — a content database left read-only in SQL Server
  will fail to upgrade; fix by flipping the database's `Read-Only` property back to
  `False` in SQL Server Management Studio before attempting upgrade
  (`technical-reference-databases-within-this-farm-are-set-to-read-only-and-will-fail-to-upgrade-unless.md`).

## Contradictions / caveats

There are two different "size ceiling" numbers in the corpus for the same object.

The general-usage **sizing recommendation** is 200 GB
(`install-software-boundaries-limits-2019.md:158`).

The **Health Analyzer alert threshold** for availability risk is a separate, lower
number (`technical-reference-some-content-databases-are-growing-too-large.md:25,27`).

Both are real, from the same docset;
they answer different questions (how big should I plan for vs. when does the built-in
monitor complain) — do not treat them as contradictory without noting which one a
question is actually asking about.

## See also
- [[sharepoint-web-applications]]
- [[sharepoint-backup-restore]]
- [[sharepoint-implementation-review]]
- [[sharepoint-overview]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[install-software-boundaries-limits-2019|Software boundaries and limits for SharePoint Servers 2016 and 2019]]
- [[administration-attach-or-detach-content-databases|Attach or detach content databases in SharePoint Server]]
- [[upgrade-and-update-upgrade-content-databases|Upgrade content databases to SharePoint Server 2016]]
- [[technical-reference-some-content-databases-are-growing-too-large|Some content databases are growing too large (SharePoint Server)]]
- [[technical-reference-content-databases-contain-orphaned-apps|Content databases contain orphaned Apps (SharePoint Server)]]
- [[technical-reference-content-databases-contain-orphaned-items|Content databases contain orphaned items (SharePoint Server)]]
- [[technical-reference-databases-within-this-farm-are-set-to-read-only-and-will-fail-to-upgrade-unless|Databases within this farm are set to read only and will fail to upgrade unless it's set to a read-write state (SharePoint Server)]]
<!-- crosslink:end -->
