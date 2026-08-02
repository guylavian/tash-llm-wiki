---
title: "Active Directory upgrade from 2008 r2 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/509601/active-directory-upgrade-from-2008-r2-to-2019
question_id: 509601
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory upgrade from 2008 r2 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/509601/active-directory-upgrade-from-2008-r2-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,  

I am going to perform an Active Directory upgrade from 2008 r2 to 2019 for a client.  

The 2008r2 infrastructure has an exchange 2010 deployed on it.  

I would like to know if there is some problem in performing the request without upgrading exchange.  

Kind regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-13*

Thank you so much DSPatrick for your valuable help

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-11*

Exchange 2010 looks to not be supported.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#supported-active-directory-environments    

As to AD upgrade; the two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
