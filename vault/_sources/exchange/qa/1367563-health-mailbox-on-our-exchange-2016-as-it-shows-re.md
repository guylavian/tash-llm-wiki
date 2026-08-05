---
title: "Health Mailbox on our exchange 2016 as it shows regular logins to itself (127.0.0.1)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1367563/health-mailbox-on-our-exchange-2016-as-it-shows-re
question_id: 1367563
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Health Mailbox on our exchange 2016 as it shows regular logins to itself (127.0.0.1)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1367563/health-mailbox-on-our-exchange-2016-as-it-shows-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our SIEM team have raised an alert against the Health Mailbox on our exchange 2016 as it shows regular logins to itself (127.0.0.1). I believe this activity is normal, but can you just confirm that is the case, so this activity can be whitelisted and not reported on in future.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-13*

Yea, I would exclude, this is normal. Those mailboxes are checking stuff  :) 

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-2013-2016-monitoring-mailboxes/ba-p/611004
