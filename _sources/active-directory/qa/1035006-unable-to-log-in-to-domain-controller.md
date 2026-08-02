---
title: "Unable to log in to domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1035006/unable-to-log-in-to-domain-controller
question_id: 1035006
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Unable to log in to domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1035006/unable-to-log-in-to-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've promoted two different 2019 servers to domain controllers in an AD domain that consists of 2012R2 domain controllers. On both servers, after adding the ADDS role and running DCPROMO I am unable to log in to the servers. The error I'm getting is "The User Profile Service service failed the sign-in. User profile cannot be loaded."    

We get his regardless of what account we try to log in with.    

I've never seen this issue before with newly promoted DC's. Does anyone have any suggestions on how to resolve this?    

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-06*

Hard to say what has happened, may need to rebuild it from scratch.     

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
