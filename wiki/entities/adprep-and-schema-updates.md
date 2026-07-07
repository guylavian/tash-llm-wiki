---
title: Adprep and Schema Updates
type: entity
domain: active-directory
slug: adprep-and-schema-updates
summary: Adprep.exe extends the AD schema and updates forest- and domain-wide objects before the first domain controller of a new Windows Server version is promoted; since Windows Server 2012 it runs automatically during promotion but can be invoked manually for in-place upgrades.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/What-s-New-in-Active-Directory-Domain-Services-Installation-and-Removal (Microsoft Learn — What's New in AD DS Installation and Removal, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/adprep/Changes-Made-by-Adprep (Microsoft Learn — Changes Made by Adprep.exe, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/RODC/Forest-Wide-Updates (Microsoft Learn — Active Directory Forest-Wide Updates, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/Domain-Wide-Updates (Microsoft Learn — Active Directory domain-wide schema updates, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers (Microsoft Learn — Upgrade domain controllers to a newer version of Windows Server, fetched 2026-06-18)
  - kb:ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal
  - kb:ad-ds-changes-made-by-adprep
  - kb:ad-ds-forest-wide-updates
  - kb:ad-ds-domain-wide-updates
  - kb:ad-ds-upgrade-domain-controllers
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, deploy, concept]
status: draft
updated: 2026-07-02
---

# Adprep and Schema Updates

**Adprep.exe prepares an existing AD forest and domain to accept domain controllers running a newer version of Windows Server by extending the schema and updating configuration objects in the forest root domain and in each domain.**

## What adprep does

`adprep.exe` runs three main operations, each targeting a different scope:

| Switch | Scope | Runs on | Credential required |
|---|---|---|---|
| `/forestprep` | Schema (forest-wide) | Schema master | Schema Admins + Enterprise Admins + Domain Admins |
| `/domainprep` | Domain-wide objects (each domain) | Infrastructure master | Domain Admins |
| `/rodcprep` | Application directory partitions | Infrastructure master of each app NC | Enterprise Admins |

`/domainprep /gpprep` sets permissions for RSOP planning mode and must be run **manually**; it is never run automatically.

## Automatic vs manual execution

Since Windows Server 2012, adprep commands run automatically when the first DC of a new Windows Server version is promoted into an existing forest via Server Manager or `ADDSDeployment` PowerShell cmdlets. The installer verifies the schema master is online before proceeding.

Manual execution is required only for **in-place OS upgrades** of an existing DC (i.e., you plan to upgrade the OS of a server that is already a DC). Adprep binary is located in `\support\adprep\` on the Windows Server installation media and supports remote execution. (inferred)

## Example manual invocation

```powershell
Adprep.exe /forestprep /forest <forest-name> /userdomain <user-domain> /user <username> /password *
```

Use `/logdsid` for detailed logging. Logs are written to `%windir%\System32\Debug\Adprep\Logs`.

## Forest-wide updates (forestprep)

`adprep /forestprep` makes cumulative schema changes tracked by the `CN=ActiveDirectoryUpdate,CN=ForestUpdates,CN=Configuration` object's **revision** attribute:

- **WS 2012**: Operations 84–130 (revision → 11) — created Claims, Central Access, Group KDS infrastructure in the Configuration partition.
- **WS 2012 R2**: Operations 131–135 (revision → 15) — created Authentication Policy Configuration, Authentication Policies, and Authentication Policy Silos containers.
- **WS 2016**: Operations 136–142 (revision → 16) — granted Extended Rights (Send-As, Receive-As, Validated-SPN, etc.) to gMSA accounts.

## Domain-wide updates (domainprep)

`adprep /domainprep` updates objects in each domain's partition, tracked by `CN=ActiveDirectoryUpdate,CN=DomainUpdates,CN=System` (revision attribute):

- **WS 2012**: Operations 78–81 (revision → 9) — created TPM Devices container; granted Clone DC extended right; granted ms-DS-Allowed-To-Act-On-Behalf-Of-Other-Identity to Principal Self.
- **WS 2012 R2**: No new operations (revision → 10).
- **WS 2016**: Operations 82–88 (revision → 15) — created CN=Keys container; granted Key Admins and Enterprise Key Admins rights; added `msDS-ExpirePasswordsOnSmartCardOnlyAccounts`.
- **WS 2016 Semi-Annual**: Operation 89 (revision → 16) — corrected Enterprise Key Admins ACE.

## FSMO dependencies

- **Schema master** must be reachable to run `/forestprep`.
- **Infrastructure master** must be reachable to run `/domainprep` and `/rodcprep`.
- **RID master** must be reachable for any DC installation.
- **Domain naming master** must be reachable to install or remove a domain.

See [[fsmo-roles]] for role locations.

## Contradictions / caveats

- `/forestprep` is run once per forest per new Windows Server version; `/domainprep` is run once per domain per new version.
- The `Enterprise Key Admins` and `Key Admins` groups are only created after a WS 2016 DC is promoted **and** takes over the PDC Emulator FSMO role.
- If WMI access to the schema master is blocked by Windows Firewall, adprep `/forestprep` returns `RPC server is unavailable (0x6ba)`. Workaround: run directly on the schema master or open WMI through the firewall.
- Smart card credentials for adprep require a special workaround: obtain the `PSCredential` via `Get-Credential`, then use the resulting `@@...` username format.

## Reference notes

- [[ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal]]
- [[ad-ds-changes-made-by-adprep]]
- [[ad-ds-forest-wide-updates]]
- [[ad-ds-domain-wide-updates]]
- [[ad-ds-upgrade-domain-controllers]]

## See also

- [[ad-ds-deployment]]
- [[install-promote-domain-controller]]
- [[upgrade-domain-controllers]]
- [[ad-functional-levels]]
- [[fsmo-roles]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-what-s-new-in-active-directory-domain-services-installation-and-removal|What's New in Active Directory Domain Services Installation and Removal]]
- [[ad-ds-changes-made-by-adprep|Changes Made by Adprep.exe]]
- [[ad-ds-forest-wide-updates|Active Directory Forest-Wide Updates]]
- [[ad-ds-domain-wide-updates|Active Directory domain-wide schema updates]]
- [[ad-ds-upgrade-domain-controllers|Upgrade domain controllers to a newer version of Windows Server]]
<!-- crosslink:end -->
