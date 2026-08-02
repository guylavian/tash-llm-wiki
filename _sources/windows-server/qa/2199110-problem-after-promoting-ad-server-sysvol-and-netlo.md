---
title: "Problem after promoting AD Server, SYSVOL and NETLOGON folder missing."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199110/problem-after-promoting-ad-server-sysvol-and-netlo
question_id: 2199110
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Problem after promoting AD Server, SYSVOL and NETLOGON folder missing.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199110/problem-after-promoting-ad-server-sysvol-and-netlo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a running AD Server Windows 2016 (AD1), now we're going to replace our AD Server to Windows 2022 (AD2)  

We have done following steps		 

-  We joined AD2 to DOMAIN.local domain

-  We added AD Service Role and DNS role

-  AD2 promoted as Primary Domain Controller

-  Transfer RID Master, PDC Emulator, Infrastructure Master, Domain Naming Master, and Schema Master to AD2

-  We ran "netdom query fsmo"	and everything looks normal.

-  In AD2, we can list users and computers from AD1

The problem are        

-  AD2 seems doesn't work when AD1 goes offline

-  AD2 don't have shared SYSVOL and NETLOGON folders

-  By doing some checking procedure, we thought the DFSR Replication was not running or even started

-  We have checked DNS configuration, We don't know for sure but its seemed ok.

-  AD2 is not advertised as PDC

How do we resolve these problems? please enlighten us, thank you very much!  

Here are some logs from both server  

AD1 

>dcdiag /c /q 

[AD1] No security related replication errors were found on this DC!  To target the connection to a specific 

source DC use /ReplSource:<DC>. 

There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL 

replication problems may cause Group Policy problems. 

......................... AD1 failed test DFSREvent 

** Did not run Outbound Secure Channels test because /testdomain: was not entered 

An error event occurred.  EventID: 0x00002720 

Time Generated: 06/16/2024   09:31:38 

Event String: 

The application-specific permission settings do not grant Local Activation permission for the COM Server application with CLSID 

An error event occurred.  EventID: 0x00002720 

Time Generated: 06/16/2024   09:40:28 

Event String: 

The application-specific permission settings do not grant Local Activation permission for the COM Server application with CLSID 

An error event occurred.  EventID: 0x00002720 

Time Generated: 06/16/2024   10:08:05 

Event String: 

The application-specific permission settings do not grant Local Activation permission for the COM Server application with CLSID 

......................... AD1 failed test SystemLog

AD2	 = dcdiag /c /q	 

Warning: DsGetDcName returned information for \AD1.DOMAIN.local, when we were trying to reach AD2.	 

SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.	 

......................... AD2 failed test Advertising	 

[AD2] No security related replication errors were found on this DC!  To target the connection to a specific source DC use	 

/ReplSource:<DC>.	 

There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL replication problems may	 

cause Group Policy problems.	 

......................... AD2 failed test DFSREvent	 

Unable to connect to the NETLOGON share! (\AD2\netlogon)	 

[AD2] An net use or LsaPolicy operation failed with error 67, The network name cannot be found..	 

......................... AD2 failed test NetLogons	 

** Did not run Outbound Secure Channels test because /testdomain: was not entered	

Update : 2024/06/18  

After trying this below method   

somehow, AD2 already advertising to AD1,   

"To work around this issue, set the SysvolReady Flag registry value to “0” and then back to “1” in the registry. To do this, follow these steps:Click Start, click Run, type regedit, and then click OK.Locate the following subkey in Registry Editor:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters  

In the details pane, right-click the SysvolReady flag, and then click Modify.In the Value data box, type 0, and then click OK.Again in the details pane, right-click the SysvolReady flag, and then click Modify.In the Value data box, type 1, and then click OK.Note This will cause Netlogon to share out SYSVOL, and the scripts folder will be present "  

the condition right now,   

AD2 have SYSVOL & NETLOGON folder with BLANK item, and wouldn't copy the AD1 policies, item, etc even we force replicate it..  

How do we solve this new problem? thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-20*

Hello David, Here is the dcdiag on both server  

AD1  

Directory Server DiagnosisPerforming initial setup: Trying to find - Pastebin.com   

AD2  

dcdiag AD2Directory Server DiagnosisPerforming initial setup: Tr - Pastebin.com  

Please enlighten us, thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-18*

when you ran the upgrade how did the DNS and Gateway information return.

To me this would be caused by bad DNS as its not gathering all the correct returns on the DC promo

Please provide me with a full Dcdiag download and run it on DNS separately please 

Dump everything here

David

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-18*

Hi Bagas Imr,

Have a nice day!

For issue 1, the error is caused by the fact that the domain control disconnection time to be replicated exceeds the survival time of the logical deletion.

Lingering objects in an AD DS forest - Windows Server | Microsoft Learn

For issue 2, it is not recommended that you set a setting for MaxOfflineTimeInDays. And there is no official documentation about it.

For issue 3, it is recommended to save.

Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server | Microsoft Learn

Best regards

Neuvi Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-18*

Hello NeuviJ, thank you for your response! After trying this below method somehow, AD2 already advertising to AD1 :  

"To work around this issue, set the SysvolReady Flag registry value to “0” and then back to “1” in the registry. To do this, follow these steps:Click Start, click Run, type regedit, and then click OK.Locate the following subkey in Registry Editor: 

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\ParametersIn the details pane, right-click the SysvolReady flag, and then click Modify.In the Value data box, type 0, and then click OK.Again in the details pane, right-click the SysvolReady flag, and then click Modify.In the Value data box, type 1, and then click OK.Note This will cause Netlogon to share out SYSVOL, and the scripts folder will be present " 

The current condition, AD2 have SYSVOL & NETLOGON folder with BLANK item, and wouldn't copy the AD1 policies, item, etc even we force replicate it.. 

questions: 

1)It seems DFSR Replicate is error in AD1. We have following log: 

"The DFS Replication service stopped replication on the folder with the following local path: C:\Windows\SYSVOL\domain. This server has been disconnected from other partners for 1505 days, which is longer than the time allowed by the MaxOfflineTimeInDays parameter (60). DFS Replication considers the data in this folder to be stale, and this server will not replicate the folder until this error is corrected." 

AD1 was new AD server replaced AD0. Seems like AD0 is still needed. How do we fix this?  

-  How to set MaxOfflineTimeInDays ? 

-  Is it save to run "How to force authoritative and non-authoritative synchronization for DFSR-replicated sysvol replication" on AD1? ,  

because client still use AD1 as main data server.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-17*

Hi Bagas Imr,

Thank you for posting in the Microsoft Community Forums.

This is a common failure and may be a problem with DFS replication.

You can troubleshoot the issue based on this article.

Troubleshoot missing SYSVOL and Netlogon shares for Distributed File System (DFS) Replication - Windows Server | Microsoft Learn 

Best regards

Neuvi Jiang
