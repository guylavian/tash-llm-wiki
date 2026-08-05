---
title: "FRS migration to DFSR, SYSVOL not deleted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160848/frs-migration-to-dfsr-sysvol-not-deleted
question_id: 1160848
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# FRS migration to DFSR, SYSVOL not deleted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160848/frs-migration-to-dfsr-sysvol-not-deleted (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

I migrated 8 Windows Server  (2012 R2 and 2016) from FRS to DFSR. A root domain has 4 servers and a child domain 4 servers.  

On 6 servers I see Sysvol_DFSR only and 2 servers have Sysvol and Sysvol_DFSR. The two servers are in the child domain. On all 8 servers the File Replication Service is disabled and replication is working fine.

My question is if the Sysvol folder can be deleted manually, there are only a few empty Policy folders inside.  

Regards  

Romar

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-14*

The underlying folder on the DCs that were migrated (FRS to DFSR) will be Sysvol_DFSR but the share name for all is Sysvol the folder name and share name for new DCs will be Sysvol when migration is completed the original SYSVOL folder is removed from the DC. If it's still there I'd make sure the migration completed without errors. (check DFSR Replication event logs) and check Dfsrmig /getmigrationstate (especially on the suspect ones)  

 --please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
