---
title: "[Migrated from MSDN Exchange Dev] restore previously deleted mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145642/migrated-from-msdn-exchange-dev-restore-previously
question_id: 145642
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] restore previously deleted mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145642/migrated-from-msdn-exchange-dev-restore-previously (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/8207d502-1a08-4685-851b-ea21b907d2f5/restore-previously-deleted-mailbox?forum=exchangesvrdevelopment  

Exchange 2016 - Management had me delete a mailbox and user for a furloughed employee. Now, 10 days later, they want me to restore the user and mailbox. Is there an easy way to do that without going to my backups?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

When you delete a mailbox, Exchange retains the mailbox in the mailbox database and switches the mailbox to a disabled state. The associated Active Directory user account is also deleted. The mailbox is retained until the deleted mailbox retention period expires, which is 30 days by default, and then it's permanently deleted (or purged) from the mailbox database.  

Until a deleted mailbox is permanently deleted from the Exchange mailbox database, you can use the EAC or the Exchange Management Shell to connect it to an Active Directory user account. You can also use the Exchange Management Shell to restore the contents of the deleted mailbox to an existing mailbox.  

For more information, see Connect or restore a deleted mailbox

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
