---
title: "Join windows in AWS to Azure Active Directory with MFA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/342964/join-windows-in-aws-to-azure-active-directory-with
question_id: 342964
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Join windows in AWS to Azure Active Directory with MFA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/342964/join-windows-in-aws-to-azure-active-directory-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can I join windows in AWS to Azure Active Directory with 2fa?  

if yes, Can I have step by step doc?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-03*

The AWS server is considered as a VM out of Azure infrastructure. Thus, you can connect the VM to Azure AD using Azure Active Directory connect and enable MFA. Here is the detailed Microsoft documentation on the procedure: join-windows-vm
