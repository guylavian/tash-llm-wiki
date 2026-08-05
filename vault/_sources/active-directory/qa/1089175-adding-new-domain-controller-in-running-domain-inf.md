---
title: "Adding new domain controller in running domain infrastructure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1089175/adding-new-domain-controller-in-running-domain-inf
question_id: 1089175
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Adding new domain controller in running domain infrastructure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1089175/adding-new-domain-controller-in-running-domain-inf (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We currently have two domain controllers in our infrastructure in a single forest. The domain controllers have Windows Server 2008R2 OS and DFL/FFL is 2008.    

Plan is to add two new domain controllers of either Windows Server 2016 or 2019 OS version, replicate the two new domain controllers with the existing two domain controllers and then switch the IP of new domain controllers (Windows Server 2016 or 2019) with the same IP that is being currently being used by Windows Server 2008R2 domain controllers. This is to ensure there are network access issues for client authentication (kerberos/ldap).    

When we proceed with setup of new domain controller we plan to block network access to this domain controller from the client systems so that clients continue to authenticate to the existing domain controller till we do the switch.    

My question is if we block the network access will the client systems that are in this domain still identify the new domain controller in anyway and will authentication requests still go there ? Also, is the mentioned overall plan viable or could there be issues in this plan implementation?    

Thankyou in advance for your response.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-16*

-  Yes, the blocking sounds problematic to me.    

-  The prerequisite before introducing the first 2016 domain controller: domain functional level needs to be 2003 or higher so no, the FRS-> DFSR migration is not required but it is recommended at some point.     

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-15*

We currently have two domain controllers in our infrastructure in a single forest. Plan is to add two new domain controllers ...... then switch the IP of new domain controllers    

A much simpler solution may be to decommission / demote one at a time, remove from network, and then stand up new one for replacement with the same name / address.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can move on to next one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
