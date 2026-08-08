---
title: "Domain controller role transfer issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187722/domain-controller-role-transfer-issue
question_id: 2187722
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Domain controller role transfer issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187722/domain-controller-role-transfer-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have one Physicals Server DC01.group.in which is domain controller and file server , we have recently create one VM at VMware ESIX and name DC.group.in (192.168.0.7)and transfer all 5 roles to this VM  but found NDTS & Sysvol folder is not replicate to new Domain Server and few issues we had observed.

 Running enterprise tests on : DC.group.in

```
Starting test: LocatorCheck 

     Warning: DcGetDcName(TIME\_SERVER) call failed, error 1355 

     A Time Server could not be located. 

     The server holding the PDC role is down. 

     Warning: DcGetDcName(GOOD\_TIME\_SERVER\_PREFERRED) call failed, error 1355 

     A Good Time Server could not be located. 

     ......................... capitalgroup.in failed test LocatorCheck 

  Starting test: Intersite 

     ......................... capitalgroup.in passed test Intersite
```

and DFSR

192.168.0.3 -- Log Name:      DFS Replication Source:        

DFSR Date:          06-09-2024 16:03:59

 Event ID:      4012 Task Category: None Level:        

 Error Keywords:      Classic 

User:          N/A 

Computer:      DCS01.group.in 

Description: The DFS Replication service stopped replication on the folder with the following local path: C:\Windows\SYSVOL\domain. This server has been disconnected from other partners for 433 days, which is longer than the time allowed by the MaxOfflineTimeInDays parameter (60). DFS Replication considers the data in this folder to be stale, and this server will not replicate the folder until this error is corrected.    To resume replication of this folder, use the DFS Management snap-in to remove this server from the replication group, and then add it back to the group. This causes the server to perform an initial synchronization task, which replaces the stale data with fresh data from other members of the replication group.   

 Additional Information:  Error: 9061 (The replicated folder has been offline for too long.) 

Replicated Folder Name: SYSVOL Share  Replicated Folder ID: 7E33ADB6-D5DF-4FF4-B1A1-CAC1E72EA9B5  

Replication Group Name: Domain System Volume  Replication Group ID: 57A740C7-0CBB-4F63-B9A8-7B84E0CF3466  Member ID: E740DF37-6189-4982-945A-2C8549A970C1 Event Xml: http://schemas.microsoft.com/win/2004/08/events/event">             4012     0     2     0     0     0x80000000000000          2860               DFS Replication     DC01.group.in                7E33ADB6-D5DF-4FF4-B1A1-CAC1E72EA9B5     433     C:\Windows\SYSVOL\domain     9061     The replicated folder has been offline for too long.     SYSVOL Share     Domain System Volume     57A740C7-0CBB-4F63-B9A8-7B84E0CF3466     E740DF37-6189-4982-945A-2C8549A970C1     60

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

Thankyou for your comment.

below link help me to rectify issue

How to Perform an Authoritative Sync of SYSVOL Data Using Distributed File System Replication (DFSR)https://www.dell.com/support/kbdoc/en-in/000207115/how-to-perform-an-authoritative-sync-of-sysvol-data-using-distributed-file-system-replication-dfsr
thankyou very much for your time

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

Hello

Good day!  

You mean there is no SYSVOL folder and Netlogon folder?

Or you mean there is no SYSVOL folder and NTDS folder 

  

Please run net share on the new Domain Controller and check if SYSVOL folder and Netlogon folder is shared on new DC.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-07*

Hi

need to add few more clarification on Sysvol & NTDS folder,

one new VM DC.group.in  , when try to access

\DC  and check shared folder (here sysvol & ntds are not showing)

but when we created one user at new Domain controller DC.group.in , it is successfully showing on my other

servers like DC01.group.in and ADC.group.in

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-06*

1.Do you mean there is only one DC (PDC) before you add one VM at VMware ESIX (VM name is DC.group.in and IP is 192.168.0.7)?  

Ans:- Actually DC1 is main domain controller and ADC.group.in is Additioanl Domain Controller but we add another DC.group.in (one VM on ESIC) to create main Domain Controller and transfer role from DC1 to DC  

2.What is the OS version of DC01.group.in?

Windows Server 2022 Std edition

3.What is the domain functional level and forest functional level?

Ans:- it was on DC1 

4.Please check if SYSVOL replication is DFSR replication.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

Ans:- dc.group.in (new domain controller) , we check Value is set 3  

5.NTDS folder missing on new VM means there is no Log folder and Database folder.  

NTDS folder is not replicated from old DC01.group.in, it will generate when you promote new VM to Domain Controller.

Ans:- but netdom query fsmo & nslookup indicating correct value to new domain controller.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-06*

Hello Arvind Dahiya,  

Thank you for posting in Microsoft Community forum.

1.Do you mean there is only one DC (PDC) before you add one VM at VMware ESIX (VM name is DC.group.in and IP is 192.168.0.7)?  

2.What is the OS version of DC01.group.in?

3.What is the domain functional level and forest functional level?

4.Please check if SYSVOL replication is DFSR replication.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

5.NTDS folder missing on new VM means there is no Log folder and Database folder.  

NTDS folder is not replicated from old DC01.group.in, it will generate when you promote new VM to Domain Controller.  

It seems New Domain Controller is not promoted successfully.  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
