---
title: Install and Promote a Domain Controller
type: entity
domain: active-directory
slug: install-promote-domain-controller
summary: Step-by-step reference for the two-phase DC provisioning workflow — role installation then ADDSDeployment promotion — covering PowerShell cmdlets, Server Manager GUI, credentials, and key flags.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/Install-Active-Directory-Domain-Services--Level-100- (Microsoft Learn — Install Active Directory Domain Services (Level 100), fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/What-s-New-in-Active-Directory-Domain-Services-Installation-and-Removal (Microsoft Learn — What's New in AD DS Installation and Removal, fetched 2026-06-18)
  - kb:ad-ds-install-active-directory-domain-services-level-100
  - kb:ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal
provenance_extracted: 22
provenance_inferred: 3
provenance_ambiguous: 0
tags: [directory-services, deploy, how-to]
status: draft
updated: 2026-07-02
graph_community: "FSMO (Operations-Master) Roles"
---

# Install and Promote a Domain Controller

**The two-phase process of adding the AD DS role binaries to a Windows Server and then running the ADDSDeployment configuration to make it a domain controller.**

## Phase 1 — Install the role

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

No reboot is required at this stage. Server Manager can install the role on remote servers by first adding them to a server pool.

## Phase 2 — Promote the server

### New forest

```powershell
Install-ADDSForest -DomainName "corp.contoso.com"
```

Optionally set functional levels, database paths, and DNS delegation:

```powershell
Install-ADDSForest `
  -DomainName corp.contoso.com `
  -CreateDNSDelegation `
  -DomainMode Win2008 `
  -ForestMode Win2025 `
  -DatabasePath "d:\NTDS" `
  -SYSVOLPath "d:\SYSVOL" `
  -LogPath "e:\Logs"
```

### Replica DC in an existing domain

```powershell
Install-ADDSDomainController `
  -Credential (Get-Credential CORP\Administrator) `
  -DomainName "corp.contoso.com"
```

To install from media (IFM) and place the DC in a specific site:

```powershell
Install-ADDSDomainController `
  -Credential (Get-Credential CONTOSO\EnterpriseAdmin1) `
  -DomainName corp.contoso.com `
  -SiteName Boston `
  -InstallationMediaPath "c:\ADDS IFM" `
  -DatabasePath "d:\NTDS" `
  -SYSVOLPath "d:\SYSVOL" `
  -LogPath "e:\Logs"
```

### New child domain

```powershell
Install-ADDSDomain `
  -Credential (Get-Credential corp\EnterpriseAdmin1) `
  -NewDomainName child `
  -ParentDomainName corp.contoso.com `
  -InstallDNS `
  -CreateDNSDelegation `
  -DomainMode Win2025 `
  -ReplicationSourceDC DC1.corp.contoso.com `
  -SiteName Houston `
  -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs" `
  -Confirm:$False
```

## Credential requirements summary

| Action | Required credential |
|---|---|
| Install new forest | Local Administrator on the target server |
| Install new child or tree domain | Enterprise Admins |
| Add replica DC | Domain Admins |
| Run `adprep /forestprep` (first DC of new WS version) | Schema Admins + Enterprise Admins + Domain Admins |
| Run `adprep /domainprep` | Domain Admins |
| Add first RODC | Enterprise Admins |

## Key flags and notes

- **`-SafeModeAdministratorPassword`** — always specify as a secure string; if omitted the cmdlet prompts interactively. Never pass cleartext.
- **`-IncludeManagementTools`** — required at role install time to get ADUC, AD Sites & Services, and other GUI tools.
- **Test cmdlets** — each install cmdlet has a `Test-ADDS*` counterpart that runs only prerequisite checks. Run these first.
- **Prerequisite validation** — the wizard (and PowerShell) verify schema master / infrastructure master reachability before proceeding.
- **Non-critical replication** — only critical data is replicated before the reboot; non-critical data replicates after. (inferred)
- **IFM media version** — IFM media must be created from a DC running the same Windows Server version as the target. Cross-version IFM is not supported.
- **ReFS** — never store the NTDS database, logs, or SYSVOL on a ReFS-formatted volume.

## RODC staged installation

See [[read-only-domain-controller]] for the two-stage RODC workflow (`Add-ADDSReadOnlyDomainControllerAccount` then `Install-ADDSDomainController -UseExistingAccount`), which separates privileged account pre-staging from the less-privileged on-site server attachment.

## Contradictions / caveats

- The `ADDSDeployment` module will not run under a 32-bit process host; scripts that mix 32-bit cmdlets will fail silently on the AD cmdlets.
- `adprep /domainprep /gpprep` is not automatic — run it separately if RSOP planning mode is needed.
- If the installation hangs at the critical replication phase (dcpromo.log shows repeated RPC 1908 errors), investigate network connectivity; the installer retries indefinitely and will not time out on its own.

## Reference notes

- [[ad-ds-install-active-directory-domain-services-level-100]]
- [[ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal]]

## See also

- [[ad-ds-deployment]]
- [[adprep-and-schema-updates]]
- [[ad-functional-levels]]
- [[read-only-domain-controller]]
- [[demote-and-remove-dc]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-install-active-directory-domain-services-level-100|Install Active Directory Domain Services on Windows Server]]
- [[ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal|What's New in Active Directory Domain Services Installation and Removal]]
<!-- crosslink:end -->
