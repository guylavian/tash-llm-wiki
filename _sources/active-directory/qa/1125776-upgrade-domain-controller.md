---
title: "Upgrade Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1125776/upgrade-domain-controller
question_id: 1125776
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Upgrade Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1125776/upgrade-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,     

What are the pre and post pre-requisite to upgrade the Domain controller from 2012 to 2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-14*

Currently we have around 10 DCs in three sites in 2012 and 2016 OS    

-   How to verify application compatibility for extend forest and domain level version.    

-  What should I plan for roll back plan?    

-  what will be the exact command for pre-post task to verify DC is healthy

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-13*

Current DC's are in VM and new DC will also be VM.    

Makes no difference, what I posted above still applies.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-13*

Any idea if any checklist before upgrade ? Current DC's are in VM and new DC will also be VM.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-12*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
