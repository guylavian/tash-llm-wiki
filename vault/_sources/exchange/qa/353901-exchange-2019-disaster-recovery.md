---
title: "Exchange 2019 - Disaster Recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/353901/exchange-2019-disaster-recovery
question_id: 353901
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 - Disaster Recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/353901/exchange-2019-disaster-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

As an Exchange Administrator, I need to prepare the Exchange 2019 Disaster recovery plan. My environment is Exchange 2019 CU7 across 2 sites. Is there any documentation or step by step procedure.   

Thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-04-13*

Hi, @Bargavi Nagarajan       

As Ashok mentioned, you may consider deploying a database availability group (DAG) for high availability and site resilience.    

To deploy a DAG, you need to deploy one or more Exchange servers in both sites.    

If the DAG is with an even number of members, a witness server is also required.    

After the DAG is created, you will be able to add database copies on members of the DAG.    

If the server which currently holds the active database copy goes down, a failover will be triggered.    

The database copy on another DAG member will be activated and the clients will be redirected to this server.    

Here are two more links which may be helpful.    

All the requirements of deploying a DAG: Plan for high availability and site resilience    

Overall steps of deploying a DAG: Deploying high availability and site resilience    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
