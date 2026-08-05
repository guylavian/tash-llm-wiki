---
title: "I am decommissioning a AD Domain Controller & DNS Manager and want to know how to move the Global Logs folder."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1334369/i-am-decommissioning-a-ad-domain-controller-dns-ma
question_id: 1334369
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# I am decommissioning a AD Domain Controller & DNS Manager and want to know how to move the Global Logs folder.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1334369/i-am-decommissioning-a-ad-domain-controller-dns-ma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are decommissioning a windows 2012 R2 Domain Controller, this was the original domain controller.  There are four other DCs running.  This DC being decommisssioned does not contain any FSMO roles. Under DNS manager it shows a "Global Logs" folder and a "Cached Lookups" folder.  When viewing DNS Manager on the other four DCs neither the Global Logs or Cached Lookups folder exists.  Do we need to migrate/add these folders to one of the remaining DNS managers?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-04*

In DNS Manager, select your DC then click "View" and select Advanced - this will show the Cache Lookups folder.

Im still searching on how to add the Global Logs folder...

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-07-21*

No, nothing needs to be done here.     

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR     

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
