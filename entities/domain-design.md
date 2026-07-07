---
title: Domain Design
type: entity
domain: active-directory
slug: domain-design
summary: How to choose between single-domain and regional-domain forest models, size domains against WAN bandwidth, and select a forest root domain.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-a-Domain-Design (Microsoft Learn — Creating a Domain Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Reviewing-the-Domain-Models (Microsoft Learn — Reviewing the Domain Models, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Determining-the-Number-of-Domains-Required (Microsoft Learn — Determining the Number of Domains Required, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Selecting-the-Forest-Root-Domain (Microsoft Learn — Selecting the Forest Root Domain, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Using-the-Organizational-Domain-Forest-Model (Microsoft Learn — Using the Organizational Domain Forest Model, fetched 2026-06-18)
  - kb:ad-ds-creating-a-domain-design
  - kb:ad-ds-reviewing-the-domain-models
  - kb:ad-ds-determining-the-number-of-domains-required
  - kb:ad-ds-selecting-the-forest-root-domain
  - kb:ad-ds-using-the-organizational-domain-forest-model
provenance_extracted: 24
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, logical-design, concept]
status: draft
updated: 2026-07-02
---

# Domain Design

**The decision process for determining domain count, domain model (single vs. regional), and forest root domain selection — optimizing replication efficiency while minimizing administrative overhead.**

## Domain purpose

A domain is a replication partition within a forest. All domain object data replicates to every DC in that domain. Adding domains reduces WAN replication pressure but increases administrative overhead (separate service administrator groups, separate Group Policy application, higher probability of object moves between domains).

The goal is to minimize domain count: Microsoft recommends no more than 10 domains in a forest for manageability.

## Single-domain model

The simplest and least expensive model. One forest = one domain = the forest root domain. All DCs can be global catalog servers, eliminating GC placement planning. Suitable when the slowest DC link speed and available bandwidth can accommodate all users per the capacity tables. (inferred: this model collapses domain design and GC placement into a single trivial decision)

## Regional domain model

Used when the slowest WAN link between DC locations cannot carry all replication traffic for a single domain. Additional regional domains are created along stable geographic boundaries (e.g., continental boundaries) rather than organizational boundaries — organizational structures change, geography is stable.

### Sizing a domain

Use the slowest DC-connecting link and the bandwidth percentage allocated to AD DS to find the per-domain user limit:

| Slowest link (Kbps) | Max users @ 1% BW | Max users @ 5% BW | Max users @ 10% BW |
|---|---|---|---|
| 28.8 | 10,000 | 25,000 | 40,000 |
| 56 | 10,000 | 50,000 | 100,000 |
| 128 | 25,000 | 100,000 | 100,000 |
| 512 | 80,000 | 100,000 | 100,000 |
| 1,500 | 100,000 | 100,000 | 100,000 |

For forests exceeding 100,000 users or links below 28.8 Kbps, consult an experienced AD designer. Lab-validate estimates before production deployment.

### Costs of adding regional domains

Each additional domain requires:
- A separate set of service administrator groups managed independently
- Separate Group Policy consistency enforcement across domains
- Separate access-control and auditing consistency enforcement
- Increased likelihood users will need to move between domains (disruptive)

## Forest root domain

The first domain deployed in a forest becomes the forest root and holds the Enterprise Admins and Schema Admins groups permanently.

### Dedicated forest root
A domain created solely for forest-level administration, holding no user accounts except SA accounts. Advantages:
- Separates forest SAs from domain SAs — regional domain admins cannot elevate to Enterprise Admins through standard tools
- Is not affected by regional reorganizations or renaming
- Presents no country/region as superior in the namespace

Disadvantage: additional management overhead for an otherwise empty domain.

### Regional domain as forest root
Select the regional domain with headquarters or the fastest network connections. Simpler than maintaining a dedicated root, but the forest root name is bound to a specific region's namespace. (inferred: this choice is a long-term commitment — forest root renaming is disruptive and rarely done)

### Naming the forest root
- Use a registered DNS suffix (e.g., `corp.contoso.com`) — registered names are globally unique and avoid conflicts during mergers or acquisitions
- Avoid single-label DNS names (e.g., `corp`) and unregistered suffixes (e.g., `.local`)
- Keep the prefix to ≤15 characters so the NetBIOS name equals the prefix

## Organizational domain model

For domain-level service autonomy without full forest isolation, place a group into a separate domain within the organizational forest. This grants the group control over DC operations, domain-wide Group Policy, and external trust management — but the forest owner (Enterprise Admins) retains override authority and schema/replication topology control. Windows Server 2008 introduced RODC support for delegating local DC maintenance without granting domain admin rights.

## Contradictions / caveats

- Before Windows Server 2008, fine-grained password policies did not exist; multiple domains were sometimes the only way to apply different password policies to different user sets. This driver largely disappears on 2008+ forests — see [[fine-grained-password-policies]].
- A domain is **not** a security isolation boundary. Groups requiring isolation from service administrators must use a separate forest.

## Reference notes
- [[ad-ds-creating-a-domain-design]]
- [[ad-ds-reviewing-the-domain-models]]
- [[ad-ds-determining-the-number-of-domains-required]]
- [[ad-ds-selecting-the-forest-root-domain]]
- [[ad-ds-using-the-organizational-domain-forest-model]]

## See also
- [[ad-logical-structure-design]]
- [[forest-design-models]]
- [[capacity-and-placement-planning]]
- [[ad-replication]]
- [[fsmo-roles]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-creating-a-domain-design|Creating a Domain Design]]
- [[ad-ds-reviewing-the-domain-models|Reviewing the Domain Models]]
- [[ad-ds-determining-the-number-of-domains-required|Determining the Number of Domains Required]]
- [[ad-ds-selecting-the-forest-root-domain|Selecting the Forest Root Domain]]
- [[ad-ds-using-the-organizational-domain-forest-model|Using the Organizational Domain Forest Model]]
<!-- crosslink:end -->
