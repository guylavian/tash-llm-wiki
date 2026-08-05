---
title: "Exchange 2016 renaming default database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/146179/exchange-2016-renaming-default-database
question_id: 146179
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 renaming default database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/146179/exchange-2016-renaming-default-database (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016- Planning to rename default database. Once it is renamed, does it rename the *.edb file and the root folder name as well, or does it maintain the existing folder and *.edb name? Does the folder path change from:  

 \mdb_default\mdb_default.edb   to   \mdb_newname\mdb_newname.edb  or does it change to  \mdb_default\mdb_newname.edb  ?   

If it does keep those elements, and i want to have a different folder/database name, do i need to delete the default and recreate a new database if i have already created 4 other databases besides the default?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-01*

Can I rename DB in production server ?
