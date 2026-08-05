---
title: "Using SMTP 365 as Smart Host for Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1005816/using-smtp-365-as-smart-host-for-exchange-server
question_id: 1005816
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Using SMTP 365 as Smart Host for Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1005816/using-smtp-365-as-smart-host-for-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

Currently we use smtp.office365.com as smart host on send connector exchange server. and we use basic authentication on smart host authentication. everything works normally, we can send emails to external domain. however, when we use an MFA-enabled account to authenticate to smtp.office365.com, the email we send fails to be sent. what i want to ask is, is there any solution for this case?    

Really appreciate for your answer!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-14*

Hi @Arief Hardiansyah   ,    

MFA is not supported, and you could refer to Andy's method.    

    

If the reply helps, you could mark it as an answer.
