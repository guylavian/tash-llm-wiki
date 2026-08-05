---
title: "Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1405929/ex6f9304-microsoft-exchange-configuration-tasks-ma
question_id: 1405929
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1405929/ex6f9304-microsoft-exchange-configuration-tasks-ma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In O365 cross tenant migration

when I run the below command on the PowerShell connected to the target tenant,

Set-MailUser -Identity "email id " -ExchangeGuid "6**-5" -EmailAddresses @{add="x500:/o******a"} -ArchiveGuid ""

I get this error

Write-ErrorMessage : Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|The operation 

couldn't be performed because the object 'email ID' couldn't be found on 

'****.PROD.OUTLOOK.COM'.

The ID is already present in the new tenant and I am able to see it using get-mailbox* -identity "**" command

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-10-27*

A mail USER and a mail BOX are not the same thing. A MailUser does not have mailbox.
