---
title: "Disable LDAP 389 and enforce LDAPS 636 in AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1613606/disable-ldap-389-and-enforce-ldaps-636-in-ad
question_id: 1613606
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Disable LDAP 389 and enforce LDAPS 636 in AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1613606/disable-ldap-389-and-enforce-ldaps-636-in-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We already install the certificate, enable LDAP signing and channel bind in AD. How to configure client’s directory service settings point to the LDAPS port (usually 636)?

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-11*

Hi @Chong •

You can use group policy or registry key:

Fore more information please refer to the following link:

How to set the client LDAP signing requirement by using a domain Group Policy Object

Please don't forget to accept helpful answer
