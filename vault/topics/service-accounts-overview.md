---
title: Service Accounts in Active Directory
type: topic
domain: active-directory
slug: service-accounts-overview
summary: The four AD service-account types — standalone MSA, group MSA, delegated MSA, and virtual accounts — how each manages passwords and SPNs, and how to choose between them by deployment topology and security need.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-service-accounts (Microsoft Learn — Service Accounts in Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview (Microsoft Learn — Group Managed Service Accounts overview, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts (Microsoft Learn — Manage Group Managed Service Accounts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/how-to-configure-spn (Microsoft Learn — How to configure SPN for Windows Server, fetched 2026-06-18)
  - kb:ad-ds-understand-service-accounts
  - kb:ad-ds-group-managed-service-accounts-overview
  - kb:ad-ds-manage-group-managed-service-accounts
  - kb:ad-ds-how-to-configure-spn
provenance_extracted: 9
provenance_inferred: 3
provenance_ambiguous: 0
tags: [users, security, directory-services, concept]
status: draft
updated: 2026-07-02
graph_community: "Group Managed Service Accounts (gMSA)"
---

# Service Accounts in Active Directory

**A service account is a security context a Windows service runs under; AD offers four kinds that trade off how widely the identity can be shared against how much of the password and SPN management Windows performs for you.**

## Body

A service account determines a service's ability to reach local and network resources. AD DS provides four account types, spanning a spectrum from least to most automated/secure.

- **Standalone Managed Service Account (sMSA)** — a managed *domain* account (introduced with Windows Server 2008 R2 / Windows 7) with automatic password rotation, simplified **SPN** management, and delegable administration. Scoped to a **single** domain-joined computer; it can't be shared across servers or used in failover clusters.
- **[[group-managed-service-accounts]] (gMSA)** — extends the sMSA across **multiple servers**, so every instance of a load-balanced or farmed service authenticates as the **same principal**. The DC computes the password from the [[kds-root-key]]; member hosts retrieve it over LDAP. This is the only type that works behind a load balancer or across a farm.
- **[[delegated-managed-service-accounts]] (dMSA)** — Windows Server 2025. A machine account with fully randomized, machine-bound keys that supersedes a traditional service account; authentication is bound to the **device identity**, which defeats credential-harvesting / Kerberoasting. Single-server, high-security scenarios.
- **Virtual accounts** — managed *local* accounts (`NT SERVICE\<name>`) that need no password management and reach the network as the computer account (`<domain>\<computer>$`). Single server, no domain identity of their own.

Password management is the dividing line (inferred): a plain user/computer account used as a service principal has **no** single-point password management, so admins must rotate keys in AD and redistribute them to every instance — exactly the toil sMSA/gMSA/dMSA remove.

**SPN management.** All managed types simplify SPN handling. SPNs (`servicePrincipalName`, format *serviceclass/host:port/servicename*) are what a Kerberos client uses to locate and mutually authenticate a service; they're normally set automatically on domain join or service install, and edited with `setspn` only when a host is renamed or a service needs a nonstandard SPN. Note that [[spn-and-upn-uniqueness]] is enforced — a duplicate SPN breaks Kerberos for the affected services (inferred).

### Choosing a type
- App on one server, want domain identity → **sMSA**.
- App across multiple servers or behind a load balancer → **gMSA** (the only multi-server option).
- High-security single-server app, want machine-bound credentials and to retire an existing account → **dMSA**.
- Single-server app that only needs local-with-network-as-computer identity → **virtual account**.

## Contradictions / caveats
- gMSA and dMSA both depend on a **[[kds-root-key]]** and **64-bit** PowerShell tooling; gMSA additionally requires domain/forest functional level 2012+.
- **Failover clusters don't support gMSAs directly** — but a clustered Windows service, IIS app pool, or scheduled task that natively supports gMSA/sMSA can use one.
- Always configure **AES** for managed accounts: if the host refuses RC4 and AES isn't set in `msDS-SupportedEncryptionTypes`, Kerberos authentication fails.
- gMSA names must be unique at the **forest** level, not just per domain.
- dMSA is **not** a drop-in for gMSA: you can't migrate an sMSA or gMSA *to* a dMSA, and dMSA is single-server only.

## Reference notes
- [[ad-ds-understand-service-accounts]]
- [[ad-ds-group-managed-service-accounts-overview]]
- [[ad-ds-manage-group-managed-service-accounts]]
- [[ad-ds-how-to-configure-spn]]

## See also
- [[group-managed-service-accounts]]
- [[delegated-managed-service-accounts]]
- [[kds-root-key]]
- [[securing-active-directory]]
- [[spn-and-upn-uniqueness]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-understand-service-accounts|Service Accounts in Windows Server]]
- [[ad-ds-group-managed-service-accounts-overview|Group Managed Service Accounts overview]]
- [[ad-ds-manage-group-managed-service-accounts|Manage Group Managed Service Accounts]]
- [[ad-ds-how-to-configure-spn|How to configure SPN for Windows Server]]
<!-- crosslink:end -->
