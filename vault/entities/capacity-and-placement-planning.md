---
title: Capacity and Placement Planning
type: entity
domain: active-directory
slug: capacity-and-placement-planning
summary: How to size and place domain controllers, global catalog servers, and FSMO role holders across sites to meet authentication, replication, and availability requirements.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Determining-the-Number-of-Domains-Required (Microsoft Learn — Determining the Number of Domains Required, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Planning-Forest-Root-Domain-Controller-Placement (Microsoft Learn — Planning Forest Root Domain Controller Placement, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Planning-Global-Catalog-Server-Placement (Microsoft Learn — Planning Global Catalog Server Placement, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Planning-Operations-Master-Role-Placement (Microsoft Learn — Planning Operations Master Role Placement, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Planning-Domain-Controller-Placement (Microsoft Learn — Planning Domain Controller Placement, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Finding-Additional-Resources-for-Windows-Server-2008-Active-Directory-Site-Topology-Design (Microsoft Learn — Finding Additional Resources for Windows Server 2008 Active Directory Site Topology Design, fetched 2026-06-18)
  - kb:ad-ds-determining-the-number-of-domains-required
  - kb:ad-ds-planning-forest-root-domain-controller-placement
  - kb:ad-ds-planning-global-catalog-server-placement
  - kb:ad-ds-planning-operations-master-role-placement
  - kb:ad-ds-planning-domain-controller-placement
  - kb:ad-ds-finding-additional-resources-for-windows-server-2008-active-directory-site-topology-design
provenance_extracted: 18
provenance_inferred: 8
provenance_ambiguous: 0
tags: [directory-services, sites-topology, fsmo, logical-design, concept]
status: draft
updated: 2026-07-02
graph_community: "Active Directory Replication & Site Topology"
---

# Capacity and Placement Planning

**Decisions on how many DCs to deploy, where to place them (per site), which DCs host global catalog, and how to distribute FSMO roles to meet latency, availability, and replication capacity targets.**

## DC count per site

Every site that requires local authentication must host at least one DC for each domain whose users are in that site. General sizing principles (inferred):
- **Minimum 2 DCs per domain per site** for redundancy — single-DC sites create a single point of failure for authentication
- Scale by user count and logon load — Microsoft's reference figures assume ~1,000 concurrent authentications per DC for standard hardware; validate in a lab for high-density scenarios
- Branch offices with poor physical security should use RODCs rather than writable DCs — see [[read-only-domain-controller]]

## Domain sizing and WAN bandwidth

DC placement decisions feed back into domain design. Replication-bandwidth sizing determines whether a single domain can cover all locations or requires regional domain splits. Key table (single domain, all GCs, AD-integrated DNS):

| Slowest DC link (Kbps) | Max users @ 1% BW | Max users @ 5% BW | Max users @ 10% BW |
|---|---|---|---|
| 28.8 | 10,000 | 25,000 | 40,000 |
| 56 | 10,000 | 50,000 | 100,000 |
| 128 | 25,000 | 100,000 | 100,000 |
| 512 | 80,000 | 100,000 | 100,000 |
| 1,500 | 100,000 | 100,000 | 100,000 |

Assumptions: 20% annual new user rate, 15% departure rate, 5 global + 5 universal group memberships per user, 1:1 user-to-computer ratio. Verify assumptions for your environment.

## Global catalog placement

In a single-domain forest, every DC can and should be a GC (no additional replication cost). In a multi-domain forest:

- Every site that contains users should have a local GC — logon for universal group membership expansion requires GC contact
- If a GC is unavailable and the DC is running Windows Server 2003+, **universal group membership caching** (UGMC) can substitute — the DC caches UGM locally after first contact with a GC; subsequent logons work without live GC access — see [[universal-group-membership-caching]]
- GC servers carry additional replication load (partial attribute set for all domain partitions); place GCs on DCs with sufficient CPU, RAM, and bandwidth

## Forest root DC placement

Forest root DCs must be accessible to create authentication trust paths for cross-domain resource access. Place forest root DCs:
- In hub locations and datacenters with reliable connectivity
- At least one per datacenter (for resilience)
- In remote sites only when WAN reliability is insufficient and the cost of a shortcut trust between the domains is higher than operating an additional DC

Shortcut trusts between regional domains can substitute for a remote forest root DC — they optimize the trust path without requiring additional DCs at that location.

## FSMO role holder placement

AD DS has five FSMO roles: Schema Master, Domain Naming Master (forest-wide) and RID Master, PDC Emulator, Infrastructure Master (per domain). Placement guidelines (inferred):

| Role | Placement recommendation |
|---|---|
| PDC Emulator | Best-connected DC in each domain; high availability critical (password changes, time sync, Group Policy) |
| RID Master | Co-locate with PDC Emulator (same domain) |
| Infrastructure Master | Do **not** place on a GC server in multi-domain forests (unless all DCs are GCs) |
| Schema Master | Any DC; rarely used; restrict access tightly |
| Domain Naming Master | Co-locate with Schema Master; restrict access |

See [[fsmo-roles]] for full operational detail and seizure procedures.

## Virtualization considerations

Virtualized DCs introduce additional placement constraints — see [[virtualized-domain-controllers]]:
- Do not run all DCs for a domain as VMs on a single physical host
- VM-generation ID safe-restore prevents USN rollback on snapshot restore
- FSMO roles on VMs are at risk if the hypervisor host fails — plan for spread across hosts/clusters

## Contradictions / caveats

- Microsoft's bandwidth sizing tables apply only to forests with up to 100,000 users and links of at least 28.8 Kbps. Larger or slower environments require custom modeling.
- The Infrastructure Master guidance (not on a GC) applies only in multi-domain forests where not all DCs are GCs. In a single-domain forest or where all DCs are GCs, the Infrastructure Master can reside on any DC.
- Time synchronization (W32tm) depends on the PDC Emulator hierarchy — placement of PDC Emulators has a cascading effect on time accuracy across the forest. See [[windows-time-service]].

## Reference notes
- [[ad-ds-determining-the-number-of-domains-required]]
- [[ad-ds-planning-forest-root-domain-controller-placement]]
- [[ad-ds-planning-global-catalog-server-placement]]
- [[ad-ds-planning-operations-master-role-placement]]
- [[ad-ds-planning-domain-controller-placement]]
- [[ad-ds-finding-additional-resources-for-windows-server-2008-active-directory-site-topology-design]]

## See also
- [[ad-logical-structure-design]]
- [[site-topology-design]]
- [[fsmo-roles]]
- [[global-catalog]]
- [[universal-group-membership-caching]]
- [[read-only-domain-controller]]
- [[virtualized-domain-controllers]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-determining-the-number-of-domains-required|Determining the Number of Domains Required]]
- [[ad-ds-planning-forest-root-domain-controller-placement|Planning Forest Root Domain Controller Placement]]
- [[ad-ds-planning-global-catalog-server-placement|Planning Global Catalog Server Placement]]
- [[ad-ds-planning-operations-master-role-placement|Planning Operations Master Role Placement]]
- [[ad-ds-planning-domain-controller-placement|Planning Domain Controller Placement]]
- [[ad-ds-finding-additional-resources-for-windows-server-2008-active-directory-site-topology-design|Finding Additional Resources for Windows Server 2008 Active Directory Site Topology Design]]
<!-- crosslink:end -->
