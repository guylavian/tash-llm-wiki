---
title: "upgrade windows 2008 R2 Domain Controllers to Windows 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1109601/upgrade-windows-2008-r2-domain-controllers-to-wind
question_id: 1109601
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# upgrade windows 2008 R2 Domain Controllers to Windows 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1109601/upgrade-windows-2008-r2-domain-controllers-to-wind (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have a couple of domain controllers running on Windows 2008 R2, there is a need to upgrade to Windows server 2019, these new domain controllers will keep the same hostname and IP address.     

I consider these are the steps:    

-  Check if AD environment is healthy (Dcdiag /v, repadmin /showrepl, and repadmin /replsum).    

-  Demote one Windows server 2008 R2 and power it off.    

-  Change the hostname of one of the Window server 2019 VMs, assign the IP previously used by the windows 2008 VM, and Add it to this existing domain.    

-  Add AD DS and DNS roles and promote this Windows server 2019 as a DC.    

-  Transfer FSMO roles to new 2019 DC if needed.    

I have some questions, hope you could help me:    

-  Do I have to run adprep /forestprep and adprep /domainprep commands on Windows DC before promoting the new DC with Windows 2019?     

-  I have some virtual machines running Terminal Server services, these vms ar running on Windows 2008 R2 as well, If I upgrade all my DCs to windows 2019, the Terminal Server services will have issues?    

-  since there are other services running on Windows Server 2008 (SQL server DBs), I am thinking of: not upgrade the forest and domain functional level, could this help?    

Thanks  in advance.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-30*

Do them one at a time moving roles off and demoting.    

Adprep is now a built-in part of domain controller promotion.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
