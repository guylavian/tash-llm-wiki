---
title: "Exchange Server 2016 Support for WAF"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1518524/exchange-server-2016-support-for-waf
question_id: 1518524
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Exchange Server 2016 Support for WAF

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1518524/exchange-server-2016-support-for-waf (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I would like to know if Exchange Server 2016 supports applying WAF in the environment. Specifically, I am interested in knowing if it supports OWA, ECP, EWS, and ActiveSync, and if there is any article from Microsoft that shows whether or not it is supported. Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-30*

Hello, you can install and configure a WAF (F5, Barracuda WAF etc..) with any software, as long as you open the required ports and configure it properly there is no problem. Some WAF offers specific pre-configured templates for Exchange services such OWA, ECP, EWS, ActiveSync..
