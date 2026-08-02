---
title: How big can a SharePoint content database get before it becomes a problem?
type: question
domain: sharepoint
slug: sharepoint-content-database-size-limits
summary: 200 GB is Microsoft's general-usage sizing recommendation (500 databases/farm caps a farm at 100 TB); up to 4 TB is supported with 0.25-2 IOPS/GB and HA/DR planning; but the SharePoint Health Analyzer fires "Some content databases are growing too large" at a lower, availability-focused 100 GB threshold, so a database can be within Microsoft's supported/recommended sizing and still trip the built-in monitor.
sources:
  - kb:install-software-boundaries-limits-2019
  - kb:technical-reference-some-content-databases-are-growing-too-large
  - kb:upgrade-and-update-upgrade-content-databases
provenance_extracted: 6
provenance_inferred: 1
provenance_ambiguous: 0
question_tier: conceptual
tags: [sp-content, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# How big can a SharePoint content database get before it becomes a problem?

**There are two different numbers in the official guidance, answering two different
questions: 200 GB is the sizing recommendation for planning, while 100 GB is the
threshold where the built-in Health Analyzer starts complaining — a database can be
"correctly" sized by Microsoft's own guidance and still trigger the monitor.**

## Answer

### The sizing recommendation: 200 GB (up to 4 TB with conditions)

The farm-wide limits reference states: "We strongly recommended limiting the size of
content databases to 200 GB, except when the circumstances in the following rows in
this table apply"
(`reference/sharepoint/install-software-boundaries-limits-2019.md:158`,
extracted). At the farm level, "With 200 GB per content database, and 500 content
databases per farm, SharePoint Server 2016 supports 100 TB of data per farm"
(`reference/sharepoint/install-software-boundaries-limits-2019.md:157`, extracted)
— the farm cap of **500 content databases** is itself a supported limit
(`reference/sharepoint/install-software-boundaries-limits-2019.md:156`, extracted).

Growing past 200 GB is still supported, up to a hard boundary: "Content databases of
up to 4 TB are supported when the following requirements are met: Disk subsystem
performance of 0.25 IOPS per GB. 2 IOPs per GB are recommended for optimal
performance," plus documented HA/DR/capacity/performance-testing planning
(`reference/sharepoint/install-software-boundaries-limits-2019.md:159-163`, extracted).
Above 4 TB, the guidance drops back to "supported" only for a narrow document-archive
scenario (no explicit size limit, but Document Center/Records Center templates, <5%
content accessed/month, and no alerts/workflows/item-level security)
(`reference/sharepoint/install-software-boundaries-limits-2019.md:170-173`, extracted).

### The monitor's threshold: 100 GB

Central Administration's Health Analyzer runs a separate, lower-stakes rule: "Rule
Name: **Some content databases are growing too large**." "Summary: The content
databases have grown larger than 100 gigabytes (GB). Large content databases can be
difficult to back up and restore. They are also more likely to cause the application to
stop responding when you perform operations that affect entire databases." "Cause:
Content databases exceed 100 GB"
(`reference/sharepoint/technical-reference-some-content-databases-are-growing-too-large.md:23-27`,
extracted). The default remediation — "Repair Automatically" — "prevent[s] new sites
from being added to these databases" once a database crosses 100 GB, and the
suggested fix is to "move some site collections to other databases"
(`reference/sharepoint/technical-reference-some-content-databases-are-growing-too-large.md:29,39-43`,
extracted).

### Why both numbers are correct at once

These aren't contradictory sources disagreeing on one fact — they measure different
things. 200 GB is the *planning* ceiling before Microsoft says you should actively
manage size (splitting site collections, evaluating RBS/alternative backup, IOPS
capacity); 100 GB is the *operational availability* threshold where the Health Analyzer
proactively guards against a large all-or-nothing database hanging routine
farm/backup operations (inferred — direct synthesis of the "difficult to back up and
restore" / "stop responding" rationale in the Health Analyzer rule against the separate
200 GB/4 TB sizing table, which never itself claims 100 GB as unsafe). A database sitting
comfortably at, say, 150 GB is fully within Microsoft's supported-and-recommended
sizing guidance and will still show up flagged in Health Analyzer.

### Splitting an oversized database

New content databases are attached (and existing ones split into) via the
`Mount-SPContentDatabase` cmdlet — Central Administration's UI path is not supported
for this: "You must use the Mount-SPContentDatabase cmdlet to attach a content
database to a web application. Using the SharePoint Central Administration pages to
attach a content database is not supported for upgrading"
(`reference/sharepoint/upgrade-and-update-upgrade-content-databases.md:190`,
extracted).

## Contradictions / caveats

The 100 GB Health Analyzer threshold and the 200 GB/4 TB sizing table are **both real,
current guidance from the same docset** — treat them as answering different questions
(when does the built-in monitor complain vs. how big should you plan for) rather than
reconciling them into a single number. If a question doesn't specify which one it's
asking about, surface both.

## See also
- [[sharepoint-content-databases]]
- [[sharepoint-web-applications]]
- [[sharepoint-backup-restore]]
- [[sharepoint-implementation-review]]
- [[sharepoint-overview]]

## References

**RH ground-truth (kb:)**
- `install-software-boundaries-limits-2019` — Software boundaries and limits for SharePoint Servers 2016 and 2019 (content database and site-collection size/count limits table)
- `technical-reference-some-content-databases-are-growing-too-large` — Some content databases are growing too large (SharePoint Server) (Health Analyzer rule)
- `upgrade-and-update-upgrade-content-databases` — Upgrade content databases (SharePoint Server) (`Mount-SPContentDatabase` attach procedure)

**Wiki**
- [[sharepoint-content-databases]]
- [[sharepoint-overview]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[install-software-boundaries-limits-2019|Software boundaries and limits for SharePoint Servers 2016 and 2019]]
- [[technical-reference-some-content-databases-are-growing-too-large|Some content databases are growing too large (SharePoint Server)]]
- [[upgrade-and-update-upgrade-content-databases|Upgrade content databases to SharePoint Server 2016]]
<!-- crosslink:end -->
