---
title: "ADFS considersation after Win2012R2 Active directory upgrade to Windows 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/519665/adfs-considersation-after-win2012r2-active-directo
question_id: 519665
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS considersation after Win2012R2 Active directory upgrade to Windows 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/519665/adfs-considersation-after-win2012r2-active-directo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Sir,  

```
Customer want to upgrade their existing Win2012R2 domain controller environment to Win2019.  It has a standalone server joined to Win2012R2 domain currently.
```

`May I know if all of the Win2012R2 DC upgrade to Windows 2019 version.  Do it has any issue on Win2012R2 ADFS server ? Will it continue work properly or need to perform corresponding upgrade?   Any document mentions on it?  

Regards,  

Joe Tam

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-19*

Nothing will happen to ADFS (assuming here that ADFS is not installed on one of the DCs about to go away).   

Although it might still be a good idea to upgrade ADFS to Windows Server 206 or 2019 to use the latest features.
