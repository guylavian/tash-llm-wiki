---
title: "Adfs how to use it!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/372432/adfs-how-to-use-it
question_id: 372432
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Adfs how to use it!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/372432/adfs-how-to-use-it (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, I'm new to the forum and I ask you a question that may seem useless.  I am studying a lot in this period and I came across ADFS, and the question arose spontaneously: but in which context is it used?  I understand that the most frequent use is for sharepoint portals.  but can it also be used for Oracle applications?  thanks and sorry are constantly evolving😁

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-27*

ADFS is a Microsoft on-premises Security Token Service: https://en.wikipedia.org/wiki/Security_token_service    

It differentiates itself from others in the market thanks to specific features.    

It is actually rarely used for SharePoint as SharePoint servers have to be domain joined and this already gives them access to the users' identities and information.    

It used to play a key role with Azure AD/Office 365 integration to provide SSO to domain joined systems. But that's no longer a requirement as we can achieve SSO with other features.    

Documentation: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview
