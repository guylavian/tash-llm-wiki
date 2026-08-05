---
title: "Active Directory - check if a computer name is already taken"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1328828/active-directory-check-if-a-computer-name-is-alrea
question_id: 1328828
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory - check if a computer name is already taken

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1328828/active-directory-check-if-a-computer-name-is-alrea (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I configure a PC, one of the first steps is to assign a name to the device. I can only choose a name who belongs in "Active Directory Users and Computers". Before assigning a name, however, I need to figure out if that name is already taken by another device. To do this:

-  I open PowerShell and ping a name; if something reply to the ping, that means that the name is already taken;

-  I use a software named Advanced IP Scanner to examine the corporate's intranet to determine which names are already taken;

-  I use an asset management tool to see which names are already taken.

Despite these checks, sometimes I assign a name already taken.

I cannot simply delete a computer name and recreate it, because our Active Directory is managed my an external provider.

I need to figure out if there is a more reliable method to check which computer names are free to be assigned. Maybe a script on PowerShell, something like this I mean.

## Answers

_No answers on this thread._
