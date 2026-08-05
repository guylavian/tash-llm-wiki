---
title: "Exchange 2019 Server Logging folder is keep increasing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1521509/exchange-2019-server-logging-folder-is-keep-increa
question_id: 1521509
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Server Logging folder is keep increasing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1521509/exchange-2019-server-logging-folder-is-keep-increa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
We have Exchange Server 2019 Dag with 4 Servers, we have notice that Exchange logging folder is keep increasing, how we can tackle this. We have third party backup as well but still logs are not getting truncated by the backup.
 
Kindly need the advice.
 
Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-08*

Open ESM and relocate log files from the c: drive to another storage pool. Ensure logs are backed up regularly to avoid data loss. Circular logging can be temporarily enabled for log flushing but is not recommended. Configuration: c: drive for system files, d: for log files, e: for data stores. Avoid making log files too large to backup efficiently. 

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-02*

Hi @IT Engineer,

Welcome to post our Q&A forum!

Regarding your problem, consider enabling circular logging on the database copies. Circular logging helps manage transaction logs by overwriting older logs, thus preventing excessive growth.

It will not affect DAG, although circular logging can help you save disk space, we do not recommend enabling circular logging in a production environment. Because the working method of the circular log is to overwrite the previous transaction log, if you want to perform data recovery, you cannot restore any data after the last full backup.

See: https://learn.microsoft.com/en-us/exchange/configure-circular-logging-for-a-mailbox-database-exchange-2013-help

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
