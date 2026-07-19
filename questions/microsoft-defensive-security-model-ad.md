---
origin: eval-cohort
title: "Microsoft's Defensive Security Model for Active Directory"
type: question
domain: active-directory
slug: microsoft-defensive-security-model-ad
summary: "Microsoft's four-pillar defensive model for AD DS: reduce attack surface, enforce least-privilege/tiered administration, monitor for compromise, and plan for breach recovery."
sources:
  - kb:ad-ds-best-practices-for-securing-active-directory
  - kb:ad-ds-reducing-the-active-directory-attack-surface
  - kb:ad-ds-implementing-least-privilege-administrative-models
  - kb:ad-ds-implementing-secure-administrative-hosts
  - kb:ad-ds-monitoring-active-directory-for-signs-of-compromise
  - kb:ad-ds-securing-domain-controllers-against-attack
  - kb:ad-ds-planning-for-compromise
  - kb:ad-ds-maintaining-a-more-secure-environment
  - kb:ad-ds-attractive-accounts-for-credential-theft
  - kb:ad-ds-avenues-to-compromise
  - kb:ad-ds-ad-forest-recovery-guide
  - kb:ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory
  - kb:ad-ds-ldap-signing
question_tier: conceptual
provenance:
  extracted: 28
  inferred: 5
  ambiguous: 0
tags: [security]
status: draft
updated: 2026-07-12
---

# Microsoft's Defensive Security Model for Active Directory

Microsoft's defensive model for Active Directory is built on the premise that **no infrastructure is ever perfectly immune** — the goal is to protect the directory from compromise, not prevent every attack attempt (extracted — `ad-ds-best-practices-for-securing-active-directory.md:19`). The model organizes into four pillars (inferred — synthesized from the four sub-articles the source reference points to):

## 1. Reduce the attack surface

Shrink the exploitable footprint so initial breaches cannot propagate to full-forest compromise.

- **Eliminate excessive privilege** — the three highest-privilege built-in groups (Enterprise Admins, Domain Admins, Administrators) should be kept empty day-to-day, populated only temporarily via PIM/PAM (`ad-ds-best-practices-for-securing-active-directory.md:85-87`). A member of any one of these three can grant themselves membership in the others — treat them as equivalent for risk purposes (`reducing-ad-attack-surface.md:53-56`).
- **Secure domain controllers** — DCs run only the DC role, no browsers or productivity software, Server Core recommended, physical+logical isolation (`ad-ds-best-practices-for-securing-active-directory.md:117-127`). Use application allowlists (AppLocker) on DCs and admin hosts (`ad-ds-best-practices-for-securing-active-directory.md:168`).
- **Isolate or decommission legacy systems** — legacy OS (2003/2000) forces weaker LAN Manager/NTLM settings domain-wide. Isolate in a separate domain/forest or use "creative destruction" — replace rather than maintain (`reducing-ad-attack-surface.md:122-128`).
- **Patch consistently** — incomplete patching is the most common entry point; patch OS, apps, and network devices (`ad-ds-best-practices-for-securing-active-directory.md:37`).
- **Pristine forest approach** — for heavily compromised environments, build a new forest from scratch, migrate only verified-clean accounts with no SID history from the legacy forest (`reducing-ad-attack-surface.md:134-138`).

## 2. Least-privilege & tiered administration

Separate administrative privileges into tiers so a workstation compromise cannot harvest domain-admin credentials.

- **Three-tier model**: Tier 0 (forest/domain-wide — DCs, AD DB, trust infrastructure), Tier 1 (member servers), Tier 2 (workstations/end-users) (`tiered-administration-model.md:11-19`).
- **Deny-logon GPOs** enforce the tiers — DA accounts are denied interactive logon, RDP, network access, batch, and service logon on all workstation and member-server OUs (`tiered-administration-model.md:24-31`).
- **Temporary membership** — privileged group membership is granted only for specific tasks, then revoked. PIM/PAM tooling automates time-bound credential vaults (`tiered-administration-model.md:33-37`).
- **Secure administrative hosts** — dedicated, hardened machines (no email, no web browsing, AppLocker allowlisting, MFA/smart card required) used exclusively for AD administration (`secure-administrative-hosts.md:12-19`). Never administer a trusted system from a less-trusted host (`ad-ds-best-practices-for-securing-active-directory.md:109`).
- **LDAP signing & channel binding** — enforce LDAP signing (SASL integrity) and LDAPS channel binding to prevent replay and MITM attacks against DCs (`ldap-signing-and-channel-binding.md:9-17`). WS2025 enforces signing by default on new installs (in-place upgrades preserve prior settings) (`ldap-signing-and-channel-binding.md:33-36`).

## 3. Monitor for signs of compromise

Event log monitoring is the primary detective control — 84% of breached organizations had evidence in logs they did not act on (`monitoring-ad-for-compromise.md:6`).

- **Single-occurrence alerts** — events that alone indicate compromise: DA logon to a workstation (Event 4964), unexpected privileged group membership change (4728/4732/4756), audit policy change (4719), service installed on DC (7045) (`monitoring-ad-for-compromise.md:21-27`).
- **Threshold/baseline alerts** — accumulation above expected rate: failed logons exceeding baseline (password spray), unexpected process creation on DCs (4688) (`monitoring-ad-for-compromise.md:39-43`).
- **Monitor critical objects continuously** — AdminSDHolder, protected group membership, VIP account attributes (cn, sAMAccountName, userPrincipalName, userAccountControl) (`monitoring-ad-for-compromise.md:31-37`).
- **Monitor AD object modifications** — Event 5136 tracks UPN/sAMAccountName changes for UPN-hijacking attacks where an attacker temporarily swaps a target's UPN to request a certificate in their name (`credential-theft-and-attractive-accounts.md:80-83`).
- **Protected Accounts & AdminSDHolder** — SDProp runs every 60 minutes on the PDC Emulator, resetting ACLs on protected accounts to the AdminSDHolder template and preventing OU-delegated permission changes from affecting privileged principals (`protected-accounts-and-groups.md:29-34`).

