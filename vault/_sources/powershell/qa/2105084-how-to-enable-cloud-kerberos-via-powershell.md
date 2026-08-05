---
title: "How to enable cloud kerberos via powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105084/how-to-enable-cloud-kerberos-via-powershell
question_id: 2105084
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# How to enable cloud kerberos via powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105084/how-to-enable-cloud-kerberos-via-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am looking for the proper scripts to install cloud kerberos to use for WHFB in a Hybrid environment.

I have found a few but none are the same.   Also are there any security impacts to do this for already established on prem certs or authentication.

Thank you for all your help on this

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-19*

You should be able to follow the document provided by Microsoft to enable and or migration to cloud trust. 

https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/deploy/hybrid-cloud-kerberos-trust?tabs=gpo
