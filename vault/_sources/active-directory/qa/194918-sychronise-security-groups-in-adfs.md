---
title: "Sychronise security groups in ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/194918/sychronise-security-groups-in-adfs
question_id: 194918
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Sychronise security groups in ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/194918/sychronise-security-groups-in-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

Is it possible to enable synchronization for security and distribution groups via ADFS.  

Kindly assist as we are looking to enable this for one our application(ERP) requirement.  

Regards,  

Mukund

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-14*

Do you mean something like SCIM?    

If so, ADFS doesn't do it. But Azure AD does.
