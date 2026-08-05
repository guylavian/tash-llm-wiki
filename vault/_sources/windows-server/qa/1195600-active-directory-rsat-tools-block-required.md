---
title: "Active directory RSAT tools block required"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195600/active-directory-rsat-tools-block-required
question_id: 1195600
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Active directory RSAT tools block required

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195600/active-directory-rsat-tools-block-required (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Dear

I am using windows server 2019 with an active directory I have more than 1500 user on my server, as well as 20 users has assign local admin like all are enterprise admin

this time I want to revoke local admin and they was used RSAT tools and manage users (like user create, delete, and update through RSAT Tools)

I need to ensure that any user can't access the RSAT tools on his devices

Thnaks

Jabad

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-04*

Hello
Thank you for your question and reaching out. I can understand you are  having query\issues related  to RSAT tool.
As it is AD integrated ,  Hence if you to revoke of Performssion or block from AD DC then it should be also blocked for RSAT.
Reference:
https://social.technet.microsoft.com/Forums/lync/en-US/7321d5a8-2332-4a77-b29b-b615e3a8ac3a/permissions-remote-server-administration-tool-windows-81?forum=winserverDS
--If the reply is helpful, please Upvote and Accept as answer--
