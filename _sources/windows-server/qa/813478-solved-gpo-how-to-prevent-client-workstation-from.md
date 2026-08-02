---
title: "[Solved]GPO - How to prevent client workstation from upgrading Windows 11"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/813478/solved-gpo-how-to-prevent-client-workstation-from
question_id: 813478
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# [Solved]GPO - How to prevent client workstation from upgrading Windows 11

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/813478/solved-gpo-how-to-prevent-client-workstation-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

My environment : 4 domain controllers : 2 Windows server 2016 Standard (1 of them hold 5 FSMO roles) , 2 Windows server 2012 Standard    

Current domain function level : Windows server 2008 R2    

I want my GPO prevent client workstation from upgrading to Windows 11 but still receive latest updates for Windows 10 , I google and found some tutorials roughly like    

Navigate to Computer Configuration > Policies > Admin Templates > Windows Components > Windows Update > Manage updates offered from Windows Update. Double click "Select the target Feature Update version", set to enabled, put "Windows 10" in the first box and "21H2" in the second.    

But this is what I see from my Windows server 2016 Standard domain controller    

    

    

What should I do ? Should I raise domain function level ? Or install Administrative Templates for windows 10 21H2 ?    

Please give me some advice thank you very much.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-20*

I follow this instruction https://learn.microsoft.com/en-us/answers/questions/813478/gpo-how-to-prevent-client-workstation-from-upgradi.html and make it work.
