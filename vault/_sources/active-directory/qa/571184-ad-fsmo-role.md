---
title: "AD - FSMO Role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/571184/ad-fsmo-role
question_id: 571184
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# AD - FSMO Role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/571184/ad-fsmo-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

I have AD Server running windows 2012 r2 (FFL/DFL). I'm planning to update 2016.  

Can anyone guide me if any prerequisites to validate before update forest and domain function level from Windows Server 2012 r2 to 2016  

Thanks in advance.!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-29*

@Gopi Ponnusamy    You can find detailed information, process and requirements here - https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/raise-active-directory-domain-forest-functional-levels

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-09-29*

Hi,  

Before upgrade the DFL and FFL from windows 2012 R2 to Windows 2016, you have to upgrade all your domain controllers on Windows 2016 if you still have a domain controllers on windows 2012. All domain controllers in your forest must be installed on Windows 2016 or higher to be able to upgrade the domain functional level DFL and forest functional level FFL to windows 2016.  

If you are talking about domain controller OS upgrade from windows 2012 to 2016 , with domain controller on windows 2012 R2 , you can promote an additional domain controller on windows 2016 and demote DC windows 2012 because windows 2016 ans Windows have the same prerequisite.   

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-29*

The prerequisite before introducing the first 2016 domain controller: domain functional level needs to be 2003 or higher    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2016, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

Also at some point either before or after I'd recommend migrating (if not already done) sysvol replication from older FRS technology to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
