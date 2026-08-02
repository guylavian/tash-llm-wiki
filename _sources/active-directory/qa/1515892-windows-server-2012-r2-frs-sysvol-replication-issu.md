---
title: "Windows Server 2012 R2 FRS Sysvol Replication issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1515892/windows-server-2012-r2-frs-sysvol-replication-issu
question_id: 1515892
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Windows Server 2012 R2 FRS Sysvol Replication issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1515892/windows-server-2012-r2-frs-sysvol-replication-issu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

NOTE:

-  This Active Directory Server is also a DCHP Sever.

I am encountering a issue which FRS Sysvol Replication issue where the gpo's and the sysvol files are not in synced.

There are two domain controller. PM_AD01 is the Primary Domain Controller meanwhile PM_AD01 is a Doman Controller. 

I have tried some solutions: 

-  I have tried to run this command repadmin /syncall /adep but still no anything resolve.

-  Repadmin /replsummary shows no errors.   

-  I have tried the nonauthoritative restore in PM_AD02 which only led me to another error where all the sysvol and netlogon files went missing and also have this error domain controller is not advertising as a time server. And also somehow the netlogon fails as well. Plus also it gave me the error SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE. 

This below link is where I refer for the nonauthoritative restore.

(https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs#nonauthoritative-restore)

Somehow I have managed to get back the sysvol files but the Netlogons file is still missing in PM_AD02. 

Below are some questions :
Questions

-  Should I do an authoritative restore ? ( For FRS Sysvol Replication )

-  Should I do a non authoritative restore ? ( For FRS Sysvol Replication )

-  Initially my plan was to fix the Sysvol Issue and then Migrate to DFSR. 

-  Someone please give me the steps to fix this Sysvol Replication issue. 

-  And after I done the nonauthoritative restore or authoritative restore I might encounter the error which is domain controller is not advertising as a time server, SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE. 

-  If I do an authoritative restore or a non authoritative restore where so I initialize it? Primary Domain Controller ? Or Domain Controller?

-  Is authoritative restore for DFSR Replication ?

-  So by right I should do nonauthoritative restore for FRS right?

-  Also I plan to restart the Netlogons Service but worry might encounter any issue since this AD Server is actually also a DCHP Sever.

At the end the FRS Sysvol replication error still persists. 

I have no idea what else to do.

I really hope someone would give me a solution for this issue as soon as possible. 

Thanks and regards,

JAY

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-28*

Hi,

-  Should I do an authoritative restore ? ( For FRS Sysvol Replication )

-  Should I do a non authoritative restore ? ( For FRS Sysvol Replication )   If you have a issue only on one domain controller you should launch nonauthoritative restore to reinitiaze FRS replication on impacted domain controller.

-  Initially my plan was to fix the Sysvol Issue and then Migrate to DFSR.   It's good blan

-  Someone please give me the steps to fix this Sysvol Replication issue.   To perform a nonauthoritative restore, stop the FRS service, configure the `BurFlags` registry key, and then restart the FRS service. Follow these steps:
   Select Start, and then select Run.
   In the Open box, type cmd and then press ENTER.
   In the Command box, type `net stop ntfrs`.
   Select Start, and then select Run.
   In the Open box, type `regedit` and then press ENTER.
   Locate the following subkey in the registry:  

   `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\NtFrs\Parameters\Backup/Restore\Process at Startup`
   In the right pane, double-click BurFlags.
   In the Edit DWORD Value dialog box, type D2 and then select OK.
   Quit Registry Editor, and then switch to the Command box.
   In the Command box, type net start ntfrs.
   Quit the Command box.
   When the FRS service restarts, the following actions occur:

-  The value for `BurFlags` registry key returns to 0.

-  Files in the reinitialized FRS folders are moved to a Pre-existing folder.

-  An event 13565 is logged to signal that a nonauthoritative restore is started.

-  The FRS database is rebuilt.

-  The member performs an initial join of the replica set from an upstream partner or from the computer that is specified in the Replica Set Parent registry key if a parent has been specified for SYSVOL replica sets.

-  The reinitialized computer runs a full replication of the affected replica sets when the relevant replication schedule begins.

-  When the process is complete, an event 13516 is logged to signal that FRS is operational. If the event is not logged, there is a problem with the FRS configuration.

-  And after I done the nonauthoritative restore or authoritative restore I might encounter the error which is domain controller is not advertising as a time server, SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.   This is another issue. related to AD replication and time configuration

-  If I do an authoritative restore or a non authoritative restore where so I initialize it? Primary Domain Controller ? Or Domain Controller?  

Please refer to the following link :  

https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs#nonauthoritative-restore

-  Is authoritative restore for DFSR Replication ?  

If you are using FRS replication not DFSR you have to use the FRS procedure mentioned in the link above.

-  So by right I should do nonauthoritative restore for FRS right?  

Yes. if you have the issue on aly some domain controller 

-  Also I plan to restart the Netlogons Service but worry might encounter any issue since this AD Server is actually also a DCHP Sever.  

DHCP service will continue working during the netlogon restore.

Please don't forget to accept helpful answer
