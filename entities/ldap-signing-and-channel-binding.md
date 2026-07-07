---
title: LDAP Signing and Channel Binding
type: entity
domain: active-directory
slug: ldap-signing-and-channel-binding
summary: LDAP signing cryptographically verifies message integrity over LDAP; channel binding ties the application-layer auth session to the SSL/TLS tunnel, together preventing replay and man-in-the-middle attacks against domain controllers.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing (Microsoft Learn — LDAP signing for Active Directory Domain Services on Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/configure-ldap-signing-certificates (Microsoft Learn — Configure certificates for LDAP over SSL in Active Directory Domain Services, fetched 2026-06-18)
  - kb:ad-ds-ldap-signing
  - kb:ad-ds-configure-ldap-signing-certificates
provenance_extracted: 22
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "Event ID 2886 — Domain controller accepts unsigned LDAP communications"
  - "Event ID 2887 — Unsigned LDAP binds detected (client source logged)"
  - "Event ID 2888 — LDAP signing disabled (highly vulnerable)"
  - "Event ID 3039 — Client does not support channel binding token (CBT)"
  - "Event ID 3040 — Channel binding token mismatch (SSL/TLS cert issue)"
tags: [ad-authn, security, concept]
status: draft
updated: 2026-07-02
---

# LDAP Signing and Channel Binding

**LDAP signing and channel binding are complementary hardening controls that protect domain controller LDAP traffic from tampering, replay, and session-hijacking attacks.**

## How each control works

**LDAP signing** digitally signs LDAP messages using SASL mechanisms (Negotiate, Kerberos, NTLM, Digest). When enforced, the domain controller rejects any SASL bind that does not request signing and any simple bind over an unencrypted connection. This guards against replay attacks — where intercepted Kerberos tickets are replayed — and man-in-the-middle packet modification.

**LDAP channel binding** uses Channel Binding Tokens (CBTs) to cryptographically bind the application-layer authentication to the underlying SSL/TLS session. This prevents an attacker positioned between client and DC from hijacking the encrypted tunnel even when SSL is in use. The process:
1. Client establishes TLS to the DC on port 636 (LDAPS) or port 3269 (global catalog LDAPS).
2. A CBT is derived from the TLS session parameters.
3. Client presents the CBT during authentication.
4. DC validates CBT match; mismatch or absence causes rejection.

## Default behavior by version

| Version | LDAP signing default | Channel binding default |
|---|---|---|
| Windows Server 2019 and earlier | Optional (unsigned accepted) | Never (CBT not required) |
| Windows Server 2025 (new install) | Required (enforced via policy) | When supported |

Upgrade installations of Windows Server 2025 preserve the prior settings to avoid disruption. (inferred) Administrators upgrading from 2019 must manually tighten the policy after verifying client compatibility.

The 2020 Microsoft advisory (KB4520412) announced staged enforcement changes for LDAP channel binding and signing across all supported versions. Environments that had not already enforced signing were expected to receive default changes through cumulative updates.

## LDAPS certificate requirements

To use LDAPS (port 636), a DC certificate must:
- Include **Server Authentication** EKU (OID `1.3.6.1.5.5.7.3.1`).
- Carry the DC's FQDN in the Subject CN or Subject Alternative Name DNS entry.
- Have its private key in the Local Computer or NTDS store using the Schannel CSP.
- Be issued by a CA trusted by both DC and clients.

Active Directory checks the NTDS store first; certificates placed there are detected without a DC restart.

## Event IDs and monitoring

Monitor **Directory Service** events in Event Viewer:

| Event ID | Meaning | Action |
|---|---|---|
| 2886 | Signing not required | Plan enforcement after auditing clients |
| 2887 | Unsigned bind detected | Identify client; configure LDAPS or signing |
| 2888 | Signing disabled | Enable immediately |
| 2889 | Signed request processed | Normal — no action |
| 3039 | Client lacks CBT support | Update client or adjust policy temporarily |
| 3040 | CBT token mismatch | Verify SSL/TLS certificate and network path |
| 3041 | CBT successful | Normal — no action |

Enable auditing via Advanced Audit Policy → Audit Directory Service Access, then monitor 2886–2889 and 3039–3041 before enforcing.

## Migration path (inferred)

1. Deploy audit mode: set signing to "Negotiate signing" and channel binding to "When supported."
2. Review events 2887 and 3039 to enumerate non-compliant clients.
3. Update or isolate legacy clients that cannot support SASL signing or CBTs.
4. Enforce: set signing to "Require signing" and channel binding to "Always."

## Contradictions / caveats

- Windows Server 2025 enforces signing by default **only for new installs**; in-place upgrades keep prior policy.
- Simple LDAP binds on port 389 remain rejected when signing is required — applications that rely on cleartext simple binds must be migrated to LDAPS (port 636) or Kerberos/NTLM with signing.
- Channel binding does not protect plain port-389 connections; it only applies to SSL/TLS sessions.

## Reference notes
- [[ad-ds-ldap-signing]]
- [[ad-ds-configure-ldap-signing-certificates]]

## See also
- [[active-directory-overview]]
- [[securing-active-directory]]
- [[ad-ds-maximum-limits]]
- [[ad-certificate-services]]
- [[advanced-audit-policy]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-ldap-signing|LDAP signing for Active Directory Domain Services on Windows Server]]
- [[ad-ds-configure-ldap-signing-certificates|Configure certificates for LDAP over SSL in Active Directory Domain Services]]
<!-- crosslink:end -->
