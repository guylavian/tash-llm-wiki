---
title: "Lock Screen  for User Configuration gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/884307/lock-screen-for-user-configuration-gpo
question_id: 884307
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Lock Screen  for User Configuration gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/884307/lock-screen-for-user-configuration-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Someone if you have done a similar function     "LockScreen Background Picture won't change"  for user configuration  ,The user can not edit the lock screen image

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-06-23*

Hi,    

You can use below GPO on Windows 10 Enterprise or Education.    

Computer Configuration\Administrative Templates\Control Panel\Personalization\Force a specific default lock screen image    

But the GPO doesn't work for Win 10 Professional. You can try User Configuration\Administrative Templates\Desktop\Desktop\Desktop Wallpaper    

For your reference:    

https://learn.microsoft.com/en-us/answers/questions/216889/windows-10-lock-screen-signin-screen-group-policy.html    

Best regards,    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it. Thanks.
