---
title: "Server 2012 sysvol has many extra folders."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327309/server-2012-sysvol-has-many-extra-folders
question_id: 327309
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Server 2012 sysvol has many extra folders.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327309/server-2012-sysvol-has-many-extra-folders (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A client site has two server 2012 DC which has sysvol replication problem using FRS.    

dcdiag - all passed    

net share netlogon and sysvol - normal    

can ping each other using FQDN - normal    

When test to place a file "abc.txt" on DC1\netlogon, "abc.txt" wasn't copied to DC2\netlogon.    

Then tried the following steps.    

-  net stop ntfrs (on two DC)    

-  Change the Burflags registry key from 0 to D4    

   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NtFrs\Parameters\Backup/Restore\Process at Startup    

-  net start ntfrs (on two DC)    

-  An event 13565 is logged to signal that a nonauthoritative restore is started.    

dcdiag - both DC server will have the following results    

      Starting test: FrsEvent  

         There are warning or error events within the last 24 hours after the  

         SYSVOL has been shared.  Failing SYSVOL replication problems may cause  

         Group Policy problems.  

Ever restart server but still not help.    

Then repeat above steps and find that there are a lot of folders in sysvol.      

    

The replication is solved suddenly now.   Can we delete "Polices_NTFRS...." files  directly in picture safely? Please help.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-23*

Safer method may be to move roles off, demote server, do cleanup, reboot, promo the problematic one again.  

--please don't forget to Accept as answer if the reply is helpful--
