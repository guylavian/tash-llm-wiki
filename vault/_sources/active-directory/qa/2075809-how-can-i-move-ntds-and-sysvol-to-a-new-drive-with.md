---
title: "How Can I Move NTDS and SYSVOL to a New Drive Without Demoting the Domain Controller?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2075809/how-can-i-move-ntds-and-sysvol-to-a-new-drive-with
question_id: 2075809
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How Can I Move NTDS and SYSVOL to a New Drive Without Demoting the Domain Controller?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2075809/how-can-i-move-ntds-and-sysvol-to-a-new-drive-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Expert 

We have promoted a Windows Server 2022 as a Domain Controller and accidentally set the NTDS database and SYSVOL folder to `C:\ADDS`. Now We need to move all of them to `D:\adds`, but we can’t demote and promote the Domain Controller again because it’s already handling traffic.

What’s the safest way to move the NTDS database and SYSVOL folder to the new drive without breaking anything? Any step-by-step help would be greatly appreciated. Thanks!

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-24*

Hello,

Here’s a step-by-step guide:

Moving the NTDS Database

-  Back Up the System

Before making any changes, ensure that you have a full backup of the system.

-  Determine Current NTDS Location

-  Open a Command Prompt as an Administrator.

-  Type `ntdsutil` and press Enter.

-  Type `activate instance ntds` and press Enter.

-  Type `files` and press Enter.

-  Type `info` and press Enter.

-  Note the current paths for the database and logs.

-  Move the NTDS Database

-  Still within the `ntdsutil` prompt, type `move DB to D:\adds` and press Enter.

-  Type `move logs to D:\adds\logs` (or any desired log destination) and press Enter.

-  Exit `ntdsutil` by typing `quit` repeatedly until you're back at the Command Prompt.

-  Restart the Domain Controller

-  Restart the Domain Controller to ensure the changes take effect.

Moving the SYSVOL Folder

-  Determine Current SYSVOL Location

-  Note the current location of the SYSVOL folder (C:\ADDS\SYSVOL).

-  Stop the DFS Replication Service

-  Open a Command Prompt as an Administrator.

-  Type `net stop dfssvc` and press Enter to stop the DFS Replication service.

-  Copy SYSVOL to New Location

-  Copy the entire contents of the SYSVOL folder to the new location (e.g., D:\adds\SYSVOL).

-  Update SYSVOL Path in Registry

-  Open the Registry Editor (`regedit`).

-  Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters`.

-  Find the `SysVol` value and update it to `D:\adds\SYSVOL`.

-  Update SYSVOL Path in Active Directory

-  Open a Command Prompt as an Administrator.

-  Type `regedt32` and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters`.

-  Change the `SysVol` and `SysVolReady` paths to the new location.

-  Open ADSI Edit.

-  Connect to the Default Naming Context.

-  Navigate to `CN=File Replication Service,CN=System,DC=domain,DC=com`.

-  Update the `msDFSR-RootPath` attribute to the new path.

-  Restart the DFS Replication Service

-  Open a Command Prompt as an Administrator.

-  Type `net start dfssvc` and press Enter to start the DFS Replication service.

-  Verify SYSVOL Replication

-  Ensure that the SYSVOL is being replicated correctly by monitoring the Event Viewer for any issues.

Suggestions:

-  Ensure that the Domain Controller is functioning correctly and that there are no errors in the Event Viewer related to replication or AD DS.

-  Run the `dcdiag` command to verify the integrity and health of your Domain Controller.

Following these steps carefully should allow you to move the NTDS database and SYSVOL folder to a new drive without demoting the Domain Controller. Always ensure you have a backup before making such changes.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
