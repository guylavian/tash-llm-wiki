---
title: "[Migrated from MSDN Exchange Dev]3 node Exchange DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/173238/migrated-from-msdn-exchange-dev-3-node-exchange-da
question_id: 173238
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]3 node Exchange DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/173238/migrated-from-msdn-exchange-dev-3-node-exchange-da (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted  on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hello Team,  

Please advise if we can setup DAG with a 3 Exchange 2016/2019 Servers.  

We currently planning to deploy 3 Exchange Servers for 3 different regions and want to have DAG setup for high redundancy.  

Kindly suggest.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-24*

Hi ,    

In order to better solve your issue, I want to confirm below information with you:    

-  What means about 3 Exchange 2016/2019 servers? You have 3 Exchange 2016 servers or Exchange 2019 servers, or you have 3 Exchange server which include Exchange 2016 and 2019 servers.     

-  What do the different regions refer to?    

Base on my knowledge, all servers within a DAG must be running the same version of Exchange and Windows operating system, and all mailbox servers in DAG need in the same Active Directory domain. In addition, the Mailbox server must not be configured as an Active Directory domain controller or global catalog server.    

If your Exchange servers meet all the required by DAG, then you could following the steps to create a DAG.    

-  In the EAC, go to Servers > Database Availability Groups.    

-  Click  +  to create a DAG.    

-  On the new database availability group page, provide the information for the DAG.    

-  Click Save to create the DAG.    

For the specific steps you could refer to: Create a database availability group    

This article could help you better to understand the DAG: Database availability groups    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
