---
title: "High availability FSMO roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190533/high-availability-fsmo-roles
question_id: 1190533
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# High availability FSMO roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190533/high-availability-fsmo-roles (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Is it possible to failover FSMO roles automatically to another domain controller if the DC with fsmo roles is unreachable?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-03-16*

No it won't be automatic, but you can easily seize or transfer the roles when needed.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
