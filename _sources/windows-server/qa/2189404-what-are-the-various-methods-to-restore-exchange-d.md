---
title: "What are the various methods to restore exchange database from backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189404/what-are-the-various-methods-to-restore-exchange-d
question_id: 2189404
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-virtualization-hyper-v"]
---
# What are the various methods to restore exchange database from backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189404/what-are-the-various-methods-to-restore-exchange-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an edb file in my backup and I want to restore it on the server. What are the methods that I can use to do so.  

-  I want to restore in the same AD forest  

-   I want to restore in a different AD forest

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-13*

Hi,

If you have created backups in Windows Server Backup, you can simply select "Action" > "Recover" to open the Recovery Wizard, choose the backup from which you want to recover the file, select "Files and folders" and browse for your edb file. Once you find the file, select it and choose the location where you want to restore it.
