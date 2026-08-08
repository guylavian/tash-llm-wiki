---
title: "Exchange 2016 Hybrid - Archive policy best practice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/407276/exchange-2016-hybrid-archive-policy-best-practice
question_id: 407276
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Hybrid - Archive policy best practice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/407276/exchange-2016-hybrid-archive-policy-best-practice (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange 2016 hybrid. For Online users we are going to enable online archiving. What are the recommendations/best practice to set the retention policy i.e. how often emails should move to archive database? 1 year, 2 year, 5 year? What is the best practice?.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-25*

Hi @Muhammad Zeeshan Afzal   ,    

Agree with Andy.    

There is no official best practice recommended by Microsoft.How to set the retention policy completely depends on the needs of users. For example, if the user mailbox receives and sends a large number of mails, and hope that the size of the primary mailbox is not too large. Then the retention period of "move to archive" can be set smaller.    

In short, it all depends on the needs of users in your organization.    

Please refer to: Retention tags and retention policies    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-24*

There is no best practice. It all depends on your company requirements and how large you want the primary mailbox size to be.
