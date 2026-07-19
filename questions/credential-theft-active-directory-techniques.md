---
origin: eval-cohort
title: How attackers target credential theft in Active Directory
type: question
domain: active-directory
slug: credential-theft-active-directory-techniques
summary: Attackers extract credential hashes, Kerberos tickets, or plaintext from LSASS memory after gaining SYSTEM/Admin access to a domain-joined host, then replay them laterally (pass-the-hash, pass-the-ticket) — targeting privileged domain accounts (EA/DA/BA), VIP accounts, and privilege-attached service accounts — to escalate to full forest compromise.
sources:
  - note: reference/active-directory/ad-ds-attractive-accounts-for-credential-theft.md
  - note: reference/active-directory/ad-ds-avenues-to-compromise.md
  - note: reference/active-directory/ad-ds-monitoring-active-directory-for-signs-of-compromise.md
provenance:
  extracted: 14
  inferred: 3
  ambiguous: 0
question_tier: conceptual
tags: [users]
status: draft
updated: 2026-07-12
aliases: [pass-the-hash, pass-the-ticket, credential theft AD, AD lateral movement]
---

# How attackers target credential theft in Active Directory

**Credential theft in AD follows a four-stage pattern: gain privileged access to a host → extract credential material from LSASS memory → replay harvested credentials laterally → escalate to forest-wide compromise via privileged domain accounts (inferred — composite framing of the reference material).**

## Body

### Stage 1: Initial foothold — gaining SYSTEM/Admin on a domain-joined host

Attackers first compromise one or two hosts via unpatched vulnerabilities, weak antimalware, misconfiguration, or application flaws (SQLi, XSS) (`ad-ds-avenues-to-compromise.md:21-25`). Common entry points:

- **Incomplete patching** — Windows systems may be patched, but non-Windows, COTS apps, and network devices are left unpatched, creating entry points (`ad-ds-avenues-to-compromise.md:54-59`).
- **Outdated applications and OS** — legacy systems force AD to store weaker hashes (LM) or reversibly encrypted passwords domain-wide (`ad-ds-avenues-to-compromise.md:66-73`).
- **Misconfiguration** — WFAS disabled, UAC disabled on servers, excessive local admin rights granted (`ad-ds-avenues-to-compromise.md:78-82`).
- **Antivirus gaps** — server populations are less consistently protected than workstations; 94% of data compromises involved servers (`ad-ds-avenues-to-compromise.md:48-51`).

### Stage 2: Credential extraction — LSASS memory dumping

Once the attacker holds SYSTEM or local Administrator on a machine, they use freely available tooling to extract credentials from **LSASS memory** (`ad-ds-attractive-accounts-for-credential-theft.md:17`). The extracted material is one of three forms:

- **NTLM hashes** — used for pass-the-hash (PTH) attacks: replaying the hash as a network logon to authenticate as that user *without knowing the password*.
- **Kerberos tickets** (TGT / service tickets) — used for pass-the-ticket (PTT): injecting the ticket into a new logon session on a target machine.
- **Plaintext passwords** — available when the Windows system stores reversibly encrypted credentials or through keylogging (e.g., the attacker installs a keystroke logger that captures credentials as they are typed).

Even without credential-dumping tools, an attacker with privileged access can install keyloggers capturing every keystroke (`ad-ds-avenues-to-compromise.md:111`).

### Stage 3: Lateral movement — replaying credentials across systems

Harvested credentials are replayed as network logons against other machines:

- **Pass-the-hash (PTH):** the extracted NTLM hash is presented directly. If the target shares the same local Administrator credentials (same username + password), the logon succeeds instantly (`ad-ds-avenues-to-compromise.md:116-120`). *(This is why uniform local admin passwords across systems is the single most dangerous configuration — one SAM extraction compromises every machine (inferred from the reference guidance).)* (`credential-theft-and-attractive-accounts:3`)
- **Pass-the-ticket (PTT):** Kerberos tickets are injected into the local session and reused on other machines. A stolen TGT authenticates against any resource in the domain.

The attacker's goal at this stage is to reach machines where **high-value accounts have logged on**, and to harvest *those* credentials — particularly domain-privileged ones (`ad-ds-attractive-accounts-for-credential-theft.md:17-18`).

### Stage 4: Target selection — what attackers are looking for

Attackers specifically target three tiers of accounts (`ad-ds-attractive-accounts-for-credential-theft.md:19-33`):

1. **Privileged domain accounts (EA/DA/BA members)** — Enterprise Admins, Domain Admins, and built-in Administrators. A single compromised DA hash authenticates against every DC in the domain. Because DCs replicate all changes, a DA compromise effectively compromises the entire forest.

2. **"Privilege-attached" accounts (service accounts)** — domain accounts with no DA membership but local Administrator rights across dozens or hundreds of servers. These are often overlooked in privilege reviews. A single such account compromise cascades across the entire server population with the same effect as a DA breach (`ad-ds-attractive-accounts-for-credential-theft.md:87-88`).

