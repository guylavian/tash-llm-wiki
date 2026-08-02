---
title: "Broken GPO interactive logon"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1424150/broken-gpo-interactive-logon
question_id: 1424150
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Broken GPO interactive logon

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1424150/broken-gpo-interactive-logon (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

first of all sorry for my english. I hope you understand my problem.

I've found two problematic policies:

interactive logon: Display user information when session is locked.

and

Interactive logon: Don't display last signed-in.

First usecase:

When I enable Don't display last signed-in. When user locks screen, it shows user display name and thats okay. When he logout, it shows empty login a password boxes. which is okay to. And this is what I want, but...

Second usecase:

When I enable Don't display last signed-in and Display user information when session is locked set to: User display name, then when screen is locked it doesn't show anything. Just empty boxes for login and password. When i change it to: User display name, domain and login. It appears again. But there is no way to go back to first usecase, because registry key is created in: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "dontdisplaylockeduserid”

Also when I disable Don't display last signed-in and Display user information when session is locked set to: User display name, it start working again.

Only way to solve this is to remove key "dontdisplaylockeduserid” from registry and enable Don't display last signed-in gpo.

I have this problem for year and it is still broken. I dont need solution, because i have it.

I want you to fix this, so it works as intended.

Thank you

## Answers

_No answers on this thread._
