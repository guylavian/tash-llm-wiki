---
title: Organizational Unit Design
type: entity
domain: active-directory
slug: organizational-unit-design
summary: Design principles for OU hierarchies in AD DS — when to use OUs for delegation vs. GPO vs. visibility scoping, and the account/resource OU split.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-an-Organizational-Unit-Design (Microsoft Learn — Creating an Organizational Unit Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Reviewing-OU-Design-Concepts (Microsoft Learn — Reviewing OU Design Concepts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Delegating-Administration-by-Using-OU-Objects (Microsoft Learn — Delegating Administration by Using OU Objects, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, logical-design, concept]
status: draft
updated: 2026-06-18
---

# Organizational Unit Design

**OUs are the primary tool for scoping administrative delegation and GPO application within a domain — they provide data autonomy but never isolate from service administrators.**

## Three purposes of OUs

1. **Delegation of administration** — assign granular rights (create/delete users, reset passwords) to data administrators over a subtree without granting domain-wide privileges
2. **GPO application scope** — apply Group Policy to a specific set of users or computers by placing them in an OU and linking a GPO
3. **Object visibility control** — limit which users can see specific objects (e.g., sensitive computer accounts) via ACLs on the OU

OU structure does not need to mirror the org chart. Design it around administrative and policy requirements, not business units (inferred: org charts change frequently; OU hierarchies that mirror them require constant restructuring).

## Account OUs and resource OUs

**Account OUs** contain user, group, and computer objects. Create one per domain as a delegation root, then subdivide by administrative boundary.

**Resource OUs** contain resource objects (e.g., server computer accounts, printer accounts) and the accounts responsible for managing them. Separate from account OUs so that resource administrators have scoped rights without touching user/group accounts.

Default containers (`CN=Users`, `CN=Computers`) are controlled by service administrators. Delegate to data administrators only by creating new OUs — do not delegate over default containers, which preserves clean SA control boundaries.

## OU owner role

The forest owner assigns each OU an OU owner — a data manager who controls the subtree. OU owners can:
- Control how administration is delegated within their subtree
- Create sub-OUs and delegate further
- Control GPO linkage within their OU

The forest owner retains full override authority over all OU subtrees (e.g., to correct ACL errors or reclaim access when an OU owner is terminated). OU ownership provides **data autonomy**, not data isolation.

## Depth and complexity guidelines

- No technical limit on OU depth, but keep depth to **10 levels or fewer** for manageability
- Deep nesting increases LDAP distinguished-name length, which some AD-enabled applications cap
- Avoid GPO inheritance complexity — flatter structures with explicit GPO links are easier to audit

## Delegation mechanics

Assign granular rights via ACL on the OU. Rights can be:
- Full control over all objects in the OU
- Rights to create/delete specific object types (e.g., user accounts only)
- Rights to modify specific attributes (e.g., password reset only)

Rights are inheritable to all sub-OUs by default. Granting "create object" in an OU implicitly grants control over all attributes of the created object, and if the object is a container, over its children.

## OU boundaries vs. domain/forest boundaries

| Need | Boundary |
|---|---|
| Data autonomy (control own data, SAs can still access) | OU |
| Service autonomy (control own DCs) | Domain |
| Service or data isolation (SAs cannot access) | Forest |

OUs are **not** a security isolation boundary. Service administrators can override OU ACLs by modifying DC system software. (inferred: this is the most common design misconception — OUs feel like security boundaries because ACLs are visible, but SA override capability is invisible)

## Contradictions / caveats

- End users should not be aware of the OU structure; it is purely an administrative tool.
- OUs are easy to restructure after deployment (unlike domains or forests), so the OU design can evolve as administrative needs change — but GPO links and delegations must be re-applied after moves.
- Some legacy AD-enabled applications parse the distinguished name to determine OU membership; very deep or renamed OUs can break such applications.

## Reference notes
- [[ad-ds-creating-an-organizational-unit-design]]
- [[ad-ds-reviewing-ou-design-concepts]]
- [[ad-ds-delegating-administration-by-using-ou-objects]]

## See also
- [[ad-logical-structure-design]]
- [[group-policy]]
- [[domain-design]]
- [[tiered-administration-model]]
