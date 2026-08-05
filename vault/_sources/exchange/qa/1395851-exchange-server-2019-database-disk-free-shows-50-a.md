---
title: "Exchange Server 2019 Database Disk Free shows 50% available"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1395851/exchange-server-2019-database-disk-free-shows-50-a
question_id: 1395851
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 Database Disk Free shows 50% available

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1395851/exchange-server-2019-database-disk-free-shows-50-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have Exchange 2019 DAG, as we check for Environment Status, it shows most of the DBs Database Disk Free as 50 or 60 percent. however we have huge Space available in the Volume where these DBs are mounted.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-22*

Dear,

Its a new 2019 DAG, we have Volumes of 6 TB, which has 4 DBs, each DB currently holding only around 200 MB (total Mailboxes) that means all 4 DBs together holding around 1 GB only. But as I mentioned before it shows "Database Disk Free shows as 50% available". Even DB2 has just 1 MB used size still shows 60% available.  

Please note we are about to migrate mailboxes in those DBs from old DAG (2016). so we are little worried can we start migration or has to do some work around or its just normal to show this percentage.

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-19*

Hello,

First of all, we’d like to know if you want to ask why the actual occupied space is larger than you expected or what causes the difference between the available disk space and the displayed available space?

Based on your description, it is recommended that you first check the disk usage statistics and check whether it is the space occupied by the database itself or the log file.

If it is the database itself, it can be speculated that there should be white space in the Exchange database, so it is recommended that you refer to the following link to clear the white space to improve utilization.

https://www.alitajran.com/clear-white-space-in-exchange-database/

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the log file takes up a large amount of space, there may be a problem with log file accumulation due to replication delays between database copies. For more information, visit Manage mailbox database copies | Microsoft Learn. When encountering this situation, first check the replication status and queue length of all replicas in the DAG to determine whether there is a replication delay or failure. We recommend that you use the Get-MailboxDatabaseCopyStatus cmdlet to obtain this information. More information can be found at Monitoring Database Availability Groups | Monitoring Database Availability Groups. If you notice a replication problem, you can try restarting the replication service or reactivating the affected replica, or you can consider temporarily pausing or deleting the problematic replica to free up disk space.

If there is any inappropriate understanding, please correct me.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
