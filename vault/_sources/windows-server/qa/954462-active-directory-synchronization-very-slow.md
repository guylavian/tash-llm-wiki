---
title: "Active Directory Synchronization very slow."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/954462/active-directory-synchronization-very-slow
question_id: 954462
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Synchronization very slow.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/954462/active-directory-synchronization-very-slow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we have a set of AD server and client synchronization is very slow.    

Once the WSUS service was set up, it took 30 minutes or more to synchronize the policy with the client. And we've tried using the command to force a policy refresh, which didn't work.    

Please assist in the investigation. thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-08*

Hi,    

The first synchronization is going to be slow as it’s doing a lot of work. I suggest that you see how slow (or not) it may be on subsequent syncs.     

I hope this answers your question.    

---------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
