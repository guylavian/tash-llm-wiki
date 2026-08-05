---
title: "How can I add a user in active directory using PowerShell?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1861574/how-can-i-add-a-user-in-active-directory-using-pow
question_id: 1861574
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How can I add a user in active directory using PowerShell?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1861574/how-can-i-add-a-user-in-active-directory-using-pow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can I add a user to a specific group in Active Directory for 35 days and then remove the user from the group using PowerShell?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-12*

Hi @Zring Abdulrazzaq Rasool ,

to add and remove users to and from on-premises Active Directory you can use these cmdlets in your script:

Add-ADGroupMember

Remove-ADGroupMember

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)

Regards

 Andreas Baumgarten
