---
title: "Install CU update for exchange server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/298030/install-cu-update-for-exchange-server-2016
question_id: 298030
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Install CU update for exchange server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/298030/install-cu-update-for-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,  

Currently my company using exchange server 2016 CU9 Version 15.1 (Build 1466.3). Does we can update to exchange server 2016 CU19 version 15.1.2176.2?  

it's recommend and best practices to update from exchange server 2016 CU9 to CU19?   

Could provide me prerequisite before update exchange CU?  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi @Suy Peang      

Like the suggestions provided by AshokM, upgrading from an earlier version before Cumulative Update 13 for Exchange Server 2016, we need to run the /PrepareAD or /PrepareDomain    

The Exchange Server prerequisites are list in the official document, prepare the software according to your windows server version.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

Hi @Suy Peang   ,    

Yes, you can upgrade from CU9 to CU19. Prepare the Active directory with PrepareSchema/PrepareAD.     

Upgrade .NET framework to 4.8 which is crucial and Immediately install the Exchange CU19.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework    

You can also check for the best practises,    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019#best-practices    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
