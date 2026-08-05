---
title: "Kerberos Pre-authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192531/kerberos-pre-authentication
question_id: 1192531
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Kerberos Pre-authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192531/kerberos-pre-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

How to check if all accounts require kerberos pre-authentication?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-03-23*

Hi @Chapter7-2723 •

This information can be found on user object.

You can launch the following Powershell command to extract the list of user with kerberos preauth not required:

`Get-ADUSer -Filter 'DoesNotRequirePreAuth -eq $true ' `

Please don't forget to mark helpful answer as accepted
