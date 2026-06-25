---
title: Windows LAPS (Local Administrator Password Solution)
type: topic
domain: active-directory
slug: windows-laps
summary: How Windows LAPS automatically rotates and backs up each device's local-admin (and DC DSRM) password to AD or Entra ID, the join-state rules that decide where, and the ACL + encryption security model for retrieval.
sources:
  - note:_sources/active-directory/windows-laps.md
  - web:https://learn.microsoft.com/windows-server/identity/laps/ (Microsoft Learn — Windows LAPS, fetched 2026-06-18)
provenance_extracted: 9
provenance_inferred: 2
provenance_ambiguous: 0
symptoms:
  - "event 10031"
  - "STATUS_POLICY_CONTROLLED_ACCOUNT"
  - "0xC000A08B"
tags: [security, directory-services, concept]
status: draft
updated: 2026-06-18
---

# Windows LAPS (Local Administrator Password Solution)

**A built-in Windows feature that automatically generates, rotates, and backs up
the password of a local administrator account (and a DC's DSRM account) into a
directory, so every machine has a unique, recoverable local-admin password.**

## Body

The core security win is that a single shared local-admin password across a fleet is
exactly what enables **pass-the-hash and lateral movement**; LAPS gives every device
a unique, rotated password instead. It is native to Windows (April 2023 update on
Win 10/11, Server 2019/2022; built into Server 2025) and is a **separate
implementation** from the deprecated legacy MSI "Microsoft LAPS" — legacy emulation
mode exists only to ease migration.

**Where the password goes is decided by join state**, not preference:
- AD-joined only → backs up only to **Windows Server Active Directory**.
- Entra-joined only → backs up only to **Microsoft Entra ID**.
- Hybrid-joined → either, but **never both at once**.
- Workplace-joined clients are unsupported.

A hard-coded **once-per-hour background task** (not the Group Policy refresh cycle —
unlike legacy LAPS, which ran as a GPO client-side extension) checks expiry,
generates a policy-compliant random password, and stores it with an expiration time
in the directory. Policy is delivered via the **Intune CSP** (preferred for Entra)
or **Group Policy** (preferred for AD). Admins can force rotation with
`Reset-LapsPassword` or the CSP, and force a cycle with `Invoke-LapsPolicyProcessing`.

Retrieval security differs by directory: Entra ID uses **RBAC** (Global Admin / Cloud
Device Admin / Intune Admin can read clear text); AD uses **ACLs plus optional
encryption** — see [[laps-password-encryption]]. Storing local-admin passwords in AD
without encryption is supported but weak; enabling encryption is the recommended
posture (inferred — Microsoft "highly recommends" it and gates history/DSRM on it).

LAPS can also manage the **DSRM account** on domain controllers (AD-only, encryption
required), which ties it to [[ad-forest-recovery]] — DSRM credentials are needed for
authoritative restores. It is disabled in safe mode/DSRM boots, rotates the password
after it detects an interactive sign-in (bounds clear-text exposure), and protects
the managed account from tampering (rejected changes raise
`STATUS_POLICY_CONTROLLED_ACCOUNT` / event 10031).

## Contradictions / caveats

- Encryption and encrypted password **history** require the **Windows Server 2016
  Domain Functional Level** or later; below that, decrypt is unsupported.
- **OS image rollback** (e.g. VM snapshot revert) creates a "torn state" where the
  stored password no longer matches the device. Rollback detection
  (`msLAPS-CurrentPasswordVersion`) fixes this on Win 11 24H2 / Server 2025 only, and
  only after `Update-LapsADSchema` extends the schema; otherwise recovery needs a
  manual rotation or the machine-account reset.

## See also
- [[laps-password-encryption]]
- [[securing-active-directory]]
- [[active-directory-overview]]
- [[active-directory-implementation-review]]
