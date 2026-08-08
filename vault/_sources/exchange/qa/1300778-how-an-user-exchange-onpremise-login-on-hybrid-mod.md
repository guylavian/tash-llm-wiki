---
title: "how an user exchange-onpremise login on hybrid mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1300778/how-an-user-exchange-onpremise-login-on-hybrid-mod
question_id: 1300778
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# how an user exchange-onpremise login on hybrid mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1300778/how-an-user-exchange-onpremise-login-on-hybrid-mod (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

I'm configuring a hybrid mode for exchange on-premise and exchange online. It is already configurated and right now I'm confused about how users on exchange on-premise login.

Can account exchange on-premise login in Outlook Web app (https://outlook.office365.com/)? I'm trying to login but throwing some exceptions about the license 

But After adding the license, it continues to throw some other exceptions. So what I really want to confirm here is can exchange on-premise accounts are allowed to login into Outlook on web?

Do anyone know the normal flow of user on the hybrid system? Where will on-premise accounts and O365 account login be?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-07*

no, not possible, the user needs to logon directly to the Exchange Server on-prem.
