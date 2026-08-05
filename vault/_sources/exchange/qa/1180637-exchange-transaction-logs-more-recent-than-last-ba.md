---
title: "Exchange transaction logs more recent than last backup time on a database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180637/exchange-transaction-logs-more-recent-than-last-ba
question_id: 1180637
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange transaction logs more recent than last backup time on a database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180637/exchange-transaction-logs-more-recent-than-last-ba (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Event ID 2137 for each database copy on this server that has all passive copies. It is the server targeted by the backup solution (Hycu) for backing up all the databases for this DAG. The event reads as follows:

RPC request to the Microsoft Exchange Information Store service for log truncation failed for database <DB Name><server name>. Error: Failed to notify source server '<another server in the DAG>' about the local truncation point. Hresult: 0xc8000713. Error: Unable to find the file.

I think it's because the oldest transaction log is from January, but the database in this particular instance was last fully backed up in December (per Exchange, but not per Hycu). Exchange is looking for transaction logs back in December that don't exist or something. Any ideas on how to resolve this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-02*

https://notes.doodzzz.net/2017/01/30/microsoft-exchange-server-2013-dag-failed-to-notify-source-server-about-the-local-truncation-point/

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-14*

Can you backup the active copy of each database instead? 

Another option would be to enable circular logging and see if that removes them all. 

CAUTION: If you do this, you must take a full backup before and after, then disable circular logging afterward if it clears the logs

Alternatively, remove the logs manually, but CAUTION again and NOT supported:

https://social.technet.microsoft.com/Forums/windows/en-US/79c8f5b9-6d05-4d0e-90d4-5854e9d72639/how-to-manual-delete-the-transaction-logs?forum=exchangesvrgenerallegacy
