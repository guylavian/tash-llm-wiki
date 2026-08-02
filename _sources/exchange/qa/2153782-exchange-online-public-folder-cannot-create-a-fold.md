---
title: "Exchange online public folder cannot create a folder as it states locked for migration."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153782/exchange-online-public-folder-cannot-create-a-fold
question_id: 2153782
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-exchange-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange online public folder cannot create a folder as it states locked for migration.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153782/exchange-online-public-folder-cannot-create-a-fold (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

Please i need your help on this issue.

I am trying to create Public Folders in this tenancy. However after creating the Public Folder mailboxes successfully the Public Folder tab still states 'No active public folder mailboxes were found for organization' and mentions this may also been seen if the PF mailbox was created with hold for migration enabled.

Neither of these is true, I notice that '(get-organizationConfig).rootpublicfoldermailbox' shows LockedforMigation is set to True, if I remove the PF Mailboxes then this clears back to False.

 

I am creating the PF Mailbox via the admin page but I have also used PowerShell and ensure I do not set locked for migration however it still doesnt help.

There have been previous attempts to migrate from on-premises Public Folders using the Microsoft batch scripts however no migration is in place currently.

There were some Public Folder mailboxes in the soft deleted that may have been created during that script attempt and therefore with lockedformigration set to true however I have removed these from soft delete.

for further clarification an attempt was made to perform a legacy batch migration from on-premises to Exchange Online before Christmas. 

However there was an error on Exchange Online that prevented the migration endpoint from creating (we had this on multiple customers and it was ultimately deemed a fault on Exchange Online due to the legacy authentication removal) and so that migration was abandoned. Now we are just trying to create new blank Public Folders.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-04*

Hi, @IniobongNkanga-8038  

According to the error message you provided, this error occurs when you create the first public folder mailbox using the HoldForMigration parameter in Exchange Server 2013 or Microsoft Exchange Server 2016 and try to create a new public folder on the Exchange server, which is made possible by design.

To resolve this issue, you need to delete the public folder mailbox, for more information, see the No active public folder mailboxes were found error - Exchange | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
