---
title: Reducing the Active Directory Attack Surface
type: entity
domain: active-directory
slug: reducing-ad-attack-surface
summary: The technical and organizational controls that shrink the exploitable footprint of an AD DS deployment — eliminating excessive privilege, isolating legacy systems, hardening domain controllers, and removing unnecessary software — so that initial breach events cannot propagate to full-forest compromise.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Reducing-the-Active-Directory-Attack-Surface (Microsoft Learn — Reducing the Active Directory Attack Surface, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Best-Practices-for-Securing-Active-Directory (Microsoft Learn — Best practices for securing Active Directory, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Avenues-to-Compromise (Microsoft Learn — Avenues to Compromise, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Planning-for-Compromise (Microsoft Learn — Planning for compromise, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Maintaining-a-More-Secure-Environment (Microsoft Learn — Maintaining a More Secure Environment, fetched 2026-06-18)
  - kb:ad-ds-reducing-the-active-directory-attack-surface
  - kb:ad-ds-best-practices-for-securing-active-directory
  - kb:ad-ds-avenues-to-compromise
  - kb:ad-ds-planning-for-compromise
  - kb:ad-ds-maintaining-a-more-secure-environment
provenance_extracted: 16
provenance_inferred: 8
provenance_ambiguous: 0
symptoms:
  - "pass-the-hash lateral movement across member servers"
  - "DC compromise via unpatched application"
  - "privilege escalation via overpopulated DA group"
  - "legacy OS requiring LAN Manager hash or reversible encryption"
tags: [security, directory-services, concept]
status: draft
updated: 2026-07-02
graph_community: "Securing Active Directory (best practices)"
---

# Reducing the Active Directory Attack Surface

**Attack surface reduction is the ensemble of controls that raises the cost of compromise: eliminate unnecessary privilege, harden DCs, isolate or decommission legacy systems, patch consistently, and create a business-driven lifecycle for all AD data.**

## Body

### The common entry points

Microsoft's assessment findings consistently identify these attack surface components:

- **Excessive privilege** — EA, DA, and BA groups overpopulated with permanent members; local Administrators groups on workstations and member servers containing hundreds of accounts; service accounts running with DA rights when only resource-specific rights are needed.
- **Incomplete patching** — Windows systems patched; non-Windows systems, COTS applications, and network devices left unpatched. A single unpatched server is a potential entry point.
- **Outdated applications and OS** — legacy apps that require LM hash storage or reversibly encrypted passwords force AD to maintain weaker security settings domain-wide, exposing the entire forest.
- **Misconfiguration** — WFAS disabled "for simplicity"; UAC disabled on servers; baselines from older OS versions applied unchanged to newer OS.
- **Permitting unauthorized applications on DCs** — tools installed for convenience add ports, service accounts, and vulnerabilities to the highest-value targets in the forest.

### Privileged accounts: the EA/DA/BA triad

All three groups (Enterprise Admins, Domain Admins, Administrators) should be treated as effectively equivalent in risk — a member of any one can grant themselves membership in the others. Correct posture:

- **EA**: empty day-to-day. Used only for forest-wide operations (adding domains, establishing trusts, raising forest functional level). Temporarily populated; audited; immediately depopulated.
- **DA**: empty day-to-day. Used only for domain-wide operations and break-glass recovery. Temporarily populated.
- **BA**: empty day-to-day except the domain's built-in Administrator account (secured with smart-card flag and deny-logon GPOs). Temporarily populated.

Schema Admins (SA) should contain members only when schema modifications are required — it is the only group that can modify the AD DS schema.

### Administrative controls

See [[tiered-administration-model]] for the full model. Key reductions:
- Apply deny-logon GPOs (deny network, batch, service, RDP, local logon) to DA/EA/BA on all workstation/server OUs.
- Enable `Account is sensitive and cannot be delegated` on the built-in Administrator in each domain.
- Enable `Smart card is required for interactive logon` on the built-in Administrator account — this resets the password to a 120-character random value.
- Audit changes to EA/DA/BA membership and alert the security team immediately.
- Use [[secure-administrative-hosts]] so privileged logons never occur on general-purpose systems.

### Domain controller hardening

DCs must be secured more stringently than any other system class:
- Install only software required for DC function. No general-purpose utilities, monitoring agents, or browsers.
- Run Server Core where possible — minimal attack surface, fewer patches needed.
- Block internet access entirely (AppLocker + WFAS + "black hole" proxy).
- Restrict RDP to jump servers only; enforce via GPO.
- Patch separately from general infrastructure to prevent a compromised update server from reaching DCs.
- Physical: BitLocker on all DC volumes; dedicated racks in datacenters; RODCs for branch offices where physical security cannot be guaranteed.

### Legacy system isolation

Legacy OS versions (Windows Server 2003, Windows 2000) in the domain force AD to maintain weaker LAN Manager or NTLM settings that increase exposure for all systems. Strategy:
1. Identify and catalog legacy systems and applications.
2. Upgrade or replace where possible ("creative destruction" — replace with a new application rather than maintaining the old one).
3. Where decommissioning is infeasible, isolate in a separate domain or forest so their weak requirements do not affect the production environment.
4. Never introduce legacy OS into a pristine forest.

### Pristine forest / "secure cell" approach

For organizations with heavily compromised or legacy-heavy environments: build a new pristine AD DS forest with current OS and secure-from-birth settings, migrate only verified-clean users, data, and applications (nonmigratory migration — fresh accounts, no SID history from the legacy forest), and treat the legacy forest as untrusted. This is an extreme measure but the only path to a trustworthy environment after a deep compromise.

### Business lifecycle management

All AD data — accounts, groups, service accounts, systems, applications — should have a named business owner and undergo regular attestation. Attackers create accounts that follow naming conventions and blend in; business owners who regularly attest to the validity of objects in their scope detect anomalies faster. Classify AD data (VIP accounts, critical servers) to prioritize monitoring and protection depth.

## Contradictions / caveats

- Removing EA/DA from the Administrators group in each domain is explicitly flagged as an inappropriate modification — they are needed for forest disaster recovery. Use deny-logon GPOs instead.
- The `Smart card is required for interactive logon` flag can be overwritten by a user with password-reset rights — implement additional controls (deny-logon GPOs) alongside the flag.
- Creative destruction of legacy applications is the right goal but carries project risk; maintain isolation of the old system while the replacement is built.
- Pristine forest migration using SID history from a compromised legacy forest can re-introduce compromised identities — use nonmigratory approaches.

## Reference notes
- [[ad-ds-reducing-the-active-directory-attack-surface]]
- [[ad-ds-best-practices-for-securing-active-directory]]
- [[ad-ds-avenues-to-compromise]]
- [[ad-ds-planning-for-compromise]]
- [[ad-ds-maintaining-a-more-secure-environment]]

## See also
- [[securing-active-directory]]
- [[tiered-administration-model]]
- [[secure-administrative-hosts]]
- [[credential-theft-and-attractive-accounts]]
- [[protected-accounts-and-groups]]
- [[ad-forest-recovery]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-reducing-the-active-directory-attack-surface|Reducing the Active Directory Attack Surface]]
- [[ad-ds-best-practices-for-securing-active-directory|Best practices for securing Active Directory]]
- [[ad-ds-avenues-to-compromise|Avenues to Compromise]]
- [[ad-ds-planning-for-compromise|Planning for compromise]]
- [[ad-ds-maintaining-a-more-secure-environment|Maintaining a More Secure Environment]]
<!-- crosslink:end -->
