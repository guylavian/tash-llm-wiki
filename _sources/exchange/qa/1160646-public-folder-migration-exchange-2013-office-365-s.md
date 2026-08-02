---
title: "Public Folder Migration - Exchange 2013 > Office 365 - Stuck at 95% - MailEnabling Public Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160646/public-folder-migration-exchange-2013-office-365-s
question_id: 1160646
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Public Folder Migration - Exchange 2013 > Office 365 - Stuck at 95% - MailEnabling Public Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160646/public-folder-migration-exchange-2013-office-365-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

I am trying to migrate our public folder to Office365 following this guide:

[https://learn.microsoft.com/en-us/exchange/collaboration/public-folders/migrate-to-exchange-online?view=exchserver-2019

Everything runs through fine, there are no errors found in an validation scripts etc. But after creating the migration batch, it fails with:

Error: FailedToMailEnablePublicFoldersException: There are 2 Public Folders that could not be mail-enabled. Please, check the migration report starting at 1/13/2023 2:37:13 PM for additional details. This may indicate that mail public folder objects in Exchange Online are out of sync with your Exchange deployment. You may need to rerun the script Sync-MailPublicFolders.ps1 on your source Exchange server to update mail-enabled public folder objects in Exchange Online Active Directory.

The migration batch is still at 95% in powershell.

Following this guide:

[https://learn.microsoft.com/en-us/exchange/troubleshoot/public-folders/public-folder-migration-fails

Returns no results.

Re-running the sync-mailenabledmodernpublic folders script finds 0 mail enabled public folders.

I've deleted the batch, new PF mailbox created in Exchange 365, and started the whole process again from the beginning but it fails at the same stage with the same error.

I have no idea what 2 folders it's trying to mail-enable as none of them are mail enabled.

Can anyone help?

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-16*

Similar thread, " Mailbox Move failed Microsoft.Exchange.MailboxReplicationService.ProxyService did not receive a reply within the configured timeout (00:00:50)  ", the issue could be caused because the DataImportTimeout value is set too low, so you could try to increase the value in the file "MsExchangeMailboxReplication.exe.config" in the path "C:\Program Files\Microsoft\Exchange Server\V15\Bin", then perform the migration again to check the result.
