---
title: "Update Exchange 2013 from CU 1 to CU 23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222866/update-exchange-2013-from-cu-1-to-cu-23
question_id: 222866
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Update Exchange 2013 from CU 1 to CU 23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222866/update-exchange-2013-from-cu-1-to-cu-23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am going to upgrade an exchange 2013 CU to CU 23, right now there is an exchange server 2007 in the environment but the services have been disabled, it is technically not alive.    

I have done testing in my own environment with the 2 of the DC's (Virtual) and did the upgrade of Exchange server (virtual) which completed successfully.  

But wondering if I can expect any gotcha's when I do this with the third DC which is running exchange 2007 added back

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-08*

Hi @Terry Schultz  ？    

According to your description, do you mean currently the environment is running Exchange 2013 CU1 properly with the Exchange 2007 added?    

If this is the case, you can go ahead to upgrade Exchange 2013 to the latest CU.    

By the way, considering that Exchange 2007 is technically not alive in your environment and it has reached the end of life, it's suggested to decommissioning Exchange Server 2007 so as to complete the entire Exchange 2007 to 2013 migration process.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
