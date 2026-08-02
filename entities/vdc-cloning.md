---
title: VDC Cloning
type: entity
domain: active-directory
slug: vdc-cloning
summary: Virtualized DC cloning (Windows Server 2012+) provisions a new domain controller by copying an existing DC's NTDS.DIT, placing DCCloneConfig.xml, and using VM-GenerationID detection to safely promote the clone — eliminating the need for full AD DS installation.
sources:
  - kb:ad-ds-virtualized-domain-controller-deployment-and-configuration
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-virtualized-domain-controller-troubleshooting
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Deployment-and-Configuration (Microsoft Learn — Virtualized Domain Controller Deployment and Configuration, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Architecture (Microsoft Learn — Virtualized Domain Controller Architecture, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/virtual-dc/Virtualized-Domain-Controller-Troubleshooting (Microsoft Learn — Virtualized Domain Controller Troubleshooting, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "Event ID 2162.*Virtual domain controller cloning failed"
  - "Event ID 2175.*clone configuration file exists on an unsupported platform"
  - "Event ID 2228.*VMGenerationID.*DCCloneConfig.xml.*couldn't be located"
  - "Event ID 29218.*cloning.*rebooted into.*DSRM"
  - "Event ID 2224.*Managed Service Account.*cloning failed"
tags: [directory-services, virtualization, how-to]
status: draft
updated: 2026-07-02
graph_community: "Active Directory Replication & Site Topology"
---

# VDC Cloning

**Virtualized DC cloning allows an administrator to deploy additional domain controllers by copying an existing VM's disk, supplying a `DCCloneConfig.xml` configuration file, and booting the copy — which detects the new VM-GenerationID and auto-promotes itself.**

## Prerequisites

| Requirement | Detail |
|---|---|
| Guest OS | Windows Server 2012 or later |
| Hypervisor | Must expose VM-GenerationID |
| PDC Emulator | Must run Windows Server 2012+ and be **online and reachable** during cloning |
| Schema | AD DS schema version ≥ 56, forest functional level ≥ Windows Server 2003 Native |
| Source DC membership | Source DC must be a member of the **Cloneable Domain Controllers** group |

The PDC Emulator is critical: it creates the Cloneable Domain Controllers group, sets the `Allow a DC to create a clone of itself` control access right on the domain NC head, and handles the `IDL_DRSAddCloneDC` RPC call (DRS UUID `E3514235-4B06-11D1-AB04-00C04FC2DCD2`, Opnum 28) that creates the clone computer object.

## Key artefacts

### DCCloneConfig.xml
The mandatory configuration file that signals cloning intent. Generate it on the source DC with:

```powershell
New-ADDCCloneConfigFile -CloneComputerName CloneDC1 -SiteName "Default-First-Site-Name" `
    -IPv4Address "10.0.0.10" -IPv4SubnetMask "255.255.0.0" `
    -IPv4DefaultGateway "10.0.0.1" -IPv4DNSResolver "10.0.0.1" -Static
```

Without `-Static`, network settings default to DHCP. The `-Offline` switch skips online validation and places the file directly on a mounted VHD. Valid placement locations (searched in order):
1. DSA Working Directory (`%systemroot%\NTDS`)
2. `%windir%\NTDS`
3. Root of removable read/write media, in drive-letter order

If the file is present but VM-GenerationID is unavailable, the clone boots into **DSRM** to prevent a duplicate DC from advertising on the network. If the file is absent and VM-GenerationID changes, [[vm-generation-id-safe-restore]] triggers instead of cloning.

### CustomDCCloneAllowList.xml
Optional allowlist for third-party services or applications that would otherwise block cloning. Any service or program returned by `Get-ADDCCloningExcludedApplicationList` and not present in this file **must** be uninstalled before cloning proceeds.

Standalone Managed Service Accounts (MSAs, introduced in Windows Server 2008 R2) must be removed with `Uninstall-ADServiceAccount` before cloning; **group MSAs (gMSAs, Windows Server 2012+) support cloning** without removal.

## Cloning procedure (high-level)

1. **Authorize source DC:** add it to the Cloneable Domain Controllers group (`Add-ADGroupMember "Cloneable Domain Controllers" <dc-samaccountname>`).
2. **Check for excluded apps:** `Get-ADDCCloningExcludedApplicationList`; uninstall or allowlist each result.
3. **Generate DCCloneConfig.xml** with `New-ADDCCloneConfigFile` (online mode validates prerequisites automatically).
4. **Shut down the source DC gracefully** — never clone from a DC stopped by power loss.
5. **Copy or export the VM disks** — export the full VM (recommended for multi-disk VMs); delete all snapshots before or after copying.
6. **Create a new VM** from the copied disks (hypervisor auto-assigns a new VM-GenerationID).
7. **Start the new VM** — cloning begins automatically; the DC reboots once and advertises normally.

If cloning fails the VM boots into DSRM. After fixing the root cause, clear the DSRM boot flag with `bcdedit /deletevalue safeboot` and reboot to retry.

## What happens during clone boot

On first boot of the clone, NTDS detects a VM-GenerationID mismatch, finds `DCCloneConfig.xml`, and:

1. Resets InvocationID and discards the RID pool.
2. Contacts the PDC Emulator to create a new DC computer object via `IDL_DRSAddCloneDC`.
3. Assigns the name and IP from `DCCloneConfig.xml` (or auto-generates them).
4. Performs a non-authoritative SYSVOL sync (DFSR or FRS).
5. Replicates missing AD objects from a partner DC using the existing NTDS.DIT as a starting point (minimizes replication traffic).
6. Renames `DCCloneConfig.xml` with a timestamp so it is not re-read on the next reboot.

The maximum number of auto-generated DC names from a single source is 9,999 (Event ID 2184). Use `<computername>` in the XML to override auto-naming.

## Unsupported cloning targets

- VHDs/VHDXs manually copied over existing files (bypasses VM-GenerationID; causes USN rollback).
- VHDs/VHDXs restored by file-level backup software.
- Passthrough disks (no virtual disk file to copy).

## Contradictions / caveats

- RODC cloning is supported (Windows Server 2012+) but creates a new KrbTgt object for the clone (Event ID 2213).
- Running `New-ADDCCloneConfigFile` in online mode performs validation; passing `-Offline` skips validation and must be used when the source DC is shut down and you need to copy the XML to the offline VHD.
- Deleting imported snapshots after importing a clone VM is **mandatory** — applying a pre-clone snapshot to a clone creates a duplicate DC identity. See [[virtualized-domain-controllers]].

## Reference notes

- [[ad-ds-virtualized-domain-controller-deployment-and-configuration]]
- [[ad-ds-virtualized-domain-controller-architecture]]
- [[ad-ds-virtualized-domain-controller-troubleshooting]]

## See also

- [[virtualized-domain-controllers]]
- [[vm-generation-id-safe-restore]]
- [[fsmo-roles]]
- [[ad-replication]]
- [[read-only-domain-controller]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-virtualized-domain-controller-deployment-and-configuration|Virtualized Domain Controller Deployment and Configuration]]
- [[ad-ds-virtualized-domain-controller-architecture|Virtualized Domain Controller Architecture]]
- [[ad-ds-virtualized-domain-controller-troubleshooting|Virtualized Domain Controller Troubleshooting]]
<!-- crosslink:end -->
