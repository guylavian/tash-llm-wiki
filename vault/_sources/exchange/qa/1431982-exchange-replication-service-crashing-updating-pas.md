---
title: "Exchange Replication service crashing updating passive copy on One DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1431982/exchange-replication-service-crashing-updating-pas
question_id: 1431982
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Replication service crashing updating passive copy on One DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1431982/exchange-replication-service-crashing-updating-pas (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am getting these errors 

Resume database guid=1bf78381-0e9f-4453-aaac-e2a5c0417e6b failed: The database copy could not be resumed because of a previous error that is preventing the resume operation. Error: A seed had begun for database copy 'DB02\L2PRDVESDR02030' but got interrupted probably because of a crash in the Microsoft Exchange Replication service. Please restart the seed using the Update-MailboxDatabaseCopy cmdlet. The following arguments were used:

RpcSeederArgs: [ InstanceGuid='1bf78381-0e9f-4453-aaac-e2a5c0417e6b', DeleteExistingFiles='True', AutoSuspend='False', SeedingPath='', LogFolderPath='', NetworkId='', StreamingBackup='False', SourceMachineName='L2PRDVESDR04030.ztbl.com.pk', DatabaseName='', ManualResume='False', SeedDatabase='1', SeedCiFiles='1', MaxSeedsInParallel='0', SafeDeleteExistingFiles='False', Flags='SeedMetaCacheDB', CompressOverride=''='<null>', EncryptOverride='='<null>' ].

SERVER SIDE administrative operation has failed the database copy could not be resumed because of previous error 

seed error had begun on DB\02 BUT got interrupted because of crash in Microsoft Exchange Replication  please restart

using update mailbox copy cmdlet the following arguments were used RPCSeederARGS:

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-21*

Hi @azhar Nasim,

Have you tried restarting the Microsoft Exchange Replication service on the affected server and restart the seeding process?

Besides, would you find error or warning events generated in event viewer on this server when this issue occurs?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
