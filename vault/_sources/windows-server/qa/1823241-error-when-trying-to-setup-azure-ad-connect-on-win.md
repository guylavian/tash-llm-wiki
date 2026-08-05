---
title: "Error when trying to setup Azure AD Connect on Windows Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1823241/error-when-trying-to-setup-azure-ad-connect-on-win
question_id: 1823241
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Error when trying to setup Azure AD Connect on Windows Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1823241/error-when-trying-to-setup-azure-ad-connect-on-win (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am currently testing Azure AD Connect (Microsoft Entra Connect) However I keep getting the same error.

I am currently using Windows Server 2022 which was freshly installed and after entering credentials (which i have provide the right privilege) i will get error

An error occured executing Configure AAD Sync Task: An error occured while sending the request

Not sure what exactly is the problem. I have tried with Server 2016, Server 2019 and getting the same error.

I've open the log but i'm lost trying to figure it out. Hope to get some assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-05*

I also encountered this issue with version Microsoft Entra Connect 2.3.20.0. I used an older installation of EntraSync, and it works without any problems.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-25*

As of AD Connect 2.3.20, TLS1.2 is required on the server.

You must enable it on the server: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-tls-enforcement

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-23*

Any Solution found for this ?
