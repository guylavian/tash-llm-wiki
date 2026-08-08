---
title: "Audit Log doesn't work in Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/397584/audit-log-doesnt-work-in-exchange-2013
question_id: 397584
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Audit Log doesn't work in Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/397584/audit-log-doesnt-work-in-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I enabled Audit Log for the mailboxes in our organization by enabling AuditEnable value as True. However when I tried  to search the log for the actions of the mailbox owner, there's no result. From the official KB, it turns out that auditing of mailbox owner actions can generate a large number of mailbox audit log entries and is therefore disabled by default.     

So I enabled the auditing of mailbox owner actions by the cmdlet below. And I did move emails from the Inbox folder to the other folders and delete some emails. However still, the cmdlet search-mailboxaudit returns none. What's the real problem?    

Set-Mailbox -Identity <> -AuditOwner "Move,MoveToDeletedItems,SoftDelete,HardDelete" -AuditEnabled $true    

https://learn.microsoft.com/en-us/exchange/mailbox-audit-logging-exchange-2013-help    

https://learn.microsoft.com/en-us/exchange/enable-or-disable-mailbox-audit-logging-for-a-mailbox-exchange-2013-help

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-18*

Hi,    

Please run the following command to check if the size of folder is 0KB:    

```
Get-MailboxFolderStatistics User2 |where{$_.Name -like "*audit*"}
```

Aslo, check the account you use is in Records Management management role group.    

Next step, follow this KB and change the language settings on the server where the searched mailbox is located:     

Search-AdminAuditLog and Search-MailboxAuditLog with parameter return empty results    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
