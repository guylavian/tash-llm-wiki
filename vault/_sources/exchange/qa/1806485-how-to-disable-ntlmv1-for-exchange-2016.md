---
title: "How to disable NTLMv1 for Exchange 2016."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1806485/how-to-disable-ntlmv1-for-exchange-2016
question_id: 1806485
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to disable NTLMv1 for Exchange 2016.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1806485/how-to-disable-ntlmv1-for-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are disabling NTLMv1 and enabling only NTLMv2 in our environment. 

We have already configured the LAN Manager Authentication Level setting on our Exchange Server 2016 server to 'Send NTLMv2 response only\refuse LM & NTLM'. 

However, do we need to configure anything within the Exchange 2016 application itself to ensure NTLMv1 connections are disabled, especially since this server serves as a relay for receiving emails from applications?

Regards,

Raj

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-10*

No, this is a Windows issue, not an Exchange one. I have done this along time ago, no issues.
