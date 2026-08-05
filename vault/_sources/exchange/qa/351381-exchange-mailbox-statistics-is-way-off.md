---
title: "Exchange Mailbox statistics is way off"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351381/exchange-mailbox-statistics-is-way-off
question_id: 351381
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Mailbox statistics is way off

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351381/exchange-mailbox-statistics-is-way-off (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have never run into this before a few days ago.  I have a user that received a lot of messages in their mailbox after an automated process went off the rails, so the mailbox size ballooned to over 8.5GB; normal users have a ProhibitSendQuota of 1GB, and a ProhibitSendReceiveQuota of Unlimited.  Naturally this was a problem for the user.  They performed some cleanup on the mailbox and actually reduced it down to just over 50MB.  The problem is that while Outlook reports the folder size to be about 50MB, the mailbox size statistic used when reporting the quota is over 1.5GB.  I check in Powershell with "Get-MailboxStatistics <user> | select *size" and the TotalItemSize is 1.507GB; this is the value being used for emailing nags about the quota and what Outlook reports as the total mailbox size.  I run "Get-MailboxFolderStatistics <user> | select Name, *Size | ft" and the Top Of Information Store reports the FolderAndSubfolderSize is 57.87MB; this matches what can be seen when looking at the folder sizes in Outlook.  I expected this to take up to 12 hours or so to catch up, but it's been a few days and the numbers just aren't updating.  I thought moving the mailbox would shake things up and make it right itself, so I moved the mailbox to another database; the move took forever, since it had to move almost 9GB of recoverable items, but it did complete.  There is still no change to the Mailbox Statistics.  

Anyone else run into this?  We are running Exchange 2016 CU19.

## Answers

_No answers on this thread._
