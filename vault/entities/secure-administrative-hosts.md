---
title: Secure Administrative Hosts
type: entity
domain: active-directory
slug: secure-administrative-hosts
summary: Dedicated, hardened workstations or jump servers used exclusively for privileged administration of Active Directory — no email, no web browsing, MFA required — so that privileged credentials are never exposed on general-purpose machines.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Implementing-Secure-Administrative-Hosts (Microsoft Learn — Implementing Secure Administrative Hosts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Best-Practices-for-Securing-Active-Directory (Microsoft Learn — Best practices for securing Active Directory, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Securing-Domain-Controllers-Against-Attack (Microsoft Learn — Securing Domain Controllers Against Attack, fetched 2026-06-18)
  - kb:ad-ds-implementing-secure-administrative-hosts
  - kb:ad-ds-best-practices-for-securing-active-directory
  - kb:ad-ds-securing-domain-controllers-against-attack
provenance_extracted: 18
provenance_inferred: 3
provenance_ambiguous: 0
symptoms:
  - "privileged credentials cached on workstation"
  - "drive-by download on admin host"
  - "pass-the-hash via compromised jump server"
tags: [security, directory-services, how-to]
status: draft
updated: 2026-07-02
graph_community: "Securing Active Directory (best practices)"
---

# Secure Administrative Hosts

**Workstations or servers configured exclusively for privileged administration, running no general productivity or browsing software, so that DA/EA credentials are never exposed on untrusted hosts.**

## Body

The core principle: **never administer a trusted system (e.g., a domain controller) from a less-trusted host.** A privileged account that logs onto a compromised workstation leaves its credentials in LSASS memory where pass-the-hash tools can harvest them; a dedicated admin host prevents this exposure.

### Design principles

1. Never administer a trusted system from a less-trusted host.
2. Require multi-factor authentication (smart card) for privileged accounts and admin tasks. GPO setting: `Computer Configuration\Policies\Windows Settings\Local Policies\Security Options\Interactive logon: Require smart card`.
3. Physical security is as important as logical security — admin hosts not stored in a secure location can be physically attacked.
4. Admin hosts should run **no** email clients, web browsers, or office productivity software. Internet access is blocked via perimeter firewall, Windows Firewall with Advanced Security (WFAS), and application allowlisting (AppLocker).

### Deployment patterns

**Dedicated physical workstations** — each IT user has two machines: a regular workstation for daily tasks and a hardened admin workstation. Simple but expensive; still caches credentials in memory when connecting to remote systems.

**Secure workstation + virtualized productivity** — the hardened physical workstation runs management tools; productivity tasks are performed via RDP into a remote VM. Privileged credentials are not deposited on the productivity VM.

**Single physical + two VMs** — one physical host (locked down); one productivity VM; one admin VM. Smart cards required for each VM connection. Credentials are not cached on the physical host.

**Jump servers (PAW/SAW)** — datacenter-hosted RD Gateway servers that IT staff connect to via RDP+smart card to reach DCs and managed systems. Per-administrator VMs on the jump server can be reset to a clean snapshot after each session, ensuring no persistent credential exposure. Jump servers should run RD Gateway to restrict connections and optionally Hyper-V for per-user VMs.

### Configuration baseline

- Run the newest OS supported by the organization.
- Apply Security Configuration Wizard baseline; combine with Microsoft Security Compliance Manager templates.
- Enable AppLocker to allowlist only approved admin tools.
- Restrict RDP connections via RD Gateway; remove interactive logon for non-admin accounts.
- Patch admin hosts separately from the general infrastructure — compromise of a shared update server must not reach admin hosts.
- BitLocker on all volumes.
- Authorized accounts only: `Computer Configuration\Policies\Windows Settings\Local Policies\Security Settings\Local Policies\User Rights Assignment`.

### Domain controller hardening specifics

DCs are the highest-value admin hosts. Additional controls beyond the above:

- No applications beyond DC role services installed.
- Internet Explorer Enhanced Security Configuration enabled for Administrators (never disable).
- No internet browsing from DCs — use AppLocker, "black hole" proxy, and WFAS to enforce.
- RDP allowed only from authorized jump servers.
- Patch DCs separately from general infrastructure.
- Server Core installation option recommended to minimize attack surface.

## Contradictions / caveats

- Logging onto a physical admin workstation for remote administration still caches credentials in memory; jump server / VM approach avoids this.
- Implementing per-administrator VMs on jump servers adds infrastructure complexity; smaller organizations may use dedicated physical workstations instead.
- Virtual DC hosts must be managed as carefully as physical DCs; storage admins who can access VM files have effective access to the AD DS database.

## Reference notes
- [[ad-ds-implementing-secure-administrative-hosts]]
- [[ad-ds-best-practices-for-securing-active-directory]]
- [[ad-ds-securing-domain-controllers-against-attack]]

## See also
- [[securing-active-directory]]
- [[tiered-administration-model]]
- [[read-only-domain-controller]]
- [[advanced-audit-policy]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-implementing-secure-administrative-hosts|Implementing Secure Administrative Hosts]]
- [[ad-ds-best-practices-for-securing-active-directory|Best practices for securing Active Directory]]
- [[ad-ds-securing-domain-controllers-against-attack|Securing Domain Controllers Against Attack]]
<!-- crosslink:end -->
