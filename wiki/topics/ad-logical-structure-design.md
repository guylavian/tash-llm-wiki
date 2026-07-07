---
title: AD Logical Structure Design
type: topic
domain: active-directory
slug: ad-logical-structure-design
summary: Spine topic covering the four-layer logical design sequence for AD DS — forest, domain, DNS, and OU — from requirements gathering through capacity planning.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Designing-the-Logical-Structure (Microsoft Learn — Designing the Logical Structure, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Understanding-the-Active-Directory-Logical-Model (Microsoft Learn — Understanding the Active Directory Logical Model, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Identifying-Forest-Design-Requirements (Microsoft Learn — Identifying Forest Design Requirements, fetched 2026-06-18)
  - kb:ad-ds-designing-the-logical-structure
  - kb:ad-ds-understanding-the-active-directory-logical-model
  - kb:ad-ds-identifying-forest-design-requirements
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, logical-design, concept]
status: draft
updated: 2026-07-02
---

# AD Logical Structure Design

**The process of defining forest, domain, DNS, and OU boundaries before deploying AD DS to achieve scalable, secure, and delegatable directory infrastructure.**

## Overview

AD DS stores and manages network resources in a hierarchical containment structure: forest → domain → organizational unit (OU). This logical model is independent of physical topology (number of DCs, network links) and must be designed before deployment to minimize costly restructuring later.

A well-designed logical structure yields:
- Simplified management of large object sets
- Consolidated domain structure with lower TCO
- Delegated administrative control at the right granularity
- Controlled replication bandwidth consumption

## The design sequence

The design team works through four layers in order:

1. **Forest design** — identify autonomy vs. isolation requirements for each group; select a forest model; determine number of forests. See [[forest-design-models]].
2. **Domain design** — choose single-domain or regional model based on WAN bandwidth and user count; select or create a dedicated forest root domain. See [[domain-design]].
3. **DNS infrastructure design** — decide AD-integrated zones, delegation, and namespace for the forest root. See [[dns-infrastructure-design]].
4. **OU design** — design delegation and GPO-application structures within each domain. See [[organizational-unit-design]].

Site topology is a physical planning step that feeds into DC/GC/FSMO placement and must be done in parallel with the logical design. See [[site-topology-design]] and [[capacity-and-placement-planning]].

## Key inputs to gather before design

- Autonomy and isolation requirements per organizational group (service isolation, data isolation, service autonomy, data autonomy) — these drive forest count (inferred)
- Network WAN topology and slowest-link bandwidth — drives domain count and site topology
- Legal and regulatory constraints — may mandate separate forests for classified data
- Existing DNS namespace and registered domain names

## Forest as the trust and security boundary

The forest is the outermost security boundary in AD DS. All domains in a forest share a schema, configuration partition, and global catalog. Domains within a forest are automatically linked by two-way transitive Kerberos trust. Service administrators in any domain can, by modifying DC system software, gain access to data in all other domains in the forest — isolation from service administrators therefore requires a separate forest, not just a separate domain or OU (inferred).

## OU vs. domain vs. forest for delegation

| Need | Use |
|------|-----|
| Data autonomy (control own data, trust forest SAs) | OU with delegated permissions |
| Service autonomy (control own DCs) | Separate domain or forest |
| Service isolation (no external SA interference) | Separate forest |
| Data isolation (legal/classified) | Separate forest (possibly air-gapped) |

## Related entities and clusters

- [[forest-design-models]] — organizational, resource, restricted-access forest types
- [[domain-design]] — single vs. regional domain, forest root selection
- [[organizational-unit-design]] — OU hierarchy, delegation, GPO scope
- [[dns-infrastructure-design]] — AD-integrated zones, namespace planning
- [[site-topology-design]] — sites, site links, DC placement inputs
- [[capacity-and-placement-planning]] — DC/GC/FSMO sizing

## Contradictions / caveats

- Domains do **not** provide data isolation or service isolation — a common operational misconception. Only a separate forest achieves true isolation from service administrators.
- Fine-grained password policies (introduced in Windows Server 2008) reduce the need to create multiple domains purely for different password requirements, which was a common driver for extra domains in pre-2008 designs.

## Reference notes
- [[ad-ds-designing-the-logical-structure]]
- [[ad-ds-understanding-the-active-directory-logical-model]]
- [[ad-ds-identifying-forest-design-requirements]]

## See also
- [[active-directory-overview]]
- [[ad-replication]]
- [[fsmo-roles]]
- [[group-policy]]
- [[dns-for-ad-ds]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-designing-the-logical-structure|Designing the Logical Structure]]
- [[ad-ds-understanding-the-active-directory-logical-model|Understanding the Active Directory Logical Model]]
- [[ad-ds-identifying-forest-design-requirements|Identifying Forest Design Requirements]]
<!-- crosslink:end -->
