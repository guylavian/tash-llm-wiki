---
title: "Exchange 2019 switch to empty DB"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1245689/exchange-2019-switch-to-empty-db
question_id: 1245689
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange 2019 switch to empty DB

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1245689/exchange-2019-switch-to-empty-db (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,
I have my exchange server 2019 on win2019 server. The user's mailbox database, .edb file is too big (more than 30GB). I need to archive this database and start with a new empty database.  The users (outlook 2019) must view the new and the old email.
How can I do this change of DB?
Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-21*

Hi @MDF ,

I need to archive this database and start with a new empty database. The users (outlook 2019) must view the new and the old email.

You can choose to move the primary mailbox to the new database, keeping the archive mailbox in the old database.
Please follow the article below to create a local move request with the EAC or use the New-MailboxMove cmdlet.
Manage on-premises mailbox moves in Exchange Server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-20*

Hello
Thank you for your question and reaching out. I can understand you are  having query\issues related  to Exchange.
You have to move to a new Mailbox in Order to end up with a smaller Database

Get-MailboxDatabase -Status | Select-Object Name, DatabaseSize, AvailableNewMailboxSpace | Format-Table -AutoSize
Then create a new Mailbox Database and use the New-MoveRequest commandlet to move the Mailboxes to a new Mailbox Database.
Get-Mailbox -Database MYOldDB
New-MoveRequest -Identity <Identity> -TargetDatabase "MYNewDB"
--If the reply is helpful, please Upvote and Accept as answer--
