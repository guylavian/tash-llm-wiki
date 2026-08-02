---
title: "Doubts about password policies in Active Directory."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184181/doubts-about-password-policies-in-active-directory
question_id: 1184181
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Doubts about password policies in Active Directory.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184181/doubts-about-password-policies-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In my ActiveDirectory have 2 password policies applied. One via GPO(Default Police Manager) and the other determined by set-ADDefaultDomainPasswordPolicy.

Which policy has priority and How to reset ADDefaultDomainPasswordPolicy values ​​determined by cmdlet with "Set-ADDefaultDomainPasswordPolicy" command?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-25*

Hi @Snoow99  

The default domain password policy can be modfied via GPO ( default domain policy) or Powershell.

So we cannot talk about priority because the both method can be used to modify the same password policy.

We talk about priority in case of use many Password polices created via Fine grained password policy feature.

Please don't forget to mark helpful answer as accepted
