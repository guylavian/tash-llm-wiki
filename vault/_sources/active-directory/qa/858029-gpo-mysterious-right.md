---
title: "GPO Mysterious Right"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/858029/gpo-mysterious-right
question_id: 858029
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO Mysterious Right

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/858029/gpo-mysterious-right (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Microsoft Community,    

I have a mysterious error when i try to edit a GPO in my Domain controller    

    

My Account is domain admin and got fully permission on the GPO folder ID.    

Already check with the builtin administrator account, the issue is the same    

The issue should be a right permission but i don"t find.    

The issue is not present on all GPO, the issue is not present when i clone the GPO

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-24*

Hi,  

the issue is the same from an another sever or DC.  

The issue is present only in certain option, not all.  

After a copy of the gpo the problem is solved

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-21*

Do you get the same error with any other GP's? Have you tried to access the GP from another workstation / server to edit it? Any errors in the event logs on the DC's around the time of the error?
