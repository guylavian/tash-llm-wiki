---
title: Credential Theft and Attractive Accounts
type: entity
domain: active-directory
slug: credential-theft-and-attractive-accounts
summary: Attackers extract credentials from memory (pass-the-hash, pass-the-ticket, plaintext) targeting the most valuable accounts — EA/DA/BA members, VIPs, and privilege-attached service accounts — to propagate compromise across the entire forest.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Attractive-Accounts-for-Credential-Theft (Microsoft Learn — Attractive Accounts for Credential Theft, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Avenues-to-Compromise (Microsoft Learn — Avenues to Compromise, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Implementing-Least-Privilege-Administrative-Models (Microsoft Learn — Implementing Least-Privilege Administrative Models, fetched 2026-06-18)
  - kb:ad-ds-attractive-accounts-for-credential-theft
  - kb:ad-ds-avenues-to-compromise
  - kb:ad-ds-implementing-least-privilege-administrative-models
provenance_extracted: 20
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "pass-the-hash"
  - "pass-the-ticket"
  - "DCSync"
  - "lateral movement"
  - "credential harvesting via mimikatz"
tags: [security, ad-authn, troubleshooting]
status: draft
updated: 2026-07-02
---

# Credential Theft and Attractive Accounts

**Attackers extract credential hashes, Kerberos tickets, or plaintext passwords from a compromised host's memory, then replay them to move laterally — with the most valuable targets being accounts in EA, DA, BA, Domain Controllers, and service accounts with broad privilege.**

## Body

### How credential theft works

An attacker who gains SYSTEM or local Administrator access to any domain-joined machine can use freely available tools to extract credentials from LSASS memory: NTLM hashes (used for pass-the-hash), Kerberos tickets (used for pass-the-ticket), and in some configurations, plaintext passwords. These are then replayed as network logons to other computers. No further compromise of those targets is needed if they share the same local Administrator credentials.

### The attractive accounts hierarchy

Three tiers of attractive targets:

1. **Privileged domain accounts (EA/DA/BA members)** — members of Enterprise Admins, Domain Admins, and built-in Administrators can modify any object in the directory, add themselves to other privileged groups, and destroy the forest. Because DCs replicate any change to the AD DS database, a single DA account compromise effectively compromises all domain controllers.

2. **VIP accounts** — executives, legal, finance, and researchers with access to sensitive IP. Even without domain privilege, their data is the ultimate attacker goal. Theft of a VIP account may not require domain admin techniques; phishing or social engineering suffices.

3. **"Privilege-attached" accounts (service accounts)** — accounts with no DA membership but with local Administrator rights across dozens of servers. A single compromise cascades across the server population with the same effect as a DA breach.

### Activities that increase risk

- **Logging onto general workstations with privileged accounts.** A DA who signs into a workstation to "do admin tasks" leaves the DA hash in LSASS. If that workstation is later compromised, the DA credential is lost.
- **Browsing the internet with a privileged account.** A drive-by download installs a keylogger in the context of the privileged user; if the account is a DA, the entire forest is at risk.
- **Uniform local Administrator passwords across systems.** A hash extracted from one machine's SAM database authenticates against every other machine with the same password — the classic pass-the-hash pivot.
- **Overpopulation of privileged groups.** Each member is a new target available 24/7. DA access is needed only temporarily; permanent membership is unnecessary and dangerous.
- **Poorly secured DCs.** DCs hold the full AD DS database including the krbtgt hash. An attacker with DC access can issue golden tickets and forge Kerberos authentication for any account indefinitely.

### Mitigations (summary)

- Keep EA/DA/BA empty on a day-to-day basis; use just-in-time PIM/PAM for temporary membership.
- Enforce [[tiered-administration-model]] so privileged credentials never touch workstations.
- Use [[secure-administrative-hosts]] so privileged logons occur only on hardened, internet-isolated hosts.
- Deploy [[windows-laps]] to randomize local Administrator passwords per machine, eliminating the lateral movement vector.
- Use [[group-managed-service-accounts]] (gMSA) or [[delegated-managed-service-accounts]] (dMSA) for services — the system manages passwords, removing human-known service credentials.
- Enable smart card / MFA for all accounts with privileged group membership.
- UPN-hijacking attack: an attacker with write access to userPrincipalName attributes can temporarily swap a target's UPN, request a certificate from AD CS in the target's name, and authenticate as the target. Monitor cn, name, sAMAccountName, userPrincipalName, and userAccountControl attributes on privileged and VIP accounts.

## Contradictions / caveats

- Pass-the-hash mitigations (Protected Users group, Credential Guard) reduce the risk but do not eliminate credential theft if the attacker can install a keylogger or extract tickets from memory by other means.
- Renaming the built-in Administrator account does not prevent attacks on it; unique passwords per system are the effective control.
- "Privilege-attached" service accounts are often overlooked in privilege reviews because they are not in EA/DA/BA — yet a single compromise cascades across the entire server population they run on.

## Reference notes
- [[ad-ds-attractive-accounts-for-credential-theft]]
- [[ad-ds-avenues-to-compromise]]
- [[ad-ds-implementing-least-privilege-administrative-models]]

## See also
- [[securing-active-directory]]
- [[tiered-administration-model]]
- [[protected-accounts-and-groups]]
- [[monitoring-ad-for-compromise]]
- [[windows-laps]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-attractive-accounts-for-credential-theft|Attractive Accounts for Credential Theft]]
- [[ad-ds-avenues-to-compromise|Avenues to Compromise]]
- [[ad-ds-implementing-least-privilege-administrative-models|Implementing Least-Privilege Administrative Models]]
<!-- crosslink:end -->
