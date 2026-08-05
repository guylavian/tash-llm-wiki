---
title: "Does Exchange Hybrid Deployment keeps a copy of emails in Exchange Online?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203457/does-exchange-hybrid-deployment-keeps-a-copy-of-em
question_id: 203457
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Does Exchange Hybrid Deployment keeps a copy of emails in Exchange Online?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203457/does-exchange-hybrid-deployment-keeps-a-copy-of-em (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are a company trying to implement a hybrid solution with Exchange "on-premises" and Microsoft 365.   

However, in the guide "Exchange Server hybrid deployments" it says that the Mailbox location after hybrid deployment is "on-premises and in Exchange-online".  

Does this mean that Microsoft makes a copy of the emails Online??   

We do not wish to have our emails in servers hosted by Microsoft. Is there a way to make this possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

Hi @Daniel Sanchez       

A hybrid environment allows you keep your mailboxes on-premise or migrate them to cloud, but you cannot have a mailbox located both on-premise and online.    

And the official document introduces this scenario "a mailbox exists in both Exchange Online and on-premises" (which is not the supported way) and the solution to resolve it.    

You could refer to this link to know more about hybrid: Exchange Server hybrid deployments    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-18*

No, that's not what it means. It means that you can have a given mailbox located either on-premises or in the cloud, but not both.
