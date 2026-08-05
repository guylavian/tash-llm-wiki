---
title: "Active Directory Account Automatically Lock Out"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1362853/active-directory-account-automatically-lock-out
question_id: 1362853
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Account Automatically Lock Out

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1362853/active-directory-account-automatically-lock-out (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have active directory domain in our environment. And we have a account lockout policy for maximum 3 wrong password count and Screen lockout policy after 5 min of inactive uses. The problem we face is, some time some account continuously getting locked.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-09*

On the DC look for event ID 4740. On servers and computers look for event 4625. Both require audit policy to be configured.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-09*

You will need to enable audit logs and do some digging into the event logs to find the source computer. Then dig into the local computer event logs to find exactly what is causing the lockouts. 

Here is a detailed guide that walks through the steps. 

https://activedirectorypro.com/account-lockout-event-id/
