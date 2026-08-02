---
title: SharePoint Server Overview — Farms, Roles, and Service Applications
type: topic
domain: sharepoint
slug: sharepoint-overview
summary: SharePoint Server is Microsoft's on-premises collaboration/content platform; a farm is one or more servers sharing a configuration database, laid out in a classic three-tier (web/application/database) topology or, from 2016+, MinRole (eight predefined server roles SharePoint auto-configures), with functionality exposed farm-wide as service applications published through proxy groups.
sources:
  - kb:sharepoint-server-md-sharepoint-server
  - kb:install-multiple-servers-for-a-three-tier-farm
  - kb:install-planning-for-a-minrole-server-deployment-in-sharepoint-server
  - kb:install-overview-of-minrole-server-roles-in-sharepoint-server
  - kb:administration-add-or-remove-a-service-application-connection-to-a-web-application
  - kb:hybrid-cloud-hybrid-search-faq
  - kb:security-for-sharepoint-server-plan-user-authentication
  - kb:security-for-sharepoint-server-authentication-overview
  - kb:install-software-boundaries-limits-2019
provenance_extracted: 12
provenance_inferred: 2
provenance_ambiguous: 0
tags: [sp-farm, sp-content, sp-search]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# SharePoint Server Overview — Farms, Roles, and Service Applications

**SharePoint Server is Microsoft's on-premises collaboration and content-management
platform; IT Pros plan, deploy, and manage it as one or more "farms" — servers that
share a configuration database and jointly host web applications, site collections, and
shared service applications (search, managed metadata, distributed cache, …).**

## Body

### What SharePoint Server is

This wiki's corpus is the official IT Pro guidance for planning, deploying, and managing
SharePoint Server Subscription Edition, 2019, 2016, and 2013
(`sharepoint-server-md-sharepoint-server.md:19`). "Farm," "server role," and "service
application" are the three organizing concepts below; every other entity in this domain
(search, distributed cache, content databases, authentication, backup, management
shell) is a piece of one of them.

### Farm architecture: the classic three-tier model

The baseline SharePoint topology — still the mental model MinRole (below) builds on —
is a **three-tier farm**: "two front-end web servers, an application server, and a
database server." The **web tier** takes user requests (and can host dedicated query
components); the **application tier** hosts Central Administration and back-end
services like crawl components, query components, and profile pages; the **database
tier** runs SQL Server, with mirroring or a failover cluster for HA
(`install-multiple-servers-for-a-three-tier-farm.md:23`).

### MinRole (SharePoint Server 2016+): SharePoint picks the services, not you

MinRole is "a new farm topology based on a set of predefined server roles" — instead of
an admin manually deciding which services run on which server, the admin assigns a
**role** to each server (at farm creation or when a server joins), and "SharePoint will
automatically configure the services on each server based on the server's role"
(`install-overview-of-minrole-server-roles-in-sharepoint-server.md:29`). It is also
self-healing: MinRole "scans each server in your farm once a day" and can auto-repair or
just report a server that has drifted from its role's expected service set
(`install-overview-of-minrole-server-roles-in-sharepoint-server.md:65`).

There are **eight pre-defined server roles in 3 categories**
(`install-planning-for-a-minrole-server-deployment-in-sharepoint-server.md:29-50`):

| Category | Roles | Notes |
|---|---|---|
| Dedicated | Front-end, Application, Distributed Cache, Search | Optimized for performance/scalability; typical in large farms |
| Shared (requires Nov 2016 PU / Feature Pack 1) | "Front-end with Distributed Cache", "Application with Search" | Combine dedicated roles on fewer servers for small/medium farms |
| Special | Single-Server Farm, Custom | Single-Server Farm replaces the old Standalone install mode and cannot exceed one SharePoint server in the farm; Custom is unmanaged by MinRole entirely |

See [[sharepoint-farm-topology]] for the full role table and how content vs. services vs.
search farms map onto these roles, and [[sharepoint-distributed-cache]] for why the
Distributed Cache role specifically does **not** get MinRole's usual HA treatment (a
cache host's data is not replicated to other cache hosts).

### Service applications and proxy groups

