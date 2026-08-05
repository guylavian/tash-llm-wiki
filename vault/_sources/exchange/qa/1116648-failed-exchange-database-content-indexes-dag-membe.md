---
title: "Failed Exchange Database Content Indexes (Dag Member)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1116648/failed-exchange-database-content-indexes-dag-membe
question_id: 1116648
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Failed Exchange Database Content Indexes (Dag Member)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1116648/failed-exchange-database-content-indexes-dag-membe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am getting "Failed Exchange Database Content Indexes" for a database added in Exchange 2013 DAG. The database is added only to one of the DAG members. The database is dismounted. If I try to mount, it shows the below error:    

Failed to mount database dbname.edb". Error: An Active Manager operation failed. Error: The database action failed. Error: Operation failed with message: MapiExceptionDatabaseError: Unable to mount database. (hr=0x80004005, ec=1108) Diagnostic context: Lid: 65256 Lid: 10722 StoreEc: 0x454 Lid: 1494 ---- Remote Context Beg ---- Lid: 45120 dwParam: 0x677817A9 Lid: 57728 dwParam: 0x67781874 Lid: 46144 dwParam: 0x67781C2D Lid: 34880 dwParam: 0x67781C2D Lid: 34760 StoreEc: 0xFFFFFDE3 Lid: 41344 Guid: 6cc6accc-98d5-4741-9fb6-97f6fd6f8d96 Lid: 35200 dwParam: 0x5D98 Lid: 46144 dwParam: 0x677829F8 Lid: 34880 dwParam: 0x677829F8 Lid: 54472 StoreEc: 0x1388 Lid: 42184 StoreEc: 0x454 Lid: 1750 ---- Remote Context End ---- Lid: 1047 StoreEc: 0x454 [Database: dbname.edb, Server: exch02.domain.com]

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-05*

Tried    

"Update-MailboxDatabaseCopy dbname\exch02 -CatalogOnly -BeginSeed"    

but it says    

"The operation couldn't be performed because object 'dbname\exch02' couldn't be found on    

'dc01.domain.com'."    

There is only one copy of this database that exists on exch02.
