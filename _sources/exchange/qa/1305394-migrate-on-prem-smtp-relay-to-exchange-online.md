---
title: "Migrate On-prem SMTP relay to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305394/migrate-on-prem-smtp-relay-to-exchange-online
question_id: 1305394
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migrate On-prem SMTP relay to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305394/migrate-on-prem-smtp-relay-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We've Some on-premises application connected to on-prem exchange 2016. and we are currently migrating all users to cloud and decommission the on-prem Exchange server.

How to connect the on-prem apps to office 365 SMTP relay.

Thanks,

Ahmed

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-14*

Why not keep the on-prem Exchange server around for that?

Otherwise, you would need to set it up like this for each app:

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365
