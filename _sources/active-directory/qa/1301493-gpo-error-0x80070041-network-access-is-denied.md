---
title: "GPO error 0x80070041, network access is denied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1301493/gpo-error-0x80070041-network-access-is-denied
question_id: 1301493
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# GPO error 0x80070041, network access is denied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1301493/gpo-error-0x80070041-network-access-is-denied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I encountered an issue while attempting to create a duplicate of an existing mapped drive Group Policy Object (GPO) and modifying it for a different path in my environment. Unfortunately, I made a mistake by specifying an incorrect path, resulting in an error. Although I promptly removed the GPO, I'm still encountering the same error when trying to navigate to the user configuration and preferences section.

This problem seems to affect all my GPOs, and even restoring a backup from another domain controller did not resolve the issue. Any suggestion?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-09*

I run the Repadmin /syncall /AdeP command in active directory.

It fixed the issue itself.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-06-08*

Hi,

It seems you have secured UNC path and hence the Network Access Denied error via the GPO, check this article and Microsoft had released a Vulnerability fix so Network drives are protected via remote code - https://support.microsoft.com/en-us/topic/ms15-011-vulnerability-in-group-policy-could-allow-remote-code-execution-february-10-2015-91b4bda2-945d-455b-ebbb-01d1ec191328

Detailed steps to resolve this issue is in the article, test this on Dev Environment and later on Prod.

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
