---
title: "Exchange Database Drive getting automatically full"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187262/exchange-database-drive-getting-automatically-full
question_id: 1187262
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange Database Drive getting automatically full

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187262/exchange-database-drive-getting-automatically-full (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

I have been using Microsoft Exchange for last one years. I have an Hybrid Environment and also have two sites DC & DR. I implemented DR four months ago. After DR implementation, I detect that, my Exchange Mailbox Database Size increasing rapidly day by day. I checked the replication from DC to DR but found no issue. Now, please suggest me how to I fix this issue because we have a budget for storage. For last two months, I extended my disk size a lot of time. So, now it become a hassle for me. Please provide me any suggestion how to I resolve this issue. Thanks in advance.

N.B: I have total four mailbox servers. Two in DC site and two in DR site. If I need to check anything from performance monitor or resource monitor then please provide me steps. I am not good at performance monitor analysis.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-08*

Hi @Md. Rubiat Haque,

-  Please check the EDB files and database log files to determine if this is causing rapid consumption of disk space.

If you have deployed a DAG, you can perform a full backup, allowing the database's transaction log to be truncated upon successful completion of the backup.

-  To prevent the accumulation of log files, try enabling circular logging for the replicated database to check the transaction log.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
