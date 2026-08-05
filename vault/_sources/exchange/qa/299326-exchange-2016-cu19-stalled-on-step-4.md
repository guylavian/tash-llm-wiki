---
title: "Exchange 2016 CU19 Stalled on Step 4"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299326/exchange-2016-cu19-stalled-on-step-4
question_id: 299326
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 CU19 Stalled on Step 4

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299326/exchange-2016-cu19-stalled-on-step-4 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're running CU19 on Exchange 2016, and we've been on Step 4 at 90% for over 2 hours now; removing exchange files. We did have one issue where we were running out of room on the C: drive, but cleared that up by removing inetpub log files that were substantial (almost a years worth). Still this did not seem to help. It is a virtual server running on VMWare vcenter 6.5 and we have a snapshot of the server prior to attempting the patch, so it is possible to reverse it. I just don't know if I should stop the execution, restart the server and try it again or just wait. There is CPU utilization on the server, but it is steady and not fluctuating at all. We had a similar issue with running updates on the server itself last night, but after about an hour it finished up. We did have to restart the server once because the update did stall at one point, and then continued without incident. Any thoughts, / advice would be greatly appreciated.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-04*

Nothing other than defender.  We're using SentinelOne but it was uninstalled before the update.  That's what I am hoping as well!  I may give that a shot in a few.
