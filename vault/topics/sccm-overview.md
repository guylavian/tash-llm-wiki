---
title: Configuration Manager (SCCM) — Overview
type: topic
domain: sccm
slug: sccm-overview
summary: The orientation page for the sccm brain — Configuration Manager's site hierarchy (CAS/primary/secondary + site systems), the client lifecycle (discovery, install, health), the four core management workloads (apps, OSD, software updates, compliance), and the extensibility surface (admin service REST API, PowerShell module) that ties it to Intune co-management.
sources:
  - kb:core-fundamentals-of-sites-and-hierarchies
  - kb:core-design-a-hierarchy-of-sites
  - kb:core-add-site-system-roles
  - kb:core-client-installation-methods
  - kb:core-introduction-to-collections
  - kb:apps-create-and-deploy-an-application
  - kb:osd-introduction-to-operating-system-deployment
  - kb:sum-software-updates-introduction
  - kb:compliance-fundamentals-of-compliance
  - kb:comanage-overview
  - kb:core-the-content-library
  - kb:sccm-intune-configmgr-develop-adminservice
  - kb:sccm-powershell-sccm-sccm-sccm-ps-p0001-0040
provenance_extracted: 11
provenance_inferred: 3
provenance_ambiguous: 0
tags: [sccm-core, sccm-apps, sccm-osd, sccm-updates, sccm-compliance]
status: draft
updated: 2026-07-23
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# Configuration Manager (SCCM) — Overview

**Microsoft Configuration Manager (ConfigMgr / SCCM, now branded as part of "Microsoft Endpoint
Configuration Manager" and cloud-attached to Intune) is a hierarchical, site-based system for
discovering, installing, and managing Windows (and cross-platform) clients — software
deployment, OS deployment, patching, and compliance, all driven from one console.**

## Body

### Site hierarchy

A deployment is one or more **sites** forming a **hierarchy**. The first site installed is either
a **central administration site** (CAS — a central point of administration for large,
geographically distributed deployments; it does not itself manage clients) or a **stand-alone
primary site** (manages clients directly, suitable for smaller deployments and can later be
expanded under a new CAS). A CAS supports multiple child **primary sites**, and a primary site
can extend its reach with child **secondary sites** for slow-network locations — the primary site
still manages all clients; the secondary site just compresses/relays traffic. See
[[sccm-site-hierarchy]] for site system roles, prerequisites, and AD DS publishing.

### Client lifecycle

Clients are installed by one of several methods — **client push** (administrative-rights install
to discovered resources, retried for up to seven days), software update point, GPO, logon
script, manual, or OSD-embedded — and are then kept healthy by scheduled **client health
checks** (verify install, prerequisites, disk space, remediate) surfaced on the **client health
dashboard**. See [[sccm-client-health]].

### Targeting: collections

Nearly every management operation (deployments, client settings, RBA scoping, maintenance
windows) targets a **collection** rather than individual resources — a saved grouping of
devices or users, built-in (e.g. All Systems) or custom, evaluated on a schedule or
incrementally. See [[sccm-collections]].

### The four core workloads

- **Application deployment** — package software into applications (with one or more
  deployment types) and deploy them to a collection; supersede/revise as versions change. See
  [[sccm-application-deployment]].
- **Operating system deployment (OSD)** — task sequences drive boot image → OS image →
  driver/settings steps to install, upgrade, refresh, or capture Windows across bare-metal, PXE,
  multicast, or media-based scenarios. See [[sccm-task-sequences-and-osd]].
- **Software updates** — synchronizes update metadata from Microsoft Update at the top-tier
  site, evaluates client compliance, and deploys either manually or via **automatic deployment
  rules (ADR)** for recurring cycles like Patch Tuesday. See [[sccm-software-updates-and-adr]].
- **Compliance settings** — configuration items bundled into configuration baselines, deployed
  to a collection, evaluated (non-deterministic order) for drift/compliance. See
  [[sccm-compliance-baselines]].

All four workloads share the same **content distribution** plumbing: distribution points hosting
a single-instance **content library**, matched to clients by boundary group. See
[[sccm-distribution-points]].

### Cloud attach and extensibility

**Co-management** concurrently manages a Windows device with both Configuration Manager and
Intune, letting an admin switch individual workloads (compliance policies, Windows Update
policies, endpoint protection, etc.) to Intune's authority while ConfigMgr keeps managing the
rest — see [[sccm-co-management]]. Programmatic/automation access goes through two surfaces: the
**admin service**, a REST API over the SMS Provider ([[sccm-admin-service]]), and the
**ConfigMgr PowerShell module**, which exposes the same functionality as cmdlets against a
site-scoped PSDrive ([[sccm-powershell-module]]).

## Contradictions / caveats

This is a **corpus-backed** domain: `reference/sccm/` holds ~2,758 imported Microsoft Learn doc
bodies (the `intune/configmgr` docset) plus PDF-chunked notes for the PowerShell cmdlet guide,
the admin service guide, and the `troubleshoot-mem-configmgr` break-fix guide (page markers
`<!-- p.N -->` inside those chunk notes — cite the chunk stem, not a page number). Per
`_meta/taxonomy.md`, `tiers-covered: [conceptual, support-kb]` — the troubleshoot corpus gives a
support-kb (known-issue) tier, but there is no `scenarios` (live-incident) tier yet, so a
break-fix answer beyond what's in `sccm-troubleshoot-mem-configmgr-*` should carry the H1
out-of-coverage banner.

## See also
- [[sccm-site-hierarchy]]
- [[sccm-client-health]]
- [[sccm-collections]]
- [[sccm-application-deployment]]
- [[sccm-task-sequences-and-osd]]
- [[sccm-software-updates-and-adr]]
- [[sccm-compliance-baselines]]
- [[sccm-distribution-points]]
- [[sccm-co-management]]
- [[sccm-admin-service]]
- [[sccm-powershell-module]]
- [[sccm-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[core-fundamentals-of-sites-and-hierarchies|Fundamentals of sites and hierarchies]]
- [[core-design-a-hierarchy-of-sites|Design a site hierarchy]]
- [[core-add-site-system-roles|Add site system roles]]
- [[core-client-installation-methods|Client installation methods]]
- [[core-introduction-to-collections|Collections introduction]]
- [[apps-create-and-deploy-an-application|Create and deploy an application]]
- [[osd-introduction-to-operating-system-deployment|Introduction to operating system deployment]]
- [[sum-software-updates-introduction|Introduction to software updates]]
- [[compliance-fundamentals-of-compliance|Understand compliance in Configuration Manager]]
- [[comanage-overview|Co-management for Windows devices]]
- [[core-the-content-library|The content library]]
- [[sccm-intune-configmgr-develop-adminservice|Administration service documentation]]
- [[sccm-powershell-sccm-sccm-sccm-ps-p0001-0040|Overview — pages 1-40]]
<!-- crosslink:end -->
