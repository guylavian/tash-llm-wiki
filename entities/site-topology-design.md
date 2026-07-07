---
title: Site Topology Design
type: entity
domain: active-directory
slug: site-topology-design
summary: Inputs and principles for designing AD DS site topology — sites, subnets, and site links — which governs replication scheduling, DC placement, and client logon optimization.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Designing-the-Site-Topology (Microsoft Learn — Designing the Site Topology, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Understanding-Active-Directory-Site-Topology (Microsoft Learn — Understanding Active Directory Site Topology, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-a-Site-Design (Microsoft Learn — Creating a Site Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-a-Site-Link-Design (Microsoft Learn — Creating a Site Link Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Finding-Additional-Resources-for-Windows-Server-2008-Active-Directory-Site-Topology-Design (Microsoft Learn — Finding Additional Resources for Windows Server 2008 Active Directory Site Topology Design, fetched 2026-06-18)
  - kb:ad-ds-designing-the-site-topology
  - kb:ad-ds-understanding-active-directory-site-topology
  - kb:ad-ds-creating-a-site-design
  - kb:ad-ds-creating-a-site-link-design
  - kb:ad-ds-finding-additional-resources-for-windows-server-2008-active-directory-site-topology-design
provenance_extracted: 14
provenance_inferred: 4
provenance_ambiguous: 0
tags: [sites-topology, replication, logical-design, concept]
status: draft
updated: 2026-07-02
---

# Site Topology Design

**Site topology maps the physical network — IP subnets and WAN links — into AD DS objects (sites, subnets, site links) that control replication scheduling and DC/client affinity.**

## What site topology governs

- **Replication scheduling and cost** — the KCC generates the intra-site and inter-site replication topology; site link cost and schedule control when and how much AD data flows over WAN links
- **DC and GC placement** — DCs are placed into sites so that clients authenticate locally without traversing WAN links
- **Client logon optimization** — the DC Locator service uses site membership to direct clients to the closest DC
- **RODC placement** — branch offices with inadequate physical security deploy RODCs; site topology determines which writable DC the RODC replicates from

## Inputs to site topology design

Gather these before designing:
1. **Physical network map** — all IP subnets and their locations
2. **WAN link speeds and available bandwidth** — used to set site link costs and replication schedules
3. **DC placement requirements** — number of users per location, authentication latency targets
4. **Forest/domain structure** — regional domains defined during [[domain-design]] map directly to site regions (inferred)
5. **GC placement requirements** — in multi-domain forests, GC servers must be reachable for logon; sites without a GC depend on universal group membership caching or WAN GC access — see [[universal-group-membership-caching]]
6. **RODC candidates** — branch sites with limited physical security

## Site design principles

- Each distinct physical location with reliable high-bandwidth intra-site connectivity (typically LAN) becomes a separate site (inferred)
- WAN-connected locations should be in separate sites so inter-site replication can be scheduled and compressed
- Sites are named and associated with IP subnets via subnet objects
- Use stable naming (e.g., geographic or datacenter codes) — site names appear in DC Locator queries and replication topology logs

## Site links and replication schedule

Site links define the path between sites with a cost (lower = preferred) and a schedule (when replication is allowed). The KCC builds bridgeheads and the inter-site replication topology from site link objects. (inferred: by default the "Bridge all site links" option is on, allowing indirect replication paths; for large or complex topologies, disabling bridging and defining explicit site link bridges gives more control)

Key parameters on a site link:
- **Cost** — relative preference; KCC selects lowest-cost path
- **Replication interval** — how often changes are replicated over the link (default 180 minutes for inter-site)
- **Schedule** — time windows when replication is permitted

## DC and GC placement relationship

Site topology design feeds directly into [[capacity-and-placement-planning]]:
- Every site that requires local authentication needs at least one DC for its domain
- Sites in multi-domain forests need a GC server or universal group membership caching enabled
- Forest root DCs should be in hub locations and datacenters; shortcut trusts can substitute for a forest root DC in remote locations where reliable connectivity exists

## Contradictions / caveats

- Sites are a physical topology construct; they do not correspond to domains or OUs
- Environments with 100+ branch sites should review the Adlb.exe bridgehead load-balancing behavior introduced in Windows Server 2008 RODC environments
- For environments with WAN links below 28.8 Kbps or very large user counts, consult a specialist — the standard domain-sizing tables do not apply

## Reference notes
- [[ad-ds-designing-the-site-topology]]
- [[ad-ds-understanding-active-directory-site-topology]]
- [[ad-ds-creating-a-site-design]]
- [[ad-ds-creating-a-site-link-design]]
- [[ad-ds-finding-additional-resources-for-windows-server-2008-active-directory-site-topology-design]]

## See also
- [[ad-logical-structure-design]]
- [[ad-replication]]
- [[knowledge-consistency-checker]]
- [[site-links-and-replication-schedule]]
- [[capacity-and-placement-planning]]
- [[universal-group-membership-caching]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-designing-the-site-topology|Designing the Site Topology]]
- [[ad-ds-understanding-active-directory-site-topology|Understanding Active Directory Site Topology]]
- [[ad-ds-creating-a-site-design|Creating a Site Design]]
- [[ad-ds-creating-a-site-link-design|Creating a Site Link Design]]
- [[ad-ds-finding-additional-resources-for-windows-server-2008-active-directory-site-topology-design|Finding Additional Resources for Windows Server 2008 Active Directory Site Topology Design]]
<!-- crosslink:end -->
