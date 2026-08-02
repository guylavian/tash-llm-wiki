---
title: "GPO related"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182279/gpo-related
question_id: 1182279
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO related

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182279/gpo-related (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have different version of Windows Install on my PC

and I have set some GPO too But I dont really identify which GPO is the reason for not showing Only shutdown button from Domain Administrator side 

But from general user side and from Local administrator side  it is visible 

I have verified it is not because of versions but

i have search for GPO none of the hiding shutdown GPO is on 

then what could be the reason can someone help me to solve this issue

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-20*

Hi @Nepali Sandhya  

Check if the GPO settings below  is applied when you login with domain adminsitrators accounts.

Check also if the right to shutdown is et on impacted machine :

Please don't forget to mark helpful answer as accepted
