---
title: "Upgrade exchange 2016 CU14 to CU18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299962/upgrade-exchange-2016-cu14-to-cu18
question_id: 299962
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Upgrade exchange 2016 CU14 to CU18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299962/upgrade-exchange-2016-cu14-to-cu18 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am planning to upgrade from exchange 2016 CU14 to CU18.   

Can I do it directly my installing a required .net framework or I have do to CU16 and then CU 18.  

Also, the active directory schema upgrade is required for CU18 from CU14?  

Thanks  

Pavan.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

Hi @pavan kumar   ,    

Yes, you can upgrade from CU14 to CU18 directly. Prepare the Active directory with PrepareSchema/PrepareAD/PrepareDomain.    

Upgrade .NET framework to 4.8, install other windows pre-requisites and install the Exchange CU18     

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016    

Please find the below screenshot for the AD value change,    

    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016#exchange-active-directory-versions    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
