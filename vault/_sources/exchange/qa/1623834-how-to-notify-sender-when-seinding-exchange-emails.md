---
title: "How to notify sender when seinding Exchange emails to distribution list contains external recipients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1623834/how-to-notify-sender-when-seinding-exchange-emails
question_id: 1623834
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to notify sender when seinding Exchange emails to distribution list contains external recipients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1623834/how-to-notify-sender-when-seinding-exchange-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to notify sender when seinding Exchange emails to distribution list contains external recipients?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-20*

In my testing with 365 groups, this works

Can you create a 365 group and test?

Note that the documentation indicates its supported as well as long as the domain of the group is not set an an external domain 

Also note that mail tips are not always immediate, so a new group may take a day to work.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-19*

Use the built in Mail tips. SHould already be enabled

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/mailtips/mailtips
