---
title: "adding 2019 domain and tranferring FSMO roles from 2008 R2 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/611125/adding-2019-domain-and-tranferring-fsmo-roles-from
question_id: 611125
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# adding 2019 domain and tranferring FSMO roles from 2008 R2 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/611125/adding-2019-domain-and-tranferring-fsmo-roles-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI,  

i have a domain primary domain controller 2008 R2 along with additional domain controller 2012 R2 in my existing environment   

Recently we plan to upgrade domain controller to 2019 by adding as additional domain controller and then transfer the FSMO roles from 2008 R2 server.  

the steps I checked before adding 2019 domain controller to SYSVOL migration from FRS to DFRS  

I would like to ask here that if i migrate SYSVOL from FRS to DFRS does any of our existing sharing will get effect in our domain environment , we also have 2003 domain member server and it has application which run over sharing will it get effected when change occur of FRS to DFRS.  

kindly advise  

Regards,  

Ehsan

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-01*

if i migrate SYSVOL from FRS to DFRS does any of our existing sharing will get effect     

No, this only pertains to active directory replication.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
