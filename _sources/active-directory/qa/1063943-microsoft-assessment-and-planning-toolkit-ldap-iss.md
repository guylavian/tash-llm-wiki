---
title: "Microsoft Assessment and Planning Toolkit - LDAP Issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1063943/microsoft-assessment-and-planning-toolkit-ldap-iss
question_id: 1063943
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Microsoft Assessment and Planning Toolkit - LDAP Issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1063943/microsoft-assessment-and-planning-toolkit-ldap-iss (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,    

Is it possible that the install of Microsoft Assessment and Planning Toolkit will create "dummy accounts and computers" which are not ours on Management Console of AD ?    

We noticed after the install that everyone which has Management Console of AD can see "dummy accounts" which in fact in AD Server do not exist and if we try to delete or disble them we get:     

" Directory object not found"     

This is becoming serios and it is really needed your opinion.    

Thank You

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-27*

Hello,    

It seems like it was fixed by upgrading the workstation on 20H2

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-10-26*

Hi,    

Did you imported sample data? I can only think of someone restoring old DB or sample database.    

Hope this helps.    

JS    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
