---
title: "Active Directory Replication Difference between SYSVOL and AD changes for example password changes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1168555/active-directory-replication-difference-between-sy
question_id: 1168555
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Replication Difference between SYSVOL and AD changes for example password changes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1168555/active-directory-replication-difference-between-sy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

WE are in the process of adding the first Windows 2019 domain controllers to a domain currently consisting of only 2008R2 DC's with a 2008R2 Domain and Forest functional level. There are two domains, a parent and child and the new 2019 DC's will only be added to the Child domain. We will be migrating from FRS to DFSR in the child domain as the first step in this process but my question is do I need to migrate from FRS to DFSR in the parent domain, which wont contain 2019 DC's,  as my assumption was that I didn't as FRS or DFSR are only used for the SYSVOL and AD objects are replicated via RPC to other DC's. Can anyone confirm if my assumption is correct please.

Thanks in advance.

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2023-02-07*

Yes, your steps sound good. Each domain FRS->DFSR migration can proceed separately.   

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
