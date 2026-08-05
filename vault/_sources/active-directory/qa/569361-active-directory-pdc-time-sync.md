---
title: "Active Directory PDC time sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/569361/active-directory-pdc-time-sync
question_id: 569361
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory PDC time sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/569361/active-directory-pdc-time-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an Active Directory Parent & Child Domain Hierarchy.  

We have root Domain's PDC is in Azure & I can see it is taking time from "VM IC Time Synchronization Provider" so do we need to sync this PDC emulator with external time source or we can rely on Azure ( I mean we don't need to be do anything as that PDC is on Azure)?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-28*

There is no right or wrong answer but I suggest to review the contents - https://learn.microsoft.com/en-us/azure/virtual-machines/windows/time-sync    

There may be delay upto 30 seconds, during memory preserving maintenance. I think you can go with both the options - internal and external time server.
