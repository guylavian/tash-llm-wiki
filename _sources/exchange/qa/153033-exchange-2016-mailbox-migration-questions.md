---
title: "Exchange 2016 (mailbox migration questions)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153033/exchange-2016-mailbox-migration-questions
question_id: 153033
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange 2016 (mailbox migration questions)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153033/exchange-2016-mailbox-migration-questions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

Going through finalizing a migration and wanted to check to make sure all of my bases were covered.  I came across the following article that is really good, but it did bring up a a couple of things I wanted to make sure I am clear on.    

https://social.msdn.microsoft.com/Forums/en-US/81a0d712-7726-452c-a4cd-97fae2b96d02/exchange-2013-to-2019-migration-move-monitoring-mailboxes?forum=Exch2019  

-   The article (and others) call out first running Set-AdServerSettings -ViewEntireForest $true.  I would assume that in a single Exchange ORG/Forest, this is not needed.  Is that correct?  If it is required in a single Forest, is it because it provides visibility to all system mailboxes to make sure no mailboxes are missed?  

-   Based on the article, we have migrated the following below, but have not migrated the monitoring mailboxes because they are not required to move and having them in the old environment won't prevent the database deletions when we decom the servers.  The article references to migrate them, but I do not believe its needed.  That is my understanding.  Is that correct?   

Have already migrated the following mailboxes:  

User, Shared, Room. & Equipment  

Arbitration  

DiscoverySearch  

AuditLog  

Public Folder  

Any other mailbox gotchas I might have missed?  

Thanks,  

CWT

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-05*

I missed that when I went back through my threads and searched the forums.  Thank you for calling that out and thanks in general.  

CWT
