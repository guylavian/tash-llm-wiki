---
title: "Exchange Migration 2010 to 2016 with automatic Mailbox Distribution - Question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/116669/exchange-migration-2010-to-2016-with-automatic-mai
question_id: 116669
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Migration 2010 to 2016 with automatic Mailbox Distribution - Question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/116669/exchange-migration-2010-to-2016-with-automatic-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

i have a DAG based on Exchange 2010 and another DAG based on Exchange 2016. Now i want to migrate users from an Exchange 2010 database to Exchange 2016 by powershell. I want to use automatic distribution of the Mailboxes.   

I will use powershell to list the users of a database and will execute via foreach-object something like New-Moverequest  -Identity $_.Name    

As long as i do not use the parameter target-databas - the automatic distribution will be uses. So for now everything is fine, but i have a question:  

Will the command automatically migrate the users mailboxes to my Exchange 2016 DAG?  

Or do i have exclude the Exchange Databases 2010 by  IsExcludedFromProvisioning $true, because otherwise they will be a possible targetdatabase in my new-moverequest command?  

Thanks  

Micha

## Answers

_No answers on this thread._
