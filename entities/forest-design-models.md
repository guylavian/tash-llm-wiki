---
title: Forest Design Models
type: entity
domain: active-directory
slug: forest-design-models
summary: The three AD DS forest models — organizational, resource, and restricted-access — and how to map autonomy/isolation requirements to the right model.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Forest-Design-Models (Microsoft Learn — Forest Design Models, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Mapping-Design-Requirements-to-Forest-Design-Models (Microsoft Learn — Mapping Design Requirements to Forest Design Models, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Autonomy-vs.-Isolation (Microsoft Learn — Autonomy vs. Isolation, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Determining-the-Number-of-Forests-Required (Microsoft Learn — Determining the Number of Forests Required, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Service-Administrator-Scope-of-Authority (Microsoft Learn — Service Administrator Scope of Authority, fetched 2026-06-18)
  - kb:ad-ds-forest-design-models
  - kb:ad-ds-mapping-design-requirements-to-forest-design-models
  - kb:ad-ds-autonomy-vs-isolation
  - kb:ad-ds-determining-the-number-of-forests-required
  - kb:ad-ds-service-administrator-scope-of-authority
provenance_extracted: 22
provenance_inferred: 5
provenance_ambiguous: 0
tags: [directory-services, logical-design, concept]
status: draft
updated: 2026-07-02
graph_community: "Active Directory — Implementation Review (Evaluation-Lens MOC)"
---

# Forest Design Models

**The three canonical patterns for how Active Directory forests are structured — organizational, resource, and restricted-access — each delivering a different combination of autonomy and isolation.**

## Autonomy vs. isolation

Before selecting a forest model, each group's requirements must be classified:

| Requirement | Definition | AD boundary needed |
|---|---|---|
| **Data autonomy** | Group manages its own data; other SAs can still access it | OU in shared forest |
| **Service autonomy** | Group controls its own DCs and directory configuration | Separate domain or forest |
| **Service isolation** | No external SA can interfere with the directory service | Separate forest |
| **Data isolation** | No external SA can access the data (legal/classified) | Separate forest (possibly air-gapped) |

Service administrators (members of Domain Admins, Enterprise Admins, Schema Admins) have full control over all data and services in the forest — they can modify DC system software, reset any password, or alter any ACL. Data isolation is therefore impossible within a shared forest.

## The three models

### Organizational forest model
User accounts and resources coexist in one forest, managed by one IT group. Every AD design requires at least one organizational forest. This model supports:
- **Service autonomy** — by creating a separate domain within the organizational forest (domain-level service autonomy only, not full isolation)
- **Data autonomy** — by delegating OUs to group data administrators

Forest trusts allow users in one organizational forest to access resources in another.

### Resource forest model
A dedicated forest holds only service accounts and resources; user accounts remain in an organizational forest. Used when service isolation is required for a critical system (e.g., manufacturing floor control). Alternate accounts in the resource forest provide fallback access if the org forest becomes unavailable. Forest trusts link the two. (inferred: the resource forest pattern directly addresses service isolation without requiring users to have accounts in the isolated environment)

### Restricted access forest model
A separate forest (and usually a separate physical network) holds classified user accounts and data. No trusts are created with other forests. Users who need access must have two workstations — one in the restricted forest, one in the org forest. This is the only model that satisfies regulatory data isolation requirements (e.g., classified government projects, financial jurisdiction constraints).

## Mapping requirements to scenarios

| Need | Scenario | Solution |
|---|---|---|
| Data autonomy only | Join existing forest | Delegate OUs |
| Service autonomy | Separate domain in org forest, or new org forest | Organizational domain/forest |
| Service isolation | New resource forest with forest trust | Resource forest |
| Data isolation | New restricted forest, no trusts | Restricted access forest |
| Limited connectivity + service autonomy | Separate org forest behind firewall | Organizational forest |

## Single-forest preference

A single forest is the least expensive configuration: all objects are in the global catalog (no cross-forest sync), and duplicate infrastructure is not required. Microsoft recommends against co-ownership of a single forest by two autonomous IT organizations and against outsourcing service administration to more than one external partner (both create governance risks). (inferred)

## Contradictions / caveats

- Domains do **not** provide data isolation or service isolation — this is a critical distinction. Only a separate forest isolates from service administrators.
- In restricted access forest scenarios, encryption alone is not sufficient to meet data isolation requirements because service administrators can bypass ACLs at the OS level.
- Cloning or copying domain controllers to create a "second instance" of a domain is unsupported and invalidates both forests' security identity.

## Reference notes
- [[ad-ds-forest-design-models]]
- [[ad-ds-mapping-design-requirements-to-forest-design-models]]
- [[ad-ds-autonomy-vs-isolation]]
- [[ad-ds-determining-the-number-of-forests-required]]
- [[ad-ds-service-administrator-scope-of-authority]]

## See also
- [[ad-logical-structure-design]]
- [[domain-design]]
- [[tiered-administration-model]]
- [[securing-active-directory]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-forest-design-models|Forest Design Models]]
- [[ad-ds-mapping-design-requirements-to-forest-design-models|Mapping Design Requirements to Forest Design Models]]
- [[ad-ds-autonomy-vs-isolation|Autonomy vs. Isolation]]
- [[ad-ds-determining-the-number-of-forests-required|Determining the Number of Forests Required]]
- [[ad-ds-service-administrator-scope-of-authority|Service Administrator Scope of Authority]]
<!-- crosslink:end -->