## 4. Plan for (assume) breach and recover

Accept that no defense is perfect; pre-build incident recovery plans.

- **Classify all AD data** — systems, applications, users — with named business owners and regular attestation (`ad-ds-best-practices-for-securing-active-directory.md:139-148`).
- **Forest recovery procedure** — the last-resort procedure when a forest-wide failure leaves every DC unusable: restore one DC per domain from backup, seize FSMO roles, reset krbtgt password twice (invalidates all pre-disaster tickets including Golden Tickets), clean up metadata, rebuild remaining DCs via fresh promotion never by reconnecting old ones (`ad-forest-recovery.md:11-27`).
- **Implement business-driven lifecycle management** — configuration management with regular compliance review, secure development lifecycle for custom apps (`ad-ds-best-practices-for-securing-active-directory.md:174-176`).
- **Windows LAPS & gMSA/dMSA** — automate local-admin password rotation per machine (LAPS) and manage service-account passwords without human interaction (gMSA/dMSA), eliminating lateral-movement vectors and Kerberoastable credentials (`securing-active-directory.md:29-31`).

## Measure taxonomy

Every recommendation in Microsoft's guidance is categorized as **Tactical** (component-focused, implementable quickly) vs **Strategic** (comprehensive, requires planning), and **Preventative** vs **Detective**. Highest-priority items — patch apps/OS, antivirus, monitor sensitive objects — are Tactical/Preventative. Strategic items (least-privilege RBAC, pristine forests, decommission legacy) provide deeper defense but require more organizational investment (`ad-ds-best-practices-for-securing-active-directory.md:155-180`).

## Key principle

The model is a **program, not a setting** (inferred — the source states "no infrastructure is ever perfectly immune", the program framing is synthesis) — no single configuration makes AD secure. It requires continuous effort across all four pillars. The EA/DA/BA triad are equivalent in risk, and protecting the AdminSDHolder object is critical because a compromised template backdoors every privileged account added to the domain (extracted — `protected-accounts-and-groups.md:47-50`).

## Sources

### Reference notes (`kb:`)
- [[ad-ds-best-practices-for-securing-active-directory|Best practices for securing Active Directory]]
- [[ad-ds-reducing-the-active-directory-attack-surface|Reducing the Active Directory Attack Surface]]
- [[ad-ds-implementing-least-privilege-administrative-models|Implementing Least-Privilege Administrative Models]]
- [[ad-ds-implementing-secure-administrative-hosts|Implementing Secure Administrative Hosts]]
- [[ad-ds-monitoring-active-directory-for-signs-of-compromise|Monitoring AD for Signs of Compromise]]
- [[ad-ds-securing-domain-controllers-against-attack|Securing Domain Controllers Against Attack]]
- [[ad-ds-planning-for-compromise|Planning for Compromise]]
- [[ad-ds-maintaining-a-more-secure-environment|Maintaining a More Secure Environment]]
- [[ad-ds-attractive-accounts-for-credential-theft|Attractive Accounts for Credential Theft]]
- [[ad-ds-avenues-to-compromise|Avenues to Compromise]]
- [[ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory|Appendix C: Protected Accounts and Groups]]
- [[ad-ds-ldap-signing|LDAP signing for AD DS]]
- [[ad-ds-ad-forest-recovery-guide|Active Directory Forest Recovery Guide]]

### Wiki pages (`[[slug]]`)
- [[securing-active-directory]]
- [[reducing-ad-attack-surface]]
- [[tiered-administration-model]]
- [[secure-administrative-hosts]]
- [[monitoring-ad-for-compromise]]
- [[credential-theft-and-attractive-accounts]]
- [[protected-accounts-and-groups]]
- [[ldap-signing-and-channel-binding]]
- [[ad-forest-recovery]]
- [[windows-laps]]
- [[group-managed-service-accounts]]
- [[ad-certificate-services]]

### Web
- [Best practices for securing Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Best-Practices-for-Securing-Active-Directory)

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-best-practices-for-securing-active-directory|Best practices for securing Active Directory]]
- [[ad-ds-reducing-the-active-directory-attack-surface|Reducing the Active Directory Attack Surface]]
- [[ad-ds-implementing-least-privilege-administrative-models|Implementing Least-Privilege Administrative Models]]
- [[ad-ds-implementing-secure-administrative-hosts|Implementing Secure Administrative Hosts]]
- [[ad-ds-monitoring-active-directory-for-signs-of-compromise|Monitoring Active Directory for Signs of Compromise]]
- [[ad-ds-securing-domain-controllers-against-attack|Securing Domain Controllers Against Attack]]
- [[ad-ds-planning-for-compromise|Planning for compromise]]
- [[ad-ds-maintaining-a-more-secure-environment|Maintaining a More Secure Environment]]
- [[ad-ds-attractive-accounts-for-credential-theft|Attractive Accounts for Credential Theft]]
- [[ad-ds-avenues-to-compromise|Avenues to Compromise]]
- [[ad-ds-ad-forest-recovery-guide|Active Directory Forest Recovery Guide]]
- [[ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory|Appendix C]]
- [[ad-ds-ldap-signing|LDAP signing for Active Directory Domain Services on Windows Server]]
<!-- crosslink:end -->
