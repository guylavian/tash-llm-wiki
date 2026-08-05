---
title: "NTFS File/Folder Deletion and Move Auditing on a Windows Network Drive"
slug: ntfs-file-deletion-audit-network-drive
status: draft
domain: windows-server
summary: "How to configure Windows NTFS auditing to track who deletes or moves folders/files on a network share, using Advanced Audit Policy, SACLs, and Event ID 4663/4660/4656."
provenance:
  extracted: 12
  inferred: 3
  ambiguous: 0
sources:
  - reference/windows-server/administration-auditpol-resourcesacl.md
  - reference/active-directory/solution-guides-deploy-security-auditing-with-central-audit-policies-demonstration-steps.md
  - reference/active-directory/solution-guides-plan-for-file-access-auditing.md
  - reference/active-directory/ad-ds-advanced-audit-policy-configuration.md
  - reference/active-directory/ad-ds-monitoring-active-directory-for-signs-of-compromise.md
  - _claude/skills/windows-eventlog/references/object-access.md
  - _claude/skills/admx-gpo/references/audit-policy-to-eventid.md
---

# NTFS File/Folder Deletion and Move Auditing on a Windows Network Drive

> **Yes, you can see who deleted or moved a folder on a Windows NTFS network drive.**  
> It requires two things: (1) enabling the **Audit File System** policy, and (2) configuring a **SACL** (System Access Control List) on the folder(s) you want to monitor.

---

## How it works (two-part configuration)

Windows NTFS auditing is a **two-layer** system:

| Layer | What | Where to set it |
|-------|------|----------------|
| **1. Audit Policy** | Tells Windows "start auditing file system events" — but alone does nothing without a SACL | Advanced Audit Policy in GPO or `auditpol.exe` |
| **2. SACL** | Tells Windows "for *this specific folder*, audit *these operations* by *these users*" | Folder Properties → Security → Advanced → Auditing, **or** Global Object Access Auditing via GPO |

Both layers must be in place — without the SACL, no events fire [ref:`ad-ds-advanced-audit-policy-configuration.md` (extracted)].

---

## Step-by-step setup

### Step 1: Enable the audit policy

You have two options:

#### Option A: Via Group Policy (recommended for domain-joined servers)

1. Open **Group Policy Management Console** (GPMC)
2. Create or edit a GPO linked to the file server's OU
3. Navigate to:  
   `Computer Configuration → Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Object Access`
4. Double-click **Audit File System** → check **Configure the following audit events** → check both **Success** and **Failure** → OK
5. (Recommended) Also enable **Audit Handle Manipulation** (same path) — Success + Failure — needed to correlate Event 4656/4658 with 4663/4660 [ref:`ad-ds-advanced-audit-policy-configuration.md` §Audit Handle Manipulation (extracted)]
6. Run `gpupdate /force` on the file server

[ref:`solution-guides-deploy-security-auditing-with-central-audit-policies-demonstration-steps.md` lines 43-45 (extracted)]

#### Option B: Via `auditpol` (ad-hoc, no GPO)

Run as Administrator on the file server:

```cmd
auditpol /set /subcategory:"File System" /success:enable /failure:enable
auditpol /set /subcategory:"Handle Manipulation" /success:enable /failure:enable
```

[ref:`ad-ds-advanced-audit-policy-configuration.md` (extracted)]

### Step 2: Configure the SACL on the folder

#### Option A: Per-folder SACL (recommended for specific important folders)

1. Right-click the folder → **Properties** → **Security** tab → **Advanced**
2. Go to the **Auditing** tab → **Add**
3. **Select a principal**: `Everyone` (or a specific group like `Domain Users`)
4. **Type**: `Success` (and optionally `Failure`)
5. **Permissions**: Check **Delete** and **Delete subfolders and files** (and **Full control** if you want all operations)
6. **Applies to**: `This folder, subfolders and files` (or as needed)
7. OK → Apply

This sets a SACL on the folder that audits DELETE operations against it [ref:`_claude/skills/windows-eventlog/references/object-access.md` lines 194-248 (extracted)].

To also capture **moves** (which are internally a copy + delete), auditing DELETE on the target folder is sufficient — when a file/folder is moved to a new location on the same volume, the source is deleted.

> **Important:** Moving a folder **within the same volume** is a metadata operation — the file is deleted from its original location. Moving **across volumes** is a copy + delete. Both produce DELETE audit events at the source location.

#### Option B: Global Object Access Auditing via GPO (applies to ALL files on the server)

1. In the same GPO, navigate to:  
   `Computer Configuration → Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Global Object Access Auditing → File system`
2. Check **Define this policy setting** → **Configure**
3. Add an auditing entry for `Everyone` with **Full control** → OK
4. This applies the SACL to **every file and folder** on the server automatically [ref:`ad-ds-advanced-audit-policy-configuration.md` lines 1697-1709 (extracted)]

> ⚠ **Volume warning:** Global Object Access Auditing generates events for *every* file access on the server — use it sparingly on file servers with heavy I/O, or filter to a specific user/group rather than Everyone.

---

## What to look for in the Security Event Log

Open **Event Viewer** → **Windows Logs** → **Security** on the file server.

### Event 4663 — An attempt was made to access an object (DELETE)

