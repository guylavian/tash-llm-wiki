---
title: "Active Directory managed service account clarification"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193710/active-directory-managed-service-account-clarifica
question_id: 1193710
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory managed service account clarification

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193710/active-directory-managed-service-account-clarifica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone, 

I need some clarification and assistance in creating the gMSA that will be used in every IIS server across the Single Forest AD domain.

How can I check if My AD Domain is capable of creating this gMSA ?

Any assistance would be very much appreciated.

Thanks,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-28*

Does the result from the PowerShell script  below can also be the proof that gMSA will works?

```
Get-KdsRootKey
Get-KdsConfiguration
```
