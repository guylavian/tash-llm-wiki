---
title: "ADFS MFA Hard token"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/819487/adfs-mfa-hard-token
question_id: 819487
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# ADFS MFA Hard token

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/819487/adfs-mfa-hard-token (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have an application that was using Azure SSO/MFA and for several reasons I had to move it back to on premises ADFS, Keeping Azure MFA, authetication works for most users, but I have a few using hard oath tokens and they get an error like this , when trying to login:    

Authetication attempt failed. Select a different sing in option.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-04-20*

Did they add the token as an authentication method to their accounts?  

What do the Azure Sign in Logs show?
