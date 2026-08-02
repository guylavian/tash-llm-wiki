---
title: "Active Directory Disaster recovery - SERVER CORE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191685/active-directory-disaster-recovery-server-core
question_id: 2191685
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Active Directory Disaster recovery - SERVER CORE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191685/active-directory-disaster-recovery-server-core (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I had taken full backup of active directory BMR on server core. Restoring the backup on different isolated machines the restoration was done the machine booted in safe mode.

I'm not much familiar with the CORE VERSION of windows in this case do I need to restore the systemstate backup using the Wbadmin or directly run the Ntdsutil 

for authoritative restoration.  upon authoritative restoration JetEngine error -1023 is appearing.

any help is this regards is highly appreciated.

Thanks and regards.

SK

## Answer (community) — community member

*upvotes: 1 · updated: 2024-01-29*

Hello shaik karamat,

Thank you for posting on the Microsoft Community Forum.

Restoring the backup on different isolated machines the restoration was done the machine booted in safe mode.

A: If you back up the DC1, you should restore the backup on DC1 instead of on different Domain Controllers.

Regarding the JetEngine error -1023, it indicates that there is a problem with the AD database file. You may not have a full backup at the time of the backup.You can try running the Eseutil command-line tool to repair the database file. For more information, please refer to the following link : Repairing Exchange databases with ESEUTIL - when and how? - Microsoft Community Hub

For the two commands you mentioned: wbadmin and ntdstil.

wbadmin is used for unauthorized restores, and ntdstil is used for authorized restores.

If there is only one domain controller in the system and you need to restore AD data on an independent domain controller, you need to perform an unauthorized restore.

If there are multiple domain controllers in the system, the modified AD data has been copied to other domain controllers, and now the AD data needs to be restored to one domain controller, and these data do not need to be copied to all domain controllers, you can use unauthorized restore.

If you need to replicate this data to all domain controllers, you must use an authorization restore.

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-31*

Hi Daisy Zhou,

I really appreciate for your extended support.

Please refer to the MS article the activity which I'm trying.

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-full-server-recovery#next-steps

Your question.

-  May I know whether you make a Domain Controller backup on the server core?

taken the full server (BMR backup) from production and moved to isolated machine.

-  And you want to restore this DC backup from this server core to different hardware machine that is also server core?

the backup which I had taken from the production it will restore your complete all drives.

regards

Shaik Karamat

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-31*

Hello shaik karamat,  

Thank you for your reply.  

May I know whether you make a Domain Controller backup on the server core?  

And you want to restore this DC backup from this server core to different hardware machine that is also server core?  

If so, after my research further, it seems you can restore DC backup to one different hardware from the link below.  

However, there is something you need to know:  

Suppose, you have only one DC in your domain. On some reason a physical server it has been running on failed.

You have a relatively recent System State of your domain controller, and you want to restore Active Directory on a brand new server using Authoritative Restore.

To start the DC restore, you must install the same Windows Server version you had on a failed DC. Install theADDSrole (don’t configure it) andWindows Server Backupfeature in the Windows Server you have just installed.

How to Restore Active Directory from a Backup? | Windows OS Hub (woshub.com)

Here is a link to install AD DS on server core.

Windows Server Core: Installing Active Directory Domain Controller | Windows OS Hub (woshub.com)

Here is a link to enter DSRM on server core.

Directory Service Restore Mode on Core | Microsoft Learn

Here is a link to how to use command to perform unauthorized restore and authorized restore.

wbadmin start systemstaterecovery | Microsoft Learn

authoritative restore | Microsoft Learn  

I am sorry, I did not find a link with how to restore DC on server core step by step.  

Note: please test in a similar lab before you make changes in production environment and check if it works fine.  

I hope the information above is helpful.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-29*

Hi Daisy Zhou,

Thanks for your reply much appreciated. 

On the above comments I am trying to perform the Active directory Disaster Recovery - for forest.   in isolated machine/ Different hardware and had taken the full back of root domain controller that includes every thing on server along with all drives, system state backup and BMR.

On isolated (hyper- v) Virtual machine attached the backup disk and the restoration was successful the machine booted in safe mode Since I'm using server core what will be the further corrective actions to have successful ADRES restoration.  

Basically I'm looking for the steps  to for the active directory disaster recovery for forest for SERVER CORE (FULL BACKUP) on different hardware 

regards

Shaik Karamat
