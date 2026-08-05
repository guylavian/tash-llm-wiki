---
title: "Upgrade/Migrate Active Directory 2008 to Updated Version Learning Path"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289727/upgrade-migrate-active-directory-2008-to-updated-v
question_id: 1289727
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Upgrade/Migrate Active Directory 2008 to Updated Version Learning Path

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289727/upgrade-migrate-active-directory-2008-to-updated-v (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we have an old Windows 2008R2 Active Directory Server. Now we are planning to upgrade it to either 2016 or 2019 (Mostly thinking of 2019). What is the best way to do it? Thank you.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-23*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR   

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
