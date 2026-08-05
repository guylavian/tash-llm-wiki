---
title: "Domain controller 2008 R2 to server 2022 and Exchange 2010 to hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/906962/domain-controller-2008-r2-to-server-2022-and-excha
question_id: 906962
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller 2008 R2 to server 2022 and Exchange 2010 to hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/906962/domain-controller-2008-r2-to-server-2022-and-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have exchange 2010SP2 and domain controller server 2008R2 and planing for Hybrid migration with domain. Controller migration to 2022    

I am planing the below steps and need advise    

1- upgrade exchange 2010 SP2 to SP3    

2- do the cutover migration onshot all mailbox migration and    

3- change Mx record     

4- demote the exchange 2010 servers    

5-after exchange migration now i can  upgrade the 2008 R2 to direct 2022 or need to do first Domain controller server 2016 and after server 2016 to server 2022 is it correct?    

Please share advise

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-28*

Thanks for reply, but mu question is    

Can i direct migrate to server 2008R2 to server 2022    

Or need first 2008R2 to server 2016 and after 2022?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-28*

now i can upgrade the 2008 R2 to direct 2022 or need to do first Domain controller server 2016 and after server 2016 to server 2022 is it correct?    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
