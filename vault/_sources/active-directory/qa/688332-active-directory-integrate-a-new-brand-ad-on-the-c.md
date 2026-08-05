---
title: "Active directory - Integrate a new brand AD on the coorporate domaine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/688332/active-directory-integrate-a-new-brand-ad-on-the-c
question_id: 688332
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active directory - Integrate a new brand AD on the coorporate domaine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/688332/active-directory-integrate-a-new-brand-ad-on-the-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we have a new brand that recently have been joined our group, so i must integrate their  AD domain to our global domain ( i have create a dedicated OU for it) but i must keep their own identity so they can use their old apps, erp , shared floders ...    

I must take the full control of their AD ( from the dedicated OU) and delegate for the local IT of this new brand the access to manage groups and acess .    

Is there any best practice to do this ( trust relationship between ADs or Federation identity management or something like that ) , please i need your suggestions.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-10*

Hello @Zied BEN SALEM       

Exactly, what you are looking for is AD FS (Federation Services). It is not a light theme to start from scratch, so I would recommend you to start with the official article of Microsoft with contains most of the information on how it works, how to configure it, steps, etc:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/understanding-key-ad-fs-concepts    

Hope this helps with your query,    

-----------    

--If the reply is helpful, please Upvote and Accept as answer--
