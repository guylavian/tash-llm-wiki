---
title: "Build a new DC from old without transfer FSMO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/319168/build-a-new-dc-from-old-without-transfer-fsmo
question_id: 319168
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Build a new DC from old without transfer FSMO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/319168/build-a-new-dc-from-old-without-transfer-fsmo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

My company's DC (2003) attached by ransomware. AD, DNS services still working but management tools and others were encrypted. Restarting the server, the virus will probably re-active.  

I thought about: disconnect the old server, set up a new clean windows server (2012 or above), promote it to AD with the same old AD domain name, IP address. Re-create usernames (~50 accounts) same login name as old AD with new passwords, and notify users to change their password on the next login (Luckily, the number of users is not much).  

Can clients be connected to new AD with current AD information? And, Can users login to their desktop with an old username and new password by new AD?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-17*

Is there a solution to solve my problem?  

You may be able to restore a recent known good backup.  

--please don't forget to `Accept as answer` if the reply is helpful--
