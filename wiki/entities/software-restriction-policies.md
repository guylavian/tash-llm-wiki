---
title: Software Restriction Policies and AppLocker
type: entity
domain: active-directory
slug: software-restriction-policies
summary: Windows mechanisms — Software Restriction Policies (legacy) and AppLocker (Windows 7/Server 2008 R2+) — that allowlist authorized executables, scripts, and DLLs on administrative hosts and domain controllers, preventing unauthorized application installation and limiting the tools an attacker can use after initial access.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Implementing-Secure-Administrative-Hosts (Microsoft Learn — Implementing Secure Administrative Hosts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Securing-Domain-Controllers-Against-Attack (Microsoft Learn — Securing Domain Controllers Against Attack, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Avenues-to-Compromise (Microsoft Learn — Avenues to Compromise, fetched 2026-06-18)
  - kb:ad-ds-implementing-secure-administrative-hosts
  - kb:ad-ds-securing-domain-controllers-against-attack
  - kb:ad-ds-avenues-to-compromise
provenance_extracted: 8
provenance_inferred: 6
provenance_ambiguous: 0
symptoms:
  - "unauthorized application installed on domain controller"
  - "attacker tooling executed on admin host"
  - "web browser launch on DC not blocked"
tags: [security, directory-services, how-to]
status: draft
updated: 2026-07-02
---

# Software Restriction Policies and AppLocker

**Allowlist-based application control mechanisms that restrict which executables, scripts, installers, and DLLs can run on a system — a preventative control that limits the tools an attacker can execute even after gaining access to a host.**

## Body

### Why application control matters for AD security

Domain controllers and administrative hosts are targets where attackers aim to install credential-harvesting tools (mimikatz, keyloggers), rootkits, and backdoors. Preventing unauthorized software execution significantly raises the cost of post-compromise activity. The Microsoft guidance explicitly recommends application allowlisting on DCs, admin hosts, and other sensitive systems.

Additionally, DC compromise is often achieved through software that was already installed — legacy monitoring tools, antivirus consoles, or browser downloads — that were not part of the DC's required role. Application control prevents this class of compromise.

### Software Restriction Policies (SRP)

Available since Windows XP / Server 2003. Configured in Group Policy under `Computer Configuration\Windows Settings\Security Settings\Software Restriction Policies`. SRP rules can restrict execution based on:
- Hash — specific file hashes.
- Certificate — software signed by a specific publisher.
- Path — file system paths.
- Zone — internet zone (for files downloaded from the internet).

SRP operates at a low level and applies to all users including administrators. The default rule is typically "Unrestricted" (allow all); switching to "Disallowed" with explicit allow rules creates an allowlist. SRP is considered legacy; AppLocker supersedes it for modern deployments.

### AppLocker

Available on Windows 7 Enterprise/Ultimate and Windows Server 2008 R2 and later. Configured in Group Policy under `Computer Configuration\Policies\Windows Settings\Security Settings\Application Control Policies\AppLocker`. AppLocker rules can be based on:
- Publisher (code-signing certificate + product name + version) — recommended for most rules; survives updates.
- Path — directory or file path.
- File hash — exact binary match.

AppLocker rule collections:
- **Executable rules** (.exe, .com)
- **Windows Installer rules** (.msi, .msp, .mst)
- **Script rules** (.ps1, .bat, .cmd, .vbs, .js)
- **Packaged app rules** (MSIX/AppX)
- **DLL rules** — optional; high performance impact; only enable on high-security systems.

AppLocker events are logged in `Application and Services Logs\Microsoft\Windows\AppLocker`. The `AuditOnly` enforcement mode logs what would be blocked without actually blocking — use this to baseline before switching to enforcement.

### Deployment on administrative hosts and DCs

The Microsoft guidance specifies:
- Administrative hosts should be configured with AppLocker (or equivalent) to allowlist only approved admin tools. Any admin application that does not adhere to secure settings should be upgraded or replaced.
- DCs should have web browsers blocked via AppLocker, WFAS (Windows Firewall with Advanced Security), and "black hole" proxy configuration.
- New tools added to admin hosts must be thoroughly tested before deployment.
- SHA1/SHA2 hashes of executables that run are also logged in the AppLocker event log when Process Creation auditing is enabled — useful for forensics.

### Integration with the broader security model

Application control is a **preventative** layer complementing **detective** controls (see [[advanced-audit-policy]]). Together they implement the "use application allowlists on domain controllers, administrative hosts, and other sensitive systems" recommendation from the security best practices summary table.

On workstations, application control reduces the blast radius of drive-by downloads and phishing payloads that attempt to install credential-harvesting tools. (inferred: the reference guidance is specific to admin hosts and DCs; workstation coverage is an extension of the same principle.)

## Contradictions / caveats

- AppLocker is only available on Enterprise/Ultimate client editions and Standard/Datacenter server editions — not Home or Pro editions.
- DLL rule enforcement has significant performance impact and is generally only applied to highly sensitive systems.
- SRP and AppLocker can conflict; use one or the other. Enable the GPO setting "Force audit policy subcategory settings to override audit policy category settings" to prevent audit policy conflicts from interfering with AppLocker log collection.
- AppLocker does not block code running in memory (fileless attacks) or scripts launched from allowed interpreters with malicious content; pair with behavioral monitoring.
- Path-based rules are weaker than publisher or hash rules because an attacker who can write to an allowed path can bypass the rule.

## Reference notes
- [[ad-ds-implementing-secure-administrative-hosts]]
- [[ad-ds-securing-domain-controllers-against-attack]]
- [[ad-ds-avenues-to-compromise]]

## See also
- [[securing-active-directory]]
- [[secure-administrative-hosts]]
- [[advanced-audit-policy]]
- [[reducing-ad-attack-surface]]
- [[group-policy]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-implementing-secure-administrative-hosts|Implementing Secure Administrative Hosts]]
- [[ad-ds-securing-domain-controllers-against-attack|Securing Domain Controllers Against Attack]]
- [[ad-ds-avenues-to-compromise|Avenues to Compromise]]
<!-- crosslink:end -->
