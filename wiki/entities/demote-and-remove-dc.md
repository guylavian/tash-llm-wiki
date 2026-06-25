---
title: Demote and Remove a Domain Controller
type: entity
domain: active-directory
slug: demote-and-remove-dc
summary: Graceful demotion uses Uninstall-ADDSDomainController via Server Manager or PowerShell; forced removal leaves orphaned metadata that must be cleaned up immediately with ntdsutil or the AD management consoles.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/Demoting-Domain-Controllers-and-Domains--Level-200- (Microsoft Learn — Demote Domain Controllers and Domains, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup (Microsoft Learn — Clean up AD DS server metadata, fetched 2026-06-18)
provenance_extracted: 22
provenance_inferred: 3
provenance_ambiguous: 0
symptoms:
  - "orphaned metadata.*NTDS Settings"
  - "Access is denied.*metadata cleanup"
tags: [directory-services, deploy, troubleshooting, how-to]
status: draft
updated: 2026-06-18
---

# Demote and Remove a Domain Controller

**The process of removing the Active Directory Domain Controller role from a server, either gracefully (recommended) or forcibly (emergency), followed by optional removal of the AD DS role binaries.**

## Graceful demotion (recommended)

### Via PowerShell

```powershell
Uninstall-ADDSDomainController
Uninstall-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

`Uninstall-ADDSDomainController` demotes the DC; `Uninstall-WindowsFeature` removes the role binaries afterward. The server **must reboot** between the two steps.

Key arguments for `Uninstall-ADDSDomainController`:

| Argument | Purpose |
|---|---|
| `-Credential` | Required if not already a member of Enterprise Admins or Domain Admins |
| `-LocalAdministratorPassword` | Sets the local Administrator password post-demotion; prompted if omitted |
| `-LastDomainControllerInDomain` | Required when removing the last DC in a domain (also removes the domain) |
| `-RemoveApplicationPartitions` | Required when removing the last DC in a domain |
| `-RemoveDNSDelegation` | Removes DNS delegation records |
| `-ForceRemoval` | Forces demotion even if the DC cannot contact other DCs — use only as a last resort |
| `-DemoteOperationMasterRole` | Seize FSMO roles before demotion (use only on force removal) |

### Via Server Manager

1. **Manage → Remove Roles and Features** → clear Active Directory Domain Services.
2. Server Manager detects the server is a DC and launches the AD DS Configuration Wizard.
3. Confirm demotion; the server reboots automatically after 10 seconds.
4. After reboot, run **Remove Roles and Features** again to strip the binaries.

## Removing the last DC in a domain

Demoting the last DC removes the domain itself. Credentials must include **Enterprise Admins** membership. During the wizard, check **Last domain controller in the domain** and confirm removal of application partitions and DNS delegation.

## Forced removal (last resort)

Use `-ForceRemoval` only when the DC cannot contact other DCs and the network issue cannot be resolved:

```powershell
Uninstall-ADDSDomainController -ForceRemoval -DemoteOperationMasterRole -Credential (Get-Credential)
```

Force demotion:
- Demotes the DC without cleaning up the DC object's metadata in Active Directory.
- All unreplicated changes (passwords, new user accounts) are **lost forever**.
- Leaves orphaned metadata that is the root cause of many AD, Exchange, SQL Server, and other support issues.

**Immediately after a forced removal, perform metadata cleanup.**

## Metadata cleanup

Metadata cleanup removes the stale DC object from the replication topology, transfers or seizes any FSMO roles the DC held, and removes FRS/DFSR connections.

### GUI method (Windows Server 2008+ RSAT — automatic)

Delete the DC's computer object from **Active Directory Users and Computers** (Dsa.msc) or delete the NTDS Settings object from **Active Directory Sites and Services** (Dssite.msc). Starting with WS 2008 RSAT, this triggers automatic metadata cleanup.

**In Dsa.msc:**
1. Expand domain → Domain Controllers OU → right-click the DC object → Delete.
2. Check "This Domain Controller is permanently offline and can no longer be demoted using DCPROMO."
3. If the DC held FSMO roles, accept the prompted role transfer.

**In Dssite.msc:**
1. Expand site → Servers → DC → right-click NTDS Settings → Delete first (triggers cleanup).
2. Then delete the server object.

### Command-line method (ntdsutil)

```
ntdsutil
  metadata cleanup
    connections
      connect to server <FQDN-of-surviving-DC>
    quit
    remove selected server <FQDN-of-removed-DC>
```

Confirm in the dialog box, then verify the DC no longer appears in Domain Controllers OU and no NTDS Settings object exists under the server object in Sites and Services.

## Common operational traps

- **Do not use `Dism.exe`** to remove the AD DS role from a promoted DC — the server will fail to boot normally.
- `Uninstall-WindowsFeature` / `Remove-WindowsFeature` will return an error if the server has not yet been demoted.
- You must **restart** after demotion before removing the `AD-Domain-Services` binaries.
- If the DC object has "Protect object from accidental deletion" enabled, the Delete operation fails with "Access is denied" — clear the flag via Properties → Object tab in ADUC (requires Advanced Features view).
- Do not remove DNS, GPMC, or RSAT tools before demotion if you intend to repromote the server soon — Server Manager reinstalls them on repromote, adding time.

## Reference notes

- [[ad-ds-demoting-domain-controllers-and-domains-level-200]]
- [[ad-ds-ad-ds-metadata-cleanup]]

## See also

- [[ad-ds-deployment]]
- [[upgrade-domain-controllers]]
- [[ad-metadata-cleanup]]
- [[fsmo-roles]]
- [[ad-forest-recovery]]
