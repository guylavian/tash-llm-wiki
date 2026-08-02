---
title: "Server 2012 R2 Issue new CAExchange Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/422778/server-2012-r2-issue-new-caexchange-certificate
question_id: 422778
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Server 2012 R2 Issue new CAExchange Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/422778/server-2012-r2-issue-new-caexchange-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I followed the step in this video, https://www.youtube.com/watch?v=E3veNIwDjI8, and got to the point were you revoke the CAExchange certificate which I did.  I think ran the powershell command shown (with admin priv) but no new CAExchange certificate appears in the Issued Certificate list.  Yes, I did refresh the list.  The command does appear to run successfully.  

What am I missing?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-04*

Nevermind.  I found WAY DOWN on the list.  Even though I sorted the list by template it did not appear at the top.
