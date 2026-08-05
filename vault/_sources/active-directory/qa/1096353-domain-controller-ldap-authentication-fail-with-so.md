---
title: "Domain controller ldap authentication fail with some app"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1096353/domain-controller-ldap-authentication-fail-with-so
question_id: 1096353
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller ldap authentication fail with some app

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1096353/domain-controller-ldap-authentication-fail-with-so (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi today we found issue with random ldap authentication fail I red about kb5019966 but this update was not installed on DCs, system like Jira,some redhat8 have problem with domain authentication have you any idea? thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-19*

Sounds like the result of recent DCOM hardening. Some registry work-arounds here may help.    

https://support.microsoft.com/en-us/topic/kb5004442-manage-changes-for-windows-dcom-server-security-feature-bypass-cve-2021-26414-f1400b52-c141-43d2-941e-37ed901c769c    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-19*

too many errors like I posted

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-19*



## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-19*



## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-19*

Not much to go on, might check for time differences, logs, etc.
