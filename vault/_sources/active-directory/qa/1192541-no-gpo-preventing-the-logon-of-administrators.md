---
title: "No GPO preventing the logon of administrators"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192541/no-gpo-preventing-the-logon-of-administrators
question_id: 1192541
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# No GPO preventing the logon of administrators

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192541/no-gpo-preventing-the-logon-of-administrators (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A way to collect an administrator credential is to take control of a workstation in the unsecure tiers and expect that an administrator will connect to it.

An attack such as credential theft or kerberos delegation is then performed.

To reduce the impact of such compromise, the best practice is to isolate components (such as admins, DC) in tiers.

Typically, a domain admin should not be allowed to connect to any workstation but login only to perform highly privileged operations.

How to prevent highly privileged admins (Tier 0) from accessing non-privileged resources?

How will admins access non-privileged resources?

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-23*

Hi

is there any other solution?

Please answer me each question. Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-23*

Hi @Chapter7-2723 •

You can use user right assignement in GPO to deny access on T1 and T2 for T0 admins.

Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment:  

You should create a OU and GPO for each tiers after that ,

On the OU T0 you link a GPO where you will deny access to T1 and T2 accounts on T0 assets 

On the OU T1 you link a GPO where you will deny access to T0 and T2 accounts on T1 assets 

On the OU T2 you link a GPO where you will deny access to T0 and T1 accounts on T2 assets 

Please don't forget to mark helpful answer as accepted
