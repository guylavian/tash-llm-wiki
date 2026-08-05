---
title: "Migrate AD Domain 2012 to 2025 but have no SYSVOL netlogon folder."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2246972/migrate-ad-domain-2012-to-2025-but-have-no-sysvol
question_id: 2246972
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Migrate AD Domain 2012 to 2025 but have no SYSVOL netlogon folder.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2246972/migrate-ad-domain-2012-to-2025-but-have-no-sysvol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have old system AD Domain run in window server 2012, PDC name is ADOLD, hole FSMO role. Run dcdiag /s with no faile. I want to migrate it to window server 2025. To do that, I have to move my system to a host term run window server 2019, name ADTemp. 

When I promote ADTemp become a Domain controler, Netlogon and SYSVOL folder are missing. I run dcdiag /s and have this error:

"   ....... ADTEMP failed test DFSREvent

```
......................... ADTEMP failed test NetLogons
``` Starting test: SystemLog

```sql
     An error event occurred.  EventID: 0x00000422
```   ...... ADTEMP2K19 failed test SystemLog"

I still move FSMO role to ADTemp and demote ADOLD. The synchronization process is still functioning normally; I can still create users and log in to the domain.

I add 2 window server2025 AD01, AD02 in domain and promote them to Domain controler. The netlogon, SYSVOL folder still not found. 

I run cmd   dcdiag /s in two server and both have this error:  
--------------

 . AD01 failed test Advertising AD01

 failed test NetLogons

. AD01 failed test SystemLog

The synchronization process is still functioning normally; I can still create users and log in to the domain. 

In all server, service Netlogon, NTDS, DFSR are running

What do I need to do to fix these errors? Since my domain services are currently running, there are many risks involved, so everything needs to be done carefully.
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-15*

HI,

Have you confirmed that your AD's SYSvol has been migrated from FRS to DFSR?

dfsrmig /getglobalstate

Refer https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr

Regards,
