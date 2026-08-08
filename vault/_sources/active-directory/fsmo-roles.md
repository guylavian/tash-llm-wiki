# Raw note — FSMO (operations-master) roles

- Source: Microsoft Learn, "FSMO roles" / "Transfer or seize FSMO roles in AD DS"
  (web:https://learn.microsoft.com/windows-server/identity/ad-ds/, fetched 2026-06-18).
- Status: notes-first ground truth for the `active-directory` domain.

## Load-bearing facts

AD replication is **multi-master**, but five operations are **single-master** —
performed by exactly one DC holding that Flexible Single Master Operation (FSMO)
role. Two roles are **forest-wide**, three are **per-domain**.

Forest-wide (one per forest):
- **Schema Master** — the only DC that can write changes to the AD schema.
- **Domain Naming Master** — controls adding/removing domains and application
  partitions in the forest.

Per-domain (one per domain):
- **RID Master** — hands out blocks (pools) of relative IDs (RIDs) to each DC so
  every security principal gets a unique SID. Without it, DCs eventually exhaust
  their RID pool and can't create new objects.
- **PDC Emulator** — the most consequential role at runtime: authoritative time
  source for the domain (top of the W32Time hierarchy), processes password
  changes/lockouts preferentially, is the default target for GPO edits (GPMC),
  and acts as the PDC for any legacy down-level clients.
- **Infrastructure Master** — updates cross-domain object references (phantom
  records) and SID/name translations. **Caveat:** in a multi-domain forest it must
  **not** sit on a Global Catalog server (unless *every* DC is a GC), or it can't
  detect stale references.

## Operations

- View holders: `netdom query fsmo`, or PowerShell `Get-ADForest` /
  `Get-ADDomain` (`.SchemaMaster`, `.RIDMaster`, `.PDCEmulator`, etc.).
- **Transfer** (graceful, source DC online): `Move-ADDirectoryServerOperationMasterRole`.
- **Seize** (source DC dead, never coming back): same cmdlet `-Force`. After a
  seize, the old holder must be **fully decommissioned** — never bring it back
  online, or you get a duplicate-role split brain.

## Failure symptoms (feed the review MOC)

- RID Master down for a long time → "cannot create new users/computers", RID pool
  exhaustion warnings (Directory Services event ~16650).
- PDC Emulator down → time skew across the domain, Kerberos failures
  (`KRB_AP_ERR_SKEW` past 5 min), account-lockout inconsistencies.
- Infrastructure Master on a GC in a multi-domain forest → stale "S-1-5-…"
  unresolved SIDs in ACLs across domains.
