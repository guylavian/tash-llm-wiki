---
title: "GPO for users will not apply to remote session on server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181245/gpo-for-users-will-not-apply-to-remote-session-on
question_id: 1181245
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO for users will not apply to remote session on server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181245/gpo-for-users-will-not-apply-to-remote-session-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

There is a GPO to map network drive. The GPO is assigned to an OU with users, and it works when the user logs in to his PC. But when he connects to the server via RDP, the policy is not applied.

If I assign the policy to the OU with the server, then the policy will apply. Although the policy itself doesn't have any settings for the computer at all.

GPO Security Filtering - Authenticated users, no WMI  filters.

The question is - why is the user's policy not applied to the remote server if it is assigned to the OU with the user and it is applied when assigned to the OU with the server?

Remote log in doesn't count as user from GPO perspective?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-20*

Hi @Anonymous  

It seems a DPO conflict between user and computer GPO settings.

 I invite you to check loopback processing to define which settings should be applied. : Loopback processing of Group Policy

Please don't forget to mark helpful answer as accepted

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-20*

Answer - one of computer policies for server was rewriting policy for user.
