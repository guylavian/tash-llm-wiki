---
title: "Exchange send report need edb log file？"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1607510/exchange-send-report-need-edb-log-file
question_id: 1607510
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange send report need edb log file？

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1607510/exchange-send-report-need-edb-log-file (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Exchange server, but I keep a large number of log files, and now I want to reduce these log files, I think of enabling circular log, but I have a question, that is, I usually use the delivery report to check some historical emails, if I enable circular log, will I be unable to query historical emails. Or are there other efficient ways to reduce storage on Exchange servers (third-party backup servers may not be allowed)?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-04*

Yes, Exchange uses circular logging to limit the message tracking log based on file size and file age to help control the hard disk space that's used by the log files.

You could refer to this article:

How to Cleanup, Truncate or Move Log Files in Exchange Server 2013/2016/2019? | Windows OS Hub (woshub.com)

In this article, we’ll look at different ways for cleaning, truncating and moving log files in Exchange Server 2013/2016/2019.

 Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.
