---
title: "Cumulative Update 8 for Exchange Server 2019 - Error: The upgrade cannot be installed..."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304404/cumulative-update-8-for-exchange-server-2019-error
question_id: 304404
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Cumulative Update 8 for Exchange Server 2019 - Error: The upgrade cannot be installed...

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304404/cumulative-update-8-for-exchange-server-2019-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi.

I have a Windows Server 2019 with Exchange Server 2019 (15.2.529.5) CU 4.

But i cannot patch Exchange Server 2019 to newest CU 8 (https://www.microsoft.com/en-us/download/details.aspx?id=102770). I get this error:  

The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.

Is there anyone who will help me to solve this.

MSI Error log:

=== Verbose logging started: 08-03-2021 19:57:49 Build type: SHIP UNICODE 5.00.10011.00 Calling process: C:\Windows\system32\msiexec.exe ===  

MSI (c) (EC:A0) [19:57:49:345]: Font created. Charset: Req=0, Ret=0, Font: Req=MS Shell Dlg, Ret=MS Shell Dlg

MSI (c) (EC:A0) [19:57:49:345]: Font created. Charset: Req=0, Ret=0, Font: Req=MS Shell Dlg, Ret=MS Shell Dlg

MSI (c) (EC:D4) [19:57:49:358]: Resetting cached policy values  

MSI (c) (EC:D4) [19:57:49:358]: Machine policy value 'Debug' is 0  

MSI (c) (EC:D4) [19:57:49:358]: ******* RunEngine:  

******* Product: {CD981244-E9B8-405A-9026-6AEB9DCEF1F1}  

******* Action:  

******* CommandLine: **********  

MSI (c) (EC:D4) [19:57:49:359]: Machine policy value 'DisableUserInstalls' is 0  

MSI (c) (EC:D4) [19:57:49:365]: Cloaking enabled.  

MSI (c) (EC:D4) [19:57:49:365]: Attempting to enable all disabled privileges before calling Install on Server  

MSI (c) (EC:D4) [19:57:49:367]: End dialog not enabled  

MSI (c) (EC:D4) [19:57:49:367]: Original package ==> C:\Windows\Installer\1dab0d.msi  

MSI (c) (EC:D4) [19:57:49:367]: Package we're running from ==> C:\Windows\Installer\1dab0d.msi  

MSI (c) (EC:D4) [19:57:49:391]: APPCOMPAT: Uninstall Flags override found.  

MSI (c) (EC:D4) [19:57:49:391]: APPCOMPAT: Uninstall VersionNT override found.  

MSI (c) (EC:D4) [19:57:49:391]: APPCOMPAT: Uninstall ServicePackLevel override found.  

MSI (c) (EC:D4) [19:57:49:391]: APPCOMPAT: looking for appcompat database entry with ProductCode '{CD981244-E9B8-405A-9026-6AEB9DCEF1F1}'.  

MSI (c) (EC:D4) [19:57:49:391]: APPCOMPAT: no matching ProductCode found in database.  

MSI (c) (EC:D4) [19:57:49:396]: MSCOREE not loaded loading copy from system32  

MSI (c) (EC:D4) [19:57:49:405]: Opening existing patch 'C:\Windows\Installer\7c68053.msp'.  

MSI (c) (EC:D4) [19:57:49:406]: Opening existing patch 'C:\Windows\Installer\23ddd018.msp'.  

MSI (c) (EC:D4) [19:57:49:408]: Note: 1: 1402 2: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer 3: 2  

MSI (c) (EC:D4) [19:57:49:408]: Original patch ==> e:\Exchange2019-KB5000871-x64-en.msp  

MSI (c) (EC:D4) [19:57:49:408]: Patch we're running from ==> e:\Exchange2019-KB5000871-x64-en.msp  

MSI (c) (EC:D4) [19:57:49:408]: SOFTWARE RESTRICTION POLICY: Verifying patch --> 'e:\Exchange2019-KB5000871-x64-en.msp' against software restriction policy  

MSI (c) (EC:D4) [19:57:49:409]: SOFTWARE RESTRICTION POLICY: e:\Exchange2019-KB5000871-x64-en.msp has a digital signature  

MSI (c) (EC:D4) [19:57:50:267]: SOFTWARE RESTRICTION POLICY: e:\Exchange2019-KB5000871-x64-en.msp is permitted to run at the 'unrestricted' authorization level.  

MSI (c) (EC:D4) [19:57:50:267]: SequencePatches starts. Product code: {CD981244-E9B8-405A-9026-6AEB9DCEF1F1}, Product version: 15.2.529.5, Upgrade code: {A4A259AB-A77F-4039-832A-27B431DDFFEA}, Product language 1033  

MSI (c) (EC:D4) [19:57:50:272]: PATCH SEQUENCER: verifying the applicability of QFE patch e:\Exchange2019-KB5000871-x64-en.msp against product code: {CD981244-E9B8-405A-9026-6AEB9DCEF1F1}, product version: 15.2.529.5, product language 1033 and upgrade code: {A4A259AB-A77F-4039-832A-27B431DDFFEA}  

MSI (c) (EC:D4) [19:57:50:272]: PATCH SEQUENCER: QFE patch e:\Exchange2019-KB5000871-x64-en.msp is not applicable.  

MSI (c) (EC:D4) [19:57:50:272]: SequencePatches returns success.  

MSI (c) (EC:D4) [19:57:50:272]: Final Patch Application Order:  

MSI (c) (EC:D4) [19:57:50:272]: {AC232540-917E-49F2-91DA-7AF02BF540A1} -  

MSI (c) (EC:D4) [19:57:50:272]: {4CF3E0E0-0835-405D-A0B5-7933E19E4DCA} -  

MSI (c) (EC:D4) [19:57:50:272]: Other Patches:  

MSI (c) (EC:D4) [19:57:50:272]: Unknown\Absent: {C3E4DD1C-13B7-4378-ACB9-808516A235B2} - e:\Exchange2019-KB5000871-x64-en.msp  

The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.  

C:\Windows\Installer\1dab0d.msi  

MSI (c) (EC:D4) [19:57:50:273]: Product: Microsoft Exchange Server - Update '{C3E4DD1C-13B7-4378-ACB9-808516A235B2}' could not be installed. Error code 1642. Additional information is available in the log file e:\ppatch.log.

MSI (c) (EC:D4) [19:57:50:273]: Windows Installer installed an update. Product Name: Microsoft Exchange Server. Product Version: 15.2.529.5. Product Language: 1033. Manufacturer: Microsoft Corporation. Update Name: {C3E4DD1C-13B7-4378-ACB9-808516A235B2}. Installation success or error status: 1642.

MSI (c) (EC:D4) [19:57:50:273]: Note: 1: 1708  

MSI (c) (EC:D4) [19:57:50:273]: Product: Microsoft Exchange Server -- Installation failed.

MSI (c) (EC:D4) [19:57:50:273]: Windows Installer installed the product. Product Name: Microsoft Exchange Server. Product Version: 15.2.529.5. Product Language: 1033. Manufacturer: Microsoft Corporation. Installation success or error status: 1642.

MSI (c) (EC:D4) [19:57:50:283]: MainEngineThread is returning 1642  

=== Verbose logging stopped: 08-03-2021 19:57:50 ===

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-09*

Hi, @BlazTU       

Agree with Andy, according to your description and the msi error log,     

it seems that you are trying to install Security Update For Exchange Server 2019 CU8 (KB5000871) on your Exchange 2019 CU4 Server.    

Please note that Security Update for Exchange server are different from Cumulative Updates(CU),     

it won't update your Exchange server to the latest CU version.    

Besides, the Security Update for Exchange server should match the CU version of your Exchange server.    

If you try to install a security update on a unsupported CU version, it would show this error as mentioned in your post:    

    

In your case, you may need to install Cumulative Update 8 for Exchange Server 2019 first. Then install the Security Update For Exchange Server 2019 CU8 (KB5000871).    

When installing Cumulative Update 8 for Exchange Server 2019:    

Since there are some changes in the active directory in CU8, please run prepareSchema/prepareAD/prepareDomain before you patch CU8.    

And it is always suggested to have a full backup of the server in case something goes wrong after the upgrade.    

When installing the Security Update For Exchange Server 2019 CU8 (KB5000871):    

After you successfully upgrade to CU8, please follow the best practices in this document to install the security update.    

For more information about the Security Update , please refer to this thread: FAQ for March 2021 Exchange Server Security Updates    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
