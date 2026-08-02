---
title: "[Migrated from MSDN Exchange Dev] Tenant A to Tenant B hybrid org relationship"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/188398/migrated-from-msdn-exchange-dev-tenant-a-to-tenant
question_id: 188398
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev] Tenant A to Tenant B hybrid org relationship

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/188398/migrated-from-msdn-exchange-dev-tenant-a-to-tenant (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Tenant A to Tenant B hybrid org relationship  

I'm sitting with a issue to setup calendar free/busy sharing between one o365 tenant and a another hybrid tenant.  

Brief description:  

Domain A is cloud only  

Domain B is Hybrid (the free/busy between on-premise and the federated cloud is working).  

I setup a org relationship from domain A to domain B (and then domain B is using Autodiscover to point to on-premise server).  I also setup a trust between domain A and the domainB's .onmicrosoft domain.  

The problem is:  

Free busy from domain A to domain B is working only for mailboxes that are still on premise.  

free busy for cloud mailboxes only work if I specify the domainB.mail.onmicrosoft.com address.  

How can I setup sharing from Domain a, to domain B for both Onpremise and cloud based mailboxes.  

I've heard talk that it is possible, but I cannot find anything on the net regarding this.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

Hi,    

This seems to be an expected behavior and this question has been recorded in o365 user voice here: Free/busy information not accesible from O365 tenant and Hybrid OnPrem/O365 tenant    

And I also found some related threads discussed about the similar issue below:    

Free/Busy O365 tenant with Hybrid O365 tennant -OrganizationRelationship    

Free/Busy O365 tenant with Hybrid O365 tenant    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
