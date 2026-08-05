---
title: "Exchange Server is modifying GPOs in AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664880/exchange-server-is-modifying-gpos-in-ad
question_id: 1664880
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server is modifying GPOs in AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664880/exchange-server-is-modifying-gpos-in-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

in our SIEM, we are getting more than 300 incident a day that a GPO has been modified by the exchange server machine account and the Property Name: msExchMailboxAuditLastAdminAccess.

Can anyone please explain this incident, and give us tips on if we should ignore it or if we should some changes on Exchange or AD server.

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-10*

Mailbox Auditing is enabled by default so that is prob expected. What exactly is getting changed according the alerts?
