---
title: "Exchange 2016 DAG - 1 out of 3 Database volume usage oversized?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113924/exchange-2016-dag-1-out-of-3-database-volume-usage
question_id: 113924
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 DAG - 1 out of 3 Database volume usage oversized?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113924/exchange-2016-dag-1-out-of-3-database-volume-usage (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have an Exchange 2016 DAG with 3x servers running CU17.  

I have many mailbox databases balanced with a copy on each server.  

One of my databases shows as healthy on EX1602 and EX1603 server with the volume sitting at 60% used but on EX1601 server that database copy of the same database on a volume the same size as the other servers shows as 90% used?  

The .EDB files are all the same size give or take a 180MB  

The Log file count is much higher on the FULL volume on EX1601 but it only translates into 500MB  

F:\System Volume Information - this hidden system folder is ballooned to nearly 200GB  

Any ideas why and how I could resolve this as I cannot access this folder?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-01*

Hi Heath,  

If you want to shrink that folder, try this:  

https://www.howtogeek.com/282214/what-is-the-system-volume-information-folder-and-can-i-delete-it/
