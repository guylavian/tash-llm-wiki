---
title: "Exchange 2016 Indexing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1146261/exchange-2016-indexing
question_id: 1146261
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Indexing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1146261/exchange-2016-indexing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I seem to be having a fun time with a Database and search not working.     

I followed the standard go to:    

```
Get-Service -Name "HostControllerService","MSExchangeFastSearch" | Stop-Service
```

went to DB folder and deleted the GUID.single file    

```
Get-Service -Name "HostControllerService","MSExchangeFastSearch" | Start-Service
```

and then     

```
Get-MailboxDatabaseCopyStatus * | Sort Name | Select Name, Status, ContentIndexState
```

normally it would show the database as crawling and start rebuilding the GUID dir     

however it shows as healthy, no sign of a GUID and search is def not working on Outlook or OWA    

```
Get-MailboxDatabase | Select-Object Name, IndexEnabled | Format-Table -AutoSize
```

DB shows as True so indexing seems to be enabled. I'm stumped, any help would be appreciated tyia

## Answers

_No answers on this thread._
