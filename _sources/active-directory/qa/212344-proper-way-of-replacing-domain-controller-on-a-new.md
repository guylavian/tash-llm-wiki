---
title: "Proper way of replacing Domain Controller on a new hardware (+ changing version old-2008r2, new- 2012r2)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/212344/proper-way-of-replacing-domain-controller-on-a-new
question_id: 212344
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Proper way of replacing Domain Controller on a new hardware (+ changing version old-2008r2, new- 2012r2)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/212344/proper-way-of-replacing-domain-controller-on-a-new (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'd like to pick the brain of some of you for the proper way of replacing Domain Controller on a new hardware (old-2008r2, new- 2012r2)? What will be the steps to achieve this one? I presume I leave 2008r2 up and running, while installing 2012 r2, transfer roles from the former then demote 2008r2 and clean the meta. Can somebody write down the proper sequence to do this. Does changing the version mean something? Same hardware vs new one?  

Thank you!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-28*

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2012, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

Also at some point either before or after I'd recommend migrating sysvol replication from older FRS technology to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to Accept as answer if the reply is helpful--
