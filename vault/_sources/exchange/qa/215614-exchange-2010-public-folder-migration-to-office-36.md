---
title: "Exchange 2010 public folder migration to Office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/215614/exchange-2010-public-folder-migration-to-office-36
question_id: 215614
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2010 public folder migration to Office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/215614/exchange-2010-public-folder-migration-to-office-36 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am a bit confused about what mailbox(es) need to be created for proxy access to the on prem Exchange 2010 public folders.     

https://learn.microsoft.com/en-us/exchange/collaboration/public-folders/configure-legacy-public-folders-for-hybrid?view=exchserver-2019     

Step 5 states    

"You will point to all of the proxy public folder mailboxes that you created in Step 2: Make remote public folders discoverable to enable the Exchange Online organization to access the on-premises public folders."    

In step 2 you create an empty mailbox database and populate it with a proxy mailbox.  Is only one proxy mailbox required to facilitate access  to all legacy public folders on a single host?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-31*

Thank you very much!!!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-31*

So is it safe to say that once the mailbox is created and the following command is run - Mailboxes that have been migrated to Office 365 will be able to access on prem public folders?  

Set-OrganizationConfig -PublicFoldersEnabled Remote -RemotePublicFolderMailboxes PFMailbox1,PFMailbox2,PFMailbox3
