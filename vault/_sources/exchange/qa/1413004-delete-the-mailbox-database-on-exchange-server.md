---
title: "Delete the mailbox Database on Exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1413004/delete-the-mailbox-database-on-exchange-server
question_id: 1413004
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# Delete the mailbox Database on Exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1413004/delete-the-mailbox-database-on-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.

We need to delete the mailbox Database in Exchange server and we receive this message:  

 This mailbox database contains one or more mailboxes, mailbox plans, archive mailboxes, public folder mailboxes or arbitration mailboxes. To get a list of all mailboxes in this database, run the command Get-Mailbox -Database Database ID. To get a list of all mailbox plans in this database, run the command Get-MailboxPlan. To get a list of archive mailboxes in this database, run the command Get-Mailbox -Database Database ID -Archive. To get a list of all public folder mailboxes in this database, run the command Get-Mailbox -Database Database ID -PublicFolder. To get a list of all arbitration mailboxes in this database, run the command Get-Mailbox -Database Database ID -Arbitration.
To disable a non-arbitration mailbox so that you can delete the mailbox database, run the command Disable-Mailbox Mailbox ID. To disable an archive mailbox so you can delete the mailbox database, run the command Disable-Mailbox Mailbox ID -Archive. To disable a public folder mailbox so that you can delete the mailbox database, run the command Disable-Mailbox Mailbox ID -PublicFolder. Arbitration mailboxes should be moved to another server; to do this, run the command New-MoveRequest Parameters. If this is the last server in the organization, run the command Disable-Mailbox Mailbox ID -Arbitration -DisableLastArbitrationMailboxAllowed to disable the arbitration mailbox. Mailbox plans should be moved to another server; to do this, run the command Set-MailboxPlan MailboxPlan ID -Database Database ID.

-  CategoryInfo : InvalidOperation: (Database ID :DatabaseIdParameter) [Remove-MailboxDatabase], AssociatedUserMailboxExistException

-  FullyQualifiedErrorId : [Server= Server,RequestId= RequestId,TimeStamp= TimeStamp ] [FailureCategory=Cmdlet-AssociatedUserMailboxExistException] XXXXXXXX,Microsoft.Exchange.Management.SystemConfigurationTasks.RemoveMailboxDatabase+ PSComputerName : Computer Name

These comandlets not results 

Get-Mailbox -Database db

Get-Mailbox -Database db -Monitoring

Get-Mailbox -Database db -Archive

Get-Mailbox -Database db -Arbitration

Get-Mailbox -Database db -AuditLog

Get-Mailbox -Database db -PublicFolder

Any ideas?

## Answers

_No answers on this thread._
