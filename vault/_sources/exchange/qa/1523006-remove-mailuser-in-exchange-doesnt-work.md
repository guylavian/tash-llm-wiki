---
title: "Remove-MailUser in Exchange doesn't work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1523006/remove-mailuser-in-exchange-doesnt-work
question_id: 1523006
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Remove-MailUser in Exchange doesn't work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1523006/remove-mailuser-in-exchange-doesnt-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have to remove a mailuser from Exchange Online. I use this command:
Remove-MailUser "4612299d-ae41-4423-a13f-f9576862eee6"

```
Write-ErrorMessage : Ex4215D1|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|Recipient "XXXXX
CNF:4612299d-ae41-4423-a13f-f9576862eee6" couldn't be read from domain controller "PA6P191A01DC002.EURP191A001.PROD.
OUTLOOK.COM". This may be due to replication delays. Switching out of Forest mode should allow this operation to com
plete successfully.
At C:\Users\dgene\AppData\Local\Temp\tmpEXO_l1dwninn.vjx\tmpEXO_l1dwninn.vjx.psm1:1192 char:13
+             Write-ErrorMessage $ErrorObject
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (Administratie m...3f-f9576862eee6:ADObjectId) [Remove-MailUser], Manag
   ementObjectNotFoundException
    + FullyQualifiedErrorId : [Server=AM9P191MB1860,RequestId=d0b134c5-6445-95f4-f947-641c5c84ea6b,TimeStamp=Fri, 0
   2 Feb 2024 15:05:39 GMT],Write-ErrorMessage
```

When I use this command: Remove-MailUser "4612299d-ae41-4423-a13f-f9576862eee6" -PermanentlyDelete

```
Write-ErrorMessage : |Microsoft.Exchange.Management.Tasks.RecipientTaskException|The mail enabled user you are tryin
g to permanently delete is not in a soft deleted state. Please make sure you soft delete the mail enabled user first
 before trying to permanently delete.
At C:\Users\dgene\AppData\Local\Temp\tmpEXO_l1dwninn.vjx\tmpEXO_l1dwninn.vjx.psm1:1192 char:13
+             Write-ErrorMessage $ErrorObject
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (XXXX...3f-f9576862eee6:ADObjectId) [Remove-MailUser], Recip
   ientTaskException
    + FullyQualifiedErrorId : [Server=AM9P191MB1860,RequestId=687c3950-aa16-b63d-ec08-9c4fa2c2a654,TimeStamp=Fri, 0
   2 Feb 2024 15:13:51 GMT],Write-ErrorMessage
```

Can anyone help me to force to delete this account?

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2024-02-02*

Can you use Get-Recipient to get the object? If so, try piping the result into the Remove-MailUser (assuming the object is a mail user and not something else like a mailbox, contact, shared mailbox, etc.).
This is really more an Exchange or O365 problem than a PowerShell issue.
