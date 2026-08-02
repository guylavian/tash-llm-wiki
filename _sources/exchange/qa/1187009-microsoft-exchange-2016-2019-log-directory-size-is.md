---
title: "Microsoft Exchange 2016/2019 Log Directory size is 20TB"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187009/microsoft-exchange-2016-2019-log-directory-size-is
question_id: 1187009
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange 2016/2019 Log Directory size is 20TB

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187009/microsoft-exchange-2016-2019-log-directory-size-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello world,

Anyone here have any advice for how I can convince other humans that a Microsoft Exchange performance latency problem that is showing high disk latency is coming from the fact their log and DB directories are 20TB in size when Microsoft recommends no larger than a 2TB disk?     Am I wrong for thinking this 20TB log directory is causing problems? 

This is in a fiber channel environment where the array is running constantly at 5ms.  No SAN congestion seen. No Hardware issues seen.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-09*

I don't think you will find a recommendation like that, but really its a waste right? No way they are generating that much in log space I would think.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-09*

There are 4 Exchange VM's sharing a single G:\ drive for the "Transaction Logs" and that disk size is 20TB.  I just feel databases don't like large log directories.  Trying to get verification that might be the cause of performance issues.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-07*

Hi @Jason Dodds ,

Is the 2TB you are referring to the OS disk?

You could refer to this blog: Looking Into Exchange Server Disk I/O Latency Issues

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