Farm-wide functionality — search, managed metadata, secure store, business data
connectivity, and more — is packaged as a **service application**. A web application
only gets access to a service application through a **proxy**, and every service
application's proxy is added to a **proxy group** (normally the farm's default proxy
group) as part of standing it up
(`administration-add-or-remove-a-service-application-connection-to-a-web-application.md:23`).
This proxy-group indirection is also the mechanism behind splitting a farm topology into a
dedicated **Content farm** (hosts web applications/site collections) and a **Service
farm** (hosts shared service applications like Search), letting one Service farm's search
or profile service be consumed by several Content farms
(`hybrid-cloud-hybrid-search-faq.md:154-156`) — see [[sharepoint-search-service]] and
[[sharepoint-farm-topology]].

### Content: web applications, site collections, content databases

A **web application** is the IIS-hosted boundary mapping content databases and
authentication zones to a URL space; **site collections** (and the sites nested under
them) are provisioned inside it, backed by one or more **content databases**. Farm-wide
supported/recommended sizing from the corpus's limits reference
(`install-software-boundaries-limits-2019.md:156-158`): up to 500 content databases per farm at a
recommended 200 GB each (100 TB total), up to 250,000 site collections per farm. See
[[sharepoint-web-applications]] and [[sharepoint-content-databases]] for the full limit
tables and the Health Analyzer rules that fire around them.

### Search, distributed cache, authentication, backup, management shell

The remaining domain entities go deep on one piece each:

- [[sharepoint-search-service]] — the six-component crawl→index→query pipeline and its four databases
- [[sharepoint-distributed-cache]] — the AppFabric-based, non-replicated social/newsfeed cache
- [[sharepoint-authentication]] — claims-based auth (Windows/forms/SAML/OIDC) vs. deprecated Windows Classic mode
- [[sharepoint-backup-restore]] — `Backup-SPFarm`/`Restore-SPFarm`, the `spbrtoc.xml` manifest, and Search's one-week RPO/RTO
- [[sharepoint-management-shell]] — the on-prem PowerShell cmdlet surface (module vs. snap-in, Windows PowerShell only)

Authentication is worth one structural note here: SharePoint's default is
**claims-based** identity (Windows, forms-based, SAML, and — Subscription Edition —
OIDC), issued by the SharePoint Security Token Service
(`security-for-sharepoint-server-authentication-overview.md:37-41`); the older **Windows
Classic** mode is deprecated, can only be created via `New-SPWebApplication`, and cannot be
migrated back to from claims once converted
(`security-for-sharepoint-server-plan-user-authentication.md:85`).

## Contradictions / caveats

MinRole and its shared/special roles are a **SharePoint Server 2016+** concept;
SharePoint 2013 only has the classic three-tier, manually-assigned-role model. When a
question doesn't specify a version, default to describing MinRole (2016+) since it is
the corpus's primary framing, but flag the version split for anyone still running 2013
(inferred from the MinRole applicability banner scoping "2013 2016 2019 Subscription
Edition" against the "What is MinRole?" text, which frames it as "introduced in
SharePoint Server 2016").

## See also
- [[sharepoint-farm-topology]]
- [[sharepoint-web-applications]]
- [[sharepoint-content-databases]]
- [[sharepoint-search-service]]
- [[sharepoint-distributed-cache]]
- [[sharepoint-authentication]]
- [[sharepoint-backup-restore]]
- [[sharepoint-management-shell]]
- [[sharepoint-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[sharepoint-server-md-sharepoint-server|Learn about how to use SharePoint Server.]]
- [[install-multiple-servers-for-a-three-tier-farm|Install SharePoint 2013 across multiple servers for a three-tier farm]]
- [[install-planning-for-a-minrole-server-deployment-in-sharepoint-server|Planning for a MinRole server deployment in SharePoint Servers 2016, 2019, and Subscription Edition]]
- [[install-overview-of-minrole-server-roles-in-sharepoint-server|Overview of MinRole Server Roles in SharePoint Servers 2016, 2019, and Subscription Edition]]
- [[administration-add-or-remove-a-service-application-connection-to-a-web-application|Add or remove service application connections from a web application in SharePoint Server]]
- [[hybrid-cloud-hybrid-search-faq|Cloud hybrid search service (Cloud SSA) FAQ]]
- [[security-for-sharepoint-server-plan-user-authentication|Plan for user authentication methods in SharePoint Server]]
- [[security-for-sharepoint-server-authentication-overview|Authentication overview for SharePoint Server]]
- [[install-software-boundaries-limits-2019|Software boundaries and limits for SharePoint Servers 2016 and 2019]]
<!-- crosslink:end -->
