---
title: Active Directory Recycle Bin
type: entity
domain: active-directory
slug: ad-recycle-bin
summary: The AD Recycle Bin is an optional feature that preserves all attributes of deleted objects so they can be fully restored; enabling it is irreversible and requires Windows Server 2008 R2 or higher domain and forest functional levels.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-recycle-bin (Microsoft Learn — Enable Active Directory Recycle Bin in Windows Server, fetched 2026-06-18)
provenance_extracted: 14
provenance_inferred: 2
provenance_ambiguous: 0
tags: [directory-services, concept, how-to]
status: draft
updated: 2026-06-18
---

# Active Directory Recycle Bin

**The Active Directory Recycle Bin preserves all link-valued and non-link-valued attributes of deleted objects, enabling full restoration including group memberships and access rights.**

## What it does

When the Recycle Bin is enabled, deleted objects are moved to a "deleted objects" container and held with their full attribute state intact. This means a restored user account automatically regains group memberships and corresponding access rights within and across domains — without any manual reconstruction. This is the key difference from the pre-Recycle-Bin method of tombstone restores, which recovered only a subset of attributes.

Without the Recycle Bin, accidentally deleted objects require an authoritative restore from backup (offline procedure), and re-linking of group memberships and attributes must be done manually. (inferred)

## Requirements

- Domain **and** forest functional level must be **Windows Server 2008 R2 or higher**.
- Must be a member of the **Domain Admins** group in the target domain.
- RSAT must be installed: either Active Directory Administrative Center (ADAC) or the Active Directory module for Windows PowerShell.

## Enabling the feature

The feature is disabled by default. It can be enabled via ADAC or PowerShell:

```powershell
Enable-ADOptionalFeature `
  -Identity 'CN=Recycle Bin Feature,CN=Optional Features,CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,DC=contoso,DC=com' `
  -Scope ForestOrConfigurationSet `
  -Target 'contoso.com'
```

If you encounter errors, try moving both the Schema Master and Domain Naming Master FSMO roles to the same DC in the root domain, then rerun.

## Restoring deleted objects

Navigate in ADAC to the **Deleted Objects** container in the target domain. Select the objects and choose **Restore** (to original location) or **Restore To** (to a specified OU).

Via PowerShell:
```powershell
# Restore to original location
Get-ADObject -Filter 'Name -Like "*User*"' -IncludeDeletedObjects | Restore-ADObject

# Restore to a different OU
Get-ADObject -Filter 'Name -Like "*User*"' -IncludeDeletedObjects |
  Restore-ADObject -TargetPath "OU=Corp,DC=contoso,DC=com"
```

Only objects deleted **after** the Recycle Bin was enabled can be recovered this way.

## Contradictions / caveats

- Enabling the Recycle Bin is **irreversible** — it cannot be disabled after activation.
- Objects deleted **before** the feature was enabled cannot be recovered via this method.
- The feature is forest-scoped; enabling it in one domain raises the functional level requirement for the entire forest.
- (inferred) The deleted objects container has a configurable tombstone lifetime; after the tombstone lifetime expires the objects are garbage-collected and permanently lost even with the Recycle Bin enabled.

## Reference notes
- [[ad-ds-active-directory-recycle-bin]]

## See also
- [[active-directory-overview]]
- [[ad-forest-recovery]]
- [[ad-functional-levels]]
- [[fsmo-roles]]
