---
origin: eval-cohort
title: Default built-in user accounts when provisioning an AD domain
type: question
domain: active-directory
slug: default-built-in-user-accounts-ad-domain
summary: Active Directory creates three built-in user accounts automatically — Administrator (RID 500), Guest (RID 501), and KRBTGT (RID 502).
sources: "kb:ad-ds-understand-default-user-accounts"
provenance_extracted: 16
provenance_inferred: 0
provenance_ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-12
graph_community: "Security Principals"
---

# What are the default built-in user accounts created when provisioning an AD domain?

When a Windows Server domain is provisioned, AD DS automatically creates three built-in user accounts — all stored in `CN=Users` (`ad-ds-understand-default-user-accounts.md:27-28`):

| Account | RID | Key properties |
|---|---|---|
| **Administrator** | 500 | Full control over all domain resources; cannot be deleted or locked out; protected by AdminSDHolder; default member of Administrators, Domain Admins, Enterprise Admins (`ad-ds-understand-default-user-accounts.md:51,78-83`) *(extracted)* |
| **Guest** | 501 | Limited passwordless access; **disabled by default**; runs a temporary profile (deleted on sign-out); not protected by AdminSDHolder (`ad-ds-understand-default-user-accounts.md:89,121,126`) *(extracted)* |
| **KRBTGT** | 502 | Service account for the KDC on every DC; password is the master key for all Kerberos TGTs in the domain; cannot be enabled, deleted, or renamed; protected by AdminSDHolder (`ad-ds-understand-default-user-accounts.md:163-164,210,215`) *(extracted)* |

## Operational notes

- **Administrator**: best practice is to rename and disable it, using named admin accounts instead. Even disabled, it can still sign in to a DC in safe mode (`ad-ds-understand-default-user-accounts.md:51,65`) *(extracted)*
- **Guest**: keep disabled. If enabled (not recommended), assign a strong password and restricted rights (`ad-ds-understand-default-user-accounts.md:101-103`) *(extracted)*
- **KRBTGT**: reset (twice, with a replication interval between) after suspected compromise, forest recovery, or as periodic hygiene (`ad-ds-understand-default-user-accounts.md:179-183`). Each RODC maintains its own separate KRBTGT account (`ad-ds-understand-default-user-accounts.md:200-202`). *(extracted)*

## References

### RH ground-truth (`kb:`)
- `kb:ad-ds-understand-default-user-accounts` — Active Directory Accounts

### Wiki
- [[default-user-accounts]]
- [[security-principals]]
- [[security-identifiers-sid]]
- [[krbtgt-reset]]
- [[read-only-domain-controller]]
