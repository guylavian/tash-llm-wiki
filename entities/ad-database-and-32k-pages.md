---
title: AD Database and 32k Pages (NTDS.dit)
type: entity
domain: active-directory
slug: ad-database-and-32k-pages
summary: Active Directory stores all directory data in NTDS.dit, an Extensible Storage Engine (ESE) database; Windows Server 2025 introduces an optional 32k page format that expands multi-valued attribute capacity from ~1,200 to ~3,200 values, but enabling it is irreversible.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/32k-pages-optional-feature (Microsoft Learn — Database 32k pages for Active Directory on Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/enable-32K-pages-optional-feature (Microsoft Learn — Enable Database 32k pages optional feature in Active Directory Domain Services on Windows Server, fetched 2026-06-18)
  - kb:ad-ds-32k-pages-optional-feature
  - kb:ad-ds-enable-32k-pages-optional-feature
provenance_extracted: 18
provenance_inferred: 3
provenance_ambiguous: 0
symptoms:
  - "In-place upgraded DC continues using 8k page format even on Windows Server 2025"
  - "Backup incompatibility after enabling 32k pages — old 8k-page backup media unusable"
tags: [directory-services, concept]
status: draft
updated: 2026-07-02
---

# AD Database and 32k Pages (NTDS.dit)

**AD DS stores all directory objects in `NTDS.dit`, an Extensible Storage Engine (ESE) database; since Windows Server 2025 a 32k-page format is available as a forest-wide optional feature that greatly expands multi-valued attribute limits.**

## NTDS.dit basics

The Active Directory database file (`NTDS.dit`) holds every object in the domain partition, the configuration partition, the schema partition, and any application directory partitions. It uses the Extensible Storage Engine (ESE), the same engine used by Exchange. The default path is `%SystemRoot%\NTDS\NTDS.dit`. SYSVOL and the database path are bounded by the Win32 `MAX_PATH` limit of 260 characters — avoid deeply nested folder structures when choosing installation paths.

The database file grows monotonically; space freed by deleted objects is not returned to the OS but is reused internally. Regular offline defragmentation (`ntdsutil files compact`) can reclaim space on disk.

## 8k vs. 32k page formats

Since Windows 2000, ESE used an **8k page** format. This imposed a practical limit on multi-valued attributes (such as group memberships stored as nonlinked attributes) of approximately **1,200 values per object** per database record page.

Windows Server 2025 introduces the **Database 32k pages optional feature**:
- Multi-valued attributes can now hold approximately **3,200 values** per object.
- Uses 64-bit Long Value IDs (LIDs) for scalability.
- New AD DS installs on Windows Server 2025 get a 32k-capable database, but run in **8k simulation mode** by default for compatibility with down-level DCs.

## Transition rules

| DC state | Page format |
|---|---|
| New install on Windows Server 2025 | 32k-capable, runs in 8k simulation mode |
| In-place upgraded from earlier version | Retains 8k format (not auto-upgraded) |
| Promoted as new replica in 2025 forest | 32k-capable, 8k simulation mode |

Moving to full 32k mode is a **forest-wide operation** requiring:
1. All DCs running Windows Server 2025 or later with a 32k-capable database.
2. Domain and forest functional levels raised to Windows Server 2025.
3. The forest free from replication errors.
4. Enterprise Admins membership to enable the feature.

Verify DC capability via ADSI Edit → `CN=NTDS Settings` → `msDS-JetDBPageSize` attribute: `32768` = 32k capable, `8192` = 8k, absent = pre-2025.

Enable via:
```powershell
$params = @{
    Identity = 'Database 32k pages feature'
    Scope    = 'ForestOrConfigurationSet'
    Server   = 'DC01'
    Target   = 'contoso.com'
}
Enable-ADOptionalFeature @params
```

Monitor replication traffic after enabling.

## Backup compatibility

Before enabling the feature, both 8k and 32k backup media can restore a Windows Server 2025 DC. After enabling, **only 32k-page backup media can restore** a Windows Server 2025 DC. Any 8k backup created before enabling is unusable unless a complete authoritative forest recovery is performed.

(inferred) This is the most operationally significant risk: test backup/restore compatibility in a staging environment using 32k-page media before enabling the feature in production.

## Performance note

Enabling the larger 32k page size can increase memory usage due to the larger buffer pool pages. Evaluate the memory footprint of DCs before enabling in memory-constrained environments. (inferred)

## Contradictions / caveats

- The 32k pages feature is **irreversible** once enabled — no rollback except full authoritative forest recovery.
- In-place upgraded DCs never auto-migrate to 32k; a new promote-over-the-wire is required to get a 32k-capable database on those machines.
- Nonlinked attribute limits per object: ~1,200 in pre-2025 forests, up to ~3,000 in Windows Server 2025 forests (see [[ad-ds-maximum-limits]]).

## Reference notes
- [[ad-ds-32k-pages-optional-feature]]
- [[ad-ds-enable-32k-pages-optional-feature]]

## See also
- [[active-directory-overview]]
- [[ad-ds-maximum-limits]]
- [[ad-functional-levels]]
- [[ad-forest-recovery]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-32k-pages-optional-feature|Database 32k pages for Active Directory on Windows Server]]
- [[ad-ds-enable-32k-pages-optional-feature|Enable Database 32k pages optional feature in Active Directory Domain Services on Windows Server]]
<!-- crosslink:end -->
