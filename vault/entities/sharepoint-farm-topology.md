---
title: SharePoint Farm Topology & Service Applications
type: entity
domain: sharepoint
slug: sharepoint-farm-topology
summary: A SharePoint farm is one or more servers sharing a configuration database; MinRole (2016+) assigns each server a predefined role (Front-end, Application, Distributed Cache, Search, Search shared roles, Single-Server Farm, Custom) so SharePoint — not the admin — decides which service instances run where, and service applications are published to consuming web apps through proxy groups.
sources:
  - kb:install-planning-for-a-minrole-server-deployment-in-sharepoint-server
  - kb:install-overview-of-minrole-server-roles-in-sharepoint-server
  - kb:install-multiple-servers-for-a-three-tier-farm
  - kb:administration-add-or-remove-a-service-application-connection-to-a-web-application
  - kb:hybrid-cloud-hybrid-search-faq
provenance_extracted: 10
provenance_inferred: 2
provenance_ambiguous: 0
symptoms:
  - "Server role configuration isn't correct"
tags: [sp-farm, concept]
status: draft
updated: 2026-07-23
graph_community: "SharePoint Server — Implementation Review (Evaluation-Lens MOC)"
---

# SharePoint Farm Topology & Service Applications

**A SharePoint farm is a set of servers sharing one configuration database; MinRole
lets each server declare a role and SharePoint starts/stops the right service instances
on it automatically, while service applications are shared across web apps through
proxy groups.**

## Body

### Classic three-tier topology

A three-tier farm has a web tier (front-end servers handling user requests), an
application tier (servers hosting Central Administration and back-end services —
crawl components, query components, profile pages), and a database tier (SQL Server,
optionally mirrored or clustered for HA). Central Administration by default runs on an
application-tier server (`install-multiple-servers-for-a-three-tier-farm.md:23,197`).

### MinRole (SharePoint Server 2016+)

MinRole is a farm topology where the admin picks a **server role** when creating or
joining a farm, and SharePoint automatically starts/stops the service instances that
role needs — instead of the admin manually choosing which services run where. Eight
predefined roles in three categories
(`install-planning-for-a-minrole-server-deployment-in-sharepoint-server.md:29-50`):

- **Dedicated roles** — Front-end (user-request-optimized), Application (background
  tasks, timer jobs, search crawl targets), Distributed Cache, Search.
- **Shared roles** (require the November 2016 PU / Feature Pack 1) — "Front-end with
  Distributed Cache" and "Application with Search," for small/medium farms that want
  fewer servers.
- **Special roles** — Single-Server Farm (replaces the old Standalone install mode; the
  admin must still install/prepare SQL Server separately and a farm with this role can
  have only one SharePoint server) and Custom (MinRole does not manage service
  instances on a Custom-role server at all).

MinRole runs a **daily self-healing scan** on every server to confirm it's running the
service instances its role requires, and can be configured to auto-repair or just report
non-compliant servers. Content farms need Front-end + Application + Distributed
Cache (+ Search if hosting it locally); Services farms need Application + Distributed
Cache (+ Search if hosting it); Search farms need only the Search role
(`install-overview-of-minrole-server-roles-in-sharepoint-server.md:65`,
`install-planning-for-a-minrole-server-deployment-in-sharepoint-server.md:70-75`).

### Service applications and proxy groups

A service application (Search, Managed Metadata, User Profile, Secure Store, …)
exposes its functionality to web applications through a **service application proxy**
that is added to a **proxy group** — normally the farm's default proxy group, created
as part of standing up the service application
(`administration-add-or-remove-a-service-application-connection-to-a-web-application.md:23`).
A web application only consumes a
service application whose proxy sits in a proxy group associated with that web
application **(inferred** from the proxy-group mechanism — not itself spelled out in
that note**)**; this indirection is the documented mechanism behind splitting a
topology into a dedicated **Content farm** (web applications/site collections) and a
**Service farm** (shared service applications), so one Service farm's search or profile
service can be consumed by several Content farms: "My SharePoint in Microsoft 365
topology consists of multiple SharePoint farms (for example, Content farm, Service
Farm)... assuming Search is in the service farm, Cloud SSA should ideally be
configured in the service farm" (`hybrid-cloud-hybrid-search-faq.md:154-156`).

## Contradictions / caveats

MinRole topology guidance and the shared-role feature are specific to SharePoint
Server 2016/2019/Subscription Edition; SharePoint 2013 only supports the classic
manual-role three-tier model (inferred from the "Overview of MinRole Server Roles in
SharePoint Servers 2016, 2019, and Subscription Edition" scoping — 2013 is absent
from that feature's applicability).

## See also
- [[sharepoint-overview]]
- [[sharepoint-web-applications]]
- [[sharepoint-distributed-cache]]
- [[sharepoint-search-service]]
- [[sharepoint-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[install-planning-for-a-minrole-server-deployment-in-sharepoint-server|Planning for a MinRole server deployment in SharePoint Servers 2016, 2019, and Subscription Edition]]
- [[install-overview-of-minrole-server-roles-in-sharepoint-server|Overview of MinRole Server Roles in SharePoint Servers 2016, 2019, and Subscription Edition]]
- [[install-multiple-servers-for-a-three-tier-farm|Install SharePoint 2013 across multiple servers for a three-tier farm]]
- [[administration-add-or-remove-a-service-application-connection-to-a-web-application|Add or remove service application connections from a web application in SharePoint Server]]
- [[hybrid-cloud-hybrid-search-faq|Cloud hybrid search service (Cloud SSA) FAQ]]
<!-- crosslink:end -->
