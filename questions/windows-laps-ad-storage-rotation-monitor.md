---
title: Where does Windows LAPS store the managed local-admin password in AD, which schema attributes are involved, and what should we monitor to verify rotation?
type: question
domain: active-directory
slug: windows-laps-ad-storage-rotation-monitor
status: draft
summary: Windows LAPS stores the managed local-admin (and DC DSRM) password on the device's computer object in AD, with an expiration time; the only schema attribute the corpus names verbatim is msLAPS-CurrentPasswordVersion (rollback detection). Verify rotation via the dedicated LAPS event-log channel, confirming the stored expiration time advances, and watching event 10031 for tamper protection.
sources:
  - web:https://learn.microsoft.com/windows-server/identity/laps/
  - wiki:windows-laps
  - wiki:laps-password-encryption
provenance:
  extracted: 9
  inferred: 2
  ambiguous: 0
question_tier: conceptual
updated: 2026-07-12
---

# Where does Windows LAPS store the managed local-admin password in AD, and how do you verify rotation is happening?

⚠️ **Provenance banner** — The mechanized `wikikb ask` gateway returned *no model answer* for this query (out-of-coverage: `support-kb` tier is not in the `conceptual` tier served for this domain), so the text below is a **corpus-synthesized** answer built from the wiki pages `[[windows-laps]]` / `[[laps-password-encryption]]` and the notes-first source `_sources/active-directory/windows-laps.md`. It is grounded in those pages only — it does **not** add attribute names or event IDs that are not present in the corpus. See the coverage caveat under *Schema attributes*.

## 1. Where the password is stored in AD

For **AD-joined** (or hybrid-joined devices that choose AD as the backup target) machines, Windows LAPS backs the managed local-admin password up **into Active Directory on the device's own computer object** (the computer account). Concretely:

- The background task generates a new policy-compliant random password on expiry and **stores it, together with an expiration time, on the computer object** in the directory. (`[[windows-laps]]`, `_sources/active-directory/windows-laps.md`)
- The backup **target is decided by join state, not by preference**: AD-joined-only → AD only; Entra-joined-only → Entra ID only; hybrid → either AD *or* Entra ID, but **never both at once**; Workplace-joined is unsupported. (`[[windows-laps]]`)
- The retrieval/access security in AD is layered: **ACLs** on the computer object's OU (granted with `Set-LapsADReadPasswordPermission` for read, `Set-LapsADResetPasswordPermission` for read/set of the expiration time) plus **optional CNG-DPAPI/AES-256 encryption** performed on the device before the value reaches AD. (`[[laps-password-encryption]]`)
- LAPS can also back up the **DSRM account** password on domain controllers (AD-only, and encryption is *required* for DSRM). (`[[windows-laps]]`)

## 2. Schema attributes involved

The `Update-LapsADSchema` cmdlet **extends the AD schema** to add the LAPS attribute set on the computer object (this is what enables storing the password/expiration and, on the latest schema, rollback detection). (`_sources/active-directory/windows-laps.md`, `[[windows-laps]]`)

The corpus names **only one** LAPS schema attribute verbatim:

- **`msLAPS-CurrentPasswordVersion`** — a GUID written to the computer object for **OS image rollback detection**. On Win 11 24H2 / Server 2025 only, if the stored version mismatches (e.g. after a VM snapshot revert, producing a "torn state" where the stored password no longer matches the device), LAPS rotates immediately. This attribute is only present after running the **latest** `Update-LapsADSchema`. (`[[windows-laps]]`, `_sources/active-directory/windows-laps.md`)

> **Coverage caveat (do not over-read):** The corpus describes LAPS as storing "the password + an expiration time" on the computer object and extending the schema via `Update-LapsADSchema`, but it does **not** enumerate the individual `msLAPS-*` attribute names (clear-text vs encrypted password, expiration-time, encrypted history, encrypted DSRM, etc.). Those attribute strings are **not present in this vault**, so they are intentionally omitted here rather than inferred. If you need the exact attribute LDAP display names, they live in the upstream Microsoft Learn "Windows LAPS" reference that the notes were distilled from — extend the wiki with that source before treating any specific attribute name as corpus-grounded.

