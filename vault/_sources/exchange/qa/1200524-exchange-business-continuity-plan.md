---
title: "Exchange Business Continuity plan"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1200524/exchange-business-continuity-plan
question_id: 1200524
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Business Continuity plan

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1200524/exchange-business-continuity-plan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want a business continuity plan  for Exchange Server 2016 DAG with 4 Servers one having all active copies and other having passive copies.How can I create this plan where is the documentation?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-07*

Hi @azhar Nasim  ,
 

According to your description, you simply install four Exchange Mailbox servers as stand-alone servers, and then incrementally configure them and mailbox databases for high availability and site resilience, as needed.

More detailed steps such as Base infrastructure and Network configuration please refer to: Deploying high availability and site resilience in Exchange Server

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
