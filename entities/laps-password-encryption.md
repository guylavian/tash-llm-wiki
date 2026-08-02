---
title: Windows LAPS — AD password encryption & access model
type: entity
domain: active-directory
slug: laps-password-encryption
summary: The AD-side LAPS retrieval security model — ACLs on the computer OU plus optional CNG-DPAPI/AES-256 encryption to a single security principal, the 2016-DFL requirement, encrypted history, and the layered read/decrypt permission tiers.
sources:
  - note:_sources/active-directory/windows-laps.md
  - web:https://learn.microsoft.com/windows-server/identity/laps/laps-concepts (Microsoft Learn — Key concepts in Windows LAPS, fetched 2026-06-18)
provenance_extracted: 7
provenance_inferred: 1
provenance_ambiguous: 0
tags: [security, directory-services]
status: draft
updated: 2026-06-18
graph_community: "Active Directory — Domain Services Overview"
---

# Windows LAPS — AD password encryption & access model

**When LAPS backs passwords to Active Directory, it secures them with ACLs on the
computer object and, recommended, CNG-DPAPI/AES-256 encryption decryptable by exactly
one security principal.**

## Body

Passwords are stored on the **computer object**. Two (optionally three) layers guard
them:

1. **ACLs** inherited from the computer's OU. Grant read with
   `Set-LapsADReadPasswordPermission`; grant read/set of the expiration time with
   `Set-LapsADResetPasswordPermission`.
2. **Encryption** (recommended). The password is encrypted **on the managed device
   before it reaches AD**, using CNG DPAPI with **AES-256**, against a **single**
   security principal set via `ADPasswordEncryptionPrincipal` (defaults to the
   domain's Domain Admins). LAPS deliberately supports only one principal (multi-
   principal CNG DPAPI bloats the buffer) — to grant several readers, encrypt to a
   **wrapper group**. The authorized principal **cannot be changed after** a password
   is encrypted.
3. **Encrypted password history** — only available when encryption is on; the device
   needs SELF read permission (`Set-LapsADComputerSelfPermission`).

Think of access as concentric tiers: read/set *expiry* (sensitive but
nondestructive — at worst forces extra rotations) → read the *password* (reserve for
Domain Admins) → *decrypt* (reserve for Domain Admins). Tighten tiers for sensitive
machines (e.g. executive laptops) versus front-line devices.

## Contradictions / caveats

- **Requires the Windows Server 2016 Domain Functional Level or later.** Below that,
  Microsoft does not support retrieving decrypted passwords, and behavior is
  undefined if pre-2016 DCs were ever promoted into the domain.
- DSRM-account backup on DCs **requires** encryption (clear-text DSRM backup is not
  offered) — this is the LAPS dependency that [[ad-forest-recovery]] relies on.
- Microsoft recommends **never** granting a managed device permission to decrypt any
  device's password, including its own (inferred constraint stated as a hard
  recommendation in the source).

## See also
- [[windows-laps]]
- [[fine-grained-password-policies]]
