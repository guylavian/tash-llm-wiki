---
title: "Exchange Online Hybrid Public Mail Folder appear error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1850473/exchange-online-hybrid-public-mail-folder-appear-e
question_id: 1850473
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Online Hybrid Public Mail Folder appear error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1850473/exchange-online-hybrid-public-mail-folder-appear-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

0

We are currently running Exchange 2016 on premises with modern public folders. We are migrating to Exchange Online using a full hybrid configuration since the migration will take a few weeks. I am trying to set up Exchange Online so that people whos mailboxes have been migrated can access the public folders on our local Exchange 2016 server. I am using this as my procedure https://docs.microsoft.com/en-us/exchange/collaboration-exo/public-folders/set-up-modern-hybrid-public-folders. We have our active directory synced with Office 365 using Azure AD Connect. Most of the public folders are mail-enabled.

When I run the second step in the referenced article () in the Exchange Online PowerShell window, I get the message `Set-OrganizationConfig -PublicFoldersEnabled Remote -RemotePublicFolderMailboxes PublicFolderMailbox1,PublicFolderMailbox2,PublicFolderMailbox3`

Couldn't find object "PublicFolderMailbox1". Please make sure that it was spelled correctly or specify a different object.

The Sync-MailPublicFolders.ps1 was run over 24 hours ago and there were no sync errors reported from AADConnect. Where can I look to see why the objects didn't sync? Or is there a better document/procedure I should be following?

Thank you.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-01*

Sync-MailPublicFolders.ps1 is not relevant here. The setting you are trying to use points to the PF mailbox objects.

Does PublicFolderMailbox1 exist in Exchange Online as a recipient ( Mail User)

check with get-recipient and search by UPN or GUID if you cant find it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-01*

Hi

Thanks for posting your question in the Microsoft Q&A forum.

You could check if the pubic folders are synced in EAC of Exchange Online. If not, please check the CsvSummaryFile, it is the path to where you would like to log synchronization operations and errors, in .csv format.

Or re-run Sync-MailPublicFolders.ps1 -Credential (Get-Credential) -CsvSummaryFile:sync_summary.csv with the -WhatIf parameter.
