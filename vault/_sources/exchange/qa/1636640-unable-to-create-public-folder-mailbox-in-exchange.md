---
title: "Unable to Create Public Folder Mailbox in Exchange Online Line - Receiving quota error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1636640/unable-to-create-public-folder-mailbox-in-exchange
question_id: 1636640
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Unable to Create Public Folder Mailbox in Exchange Online Line - Receiving quota error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1636640/unable-to-create-public-folder-mailbox-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Unable to create the hierarchy serving public folder mailbox, receiving a error message -  exceeded the resource quota (100) enforced by policy "Recipient Quota Policy: PublicFolderHierarchyMailboxCountQuota"   Please note there an no Public Folder Mailboxes showing in our tenancy.

I am however able to create secondary non-hierarchy serving public folder mailboxes using powershell.

Any help would be appreciated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-01*

Is it the pure Exchange Online? Did you have migrated PF from Exchange On-premises?

You mentioned that you cannot create hierarchy public folder mailbox, but you can create secondary non-hierarchy serving public folder mailboxes, how did you verify this? Because the only difference between creating the primary hierarchy mailbox and a secondary hierarchy mailbox is that the primary mailbox is the first one created in the organization. How did you create the primary mailbox?

Please run the following command to verify that you have successfully created the primary public folder mailbox:

Get-OrganizationConfig | Format-List RootPublicFolderMailbox

Reference: Create a public folder mailbox in Exchange Online | Microsoft Learn
