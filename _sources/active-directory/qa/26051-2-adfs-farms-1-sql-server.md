---
title: "2 ADFS Farms 1 SQL Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/26051/2-adfs-farms-1-sql-server
question_id: 26051
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# 2 ADFS Farms 1 SQL Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/26051/2-adfs-farms-1-sql-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently planning on rebuilding my ADFS farm from scratch and point it to a new domain (sts.example2.com)  

My current ADFS Farm (sts.example1.com) uses SQL server for the configuration and artifact databases.  

The configuration database will not be an issue (i think) as i will install it on Windows Server 2019 and ADFS should create the default database with the prefix V4 (current one on Windows Server 2016, prefix V3 for the database).  

My question is related to the Artifact resolution database. As i only have access to one SQL Server instance would there be any issues with the farms if they share the same Artifact resolution database? From what i read there is no way to change the name of the DB during the initial setup. Can i setup it up using the default and then point it to a different database?  

Cheers and thanks.

## Answers

_No answers on this thread._