This is the primary event for a **file/folder delete**. For a move on the same volume, the original location produces a DELETE 4663.

```xml
An attempt was made to access an object.
Subject:
   Security ID:   ACME\john.doe
   Account Name:  john.doe
   Logon ID:      0x1f41e
Object:
   Object Server: Security
   Object Type:   File
   Object Name:   D:\SharedFolder\ImportantProject\
   Handle ID:     0x40
Process Information:
   Process Name:  C:\Windows\explorer.exe
Access Request Information:
   Accesses:      DELETE
   Access Mask:   0x10000
```

[ref:`_claude/skills/windows-eventlog/references/object-access.md` lines 207-225 (extracted)]

The key field is `Accesses: DELETE` combined with the `Object Name` (the full path) and the `Account Name` (who did it).

### Event 4660 — An object was deleted

Fires when the object is actually gone, but **doesn't include the object name** — you must correlate `Handle ID` to the matching 4656 or 4663 event to know what was deleted [ref:`_claude/skills/windows-eventlog/references/object-access.md` lines 155-183 (extracted)].

### Event 4656 — A handle to an object was requested

Precedes the deletion — logs the requested access (including DELETE). Contains the `Object Name` and `Handle ID` that tie to 4660 [ref:`_claude/skills/windows-eventlog/references/object-access.md` lines 59-98 (extracted)].

### Event 5145 — Detailed File Share access (for a network drive)

When the access is over a network share (not local), Event **5145** logs *every* access attempt to a file/folder *within* the share, including the source IP address of the client and the exact permissions requested [ref:`_claude/skills/windows-eventlog/references/object-access.md` lines 471-508 (extracted)].

> **Crucial detail:** On a network drive, both 4663 (file system access on the server) **and** 5145 (share access check) may fire. The 5145 contains the **source IP address** of the client — invaluable for identifying the machine used by the person who deleted the folder [ref:`_claude/skills/windows-eventlog/references/object-access.md` (extracted)].

---

## Detecting moves specifically

A **move to a new name or location on the same volume** is not logged as a distinct "MOVE" operation — it produces:

1. A **DELETE** 4663 on the source location (old path)
2. A **WriteData** 4663 on the destination (new path)

To detect renames/moves reliably, look for 4663 events where:
- `Accesses: DELETE` fires on the original object path, **and**
- Within a short time window, the same process and logon session produces 4663 with `Accesses: WriteData/AddFile` on a different path

[ref:`_claude/skills/windows-eventlog/references/object-access.md` (inferred — standard Windows behavior)]

---

## Summary checklist

| Step | Action | Result |
|------|--------|--------|
| 1 | Enable **Audit File System** (GPO or `auditpol`) | Windows starts accepting file audit events |
| 2 | (Optional) Enable **Audit Handle Manipulation** | 4656/4658 events fire for handle correlation |
| 3 | Set a **SACL** on the folder (per-folder or Global) | Auditing actually fires when DELETE occurs |
| 4 | Check Event Viewer → Security for **4663** (DELETE) | See who deleted what and when |
| 5 | For network access, also check **5145** for source IP | See which machine the user was on |

---

## What if you didn't enable auditing before the deletion?

If the auditing was **not** configured before the folder was deleted, the events were never generated. The deletion cannot be retroactively traced through Windows auditing alone.

**Possible alternatives:**
- Check **Volume Shadow Copies** (Previous Versions) on the server — the folder might be recoverable even if you can't identify who deleted it
- Check **File Server Resource Manager** (FSRM) file screens or storage reports if configured
- Check backup logs for the last known-good backup time
- On Windows Server 2016+ with **Windows LAPS** or other backup/restore points, you may restore the folder's contents even without knowing the perpetrator

---

## References

### RH ground-truth
- `ref:reference/active-directory/solution-guides-deploy-security-auditing-with-central-audit-policies-demonstration-steps.md` — Microsoft Learn: Deploy Security Auditing with Central Audit Policies (Demonstration Steps)
- `ref:reference/active-directory/solution-guides-plan-for-file-access-auditing.md` — Microsoft Learn: Plan for File Access Auditing
- `ref:reference/active-directory/ad-ds-advanced-audit-policy-configuration.md` — Microsoft Learn: Advanced Security Audit Policy Configuration
- `ref:reference/active-directory/ad-ds-monitoring-active-directory-for-signs-of-compromise.md` — Microsoft Learn: Monitoring AD for Signs of Compromise
- `ref:reference/windows-server/administration-auditpol-resourcesacl.md` — Microsoft Learn: auditpol resourceSACL command reference
- `ref:reference/active-directory/ad-ds-appendix-l-events-to-monitor.md` — Microsoft Learn: Events to Monitor (Appendix L)
- `ref:_claude/skills/windows-eventlog/references/object-access.md` — Ultimate Windows Security Log Encyclopedia: Object Access (File System, Registry, Handle, File Share)
- `ref:_claude/skills/admx-gpo/references/audit-policy-to-eventid.md` — Advanced Audit Policy subcategory → Security Event ID map

### Wiki
- [[advanced-audit-policy]]
- [[group-policy]]
- [[monitoring-ad-for-compromise]]
- [[security-principals]]
- [[windows-server-overview]]
