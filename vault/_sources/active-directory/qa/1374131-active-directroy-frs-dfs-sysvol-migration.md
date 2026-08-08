---
title: "Active Directroy FRS-DFS  SYSVOL MIGRATION"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374131/active-directroy-frs-dfs-sysvol-migration
question_id: 1374131
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directroy FRS-DFS  SYSVOL MIGRATION

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374131/active-directroy-frs-dfs-sysvol-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

```
I have 3 Windows 2012 R2 Domain controllers and one Windows 2008R2 Domain Controller, if i want to introduce Windows Server 2016 to my network, I will have to migrate FRS to DFS. I have already read the white paper.
```

https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr.

Please answer the following question before i proceed,

-  All FSMO roles are on Windows 2012 R2 shall I run the below command on all the servers  ? 

dfsrmig /setglobalstate 1

2)Do I have to install the DFS replication service on all the Domain Controllers ?

Note: We have been Upgrading Domain Controllers from Windows 2000.

Thanks

Syed

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-22*

Hello Dave thanx for the follow-up. I have succeeded with 2 stages and giving some time to servers before I start with stage 3

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-09-21*

All FSMO roles are on Windows 2012 R2 shall I run the below command on all the servers ?    

You can follow along here. FRS replication migration to DFSR       

Do I have to install the DFS replication service on all the Domain Controllers ?     

No, you do not.     

We have been Upgrading Domain Controllers from Windows 2000     

Domain controllers will need to be a minimum of Server 2008 before migration can take place.             

--please don't forget to close up the thread here by marking answer if the reply is helpful--
