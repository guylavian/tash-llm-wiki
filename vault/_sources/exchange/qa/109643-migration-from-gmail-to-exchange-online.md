---
title: "Migration from Gmail to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/109643/migration-from-gmail-to-exchange-online
question_id: 109643
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Migration from Gmail to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/109643/migration-from-gmail-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I currently have a client who is using Gmail business and is looking to migrate to Exchange Online.  The challenge is there are 50-60 mailboxes that have more than 100GB of mailbox data.  The data cannot be deleted and needs to be kept for 3-5 years before being archived or deleted.  

Is there a way to migrate this data to Exchange Online and possibly get larger mailboxes for these specific accounts?

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-29*

Hi @Dhillan Kalyan   , totally agree with the suggestions above. You will get error if you attempt to migrate mailboxes larger than 100GB. So we will need to perform the below actions to make the mailboxes able to be migrated.    

-  Exporting the contents of the Mailbox to PST    

-  Reducing the size of the mailbox bringing it to under 100GB by deleting or moving content    

-  Importing the PST into the Cloud Archive Mailbox    

Please also referring to the official document about Mailbox storage limits in Exchange online.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-09-28*

Hi,    

You can follow the instruction in the below article for the migration of Gmail to Microsoft 365.    

https://learn.microsoft.com/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrate-g-suite-mailboxes    

For larger mailboxes, you can extract the PST's and make the primary mailbox less than 100GB, so migration can be performed similar to other mailboxes. Enable the In-place archiving in Exchange Online for those users and import the PST. Please also verify the license type include the unlimited archiving.
