---
title: "[Migrated from MSDN Exchange Dev] Exchange Server 2016 - System Crashed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/191564/migrated-from-msdn-exchange-dev-exchange-server-20
question_id: 191564
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Exchange Server 2016 - System Crashed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/191564/migrated-from-msdn-exchange-dev-exchange-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.    

[MSDN thread link] Exchange Server 2016 - System Crashed    

[Original post]    

Any suggestion on this?    

46571-bugcheck-analysis.txt

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-12-09*

Hi,    

From the FAILURE_BUCKET_ID in the debugging details, it seems that crash could be related to the MSExchangeHMWorker.exe:      

FAILURE_BUCKET_ID: 0xEF_wininit.exe_BUGCHECK_CRITICAL_PROCESS_TERMINATED_BY_MSExchangeHMWorker.exe_5f28_ANALYSIS_INCONCLUSIVE!unknown_function    

Probabaly Managed availability was attempting to fix a issue by terminating a process, and that led to the system crash. Given this, as according to this official document, "the two primary management tools for managed availability are the Windows Event Log and the Shell", it's recommended to go through the Event logs such as the RecoveryActionResults event log via event viewer and see if more clues can be found:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

If the DB is damaged you have a few options to resolve the issue  

NOTE:  Before taking any action against the EDB, make an offline copy of the database to an alternate location just in case things go south, however, before attempting this execute # 1 & 2 below since if there is a disk related issue you want to resolve that before putting further load on the system as that can damage the DB further   

-  As YukiSun suggested check out the APPLICATION & SYSTEM event logs.  Filter to only show critical and error events to determine the related issues to this  

-  If you see anything disk related in the SYSTEM event logs get those resolved first else you will just be creating more damage  

-  If the DB has damage you can run eseutil /P to see if it can be repaired, however, note the /P is a destructive process so you want to have an offline DB copy saved in an alternate location AND you want any disk related issues solved else you will damage the EDB more.  

-  If disk system is without issue the other option to get users back online in shortest amount of time would be to do a dial-tone restore and you can read more about that here https://support.lucid8.com/support/home[home][1]  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
