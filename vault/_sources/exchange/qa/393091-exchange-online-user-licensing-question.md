---
title: "exchange online user  licensing question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/393091/exchange-online-user-licensing-question
question_id: 393091
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange online user  licensing question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/393091/exchange-online-user-licensing-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello we are performing manual tenant to tenant migration of exchange online data.   

when i create the users in my destination tenant do i need to assign a license right away? Or do we still have 30 days.   

i will need to restore mailbox data .   

so when i create my users does the mailbox automatically get created or is the license assignment required?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-12*

Depends on how you are provisioning the mailboxes. The "normal" workflow is to apply a license, which in turn provisions the mailbox. You dont need to do it right away, only once you need the mailbox provisioned.  

Alternatively you can use the New-Mailbox cmdlet with the -MicrosoftOnlineServicesID parameter to provision a mailbox directly, then assign the license (30 days period still applies).
