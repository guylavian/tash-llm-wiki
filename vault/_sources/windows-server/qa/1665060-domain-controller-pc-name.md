---
title: "Domain controller pc name"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1665060/domain-controller-pc-name
question_id: 1665060
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller pc name

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1665060/domain-controller-pc-name (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

I accidentally changed the PC name of the domain controller and no user can login anymore.

can you please advise?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-10*

domain controller is in virtual machine in esxi and when i connect with remote sektop connection and enter administrator user , this message appear : (the security database on the server does not have a computer account for this work station trust relation ship)

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-10*

Connect directly to the domain controller by using a console session or a Remote Desktop connection and change the name back. 

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