3. **VIP accounts** — executives, legal, finance, researchers. Even without domain privilege, their data is the ultimate goal. Phishing/social engineering suffices; no advanced techniques needed (`ad-ds-attractive-accounts-for-credential-theft.md:21-32`).

### Activities that enable credential theft

Microsoft identifies specific admin behaviors that dramatically increase risk (`ad-ds-attractive-accounts-for-credential-theft.md:40-75`):

- **Logging onto unsecured workstations with privileged accounts.** A DA who signs into a compromised workstation leaves the DA hash in LSASS (`ad-ds-attractive-accounts-for-credential-theft.md:44`).
- **Browsing the internet with a highly privileged account.** A drive-by download installs malware in the privileged user's context; if the account holds DA privileges, the entire forest is at risk (`ad-ds-attractive-accounts-for-credential-theft.md:62-65`).
- **Uniform local Administrator passwords.** A hash extracted from one SAM database authenticates against every machine with the same password (`ad-ds-attractive-accounts-for-credential-theft.md:67-68`).
- **Overpopulated privileged groups.** Each permanent EA/DA/BA member is a target available 24/7. The actual need for DA privileges is temporary and infrequent (`ad-ds-attractive-accounts-for-credential-theft.md:70-71`).
- **Poorly secured DCs.** DCs hold the full AD DS database including the krbtgt hash. Compromise grants golden-ticket capability and indefinite persistence (`ad-ds-attractive-accounts-for-credential-theft.md:73-74`).

### Advanced post-exploitation: DCSync and Golden Tickets

Once attackers hold a sufficiently privileged account:

- **DCSync** — using DRSUAPI replication to impersonate a DC and request account password hashes from the domain, including the krbtgt account, without ever logging on to a DC (`monitoring-ad-for-compromise:4`).
- **Golden Ticket** — forging a Kerberos TGT using the stolen krbtgt hash, granting authentication as *any* account for as long as the forged ticket is valid (`credential-theft-and-attractive-accounts:2`).
- **UPN hijacking** — attackers with write access to `userPrincipalName` swap a target's UPN, request an AD CS certificate in their name, and authenticate as the target. Monitor attribute changes on `cn`, `name`, `sAMAccountName`, `userPrincipalName`, `userAccountControl` (`credential-theft-and-attractive-accounts:5`).

### Defensive mitigations

The wiki's [[securing-active-directory]] page organizes the Microsoft defensive model into four moves:

1. **Reduce the attack surface** — empty EA/DA/BA day-to-day; harden DCs (Server Core, AppLocker, no internet); isolate or decommission legacy systems; unique local admin passwords per machine via [[windows-laps]] (`reducing-ad-attack-surface:6-7`).
2. **Enforce least-privilege + tiered administration** — [[tiered-administration-model]] prevents privileged credentials from touching workstations; [[secure-administrative-hosts]] (hardened, internet-isolated jump hosts) are the only machines where admin logons occur (`securing-active-directory:2`).
3. **Protect privileged credentials** — [[group-managed-service-accounts]] (gMSA) and [[delegated-managed-service-accounts]] (dMSA) eliminate human-managed service passwords; Protected Users group and Credential Guard reduce LSASS exposure (`securing-active-directory:3`).
4. **Monitor and plan for compromise** — alert on Event 4964 (DA logon to workstation), Event 4728 (DA group change), Event 5136 (attribute modification on VIP accounts), DCSync attempts. Establish baselines for failed logons (4625) and process creation on DCs (4688). Pre-build [[ad-forest-recovery]] capability (`monitoring-ad-for-compromise:7`).

## See also
- [[credential-theft-and-attractive-accounts]]
- [[securing-active-directory]]
- [[reducing-ad-attack-surface]]
- [[tiered-administration-model]]
- [[secure-administrative-hosts]]
- [[monitoring-ad-for-compromise]]
- [[protected-accounts-and-groups]]
- [[windows-laps]]
- [[group-managed-service-accounts]]
- [[delegated-managed-service-accounts]]
- [[ad-forest-recovery]]

## References

### RH ground-truth (MS Learn reference notes)
- `ad-ds-attractive-accounts-for-credential-theft.md` — Attractive Accounts for Credential Theft
- `ad-ds-avenues-to-compromise.md` — Avenues to Compromise
- `ad-ds-monitoring-active-directory-for-signs-of-compromise.md` — Monitoring Active Directory for Signs of Compromise
- `ad-ds-reducing-the-active-directory-attack-surface.md` — Reducing the Active Directory Attack Surface
- `ad-ds-best-practices-for-securing-active-directory.md` — Best practices for securing Active Directory

### Wiki pages cited
- [[credential-theft-and-attractive-accounts]]
- [[securing-active-directory]]
- [[reducing-ad-attack-surface]]
- [[monitoring-ad-for-compromise]]
