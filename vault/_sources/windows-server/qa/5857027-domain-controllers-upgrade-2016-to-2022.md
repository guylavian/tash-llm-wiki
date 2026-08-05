---
title: "Domain controllers upgrade 2016 to 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5857027/domain-controllers-upgrade-2016-to-2022
question_id: 5857027
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Independent Advisor"]
---
# Domain controllers upgrade 2016 to 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5857027/domain-controllers-upgrade-2016-to-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

we have 2016 DCs and have plan to upgrade it to 2022 soon, servers are in Azure not on prem . so we are planning to demote and handover so the os team can do inplace upgrade. Is it possible to perform inplace upgrade for the cloud server, how the ISO will be chosen for that.appreciate if you could give some insights about this

The reason we prefer inplace is to avoid the baseline configuration and tools installation in the new server and save time. Also we want to retain the same name and IP

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-04-11*

Hi SAGA,

I just wanted to follow up and see which upgrade path your team ultimately decided to take for your Azure Domain Controllers.

Did you end up deploying a fresh Windows Server 2022 VM from the marketplace to keep your Azure control-plane integrations intact, or did the OS team proceed with the in-place upgrade using the attached Managed Disk method?

If you ran into any unexpected issues swapping the static IPs, or if you need further guidance on transferring the FSMO roles, please do not hesitate to reach out. I am always here to help ensure your AD environment stays stable!

Tracy.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-04-10*

Hi SAGA,

I completely understand why you prefer an in-place upgrade-retaining the exact same IP, hostname, and baseline configurations saves a massive amount of provisioning time. However, while your plan to demote the 2016 server before upgrading makes the process technically supported, performing an in-place upgrade on an Azure VM comes with a significant operational penalty.

The Azure Control-Plane Catch: When you perform an in-place upgrade inside the guest OS, Azure's underlying fabric metadata does not update. Azure will permanently view this VM's source image as "Windows Server 2016." This mismatch permanently breaks critical Azure management integrations, including the Azure Update Manager, Hotpatching, and Auto OS image upgrades.

The Microsoft Recommended Path: For Domain Controllers, the definitive best practice is to entirely avoid in-place upgrades. You should deploy a brand-new Windows Server 2022 VM from the Azure Marketplace, join it, promote it, transfer your FSMO roles, and then demote the old 2016 server. If keeping the exact same IP address is a strict requirement for your environment, you can simply reassign the old static IP to the new 2022 VM immediately after the 2016 server is demoted and shut down.

How to upgrade if you must proceed: If your OS team accepts the loss of Azure control-plane features and insists on an in-place upgrade for the demoted server, you do not use a traditional ISO file in the cloud. Here is the exact method:

Attach Media: Create and attach an Azure Managed Disk that contains the extracted Windows Server 2022 installation media to your VM.

Execute Setup: RDP into the server, locate the drive letter of the attached disk, open an elevated PowerShell prompt, and run the following command: `.\setup.exe /auto upgrade /dynamicupdate disable /eula accept`

Monitor: The RDP session will drop during the upgrade, but you can monitor the installation progress via the Azure Boot Diagnostics screenshot feature in the portal.

I hope this gives you the clear insights needed to weigh the risks and make the best architectural decision for your Active Directory environment. If this helped clarify the Azure-specific upgrade mechanics, please click "Accept Answer".

Tracy.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-10*

Yes, in-place OS upgrade of Azure VMs from Windows Server 2016 to 2022 is supported, but it has trade-offs, and for domain controllers the recommended approach is to add new 2022 DCs and demote the old 2016 DCs rather than in-place upgrade.

1. Recommended approach for domain controllers

For Active Directory Domain Services, the guidance is:

-  Prefer adding new Windows Server 2022 domain controllers and demoting/removing the 2016 DCs instead of in-place upgrading existing DCs.

-  General steps:

-  Build new Windows Server 2022 VMs in Azure and join them to the existing domain.

-  Install the Active Directory Domain Services role on the new servers.

-  Promote them to domain controllers in the existing domain. When doing this via Server Manager/PowerShell, `adprep /forestprep` and `adprep /domainprep` are run automatically as part of the promotion.

-  Move FSMO roles to a new 2022 DC using `Move-ADDirectoryServerOperationMasterRole`.

-  Verify FSMO role placement with `Get-ADDomain` and `Get-ADForest`.

-  Demote and remove the old 2016 DCs.

-  After all DCs are on supported OS versions, raise forest and domain functional levels if desired and supported.

This method avoids the risks of in-place OS upgrades on DCs and is the documented best practice.

Relevant details:

-  Windows Server 2019 or later DCs require at least Windows Server 2008 forest functional level.

-  AD DS on newer OS versions is supported as long as functional level requirements are met.

2. In-place upgrade of Azure VMs (if still required)

If the OS team still wants to do an in-place upgrade of the VM OS (for non-DC workloads, or after demotion of DC role):

-  In-place upgrade of Azure VMs to Windows Server 2019/2022/2025 is supported.

-  High-level prerequisites:

-  Confirm the upgrade path is supported for Windows Server 2016 → 2022 using the Windows Server upgrade matrix.

-  Run the Azure VM Windows OS Upgrade Assessment Tool to validate the path and known issues.

-  Ensure the OS disk has enough free space; expand the OS disk if needed.

-  Temporarily disable antivirus/antispyware and firewalls during the upgrade.

How the ISO is used/“chosen” in Azure

The documented pattern is:

-  Attach an upgrade disk (containing the Windows Server 2022 installation media) to the VM.

-  Start the VM and connect via RDP or Bastion.

-  Identify the drive letter of the attached upgrade disk (commonly E: or F:).

-  In an elevated PowerShell session, change directory to the root of that disk.

-  Start the upgrade with:

```
.\setup.exe /auto upgrade /dynamicupdate disable /eula accept
```

-  Select the correct “Upgrade to” image according to the Windows Server upgrade matrix when prompted.

During the upgrade the RDP session will disconnect; progress can be monitored via Azure boot diagnostics screenshots.

3. Azure-specific considerations

-  In-place upgrade in Azure breaks some control-plane integrations: after upgrade, features such as Auto guest patching, Auto OS image upgrades, Hotpatching, and Azure Update Manager will not function as if the VM were deployed from a native 2022 image, because the VM’s source image metadata (publisher/offer/plan) remains the original 2016 image.

-  To retain full Azure image-based management capabilities, the alternative is to deploy new Windows Server 2022 VMs from marketplace images and migrate roles/data, which aligns with the recommended DC upgrade method.

4. Summary for the scenario

-  For domain controllers: do not in-place upgrade DCs. Instead:

-  Add new 2022 DCs in Azure → move FSMO roles → demote/remove 2016 DCs → optionally raise functional levels.

-  For OS-only upgrade of non-DC Azure VMs (or DCs after demotion): in-place upgrade is supported using an attached ISO/upgrade disk and `setup.exe /auto upgrade`, but be aware of Azure control-plane feature limitations post-upgrade.

References:

-  Upgrade domain controllers to a newer version of Windows Server

-  In-place upgrade for VMs running Windows Server in Azure