Encryption and encrypted password **history** additionally require the **Windows Server 2016 Domain Functional Level** or later; below that, decrypted retrieval is unsupported. (`[[laps-password-encryption]]`)

## 3. What to monitor to verify rotation is actually happening

**Mechanism recap:** A hard-coded **once-per-hour background task** (not the Group Policy refresh cycle, and not Task Scheduler — unlike legacy LAPS) checks expiry, generates a new password, and writes it plus a new expiration time to the computer object. (`[[windows-laps]]`, `_sources/active-directory/windows-laps.md`)

Corpus-grounded monitoring signals:

1. **The dedicated LAPS event-log channel.** The notes list a "dedicated event log channel" as the management/monitoring surface for LAPS. Watching this channel for backup/rotation and error activity is the primary way to confirm the hourly task is running and succeeding. (`_sources/active-directory/windows-laps.md`)
2. **Confirm the stored expiration time advances.** Because every rotation writes a fresh password *with a new expiration time* on the computer object, the direct proof that rotation is occurring is that the expiration timestamp keeps moving forward on schedule. You can read it via the LAPS PowerShell module / ADUC properties dialog. (`[[windows-laps]]`)
3. **Event 10031 — tamper protection is live.** An unexpected password change on the managed account is rejected with `STATUS_POLICY_CONTROLLED_ACCOUNT` (0xC000A08B) and logged as **event 10031** in the LAPS channel. While this is a *tamper* signal rather than a *rotation-success* signal, its presence confirms LAPS is actively protecting the account and the agent is running. (`[[windows-laps]]`, `_sources/active-directory/windows-laps.md`)
4. **Rollback-triggered rotation (24H2+/Server 2025).** Monitoring for immediate rotations driven by `msLAPS-CurrentPasswordVersion` mismatch (e.g. after a VM snapshot revert) validates that the rollback-detection path works. (`[[windows-laps]]`)
5. **Decrypt/retrieval health.** Verify the authorized encryption principal (default: Domain Admins, via `ADPasswordEncryptionPrincipal`) can actually read *and* decrypt the stored password. A "decrypt fails / DFL too low" symptom means encryption needs the 2016 DFL — a config-monitoring check. (`[[laps-password-encryption]]`, `_sources/active-directory/windows-laps.md`)
6. **Force-and-confirm drill.** You can force a rotation with `Reset-LapsPassword` (local) or the CSP `ResetPassword` action, or force a policy cycle with `Invoke-LapsPolicyProcessing`, then confirm the expiration time refreshed — a good synthetic test during rollout. (`[[windows-laps]]`, `_sources/active-directory/windows-laps.md`)

## References

### RH ground-truth (Microsoft Learn / `web:`)
- `web:https://learn.microsoft.com/windows-server/identity/laps/` — Microsoft Learn, *Windows LAPS* (What is Windows LAPS?, Key concepts, passwords and passphrases, Get started, Migrate from legacy LAPS, Use Windows LAPS event logs). This is the notes-first source distilled into `_sources/active-directory/windows-laps.md` (PDF export of *windows-server identity*, fetched 2026-06-18).

### Wiki / vault (`wiki:`)
- [[windows-laps]] — `topics/windows-laps.md` (join-state rules, hourly task, DSRM, rollback detection, msLAPS-CurrentPasswordVersion).
- [[laps-password-encryption]] — `entities/laps-password-encryption.md` (AD ACL + CNG-DPAPI/AES-256 encryption model, 2016 DFL requirement, permission tiers).

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[windows-laps|Windows LAPS (Local Administrator Password Solution)]]
- [[laps-password-encryption|Windows LAPS — AD password encryption & access model]]
<!-- crosslink:end -->
