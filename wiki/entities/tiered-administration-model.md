---
title: Tiered Administration Model
type: entity
domain: active-directory
slug: tiered-administration-model
summary: A least-privilege framework that separates AD administration into discrete tiers — forest/domain-wide (Tier 0), servers (Tier 1), workstations/users (Tier 2) — so that a credential compromise at one tier cannot be used to escalate to a higher tier.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Implementing-Least-Privilege-Administrative-Models (Microsoft Learn — Implementing Least-Privilege Administrative Models, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Reducing-the-Active-Directory-Attack-Surface (Microsoft Learn — Reducing the Active Directory Attack Surface, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Best-Practices-for-Securing-Active-Directory (Microsoft Learn — Best practices for securing Active Directory, fetched 2026-06-18)
  - kb:ad-ds-implementing-least-privilege-administrative-models
  - kb:ad-ds-reducing-the-active-directory-attack-surface
  - kb:ad-ds-best-practices-for-securing-active-directory
provenance_extracted: 14
provenance_inferred: 5
provenance_ambiguous: 0
symptoms:
  - "pass-the-hash"
  - "lateral movement"
  - "privilege escalation"
tags: [security, directory-services, concept]
status: draft
updated: 2026-07-02
---

# Tiered Administration Model

**A layered privilege architecture where administrative accounts and the hosts they log onto are restricted to a single tier, preventing credential theft at one level from compromising the entire forest.**

## Body

The model enforces a principle: never administer a higher-trust system from a lower-trust host. The three tiers most commonly described are:

- **Tier 0 (Control Plane)** — Domain controllers, the AD DS database, trust infrastructure, and forest-wide configuration. Only Tier 0 admin accounts log onto Tier 0 systems. The highest-privilege built-in groups — Enterprise Admins (EA), Domain Admins (DA), and built-in Administrators (BA) — are Tier 0.
- **Tier 1 (Servers)** — Member servers, applications, and services. Tier 1 admin accounts have no rights on Tier 0 systems.
- **Tier 2 (Workstations/Users)** — End-user devices. Tier 2 admin accounts (help-desk, etc.) have no rights on Tier 0 or Tier 1.

The source material emphasizes that EA, DA, and BA groups should contain **no day-to-day users**. Membership is temporary, audited, and revoked as soon as a task is done. Accounts that are members of any of the three groups can be used to compromise or destroy the AD DS environment. (inferred: the tiered model is the operational implementation of this maxim — the reference describes the principle; the tier naming convention derives from Microsoft's PAW/ESAE documentation.)

### Privilege controls

GPOs enforce deny-logon user rights so that DA accounts cannot interactively sign into workstations or member servers:

- Deny access to this computer from the network
- Deny log on as a batch job
- Deny log on as a service
- Deny log on locally
- Deny log on through Remote Desktop Services

These rights are applied in GPOs linked to workstation/member-server OUs. Jump servers used to reach domain controllers must be in a separate OU that is exempt from the deny-logon GPOs.

### Privileged Identity Management (PIM)

Temporary membership — accounts are placed in privileged groups only when needed and removed after the task — is the recommended pattern. PIM/PAM tooling can automate this with time-bound credential vaults and workflow approval. Unprivileged management accounts (no standing DA rights) are used to populate and depopulate privileged groups, removing the catch-22 of needing a privileged account to manage privilege.

### Role-Based Access Controls (RBAC)

Roles are implemented as AD security groups with delegated rights scoped to the minimum needed. Help-desk roles reset passwords; DNS admins manage DNS zones; neither role inherits forest-wide privilege. Membership in large domain groups nested into local Administrators on member servers is a common misconfiguration that effectively grants broad privilege to hundreds of accounts (inferred from the source's assessment findings).

## Contradictions / caveats

- A member of any of EA, DA, or BA can grant themselves membership in the others — treat them as effectively equivalent for risk purposes.
- Removing EA from Administrators in each domain is an inappropriate modification: EA rights are needed in forest disaster-recovery scenarios.
- DA group is by default a member of the local Administrators group on all domain members — removing this nesting breaks disaster recovery; use deny-logon GPOs instead.
- Schema Admins (SA) should contain members only when schema changes are required and is otherwise empty.
- The `adminCount=1` attribute lingers on accounts after they are removed from protected groups; those objects stop inheriting OU-delegated permissions until the attribute is cleared. See [[protected-accounts-and-groups]].

## Reference notes
- [[ad-ds-implementing-least-privilege-administrative-models]]
- [[ad-ds-reducing-the-active-directory-attack-surface]]
- [[ad-ds-best-practices-for-securing-active-directory]]

## See also
- [[securing-active-directory]]
- [[secure-administrative-hosts]]
- [[protected-accounts-and-groups]]
- [[credential-theft-and-attractive-accounts]]
- [[monitoring-ad-for-compromise]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-implementing-least-privilege-administrative-models|Implementing Least-Privilege Administrative Models]]
- [[ad-ds-reducing-the-active-directory-attack-surface|Reducing the Active Directory Attack Surface]]
- [[ad-ds-best-practices-for-securing-active-directory|Best practices for securing Active Directory]]
<!-- crosslink:end -->
