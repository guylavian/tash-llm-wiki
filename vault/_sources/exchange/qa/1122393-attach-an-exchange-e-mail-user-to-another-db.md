---
title: "Attach an Exchange E-Mail User to another DB"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1122393/attach-an-exchange-e-mail-user-to-another-db
question_id: 1122393
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Attach an Exchange E-Mail User to another DB

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1122393/attach-an-exchange-e-mail-user-to-another-db (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Is it possible to remove an exchange user from a corrupted database and attach it to a healthy copy of the database? Move database operation is not working because the corrupted database is dismounted and cannot be mounted.    

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-09*

Thanks to all for the suggestions. The problem was resolved by following the article below:    

https://practical365.com/exchange-2016-failed-content-index/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-09*

Hi @create share      

please request to advise the version of exchange    

please try to see the below steps mention , hope it will help    

https://www.alitajran.com/move-mailbox-to-another-database-with-powershell/    

or    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recovery-databases?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-09*

You may need to use the dialtone recovery to bring the database up.    

Backup the corrupted logs and database by copying the data to a different directory.    

Create a dial tone database    

Re-home all user accounts to the new dial tone database    

Create a recovery database    

Mount/Dismount Recovery Database    

Move log files and database    

Restore email from the dial tone database back into the production database.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-09*

@create share       

You could try to follow this article to recover this database and mailboxes in it: Restore data using a recovery database in Exchange Server     

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
