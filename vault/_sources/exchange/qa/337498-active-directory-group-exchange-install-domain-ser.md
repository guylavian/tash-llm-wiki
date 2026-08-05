---
title: "Active Directory Group: Exchange Install Domain Servers purpose"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337498/active-directory-group-exchange-install-domain-ser
question_id: 337498
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Active Directory Group: Exchange Install Domain Servers purpose

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337498/active-directory-group-exchange-install-domain-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can anybody telll me if the group "Exchange Install Domain Servers" is needed past the installation of Exchange 2019?  What is it's purpose if it must stay?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-30*

Agree - it's not hurting anything.  I'm just trying to mitigate all of the insecure paths that Exchange creates in AD.  This group is a member of a sensitive AD group that could be taken advantage of.
