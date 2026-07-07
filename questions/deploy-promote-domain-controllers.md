---
title: How to deploy and promote domain controllers in an Active Directory forest
type: question
domain: active-directory
slug: deploy-promote-domain-controllers
summary: Two-phase process: install the AD DS role, then promote via Install-ADDSForest (new forest), Install-ADDSDomain (child/tree), Install-ADDSDomainController (replica DC), or staged RODC. Adprep runs automatically; site assignment, DSRM password, and DNS delegation are key prerequisites.
sources:
  - ref:topics/ad-ds-deployment.md
  - ref:entities/install-promote-domain-controller.md
  - ref:entities/upgrade-domain-controllers.md
  - kb:ad-ds-install-active-directory-domain-services-level-100
  - kb:ad-ds-install-a-new-windows-server-2012-active-directory-forest-level-200
  - kb:ad-ds-install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain-level-200
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
status: draft
updated: 2026-07-07
---

# How to deploy and promote domain controllers in an Active Directory forest

AD DS domain controller deployment follows a **two-phase** workflow: install the role binaries, then promote.

## Phase 1 — Install the AD DS role

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

No reboot required. `-IncludeManagementTools` installs ADUC, AD Sites & Services, and the AD PowerShell module.

## Phase 2 — Promotion (four scenarios)

| Scenario | Cmdlet | Min credential |
|---|---|---|
| **New forest** | `Install-ADDSForest` | Local Admin |
| **New child/tree domain** | `Install-ADDSDomain` | Enterprise Admins |
| **Replica DC** in existing domain | `Install-ADDSDomainController` | Domain Admins |
| **RODC** (staged) | `Add-ADDSReadOnlyDomainControllerAccount` + `Install-ADDSDomainController -UseExistingAccount` | Enterprise Admins (stage 1); delegated (stage 2) |

Each has a `Test-ADDS*` test counterpart — run it first.

### New forest example

```powershell
Install-ADDSForest `
  -DomainName "corp.contoso.com" `
  -DomainMode Win2025 -ForestMode Win2025 `
  -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs"
```

DNS Server is installed automatically unless disabled.

### Replica DC in existing domain (with IFM + site placement)

```powershell
Install-ADDSDomainController `
  -Credential (Get-Credential) `
  -DomainName "corp.contoso.com" `
  -SiteName Boston `
  -InstallationMediaPath "c:\ADDS IFM" `
  -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs"
```

IFM media must be created from a DC of the **same OS version**.

### New child domain

```powershell
Install-ADDSDomain `
  -Credential (Get-Credential) `
  -NewDomainName child `
  -ParentDomainName corp.contoso.com `
  -InstallDNS -CreateDNSDelegation `
  -DomainMode Win2025 `
  -ReplicationSourceDC DC1.corp.contoso.com `
  -SiteName Houston `
  -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs"
```

## Key prerequisites

- **DSRM password** — required; always pass as a secure string (`-SafeModeAdministratorPassword`).
- **Adprep** — runs automatically for new promotions (schema master → forestprep, infrastructure master → domainprep) when the first DC of a new Windows Server version is added. In-place upgrades require manual `adprep /forestprep` + `adprep /domainprep` (`adprep /domainprep /gpprep` is never automatic).
- **DNS delegation** — create delegations when adding child domains.
- **FSMO reachability** — promotion requires the schema master (forestprep) and infrastructure master (domainprep).
- **Storage** — never place NTDS, logs, or SYSVOL on ReFS.
- **Site assignment** — use `-SiteName` to place the DC in the correct AD site; defaults to the caller's site.

## Post-deployment

1. Verify FSMO holders (`Get-ADDomain`, `Get-ADForest`).
2. Transfer FSMO roles to new DCs if replacing old ones.
3. Raise domain/forest functional levels once all old DCs are removed (irreversible).

## Contradictions / caveats

- The `ADDSDeployment` module requires a 64-bit process — 32-bit hosts fail silently.
- `dcpromo.exe` is deprecated since WS 2012 — all promotion uses `ADDSDeployment`.
- Adprep `gpprep` is never automatic; run manually if RSOP planning mode is needed.
- If replication hangs at critical replication (RPC 1908 in dcpromo.log), the installer retries indefinitely.

## References

### Microsoft Learn (kb:)
- Install Active Directory Domain Services [[kb:ad-ds-install-active-directory-domain-services-level-100]]
- Install a New Windows Server 2012 AD DS Forest (Level 200) [[kb:ad-ds-install-a-new-windows-server-2012-active-directory-forest-level-200]]
- Install a Replica Windows Server 2012 DC in an Existing Domain (Level 200) [[kb:ad-ds-install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain-level-200]]

### Wiki pages
- [[ad-ds-deployment]] — spine: role install + promotion + prerequisites + post-deploy
- [[install-promote-domain-controller]] — step-by-step cmdlet reference with flags
- [[upgrade-domain-controllers]] — clean-OS promotion + demotion workflow, FSMO connectivity prereqs
- [[adprep-and-schema-updates]] — adprep scenarios and credential requirements
- [[ad-functional-levels]] — one-way raises, per-version minimums
- [[read-only-domain-controller]] — staged RODC deployment
- [[demote-and-remove-dc]] — graceful demotion + forced removal/cleanup

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-install-active-directory-domain-services-level-100|Install Active Directory Domain Services on Windows Server]]
- [[ad-ds-install-a-new-windows-server-2012-active-directory-forest-level-200|Install a New Windows Server 2012 Active Directory Forest (Level 200)]]
- [[ad-ds-install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain-level-200|Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)]]
<!-- crosslink:end -->
