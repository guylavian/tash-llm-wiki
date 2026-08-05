---
title: "[Migrated from MSDN Exchange Dev] Message Queue is stucked"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145706/migrated-from-msdn-exchange-dev-message-queue-is-s
question_id: 145706
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Message Queue is stucked

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145706/migrated-from-msdn-exchange-dev-message-queue-is-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/01a11b47-0838-4f90-8069-93db711f9383/message-queue-is-stucked?forum=exchangesvrdevelopment  

Hey all,  

A common problem in our environment is that exchange delivery queue is stuck because it's full.  

We can temporary resolve this issue simply by expanding the drive which the queue on (luckily it's simple)  

Do you can tell what generally cause this issue? how do you recommend to act to resolve this issue forever?.  

tnx

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

Delivery queues are dynamically created when they're required, and are automatically deleted when the queue is empty and the expiration time has passed. The queue expiration time is controlled by the QueueMaxIdleTime parameter on the Set-TransportService cmdlet. The default value is three minutes.  

Did you manually change that value?  

Open Queue viewer and find those delivery queues, are there any similarity among them? Be free to post a snapshot you see (with personal information covered).

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
