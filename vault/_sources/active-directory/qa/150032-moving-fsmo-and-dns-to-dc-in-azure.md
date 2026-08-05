---
title: "Moving FSMO and DNS to DC in Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150032/moving-fsmo-and-dns-to-dc-in-azure
question_id: 150032
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Moving FSMO and DNS to DC in Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150032/moving-fsmo-and-dns-to-dc-in-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

I will be moving an on-prem DC to Azure. The plan is to create a new VM in Azure, join to the domain, install AD roles and promote the VM as DC. I should be OK with this, however, trying to find out the best way to move the two below. Eventually, the on-prem DCs will get removed completely.  

The best way to move:  

-  FSMO?  

-  DNS? - is it going to be automatically replicated to the DC in Azure and I do not need to make any manual configuration? If so, how long (hrs/days) should I wait to be sure that they are really synced? Found some info about waiting at least 48 hrs, but I'm not sure  

would appreciate all your recommendation, as this is my first time doing sommething like this :)

## Answers

_No answers on this thread._
