---
title: "System Mailbox database redundancy check failures"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1623844/system-mailbox-database-redundancy-check-failures
question_id: 1623844
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# System Mailbox database redundancy check failures

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1623844/system-mailbox-database-redundancy-check-failures (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are a hybrid deployment. We have two exchange 2019 servers. User mailboxes migrated to Exchange Online. We have two mailboxes on prem for our archive application. We have an smtp relay for our in-house apps and multifunction printers.   We had an outside consultant do the hybrid setup and migration.  We have DB1 and DB2 on server1.  DB3 and DB4 on server2. When I run the Test-Replication command, I get the following for the SYSTEM mailbox on each server.  Is this a concern?  If so, how do I correct?  Thanks.

   DatabaseRedundancy FAILED   There were database redundancy check failures for database

   'Mailbox Database ##########' that may be lowering its redundancy and putting the  database at risk of data loss.  Redundancy Count: 1. Expected Redundancy Count: 2. Detailederror(s):Database 'Mailbox Database ##########' does not have enough copies configured to meet the validation criteria.

DatabaseAvailability  FAILED   There were database availability check failures for database

 'Mailbox Database ##########' that may be lowering its availability. Availability Count: 1. Expected Availability  Count: 2. Detailed error(s): Database 'Mailbox Database ##########' does not have enough copies configured to meet the validation criteria.

## Answers

_No answers on this thread._
