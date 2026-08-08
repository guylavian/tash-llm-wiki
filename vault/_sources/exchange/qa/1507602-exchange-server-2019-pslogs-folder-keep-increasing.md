---
title: "Exchange Server 2019 PSlogs folder keep increasing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1507602/exchange-server-2019-pslogs-folder-keep-increasing
question_id: 1507602
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 PSlogs folder keep increasing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1507602/exchange-server-2019-pslogs-folder-keep-increasing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
We have Exchange 2019DAG with 4 Nodes, recently we have notice PSlogs folder is significantly increasing. its about 50 GB, however in other nodes its only 1 GB. This folder contains PowerShell_transcript logs.
Kindly need the work around for this issue
Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-23*

Hello @IT Engineer  ,

Welcome to the Q&A forum！

It is understood that this may be caused by the accumulation of log files. You could try delete old logs i.e. manually delete old or unnecessary log files from PSlogs folder. Before doing this, make sure these logs are not required for troubleshooting or other purposes.

Alternatively, this could also be caused by internal Exch Diag logs. This content will be automatically deleted after up to 30 days. If not, you could use PowerShell to clear the Exchange logs and get the free space on the Exchange Server. For more information, please refer to:https://www.alitajran.com/cleanup-logs-exchange-2013-2016-2019/
(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

Hope the above information is helpful to you.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
