---
title: "Exchange on prem public folders move from 2016 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1382605/exchange-on-prem-public-folders-move-from-2016-to
question_id: 1382605
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange on prem public folders move from 2016 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1382605/exchange-on-prem-public-folders-move-from-2016-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm decomishoning an exchange 2016 server, i've migrated the public folder mailbox over to 2019. 

I've verified everything is moved, but when i shut down 2016 the shared folders and calendars disapear.

Booting up the 2016 server restores all folders.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-06*

Exchange 2016's Public Folder Mailbox is removed when you shut it down. This is so because public folders are kept in a unique mailbox called the Public Folder Mailbox. The Public Folder Mailbox is automatically generated when Exchange 2016 is launched.

You must transfer the Public Folder Mailbox to a new Exchange server, such as Exchange 2019, to prevent your public folders and calendars from disappearing when you shut down Exchange 2016. After relocating the Public Folder Mailbox, Exchange 2016 can be safely terminated.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-06*

Hi @Geoff Griffith  

Just want to confirm with you the migration status of public folder mailbox and public folder.

`Get-MoveRequest`

View the location of public folder mailboxes after the move request is completed.

`Get-Mailbox -PublicFolder | Get-MailboxStatistics | Format-Table ServerName,DisplayName,TotalItemSize`

Also, are you referring to the folder and calendar in the public folder?

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
