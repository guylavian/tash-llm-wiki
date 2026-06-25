---
title: Upgrade Domain Controllers
type: entity
domain: active-directory
slug: upgrade-domain-controllers
summary: The recommended approach to upgrading DCs is a clean-OS-install promotion of new servers followed by demotion of old ones, not an in-place OS upgrade; adprep runs automatically for new promotions but must be run manually for in-place upgrades.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers (Microsoft Learn — Upgrade domain controllers to a newer version of Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels (Microsoft Learn — Active Directory Domain Services Functional Levels, fetched 2026-06-18)
provenance_extracted: 16
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, deploy, how-to]
status: draft
updated: 2026-06-18
---

# Upgrade Domain Controllers

**The process of replacing domain controllers running an older Windows Server version with DCs running a newer version — the recommended method is clean-OS promotion + demotion, not in-place OS upgrade.**

## Recommended workflow (clean install)

1. **Join** a new Windows Server machine to the forest as a member server.
2. **Install the AD DS role** and promote it as a replica DC (see [[install-promote-domain-controller]]). Server Manager runs adprep automatically if this is the first DC of the new OS version.
3. **Move FSMO roles** to the new DC:
   ```powershell
   Move-ADDirectoryServerOperationMasterRole -Identity "NewDC" -OperationMasterRole 0,1,2,3,4
   ```
4. **Verify FSMO holders**:
   ```powershell
   Get-ADDomain | FL InfrastructureMaster, RIDMaster, PDCEmulator
   Get-ADForest | FL DomainNamingMaster, SchemaMaster
   ```
5. **Demote** the old DC (see [[demote-and-remove-dc]]).
6. Once all old DCs are removed, **raise functional levels** (see [[ad-functional-levels]]).

The clean-install method is preferred because it includes full AD performance improvements introduced in the newer Windows Server release. (inferred)

## In-place OS upgrade

If you choose an in-place upgrade (upgrading the OS on a server that is already a DC):

- Run `adprep /forestprep` and `adprep /domainprep` **manually** before the upgrade — they are not run automatically for in-place paths.
- Only 64-bit version upgrades are supported. Confirm the upgrade path against the [Supported upgrade paths](https://learn.microsoft.com/en-us/windows-server/get-started/supported-upgrade-paths) matrix.

## Minimum forest FL requirements for new OS versions

| New DC OS | Minimum forest FL |
|---|---|
| Windows Server 2019 or later | Windows Server 2008 |
| Windows Server 2016 | Windows Server 2003 |

If the forest FL is below the minimum, promotion is blocked until old DCs are removed and the FL is raised.

## FSMO connectivity prerequisites

Before promoting the first DC of a new Windows Server version, the installation machine must be able to reach:

| Action | Required FSMO role(s) |
|---|---|
| First DC of new OS in a forest | Schema master (forestprep) + Infrastructure master (domainprep) |
| First DC in domain (forest schema already extended) | Infrastructure master |
| Install/remove a domain | Domain naming master |
| Any DC installation | RID master |
| First RODC in forest | Infrastructure master (each app directory partition) |

## Incompatibilities

AD DS cannot be installed on:
- Windows MultiPoint Server
- Windows Server Essentials

AD DS cannot coexist with:
- Microsoft Hyper-V Server role
- Remote Desktop Connection Broker role

## Contradictions / caveats

- No new forest or domain functional levels have been added since Windows Server 2016; WS 2019, 2022, and 2025 use WS 2016 as the most recent FL (WS 2025 adds a DFL for 32k pages, but it is the same incremental model).
- After a functional level is raised it cannot be rolled back without forest recovery (see [[ad-forest-recovery]]), so ensure all DCs are upgraded before raising FL.
- Remote Server Administration Tools for Windows 10/later can manage DCs without needing a matching OS version. (inferred)

## Reference notes

- [[ad-ds-upgrade-domain-controllers]]
- [[ad-ds-active-directory-functional-levels]]

## See also

- [[ad-ds-deployment]]
- [[install-promote-domain-controller]]
- [[adprep-and-schema-updates]]
- [[ad-functional-levels]]
- [[demote-and-remove-dc]]
- [[fsmo-roles]]
