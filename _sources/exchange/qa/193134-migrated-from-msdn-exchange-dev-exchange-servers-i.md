---
title: "[Migrated from MSDN Exchange Dev]exchange servers integration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/193134/migrated-from-msdn-exchange-dev-exchange-servers-i
question_id: 193134
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]exchange servers integration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/193134/migrated-from-msdn-exchange-dev-exchange-servers-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi  

I'm my organization we have 2 exchange servers each servers named as hdmail04.minz.local, hdmail05.minz.local  

The exchange server integrated with DAG server. Yesterday 1 server after reboot cannot start "failed   

Failed to create or access memory contents) error  

All storages full. External domain minz.uz I want to install new exchange server but showing error like setup can't use the same site as Default-site-name. I tried to add disk but didn't work. These servers working as hyper v machine and controlling via Failover cluster manager. Exchange server version is 2013 working on Windows server 2012 r2 standard

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-10*

Hi ,    

According to I research the error message and information you provided, I think the reason for this issue is insufficient drive space, which has nothing to do with Exchange server. Based on my research on similar cases, you could try to create a new VM and attach the old VHD to it.    

For the similar cases you could refer to: failed to create memory content file hyper-v and Error When Starting VM Failed to create memory contents file    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
