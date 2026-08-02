---
title: "Exchange 2013 not working after cu23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384214/exchange-2013-not-working-after-cu23
question_id: 384214
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 not working after cu23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384214/exchange-2013-not-working-after-cu23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Services are up, nobody can connect, Outlook will time out saying folders cannot be opened. OWA says mailbox disabled. All services started. Loaded cu23 and post update fix for known Exchange exploit last night, and now, nobody can work and we cannot find any way to reach Microsoft about this, it is utterly maddening to say the least. Everything was fine until we ran the cu23 update and the post update patch. Reran the cu23 setup, no change. Need a way to reach Microsoft re: this exploit riddled and now non-functioning software. Whole office has no mail until this is fixed.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

OWA works - we were using the only user mailbox (other than admin) that did not have OWA. EMC works. But no Outlook clients can connect. In EMC all looks normal, it does give us a "Microsoft Exchange Server Auth Certificate" on server MAIL has expired - but it is not, we even created it from scratch, and it still says it.
