---
title: "Best practices to apply GPO to only one computer in an OU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155474/best-practices-to-apply-gpo-to-only-one-computer-i
question_id: 155474
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Best practices to apply GPO to only one computer in an OU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155474/best-practices-to-apply-gpo-to-only-one-computer-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I am currently running 2012R2 DC in my environment.  I am going to add on another 2016 or 2019 as the 2nd DC.  I do need to apply some setting via GPO (as requested by Security Team) on the new DC.  There is an existing GPO for the 2012R2 but some of the settings are not applicable to 2016/2019.    

In this case, I will be creating a new GPO.  Knowing the new DC will appear in the Domain Controller OU once I promoted it, it will definitely inherited the existing GPO.  My understanding is, never never touch the Domain Controller OU and never create sub-OU within.    

Appreciate any advise on how to avoid exisitng GPO from applying to new DC and also to apply new GPO for the new DC only.    

Thank you in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

Hi Hannah,  

Appreciate the provided suggestion.  WMI filters works well for me.  Thank you.
