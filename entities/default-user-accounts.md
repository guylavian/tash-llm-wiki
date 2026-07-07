---
title: Default User Accounts
type: entity
domain: active-directory
slug: default-user-accounts
summary: Active Directory creates three built-in user accounts automatically when a domain is provisioned — Administrator (RID 500), Guest (RID 501), and KRBTGT (RID 502) — each with distinct security properties and operational considerations.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts (Microsoft Learn — Active Directory Accounts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers (Microsoft Learn — Security Identifiers, fetched 2026-06-18)
  - kb:ad-ds-understand-default-user-accounts
  - kb:ad-ds-understand-security-identifiers
provenance_extracted: 22
provenance_inferred: 3
provenance_ambiguous: 0
tags: [directory-services, security, users, concept]
status: draft
updated: 2026-07-02
---

# Default User Accounts

**When a Windows Server domain is created, AD DS automatically provisions three built-in user accounts — Administrator, Guest, and KRBTGT — stored in `CN=Users` and protected by special security rules.**

## Administrator Account

| Attribute | Value |
|---|---|
| Well-known SID/RID | S-1-5-`<domain>`-500 |
| Default member of | Administrators, Domain Admins, Enterprise Admins (forest root), Schema Admins (forest root), Group Policy Creator Owners, Domain Users |
| Protected by AdminSDHolder | Yes |

The Administrator account has Full Control over all domain resources. It **cannot be deleted or locked out**, but can be renamed or disabled. Even when disabled, it is still usable to sign in to a domain controller via safe mode. The person who runs the AD DS installation wizard sets the initial password.

Best practice: rename and disable the domain Administrator account where operationally feasible; create named admin accounts for day-to-day administration instead. For domain-level tasks, use a dedicated privileged account from which you do not browse the internet or read email (see [[securing-active-directory]]).

## Guest Account

| Attribute | Value |
|---|---|
| Well-known SID/RID | S-1-5-`<domain>`-501 |
| Default member of | Guests, Domain Guests |
| Protected by AdminSDHolder | No |

The Guest account provides limited, passwordless access and is **disabled by default**. Because it has a well-known SID and can provide anonymous-style access, it represents an attack surface. Keep it disabled; if it must be enabled, assign it a strong password and restricted rights for the minimum duration needed.

Guest account behaviour: when a Guest member signs out, the entire user profile (`%userprofile%`) is deleted — Guests always run a temporary profile.

## KRBTGT Account

| Attribute | Value |
|---|---|
| Well-known SID/RID | S-1-5-`<domain>`-502 |
| Default member of | Domain Users |
| Protected by AdminSDHolder | Yes |
| Can be enabled | No |
| Can be deleted or renamed | No |

KRBTGT is the service account for the **Key Distribution Center (KDC)** on every domain controller. Its password is the master secret from which all Kerberos Ticket-Granting Tickets (TGTs) in the domain are derived — changing it invalidates all currently issued TGTs domain-wide.

### RODC KRBTGT

Each Read-Only Domain Controller (RODC) uses a **separate KRBTGT account** (with its own password) to sign and encrypt TGTs it issues. This isolates RODC compromise: resetting an RODC's KRBTGT does not affect the rest of the domain, and resetting the main KRBTGT does not immediately affect TGTs the RODC issued. See [[read-only-domain-controller]] for full RODC credential caching details.

### Password Reset Guidance

Reset KRBTGT password:
- After suspected domain compromise (Golden Ticket attack mitigation — see [[krbtgt-reset]]).
- After forest recovery before bringing DCs back online.
- On a regular schedule as part of credential hygiene.

**Operational impact**: resetting KRBTGT must be done **twice** (the first reset changes the password; the second discards the previous password so no old TGTs remain valid). Allow replication to complete between resets. All existing TGTs will be rejected by DCs after the reset; users and services must reauthenticate. Rebooting affected computers is the most reliable way to force reauthentication. NTLM sessions are unaffected. (inferred — the two-reset requirement and replication window are standard practice described implicitly across the reset guidance; the source states the operational effect of the first reset only.)

## Protecting Default Accounts

All default domain accounts reside in `CN=Users` — do not move them. Accounts protected by AdminSDHolder (Administrator, KRBTGT) have their permissions periodically rewritten from the AdminSDHolder security descriptor; to change permissions on these accounts, modify the AdminSDHolder object in `CN=System`, not the accounts directly.

Best practices for all privileged domain accounts (inferred — synthesised from the separate-accounts and restrict-sign-in sections):
- Separate privileged accounts from daily-use accounts.
- Mark sensitive accounts with "Account is sensitive and cannot be delegated" to block Kerberos delegation attacks.
- Use Group Policy to deny Domain Admins sign-in to workstations and member servers (Deny logon locally / Deny logon through Remote Desktop Services).
- Do not allow admin accounts access to email or the internet.

## Contradictions / caveats
- The Administrator account cannot be locked out, which means lockout policies do not protect it from brute-force attacks — rename/disable it or rely on smart-card requirements.
- DES encryption for Kerberos is disabled by default from Windows Server 2008 R2 / Windows 7 onward; enabling "Use DES encryption types for this account" on any account will require a matching domain-policy change or authentication will fail.

## Reference notes
- [[ad-ds-understand-default-user-accounts]]
- [[ad-ds-understand-security-identifiers]]

## See also
- [[security-principals]]
- [[security-identifiers-sid]]
- [[krbtgt-reset]]
- [[read-only-domain-controller]]
- [[securing-active-directory]]
- [[fsmo-roles]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-understand-default-user-accounts|Active Directory Accounts]]
- [[ad-ds-understand-security-identifiers|Security Identifiers]]
<!-- crosslink:end -->
