---
title: "Event ID 4017 MSExchangeIS every 15 minutes for one database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2114632/event-id-4017-msexchangeis-every-15-minutes-for-on
question_id: 2114632
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Event ID 4017 MSExchangeIS every 15 minutes for one database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2114632/event-id-4017-msexchangeis-every-15-minutes-for-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are migrating mailboxes  with -SuspendWhenReadyToComplete from Exchange 2016 to a new databases in Exchange 2019 CU14

No mailboxes migrated at 100% yet

Only ONE database  for each node of the new DAG in Exchange 2019 generate the event ID 4017 every 15 minutes

The Timed Events Processing is delayed for database XXXXX (Oldest event: 10/23/2024 10:08:00 AM, Skipped Events: 1, Skipped mailboxes: 1)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-04*

Hi @Sara Rojas  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are experiencing timed event processing issues during mailbox migration. Event ID 4017 indicates a processing delay, which can be due to a number of reasons. Here are a few steps you can take to troubleshoot and resolve this issue:

-  Make sure your Exchange server has enough resources (CPU, memory, disk I/O) to handle the migration process. Resource limitations can cause processing delays.

-  Verify the health of the databases involved. Use the Get-MailboxDatabaseCopyStatus cmdlet to check the status of database copies and make sure they are running properly.

-  Large or highly active mailboxes can sometimes cause delays. Consider temporarily reducing the load by staggering the migration of larger mailboxes.

-  You can try pausing and then resuming the migration batch to see if that eliminates the delay.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
