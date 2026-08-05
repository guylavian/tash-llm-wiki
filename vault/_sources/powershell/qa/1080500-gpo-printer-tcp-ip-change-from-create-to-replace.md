---
title: "GPO - printer tcp/ip change from create to replace"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1080500/gpo-printer-tcp-ip-change-from-create-to-replace
question_id: 1080500
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# GPO - printer tcp/ip change from create to replace

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1080500/gpo-printer-tcp-ip-change-from-create-to-replace (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm looking for information but I can't find it. I'm not an expert in PowerShell and even less in handling gpo's with PS.    

Would it be possible to modify a gpo that is configured to create a tcp/ip printer and we want it to be Replace for a while?    

If we had to change one printer nothing happens, we change it through the GUI and that's it, the problem is that there are 400 printers and after 48/72 hours we have to change it again to create.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

I don't know how was created, when I arrived one year ago everything was created.    

If you have to modify 5 or 10 objects probably you can do it without any mistake, but if you have to make 400 changes sure you are going to make some mistakes and obviously is more useful and quick automatize the process ( if it is possible ) than do it manually

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-10*

Because I have to do this change 400 times and 48 hours later another 400 times.    

There are more or less 5000 printers, and every printer has its own GPO, and we have to correct 400.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-08*

Why use PowerShell? GPO's are centralized so making a change should be easy to accomplish using the GUI. I'm pretty sure his is going to be a change in the Group Policy Preference.    

I think you'd do better by adding the tag windows-group-policy to your question and removing the windows-server-powershell tag.
