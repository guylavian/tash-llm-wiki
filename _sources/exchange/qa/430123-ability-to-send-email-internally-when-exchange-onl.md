---
title: "Ability to send email internally when Exchange online is not avaialble"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430123/ability-to-send-email-internally-when-exchange-onl
question_id: 430123
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Ability to send email internally when Exchange online is not avaialble

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430123/ability-to-send-email-internally-when-exchange-onl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Scenario  

Using the Exchange hybrid setup and with most email boxes in the cloud.  At some point internet connection might be down, or online exchange services not avaialble.  Internal processes heavily utilising email.   

Question  

Is there a plan by Microsoft to allow the on-premise server to send email internally using the onpremise server whilst exchange online is ot available,  Then when it comes back online everything switches back to using exchange online and emails that we created internally replicated to exchange online.   

The reasoning is that there are so many notifications generated internally coming through email, and the unavailability of Exchange online for what ever reason hiders internal processes that use workflows which in tern use email.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-10*

You would have to make any changes like that manually. There is no plan or ability by Microsoft to do this automatically.
