---
title: "On-Prem Forest Domain Controller Migration with Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/965853/on-prem-forest-domain-controller-migration-with-az
question_id: 965853
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# On-Prem Forest Domain Controller Migration with Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/965853/on-prem-forest-domain-controller-migration-with-az (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am looking for some best practices. Long story short, my company is breaking away from our parent company. Currently, the have a DC part of a forest (ad.lmm___.com). We are looking to build a new forest (core.lmm____.com). Our primary domain is (lmm___.com). After the forest is built, we will use the active directory migration tool and sync to Azure with the AD Connect tool. Once this is done, the plan is to have the users log in and start ADMT, let it do its thing. We just got out of a meeting between the 2 companies and I think we over complicated this process.      

Is there a best practice for this? My concern is our 0365 suite and Exchange 0365.    

Thank you in advance for any insight.     

Steven

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-17*

Hi Steven,    

I think some of the points are not clear, do you have your own tenant after the split? Where are the mailboxes hosted is it onprem or hybrid setup currently? Do you own the new domain name for the Azure setup? There are lot of questions and information required for this kind of scenario .    

I would suggest you follow this guidelines for Tenant to Tenant migrations - microsoft-365-tenant-to-tenant-migrations    

For Onpremise migration to another domain please follow the guidelines here  - cc974332(v=ws.10)
