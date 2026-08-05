---
title: "Exchange 2016 Recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/109658/exchange-2016-recovery
question_id: 109658
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
---
# Exchange 2016 Recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/109658/exchange-2016-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We are using Veeam to backup 2 X Exchange 2016 Mailbox servers. It's configured as application aware backups. Both the servers are part of a single DAG with 10 Databases (5 active on 1st server and another 5 with second server). With Veeam, Full server backup is configured with passive database volumes and excluded active DB volumes. In case of a disaster, how can we recover the servers in following scenarios?  

a) Single server failure  

In this case, the second server will have all DBs with active copies. We restore the failed server with volumes contains passive copies. There after we create 5 new volumes and attach to the restored server. Then how exactly can we proceed and check the DB health?  

b) Both servers failed  

We will restore both the servers with volumes containing passive DB volumes. It's not clear how to proceed further  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-04*

Hi  

Single server failure situation can be managed with above comments and there are docs available for it. But we didn't find any docs saying how to restore the DAG in case of a complete DAG member failure (we have 2 X servers in single DAG in single AD site)

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-03*

Hi  

Are you doing snapshots of your servers? Remember restoring a VM back in time will result in dataloss.  

If you lose a node in a DAG, you firstly can shutdown that node, Reset the computer account in AD and then create a new VM with the same name and IP and join it back to the domain. After that you can get all the updates done and then when you install Exchange again, you will use the recovery switch. After that apply any security updates for that CU and then you need to remove the member from the DAG and its copies before you can add it back to the same DAG. Once added back to the DAG you can then seed you copies again.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-29*

-  Follow this link to restore a failed server: https://practical365.com/exchange-server/recovering-a-failed-exchange-2016-database-availability-group-member    

     And you can run these commands to verify the health and status of the recovered DAG member:  

    Test-ReplicationHealth <ServerName>  

    Get-MailboxDatabaseCopyStatus -Server <ServerName>  

-  So the DAG is losing quorum, you should ask for support from Veeam.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
