---
title: "Exchange 2013 Integrity Check"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/139972/exchange-2013-integrity-check
question_id: 139972
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 Integrity Check

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/139972/exchange-2013-integrity-check (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have recently run an eseutil integrity check on my exchange 2013 database. I am receiving one particular warning in the log file it produced very frequently. I am not able to find good information on what the warning means. Please see warning below, any insight would be helpful.  

WARNING: orphaned LV (lid 18500, refcount 0). Offline defragmentation should fix this.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

Thank you for the explanation that makes much more sense now. I am sorry, I mistyped, we have 90+ accounts in the particular database that is getting the Orphaned LV warning. So, no we don't have a DAG. What would be the risk of leaving the database as is with the orphaned LV errors?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

It was an issue where 4 databases got corrupt at the same time with 90+ accounts. We were able to recover from backups. We have yet to discover what the issue was that corrupt the databases as we have redundant hardware and HA cluster. Either way i respect your opinion as to why we would run eseutil. Can you please let me know what would be a more effective way to find the integrity of our databases and or please answer the original question which no one seems to know the answer to?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-26*

Just curious why you ran this in the first place?  :)  

Honestly, running integrity checks or doing anything with eseutil is really old hat and not something I would even bother with.  

If you are experiencing issues, then simply move mailboxes to another database and remove the problematic database.
