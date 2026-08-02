---
title: "Exchange Online PowerShell filter bug"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1669311/exchange-online-powershell-filter-bug
question_id: 1669311
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Exchange Online PowerShell filter bug

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1669311/exchange-online-powershell-filter-bug (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Exchange Online PowerShell module seems to have a bug within the -Filter argument for Get-Mailbox. Specifically with the AuditEnabled property of a mailbox. I've tried the following:

`Get-Mailbox -Filter 'AuditEnabled -eq $False'`

`Get-Mailbox -Filter "AuditEnabled -eq 'False'"`

They don't seem to work though:

Using double quotes like `Get-Mailbox -Filter "AuditEnabled -eq $False"` just throws an error for invalid filter syntax so that's not it. Anyone seen this before?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-16*

Try `"AuditEnabled -eq `$False"`

See: https://learn.microsoft.com/en-us/powershell/exchange/recipient-filters?view=exchange-ps#additional-opath-syntax-information

-  System values: Don't enclose system values (for example, $true, $false, or $null). To enclose the whole OPATH filter in double quotation marks, you need to escape the dollar sign in system value (for example, `$true).
