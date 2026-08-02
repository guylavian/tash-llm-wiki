---
title: "How to disable and enableusb on one GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1371108/how-to-disable-and-enableusb-on-one-gpo
question_id: 1371108
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How to disable and enableusb on one GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1371108/how-to-disable-and-enableusb-on-one-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone

I will create two GPOs. one GPO with the name DisableUSB and one enableUSB. disableUSB I set authenticated users, all users apply GPO. and enable USB add the user you want to enable. when run on the user's laptop the function is still disabled. Is the user set in enableusb?

Thank You

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

I think this is what you need:

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731387(v=ws.10)?redirectedfrom=MSDN
