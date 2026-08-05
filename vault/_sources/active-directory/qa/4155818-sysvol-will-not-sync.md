---
title: "SYSVOL will not sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4155818/sysvol-will-not-sync
question_id: 4155818
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# SYSVOL will not sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4155818/sysvol-will-not-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 16 DC in my enviroment, all 2019 Standard. I have one that will not sync sysvol, only noticed after GP changes didn't go out to a certain site. There are no other replication issues on this or any other DC, just DFSR on the one. I have tried every fix I can find with no luck. Here is everything I've done, hopefully someone out there has some insight. 

Demoted DC, removed AD DS and then brought it back as a DC. Figured I'd just start here instead of messing around but unfortunately didn't work. Sysvol and Netlogon shares were not created after promotion so followed this to fix

[Solved] SYSVOL and NETLOGON Shares Missing on New DC (thesysadminchannel.com)

Most things pointed to this article as the fix

Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server | Microsoft Learn

I got the 4114 event after disabling but then nothing after setting back to True.

Next I followed 

Troubleshoot missing SYSVOL and Netlogon shares for Distributed File System (DFS) Replication - Windows Server | Microsoft Learn

It comes back with "no instance(s) available." then points to the above arcticle as the fix which already failed to fix

Verified HKLM\System\CurrentControlSet\Services\DFSR\Parameters\ DWORD:StopReplicationOnAutoRecovery was set to 0 and ran the wmic resumereplication command but also came back with "no instance(s) available." 

Verified all keys in "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DFSR" match other non-authoritive DCs

Verified permissions are correct on c:\system volume information and windows\sysvol

All DCDIAG and REPADMIN tests come back without error

If you need any other info to help, please let me know

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-04-06*

Hi, I'm David.

Sorry. The Microsoft Community is a forum for home users.

Due to the scope of your question, I suggest you access the link below, which will direct you to the Microsoft Q&A page.

https://learn.microsoft.com/en-us/answers/index...

Microsoft Q&A has IT professionals and system administrators who can best help with this type of question.

Best regards.
