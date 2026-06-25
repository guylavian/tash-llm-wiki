---
title: AD DS Deployment
type: topic
domain: active-directory
slug: ad-ds-deployment
summary: Spine page for installing and promoting domain controllers in a forest — covers role installation, promotion scenarios (new forest, replica DC, child/tree domain, RODC), and the tools and prerequisites involved.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/AD-DS-Deployment (Microsoft Learn — AD DS Deployment, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/Install-Active-Directory-Domain-Services--Level-100- (Microsoft Learn — Install Active Directory Domain Services, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/What-s-New-in-Active-Directory-Domain-Services-Installation-and-Removal (Microsoft Learn — What's New in AD DS Installation and Removal, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, deploy, concept]
status: draft
updated: 2026-06-18
---

# AD DS Deployment

**The end-to-end process of installing the AD DS role on a Windows Server and promoting it to a domain controller in a new or existing forest.**

## Overview

Deploying a domain controller involves two discrete phases:

1. **Role installation** — add the `AD-Domain-Services` Windows feature (binaries only, no configuration yet).
2. **Promotion** — run the Active Directory Domain Services Configuration Wizard (GUI) or an `ADDSDeployment` PowerShell cmdlet to actually promote the server to a DC.

Beginning with Windows Server 2012, `dcpromo.exe` is deprecated; all promotion is driven by Server Manager or the `ADDSDeployment` module. `adprep` is integrated automatically — it runs against the schema master (forestprep) and infrastructure master (domainprep) when adding the first DC of a new Windows Server version to an existing forest. (inferred)

## Promotion scenarios

| Scenario | PowerShell cmdlet | Minimum credential |
|---|---|---|
| New forest | `Install-ADDSForest` | Local Administrator |
| New child/tree domain | `Install-ADDSDomain` | Enterprise Admins |
| Replica DC in existing domain | `Install-ADDSDomainController` | Domain Admins |
| Read-Only DC (staged) | `Add-ADDSReadOnlyDomainControllerAccount` then `Install-ADDSDomainController -UseExistingAccount` | Enterprise Admins (stage 1); delegated user (stage 2) |

Each cmdlet has a corresponding test cmdlet (e.g. `Test-ADDSForestInstallation`) that performs only the prerequisite check without installing. Passing the test before the real run is strongly recommended.

## Key prerequisites and design choices

- **DSRM password** — required for every promotion; store it securely (see [[securing-active-directory]]).
- **DNS** — a DNS server is installed automatically with `Install-ADDSForest` unless disabled. Create DNS delegations when adding child domains. Never store NTDS, logs, or SYSVOL on ReFS volumes.
- **Functional levels** — set domain and forest functional levels as high as the environment supports at deployment time. See [[ad-functional-levels]].
- **Site assignment** — use `-SiteName` to place the DC in the correct AD site; defaults to the site of the calling machine (inferred). See [[site-topology-design]].
- **Install from media (IFM)** — use `-InstallationMediaPath` to bootstrap replica DCs over the WAN; IFM media must be created from a DC of the same OS version.
- **RODC** — staged installation separates account creation (Domain Admins) from server attachment (delegated user). See [[read-only-domain-controller]].
- **Adprep** — runs automatically for new promotions; run manually with `adprep /forestprep` and `adprep /domainprep` before in-place OS upgrades. See [[adprep-and-schema-updates]].

## Post-deployment tasks

After the first DC is promoted in a new version OS, transfer or seize [[fsmo-roles]] to the new DC once all old DCs have been replaced, then raise functional levels. See [[upgrade-domain-controllers]].

## Contradictions / caveats

- `Uninstall-WindowsFeature`/`Remove-WindowsFeature` will not remove the AD DS role binaries until the server has been demoted; attempting to do so returns an error.
- `adprep /domainprep /gpprep` is NOT run automatically — it must be run manually if RSOP planning mode is needed.
- The `ADDSDeployment` module requires a 64-bit process; scripts that mix it with 32-bit cmdlets will fail.
- Do not use `Dism.exe` to remove the AD DS role from a promoted DC — the server will fail to boot.

## Reference notes

- [[ad-ds-ad-ds-deployment]]
- [[ad-ds-install-active-directory-domain-services-level-100]]
- [[ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal]]

## See also

- [[install-promote-domain-controller]]
- [[adprep-and-schema-updates]]
- [[ad-functional-levels]]
- [[upgrade-domain-controllers]]
- [[demote-and-remove-dc]]
---
