---
title: "Regedit GPO does not apply, but it is downloaded by domain client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/483000/regedit-gpo-does-not-apply-but-it-is-downloaded-by
question_id: 483000
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Regedit GPO does not apply, but it is downloaded by domain client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/483000/regedit-gpo-does-not-apply-but-it-is-downloaded-by (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,     

I created a new GPO inside company domain.    

    

Later I linked to the properly domain users OU and laptop client downlod GPO properly, but this GPO is not applied.    

Domain controller is Win 2016 DataCenter and client is Windows 10 Pro.    

What can I do?    

Thanks in advanced

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-22*

Dear @ DaisyZhou-MSFT,    

Thanks for your detailed guide!    

I deleted GPO and I followed your guide. Now it is working fine!    

    

Instead in your picture path is different.    

    

Thanks for your help!    

Best regards!    

Federico

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-20*

First, enable logging and see what's wrong: http://www.virtuallyimpossible.co.uk/enable-group-policy-preference-logging-and-tracing
