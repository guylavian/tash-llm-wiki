---
title: "BUG, GPO copy didn't work since last patchday"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1009013/bug-gpo-copy-didnt-work-since-last-patchday
question_id: 1009013
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# BUG, GPO copy didn't work since last patchday

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1009013/bug-gpo-copy-didnt-work-since-last-patchday (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi all,    

since last patchday copy files didn't work,    

GPO copy one file with 0 byte than it stop copy operation!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-27*

Here is a workaround to the issue:    

https://www.reddit.com/r/sysadmin/comments/xcxdss/patch_tuesday_megathread_20220913/    

EDIT6: If GPOs are still giving you issues, here is Microsoft's official workaround:    

Uncheck the "Run in logged-on user's security context (user policy option)." Note: This might not mitigate the issue for items using a wildcard (*).    

Within the affected Group Policy, change "Action" from "Replace" to "Update."    

If a wildcard (*) is used in the location or destination, deleting the trailing "" (backslash, without quotes) from the destination might allow the copy to be successful.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-27*

same problem: GPO copies just files names, but 0 KB, if copy manually the file copy sucessfull
