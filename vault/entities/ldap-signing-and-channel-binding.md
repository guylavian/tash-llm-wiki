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
  - "web:https://learn.microsoft.com/en-us/answers/questions/1005680/ldaps-with-sasl-external-on-port-636-active-direct (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1130584/ldap-signing-on-domain-controllers (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1159842/ldap-server-signing-requirements-and-sasl-gss-spne (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1388935/ldap-is-used-over-port-389-although-ldaps-is-confi (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1161291/how-to-fix-00000003-ldaperr-dsid-0c060469-comment (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1159767/mvc-application-hosted-in-dmz-server-throwing-ldap (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 28
provenance_inferred: 5
provenance_ambiguous: 1
symptoms:
  - "Event ID 2886 — Domain controller accepts unsigned LDAP communications"
  - "Event ID 2887 — Unsigned LDAP binds detected (client source logged)"
  - "Event ID 2888 — LDAP signing disabled (highly vulnerable)"
  - "Event ID 3039 — Client does not support channel binding token (CBT)"
  - "Event ID 3040 — Channel binding token mismatch (SSL/TLS cert issue)"
  - "LdapErr: DSID-0C0905F0.*Invalid Authentication method — SASL EXTERNAL bind fails on port 636 (LDAPS) only"
  - "LdapErr: DSID-0C060469.*Error decrypting ldap message — reported cert-chain issue on AD LDS/ADAM"
tags: [ad-authn, security, concept]
status: draft
updated: 2026-07-25
graph_community: "Securing Active Directory (best practices)"
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

## Community Q&A (upstream) — operational details and field error signatures

> Microsoft Q&A community threads, not Microsoft support statements. Answerer
> roles are noted per claim.

**Policy changes apply without a DC restart.** An MVP answer, citing current
Microsoft Learn policy-setting pages, confirms that both "Domain controller:
LDAP server signing requirements" and "Domain controller: LDAP server channel
binding token requirements" take effect immediately when changed via Local
Security Policy/GPO — no DC restart needed. (Whether the legacy
`LdapEnforceChannelBinding` registry-key method also needs a restart is **not**
established by this thread or by the cited MS Learn notes — it only confirms the
two GPO-based settings do not (ambiguous).) (web:1130584)

**Enforcing signing rejects SASL GSS-SPNEGO on port 389 too.** A Microsoft
Moderator confirms that once "Require signing" is enabled on the DC, **all**
LDAP connections on port 389 that aren't signed get rejected — including
SASL GSS-SPNEGO binds, not just simple binds. Event IDs 2887/2888/2889 should
be reviewed and any non-compliant applications remediated before enforcing
(web:1159842).

**Enforcing "Require signing" + channel binding does not move built-in Windows
tools to LDAPS.** A Microsoft Moderator and two MVP/Volunteer-Moderator
answers agree: native Windows LDAP clients — `dsa.msc` (Active Directory
Users and Computers), `Get-GPOReport`, and other MMC snap-ins — stay hardcoded
to port 389 (using signing) even after the DC is configured to require
signing and "Always" channel binding on 636. There is no supported way to
force these specific tools onto LDAPS; only applications that are explicitly
programmed/configured to use LDAPS (or client-initiated StartTLS) actually
move traffic to port 636 or use TLS on 389 (web:1388935).

**Field signature — SASL EXTERNAL fails on port 636 but works on port 389 with
StartTLS.** A thread configuring certificate-based SASL EXTERNAL binds over
LDAPS reports `ldap_sasl_interactive_bind_s: Authentication method not
supported (7)` / `00002027: LdapErr: DSID-0C0905F0, comment: Invalid
Authentication method` specifically on port 636, while the identical bind
(same client cert, same CA trust) succeeds via StartTLS on port 389. Debug
logs confirmed the TLS handshake and certificate verification completed on
both sides before the bind failure. **The thread never reaches a resolution**
— community replies narrow the generic Windows error code to
`CRYPT_E_NO_VERIFY_USAGE_DLL` (web:1005680) but explicitly note it carries no
diagnostic detail, and the last replies are still requesting more trace data
(web:1005680) **(ambiguous)** — treat "SASL EXTERNAL over LDAPS" failures as
an open, unconfirmed field report, not a documented AD limitation.

**Field signature — "Error decrypting ldap message" (DSID-0C060469) against
AD LDS.** Reported against an AD LDS (ADAM) instance, not a DC:
`00000003: LdapErr: DSID-0C060469, comment: Error decrypting ldap message`.
A Microsoft Moderator's single, unconfirmed reply attributes this to a
certificate problem — check that the root certificate is installed correctly
on the server; the thread has no follow-up confirming the fix
(web:1161291).

**Field signature — "LDAP server is unavailable" for some users from a DMZ
app.** An MVC application hosted in a DMZ threw "LDAP server is unavailable"
for a subset of users only (others, on the internal network, worked fine). A
Microsoft Moderator's single reply attributes this to a network/firewall gap
between the DMZ and the domain controllers and points to the standard AD
trust/domain firewall port-requirements guidance; unconfirmed by the poster
(web:1159767).

## Contradictions / caveats

- Windows Server 2025 enforces signing by default **only for new installs**; in-place upgrades keep prior policy.
- Simple LDAP binds on port 389 remain rejected when signing is required — applications that rely on cleartext simple binds must be migrated to LDAPS (port 636) or Kerberos/NTLM with signing.
- Channel binding does not protect plain port-389 connections; it only applies to SSL/TLS sessions.
- The three unconfirmed community field reports above (SASL EXTERNAL on 636,
  the AD LDS decrypt error, and the DMZ "server unavailable" error) are
  included because they are the concrete error signatures operators actually
  search for — but none has a corpus-confirmed root cause. Both the
  "certificate problem" and "network/firewall" diagnoses are single-reply,
  unconfirmed hypotheses (inferred).

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
