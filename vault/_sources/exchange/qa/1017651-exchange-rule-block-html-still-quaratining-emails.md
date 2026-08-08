---
title: "Exchange rule block HTML still quaratining emails from specific senders"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1017651/exchange-rule-block-html-still-quaratining-emails
question_id: 1017651
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange rule block HTML still quaratining emails from specific senders

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1017651/exchange-rule-block-html-still-quaratining-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a block all HTML Exchange rule for exchange online. I added an exception for 3 specific sender is (the external users email addresses) but emails are still being quarantined because of the HTML rule.     

Priority is set to 51 & the emails are whitelisted on the O365 defender Spam policy as well.    

When investigating via exchange message trace & message explorer the reason for quarantine says because of the exchange rule HTML, but when looking at O365 explorer I see a all overrides,  Allowed by organization policy : Sender address list (Safe sender / Blocked sender), but when looking in the details it says messages may or may not be effected.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-26*

Sender address was not the full address (I was using send-on behalf address)
