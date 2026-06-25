---
title: Monitoring Active Directory for Signs of Compromise
type: entity
domain: active-directory
slug: monitoring-ad-for-compromise
summary: Event log monitoring strategy for AD DS — which event IDs to alert on immediately (DA logon to workstation, unexpected group membership changes) vs. accumulate as baselines — and which AD objects/attributes to watch for signs of privilege escalation or DCSync.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Monitoring-Active-Directory-for-Signs-of-Compromise (Microsoft Learn — Monitoring Active Directory for Signs of Compromise, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Audit-Policy-Recommendations (Microsoft Learn — Audit Policy Recommendations, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Best-Practices-for-Securing-Active-Directory (Microsoft Learn — Best practices for securing Active Directory, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 5
provenance_ambiguous: 0
symptoms:
  - "DA account logged on to non-DC workstation (Event 4964)"
  - "unexpected member added to Domain Admins (Event 4728)"
  - "unauthorized service installed on DC"
  - "antivirus disabled or removed"
  - "high volume of failed logons — password spray"
  - "DCSync replication rights granted to non-DC account"
tags: [security, directory-services, troubleshooting]
status: draft
updated: 2026-06-18
---

# Monitoring Active Directory for Signs of Compromise

**Event log monitoring is the primary detective control for AD compromise; 84% of breached organizations had evidence in their event logs they did not act on — the gap is alert design, not data availability.**

## Body

### Two alert patterns

Effective AD monitoring produces two types of alerts:

1. **Single-occurrence alerts** — events that, on their own, indicate unauthorized activity.
2. **Threshold/baseline alerts** — an accumulation of events above an expected rate (e.g., failed logons exceeding a baseline signals password-spraying).

### Critical single-occurrence events to alert on immediately

| Scenario | Event ID | Notes |
|---|---|---|
| DA logs on to a non-DC workstation | 4964 (Special Groups logon) | DA is forbidden from workstations by [[tiered-administration-model]] GPO |
| Unexpected member added to Domain Admins | 4728 (member added to global security group) | Immediate investigation required |
| Unexpected member added to Enterprise Admins | 4728 / 4756 | EA should be empty |
| Unauthorized service installed on a DC | 7045 (new service installed) | DCs should be single-role |
| Disabled privileged account (built-in Administrator) enabled | 4722 (account enabled) | Should only happen in break-glass |
| Standard user added to privileged group | 4728/4732/4756 | |
| Audit policy changed | 4719 (system audit policy changed) | Attackers disable auditing |
| Antivirus/antimalware disabled | vendor-specific + 7036 (service state change) | Restart protection automatically |
| AD object modification — UPN/sAMAccountName on VIP account | 5136 (directory service object modified) | UPN hijacking for cert spoofing |

### Objects and attributes to monitor continuously

- **Protected group membership**: Administrators, Domain Admins, Enterprise Admins, Schema Admins.
- **VIP and privileged accounts** — attributes on the Account tab: `cn`, `name`, `sAMAccountName`, `userPrincipalName`, `userAccountControl`.
- **Disabled privileged accounts** for re-enabling (event 4722).
- **Management accounts** — all write operations.
- **Domain controller accounts** for unexpected changes.
- **AdminSDHolder object** — changes here cascade to all protected accounts.

### Baseline accumulation (threshold) alerts

Establish a normal rate of failed logons per hour/day; alert when exceeded. A single failed logon is noise; hundreds in minutes is a password spray. Similarly, baseline expected process creation rates on DCs — unexpected process creations (event 4688 with command-line auditing enabled) on a DC are high-severity signals. See [[advanced-audit-policy]] for enabling command-line process auditing (event 4688 + "Include command line" GPO setting).

### Key event IDs reference

| Event ID | Description | Alert priority |
|---|---|---|
| 4624 | Successful logon | Baseline |
| 4625 | Failed logon | Threshold alert |
| 4648 | Logon with explicit credentials | Medium — watch for runas of DA on workstation |
| 4719 | Audit policy changed | High |
| 4720 | User account created | Medium |
| 4722 | Account enabled | High if privileged account |
| 4726 | User account deleted | Medium |
| 4728/4732/4756 | Member added to security group (global/local/universal) | High if privileged group |
| 4738 | User account changed | High if VIP/privileged |
| 4964 | Special groups assigned to new logon | High |
| 5136 | Directory service object modified | High if on protected/VIP object |
| 5137 | Directory service object created | Medium |
| 5141 | Directory service object deleted | High |
| 4688 | New process created (+ command-line if enabled) | Medium/High on DCs |
| 4769 | Kerberos service ticket requested | Baseline; watch for RC4 requests (DES downgrade / AS-REP roasting) |

### Workstations vs. servers

Initial breach activity often surfaces on workstations first. Focusing monitoring only on DCs misses lateral-movement indicators that appear on end-user machines (inferred from source text: "initial signs of malicious activity often appear on workstations").

### Integration with Microsoft Defender for Identity

Microsoft Defender for Identity (formerly Azure ATP) places a sensor on DCs and provides behavioral analytics for pass-the-hash, pass-the-ticket, DCSync, golden ticket, and LDAP reconnaissance attacks. The sensor connects to the cloud via a one-way proxy connection, keeping DC internet exposure minimal (inferred synthesis from the DC hardening reference).

## Contradictions / caveats

- Group Policy does not always accurately report the status of all enabled auditing policies; use `auditpol /get /category:*` to verify the effective policy, not the GPO display.
- Enabling "Force audit policy subcategory settings to override audit policy category settings" is required in Group Policy so that advanced subcategory settings take effect (event 4719 is logged when settings are overwritten).
- High-volume events (Filtering Platform Connection, Detailed File Share) can create log noise that masks real signals; tune before enabling.
- 85% of breaches took several weeks to notice — monitoring without alert-driven response is insufficient.

## Reference notes
- [[ad-ds-monitoring-active-directory-for-signs-of-compromise]]
- [[ad-ds-audit-policy-recommendations]]
- [[ad-ds-best-practices-for-securing-active-directory]]

## See also
- [[securing-active-directory]]
- [[advanced-audit-policy]]
- [[tiered-administration-model]]
- [[protected-accounts-and-groups]]
- [[credential-theft-and-attractive-accounts]]
