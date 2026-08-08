---
title: "ADFS Database Login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315835/adfs-database-login
question_id: 315835
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Database Login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315835/adfs-database-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Considering options to migrate ADFS DB to cloud from Local SQL Server. Is it possible to reconfigure ADFS to use a local sql login instead of a domain users in DB?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-03-18*

Do you mean Azure SQL? If so, that's not supported.  

You might consider using the local WID instead of a SQL instance anyways. It is much easier to manage, does not require extra licenses nor an additional servers.
