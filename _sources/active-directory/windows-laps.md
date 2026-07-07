# Raw note — Windows LAPS (Local Administrator Password Solution)

- Source: Microsoft Learn, "What is Windows LAPS?", "Key concepts in Windows LAPS",
  "Windows LAPS passwords and passphrases", "Get started…", "Migrate to Windows
  LAPS from legacy LAPS", "Use Windows LAPS event logs"
  (web:https://learn.microsoft.com/windows-server/identity/laps/, distilled from the
  *windows-server identity* PDF export, fetched 2026-06-18).
- Status: notes-first ground truth (paraphrased — no verbatim) for the
  `active-directory` domain.

## What it is

Windows LAPS is a built-in Windows feature that **automatically rotates and backs
up the password of a local administrator account** on devices joined to Windows
Server Active Directory or Microsoft Entra ID. It can also back up the **DSRM
(Directory Services Restore Mode) account password** on domain controllers.

- Native to Windows since the April 11 2023 update (Win 10/11, Server 2019/2022)
  and built into Server 2025. **Distinct from** the deprecated legacy MSI "Microsoft
  LAPS" product (legacy is deprecated as of Win 11 23H2; install blocked on newer OS).
- Free; backing up to AD needs no extra license, backing up to Entra ID needs Entra
  ID Free or higher.

## Why (benefits)

- Defeats **pass-the-hash / lateral-traversal** by ensuring every machine's local
  admin password is unique and rotated.
- Recover otherwise-inaccessible devices; safer help-desk hand-off.
- Fine-grained access model (ACLs + optional encryption in AD; RBAC in Entra ID).

## Backup targets & join-state rules

- Entra-joined only → can back up **only to Entra ID**.
- AD-joined only → can back up **only to AD**.
- Hybrid-joined → either AD **or** Entra ID (not both at once).
- Workplace-joined clients are **not** supported.

## Key concepts / architecture

- Components on the managed device: `laps.dll` (core), `lapscsp.dll` (CSP),
  `lapspsh.dll` (PowerShell). Policy via **Intune CSP** (preferred for Entra) or
  **Group Policy** (preferred for AD).
- A **background task wakes once per hour** (hard-coded, not Task Scheduler, not the
  GP refresh cycle — unlike legacy LAPS which was a GPO client-side extension). It
  generates a new policy-compliant random password on expiry, stores it + an
  expiration time in the directory, and rotates automatically.
- Manual rotation: `Reset-LapsPassword` (local), the CSP ResetPassword action, or
  editing the expiration time in AD. Force a cycle with `Invoke-LapsPolicyProcessing`.

## AD password security (two/three layers)

1. **ACLs** on the computer object's OU — `Set-LapsADReadPasswordPermission` (read)
   and `Set-LapsADResetPasswordPermission` (read/set expiry).
2. **Encryption** (recommended) — needs the **Windows Server 2016 Domain Functional
   Level** or later; uses CNG DPAPI / AES-256; encrypts the password on the device
   *before* it reaches AD, decryptable by **one** security principal
   (`ADPasswordEncryptionPrincipal`; defaults to Domain Admins). For multiple
   readers, wrap them in a group.
3. **Encrypted password history** — only when encryption is on; device needs SELF
   read permission (`Set-LapsADComputerSelfPermission`).

Suggested permission tiers: read/set *expiry* (sensitive but nondestructive) →
read *password* (reserve for Domain Admins) → *decrypt* (reserve for Domain Admins).

## Other behaviors

- **DSRM** backup: AD-only, encryption required. Recoverable as long as ≥1 DC in the
  domain is reachable; otherwise restore DSRM passwords from backups.
- **Password reset after authentication** — rotates the password once it detects the
  account was used to sign in (bounds clear-text exposure); configurable grace
  period. Not supported for DSRM.
- **Tampering protection** — rejects unexpected password changes with
  `STATUS_POLICY_CONTROLLED_ACCOUNT` (0xC000A08B), logged as event 10031.
- **Disabled in safe mode / DSRM / abnormal boot.**
- **OS image rollback detection** (Win 11 24H2 / Server 2025) — stores a GUID in
  `msLAPS-CurrentPasswordVersion`; on mismatch (e.g. VM snapshot revert) rotates
  immediately. Requires running the latest `Update-LapsADSchema`. AD-only.
- Management/monitoring: ADUC properties dialog, a dedicated **event log channel**,
  and the LAPS PowerShell module.

## Symptoms (feed the review MOC)

- Event **10031** in the LAPS channel → blocked tamper attempt on the managed account.
- IT admin can't sign in with the stored LAPS password after a VM snapshot
  revert → "torn state"; fixed by rollback detection (24H2+) or manual rotation.
- Decrypt fails / "DFL too low" → encryption needs the 2016 DFL or later.
