---
title: "Best way to migrate from hosted exchange provider to EXO with existing users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1100377/best-way-to-migrate-from-hosted-exchange-provider
question_id: 1100377
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Best way to migrate from hosted exchange provider to EXO with existing users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1100377/best-way-to-migrate-from-hosted-exchange-provider (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a hosted Exchange provider which does not give us direct access to management tools, but only through a Java tool. We are moving to Microsoft 365 and would like to migrate users in batches. (I have setup an ad-hoc hybrid system using rules and a connector.) We have about 150 email users on the other provider, but about 100 of those already have MSO accounts with (empty) mailboxes due to our prior use of Teams and SharePoint.    

Since we are unable to sync directories, is there any possibility of migrating to existing users so they maintain their Teams and SharePoint data? Or are we stuck exporting PST files or using IMAP? And is IMAP a reasonable choice here for those who aren't too attached to their contacts or calendars? I have done that in the past from non-Exchange platforms and experienced occasional glitches. Should I expect better, worse, or the same with Exchange 2013?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-25*

Classic EAC to the rescue. The old migration wizard correctly defers to autodiscover for the server information. I was able to connect for a test migration. Sadly, even after changing my test account to "onmicrosoft" to clear the "proxy address is already being used..." error, I receive an AD sync error because the alias is still the same, just like when trying to create the same email address on two different domains. Microsoft trying to save us from ourselves again. So it looks like the answer is "No, it can't be done." Apparently the users must be completely removed from Azure AD before attempting the migration due to this bug.    

Thanks to everyone who attempted to help.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-25*

Hi @Kevin Wade   ,    

Deleting EXO licenses may cause loss of user data, and it is difficult to export backups of Teams and SharePoint user data. If you want to use cutover to migrate mailboxes, you could refer to Migrate email to Exchange Online using the Exchange cutover method. Here are the prerequisites and methods for migration.    

In addition, for migration, you could refer to the mail migration advisor, it could help you plan your migration and assist you with the migration.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-23*

Before taking up a migration process, you need to be prepared with pre-migration, migration, and post-migration planning to avail a hassle-free cloud migration. You can check this article How to Decide Best Migration Path from Exchange to Office 365? for more information.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-23*

Hi @Kevin Wade   ,    

You could migrate your IMAP mailboxes to Microsoft 365 or Office 365.  When you migrate the user's email by using IMAP migration, only the items in the users' inbox or other mail folders are migrated. Contacts, calendar items, and tasks can't be migrated with IMAP, but they can be by a user. In addition, you may need to have the appropriate permissions and the source system supports IMAP migration in order for you to use IMAP.    

The easiest way is to let the user export the on-premise mails through outlook then import them to the mailbox in cloud, change the MX record to make new mails coming to cloud.    

For some users who already have a mailbox, refer to this approach:    

Backing up the users 365 mailbox to PST    

Revoking the 365 license (which deletes the 365 mailbox)    

Forcing an Azure AD sync    

Migrating the on-site mailbox to Exchange 365    

Re-assigning the license    

Importing mails from the PST back into the 365 mailbox again    

You could refer to the similar case: Exchange 365 Migration - Single user, dual mailboxes    

Unable to synchronize directories, see if this helps you: How to merge an Office 365 account with an on-premises AD account after hybrid configuration?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
