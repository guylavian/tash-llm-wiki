---
title: "Active Directory Domain Services Stops after 10-15 minutes."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/757119/active-directory-domain-services-stops-after-10-15
question_id: 757119
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Domain Services Stops after 10-15 minutes.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/757119/active-directory-domain-services-stops-after-10-15 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A client is using 2012R2 DC, all the fsmo roles are installed in the same one. Everytime the customer start the DC the ADDS service stops working after 10-15 minutes. Customer has 5 DCs including one 2008R2. All the DCs having same issue.   

I have initially changed the value of sysvol to 1.   

Tried uninstalling the update KB5009624 and installing the patch which I thought may causing the problem also installed the patch KB5010794.   

What could be causing the issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-04*

Hello.. Everyone..  

I have installed windows server 2016 in my system then active directory install than active directory is error

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-03*

the ADDS service stops working after 10-15 minutes  

how are you evaluating?  

what's captured in the event logs when this happens?
