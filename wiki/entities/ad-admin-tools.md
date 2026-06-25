---
title: Active Directory Administration Tools
type: entity
domain: active-directory
slug: ad-admin-tools
summary: The primary AD DS management tools are ADAC (dsac.exe), the AD PowerShell module, GPMC, and dsa.msc; ADAC's PowerShell History Viewer bridges GUI administration with scripting and is the required UI for enabling the Recycle Bin.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/Advanced-AD-DS-Management-Using-Active-Directory-Administrative-Center--Level-200- (Microsoft Learn — Advanced AD DS Management Using Active Directory Administrative Center (Level 200), fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/use-active-directory-administrative-center-powershell-history (Microsoft Learn — Use the Active Directory Administrative Center Windows PowerShell History Viewer in Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Enabling-Advanced-Features-for-AD-DS (Microsoft Learn — Enabling Advanced Features for AD DS, fetched 2026-06-18)
provenance_extracted: 12
provenance_inferred: 5
provenance_ambiguous: 0
tags: [directory-services, concept, how-to]
status: draft
updated: 2026-06-18
---

# Active Directory Administration Tools

**The core GUI and PowerShell tools for managing AD DS: ADAC (dsac.exe), the ActiveDirectory PowerShell module, GPMC (gpmc.msc), and the classic dsa.msc snap-in.**

## Body

### Active Directory Administrative Center (ADAC / dsac.exe)

Introduced in Windows Server 2008 R2 and significantly enhanced in Windows Server 2012, **ADAC** is the primary graphical tool for AD DS management. It is built on top of the ActiveDirectory PowerShell module — every GUI action ADAC takes translates to one or more PowerShell cmdlets, which are visible in the **PowerShell History Viewer** pane.

Key capabilities:

- Browse, search, create, and manage users, groups, computers, and OUs.
- Enable and manage the **Active Directory Recycle Bin** (the Tasks pane exposes "Enable Recycle Bin" when logged on with Enterprise Admins rights and the forest functional level is at least Windows Server 2008 R2; this is irreversible).
- Create and manage **Fine-Grained Password Policies** (Password Settings Objects in the Password Settings Container) with a graphical editor — the first such GUI, introduced in Windows Server 2012 (previously required ADSIEdit or PowerShell).
- Manage objects across forests connected by trust without launching a separate tool instance.
- Stage and manage RODC computer accounts (see [[read-only-domain-controller]]).

ADAC requires the **Active Directory Web Services (ADWS)** service (port TCP 9389) to be running on at least one accessible DC. If ADWS is unavailable, ADAC shows "Cannot connect to any domain."

#### PowerShell History Viewer

The History Viewer displays the exact PowerShell cmdlets and arguments ADAC executed for each GUI operation. Practitioners can expand a history entry, copy the command, and adapt it into a reusable script — making ADAC a graphical PowerShell scripting studio (inferred from the design intent described in the reference).

ADAC logs can be enabled via a `dsac.exe.config` file placed in the same directory as dsac.exe, with verbosity levels None / Error / Warning / Info / Verbose.

### ActiveDirectory PowerShell Module

The **ActiveDirectory** module ships as part of RSAT and provides over 100 cmdlets for managing every aspect of AD DS:

- `Get-ADUser`, `New-ADUser`, `Set-ADUser`, `Remove-ADUser`
- `Get-ADGroup`, `Add-ADGroupMember`
- `Get-ADComputer`, `Get-ADDomainController`
- `Enable-ADOptionalFeature` — used to enable the Recycle Bin (`Enable-ADOptionalFeature -Identity 'CN=Recycle Bin Feature,...'`)
- `Restore-ADObject` — restore deleted objects from the Recycle Bin or nondomain partitions
- `Add-ADDSReadOnlyDomainControllerAccount`, `Install-ADDSDomainController` — RODC deployment
- `Get-ADFineGrainedPasswordPolicy`, `New-ADFineGrainedPasswordPolicy`, etc.

The module is used internally by ADAC; cmdlets it generates are visible in the History Viewer (inferred).

### Group Policy Management Console (GPMC / gpmc.msc)

GPMC is the authoritative tool for Group Policy management. It provides a forest/domain/site/OU tree, linking GPOs, managing permissions, modeling policy application (Resultant Set of Policy), and running GP Results reports. GPMC is the required tool for [[group-policy]] administration. It is available as part of RSAT and installed on DCs by default (inferred from GP management best practice).

### Active Directory Users and Computers (ADUC / dsa.msc)

The classic MMC snap-in from Windows 2000 that remains available for compatibility. It supports all core user, group, computer, and OU operations. For advanced tasks — Recycle Bin, FGPPs, PowerShell scripting guidance — ADAC is preferred. ADUC is also used for delegating control via the **Delegation of Control Wizard**.

### Enabling AD DS Advanced Features

Advanced optional features (Recycle Bin, LAPS, 32K database pages) require both a minimum forest/domain functional level and an explicit enablement step. Raising functional levels is done via ADAC, PowerShell (`Set-ADDomainMode`, `Set-ADForestMode`), or the classic dsa.msc / AD Domains and Trusts snap-in. See [[ad-functional-levels]] and [[ad-recycle-bin]].

## Contradictions / caveats

- ADAC cannot restore objects from Configuration, Domain DNS, or Forest DNS partitions — use `Restore-ADObject` for those.
- ADAC cannot restore a full OU subtree in a single action when the parent was also deleted; restore parent first, then children top-down.
- The PowerShell History Viewer shows only the commands ADAC issued — it is not a global audit log. For security auditing use [[advanced-audit-policy]] and event log monitoring.
- ADAC relies on ADWS (TCP 9389); firewalls must allow this port from management workstations to DCs.

## Reference notes
- [[ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200]]
- [[ad-ds-use-active-directory-administrative-center-powershell-history]]
- [[ad-ds-enabling-advanced-features-for-ad-ds]]
- [[ad-ds-active-directory-recycle-bin]]

## See also
- [[group-policy]]
- [[fsmo-roles]]
- [[fine-grained-password-policies]]
- [[ad-recycle-bin]]
- [[read-only-domain-controller]]
