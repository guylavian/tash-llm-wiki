---
title: "Convert a domain controller from datacenter to standard"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/211491/convert-a-domain-controller-from-datacenter-to-sta
question_id: 211491
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Convert a domain controller from datacenter to standard

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/211491/convert-a-domain-controller-from-datacenter-to-sta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have many domain controllers with Datacenter licence. Can we convert them to Standard version ?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-12-27*

No, you cannot downgrade the installation of windows from DataCenter to Standard. The simplest solution is to stand up a new one for replacement.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--    

please don't forget to Accept as answer if the reply is helpful--
