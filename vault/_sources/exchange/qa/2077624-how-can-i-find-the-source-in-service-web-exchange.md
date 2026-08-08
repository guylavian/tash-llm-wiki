---
title: "How can I find the source in service web exchange of a repeated Active Directory Locked out user ??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2077624/how-can-i-find-the-source-in-service-web-exchange
question_id: 2077624
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# How can I find the source in service web exchange of a repeated Active Directory Locked out user ??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2077624/how-can-i-find-the-source-in-service-web-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are experiencing account lockout issues, and in Event Viewer, we see the following details:

-  Error Code: `0xC0000234` (Account locked out)

-  Process: `C:\Windows\System32\inetsrv\w3wp.exe`

-  Caller Process ID: `0x4618`

It seems to be related to IIS, but we're not sure what's causing these lockouts. Can anyone provide guidance on what might be triggering this and how to troubleshoot it?

Thanks in advance!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-24*

Hello,

Thank you for posting in Q&A forum.

Error status code 0xc0000234 means that the user account has been automatically locked due to too many invalid login or password change attempts. For details, you can refer to the following link:

https://shellgeek.com/error-code-0xc0000234-event-id-4776-fix/

I hope the information above is helpful.

Best regards

Zunhui

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-09-24*

Its a windows thing, so you can use this to track it down:

https://www.windows-active-directory.com/account-lockout-event-id-how-to-find-account-lockouts.html#:~:text=Using%20Event%20Viewer%20to%20Find%20Account%20Lockouts&text=Open%20the%20Event%20Viewer%20by,(on%20servers%20and%20workstations).
