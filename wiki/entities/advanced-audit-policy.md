---
title: Advanced Audit Policy Configuration
type: entity
domain: active-directory
slug: advanced-audit-policy
summary: Windows Vista / Server 2008 and later audit subsystem that replaces the nine legacy audit categories with granular subcategories, enabling organizations to enable only high-signal event types and suppress noise, configured via GPO or auditpol.exe.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration (Microsoft Learn — Advanced Audit Policy Configuration settings, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Monitoring-Active-Directory-for-Signs-of-Compromise (Microsoft Learn — Monitoring Active Directory for Signs of Compromise, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Audit-Policy-Recommendations (Microsoft Learn — Audit Policy Recommendations, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/Command-line-process-auditing (Microsoft Learn — Command line process auditing, fetched 2026-06-18)
  - kb:ad-ds-advanced-audit-policy-configuration
  - kb:ad-ds-monitoring-active-directory-for-signs-of-compromise
  - kb:ad-ds-audit-policy-recommendations
  - kb:ad-ds-command-line-process-auditing
provenance_extracted: 22
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "4719 — audit policy changed (attacker disabled auditing)"
  - "STOP: C0000244 — audit failure caused CrashOnAuditFail"
tags: [security, directory-services, how-to]
status: draft
updated: 2026-07-02
---

# Advanced Audit Policy Configuration

**Granular audit subcategories available from Windows Server 2008 onward, configured under `Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy Configuration\System Audit Policies`, replacing the nine blunt legacy categories with fine-grained, per-subcategory success/failure controls.**

## Body

### Legacy vs. advanced

Windows originally offered nine audit categories: Account Logon Events, Account Management, Directory Service Access, Logon Events, Object Access, Policy Change, Privilege Use, Process Tracking, System Events. Each generates events for all activity in its scope — too coarse for production use.

The Advanced Audit Policy adds subcategories under each main category. Use `auditpol /list /subcategory:*` to enumerate all available subcategories. This is a binary choice per system: either use legacy categories or advanced subcategories — they cannot both be active. Enable the override policy to prevent legacy settings from overwriting subcategory configuration:

**Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options**: `Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings` — set to **Enabled**.

### Key subcategories for AD security monitoring

**Account Logon:**
- Credential Validation (4776/4777) — High volume on DCs; baseline recommendation: Yes.
- Kerberos Authentication Service (4768/4771/4772) — Detects AS-REP roasting and TGT failures.
- Kerberos Service Ticket Operations (4769/4770) — Track service ticket requests; RC4 encryption type in 4769 may signal ticket harvesting.

**Account Management:**
- Security Group Management (4727–4758, 4764) — Low volume; default Success; alert on changes to privileged groups.
- User Account Management (4720/4722–4726/4738/4740/4765/4766/4780/4781/4794) — Low volume; baseline Success+Failure.

**Detailed Tracking:**
- Process Creation (4688) — Baseline: Yes/No. Enable command-line logging via separate GPO: `Administrative Templates\System\Audit Process Creation\Include command line in process creation events`. Command-line text appears in plaintext — consider data sensitivity. SHA1/SHA2 hash of the executable is also logged in the AppLocker event log.
- DPAPI Activity (4692–4695) — Stronger recommendation only; indicates attempts to access stored secrets.

**DS Access (DCs only):**
- Directory Service Changes (5136/5137/5138/5139/5141) — Critical: modifications to AD objects. Baseline: DC/DC.
- Directory Service Access (4662) — High volume on DCs; enable with SACL configuration on sensitive objects.

**Logon/Logoff:**
- Logon (4624/4625/4648/4675) — Baseline: Success+Failure. Essential for lateral movement detection.
- Special Logon (4964) — Low volume; alert immediately when DA member logs onto non-DC. Baseline: Success.
- Account Lockout (4625) — Threshold alerting for password spray.

**Policy Change:**
- Audit Policy Change (4715/4719/4817/4902/4904–4908/4912) — Low volume; alert immediately (4719 means audit was changed, possibly disabled by attacker).

**System:**
- Security State Change, Security System Extension, System Integrity — Baseline: Yes/Yes.

### Configuration methods

**GPO (preferred for domain):**
`Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy` — set subcategories to Success, Failure, or both.

**auditpol.exe (local or scripted):**
```
auditpol /set /subcategory:"user account management" /success:enable /failure:enable
auditpol /set /subcategory:"logon" /success:enable /failure:enable
auditpol /get /category:*   # verify effective policy
```
Note: GPO typically prevails over local auditpol settings when both are configured. Use `auditpol /get` to verify the effective policy — Group Policy display may not accurately reflect what is active.

**CrashOnAuditFail:**
`auditpol /set /option:CrashOnAuditFail /enable` — causes the system to immediately stop (STOP: C0000244) if a security audit cannot be logged. Only appropriate for high-assurance environments; requires careful log rotation to avoid unplanned outages.

### Baseline recommendations summary (Windows Server)

| Category | Baseline (Success/Failure) |
|---|---|
| Credential Validation | Yes / Yes |
| Security Group Management | Yes / Yes |
| User Account Management | Yes / Yes |
| Process Creation | Yes / No |
| Directory Service Access | DC / DC |
| Directory Service Changes | DC / DC |
| Logon | Yes / Yes |
| Special Logon | Yes / No |
| Audit Policy Change | Yes / Yes |
| Authentication Policy Change | Yes / No |
| Security State Change | Yes / Yes |
| Security System Extension | Yes / Yes |
| System Integrity | Yes / Yes |

## Contradictions / caveats

- High-volume subcategories (Filtering Platform Connection, Detailed File Share, Sensitive Privilege Use, IPsec) can generate thousands of events per second; enable only when specifically needed and after testing log storage capacity.
- Command-line process auditing logs credentials in plaintext if a user types a password as a command-line argument — restrict read access to the Security event log on sensitive systems.
- DPAPI Activity auditing (4692–4695) can generate high volume during backup operations if `FullPrivilegeAuditing` is also enabled.

## Reference notes
- [[ad-ds-advanced-audit-policy-configuration]]
- [[ad-ds-monitoring-active-directory-for-signs-of-compromise]]
- [[ad-ds-audit-policy-recommendations]]
- [[ad-ds-command-line-process-auditing]]

## See also
- [[securing-active-directory]]
- [[monitoring-ad-for-compromise]]
- [[software-restriction-policies]]
- [[tiered-administration-model]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-advanced-audit-policy-configuration|Advanced Audit Policy Configuration settings]]
- [[ad-ds-monitoring-active-directory-for-signs-of-compromise|Monitoring Active Directory for Signs of Compromise]]
- [[ad-ds-audit-policy-recommendations|System Audit Policy recommendations]]
- [[ad-ds-command-line-process-auditing|Command line process auditing]]
<!-- crosslink:end -->
