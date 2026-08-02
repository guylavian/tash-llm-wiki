---
title: Security Groups
type: entity
domain: active-directory
slug: security-groups
summary: Active Directory security groups collect accounts into manageable units for assigning permissions and user rights; three scopes (Domain Local, Global, Universal) plus the AGDLP nesting pattern govern where permissions can be granted and what can be a member.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups (Microsoft Learn — Active Directory Security Groups, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-principals (Microsoft Learn — Security Principals, fetched 2026-06-18)
  - kb:ad-ds-understand-security-groups
  - kb:ad-ds-understand-security-principals
provenance_extracted: 20
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, security, concept]
status: draft
updated: 2026-07-02
graph_community: "Security Principals"
---

# Security Groups

**An Active Directory security group is a collection of user accounts, computer accounts, and other groups that can be managed as a single unit for assigning permissions and user rights.**

## Group Types

AD has two group types:
- **Security groups** — security-enabled; listed in DACLs; can receive permissions and user rights. Also usable as email distribution lists.
- **Distribution groups** — not security-enabled; cannot be added to DACLs; used solely for email.

## Group Scope

Scope controls where a group's permissions can be granted and which principals may be members.

| Scope | Members accepted | Permissions grantable | Can be a member of |
|---|---|---|---|
| **Universal** | Accounts, Global groups, or Universal groups from any domain in the forest | Any domain in same forest, or trusting forests | Domain Local groups in the forest or trusting forests; other Universal groups |
| **Global** | Accounts and Global groups from the **same domain** only | Any domain in the same forest or trusting domains/forests | Universal groups; Domain Local groups anywhere in forest |
| **Domain Local** | Accounts, Global groups, Universal groups from any domain or trusted domain; other Domain Local groups from the **same domain** | Within the **same domain** only | Other Domain Local groups in same domain; local groups on computers in same domain |

There is also **Builtin Local** scope, used by default groups in the Builtin container; that scope and type cannot be changed.

## AGDLP Nesting Pattern

The recommended design pattern is **A**ccounts → **G**lobal groups → **D**omain **L**ocal groups → **P**ermissions:

1. Place user and computer accounts into **Global** groups that represent roles (e.g., "Finance Users").
2. Nest Global groups (potentially from multiple domains) into **Domain Local** groups that represent resource access (e.g., "Finance Share Read").
3. Assign **permissions** on the resource to the Domain Local group.

This pattern centralises role definition in Global groups and resource access in Domain Local groups, making cross-domain permission grants manageable. (inferred — AGDLP is implied by the scope rules; the source describes scope mechanics but does not use the acronym explicitly.)

In forests with multiple domains, **Universal** groups may sit between Global and Domain Local to bridge the domain boundary. The extended pattern is AGUDLP. (inferred — extension of AGDLP to multi-domain forests based on Universal group membership rules.)

## AdminSDHolder Protection

High-privilege groups (Domain Admins, Enterprise Admins, Schema Admins, Administrators, Backup Operators, Account Operators, Print Operators, Server Operators, and others) are protected by a background process that periodically applies the security descriptor from the **AdminSDHolder** object in `CN=System`. To change permissions on these groups or their members you must modify the AdminSDHolder descriptor — changes made directly to the group objects will be overwritten.

## Key Default Groups

| Group | SID | Scope | Notable |
|---|---|---|---|
| Domain Admins | S-1-5-domain-512 | Global | Default member of Administrators on all domain-joined machines |
| Enterprise Admins | S-1-5-root-519 | Universal (native mode) / Global (mixed) | Forest-wide changes; exists only in forest root domain |
| Schema Admins | S-1-5-root-518 | Universal / Global | Schema modification rights |
| Domain Users | S-1-5-domain-513 | Global | Default group for every user account created |
| Protected Users | S-1-5-domain-525 | Global | Introduced Windows Server 2012 R2; blocks NTLM, DES, RC4, CredSSP; TGT lifetime 4 h |
| Cloneable Domain Controllers | S-1-5-domain-522 | Global | Members (DCs) may be cloned — Windows Server 2012+ |

See [[default-user-accounts]] for Administrator, Guest, and KRBTGT which have their own well-known RIDs.

## Why Groups over Individual ACEs

Using group SIDs in ACLs instead of individual user SIDs keeps ACLs small and speeds security checks. In domains with thousands of users, per-user ACEs become unmanageable and slow. (inferred — the source states this as a design rationale for groups but does not quantify "slow".)

## Contradictions / caveats
- Enterprise Admins is Universal in native mode domains but Global in mixed mode — behaviour depends on domain functional level.
- Universal group membership changes cause full universal group membership replication in Windows 2000 forests; Windows Server 2003+ forests cache universal group membership at the GC (see [[universal-group-membership-caching]]).
- Protected Users group protection requires a Windows Server 2012 R2+ PDC emulator in the account domain; member workstations/servers must be at least Windows 8.1 / Windows Server 2012 R2 to enforce all protections.

## Reference notes
- [[ad-ds-understand-security-groups]]
- [[ad-ds-understand-security-principals]]

## See also
- [[security-principals]]
- [[security-identifiers-sid]]
- [[special-identity-groups]]
- [[fsmo-roles]]
- [[securing-active-directory]]
- [[universal-group-membership-caching]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-understand-security-groups|Active Directory Security Groups]]
- [[ad-ds-understand-security-principals|Security Principals]]
<!-- crosslink:end -->
