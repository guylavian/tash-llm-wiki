---
title: "Move System Mailboxes in Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1370272/move-system-mailboxes-in-exchange-2013
question_id: 1370272
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Move System Mailboxes in Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1370272/move-system-mailboxes-in-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have two databases in the C drive that take up much space. When I am checking the mailboxes in EMC, none exists under these DBs. I believe the system mailboxes are under these DBs. How can I move these mailboxes to another partition?

Exchange 2013 on Premise DAG (2 Nodes)

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-18*

Hi @ create share ,

Just wondering if you already have a mailbox database installed in another partition?

If so, you can migrate the arbitration mailboxes to the database by following these steps:

-  Run the following command in EMS to view the location of the arbitration mailboxes:

```
Get-Mailbox -Arbitration | Format-Table Name, ServerName, Database, AdminDisplayVersion
```

 

-  Check the name of the mailbox database in your environment:

```
Get-MailboxDatabase  | Sort Name | Format-Table Name, Server, Mounted, AdminDisplayVersion，EdbFilePath
```

-  Use the following command to migrate the arbitration mailboxes to the database in a different partition:

```
Get-Mailbox -Arbitration | New-MoveRequest -TargetDatabase "DB02"
```

-  Check the progress of the arbitration mailboxes move request:

```
Get-MoveRequest | Get-MoveRequestStatistics
```

-  Verify that the arbitration mailbox was successfully moved to the target database:

```
Get-Mailbox -Arbitration | Format-Table Name, ServerName, Database, AdminDisplayVersion
```

 

If the mailbox database does not exist in the other partition, you can refer to this link to migrate the mailbox database to a different disk：

https://www.alitajran.com/move-exchange-database-to-another-drive/

（Note:Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.）

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
