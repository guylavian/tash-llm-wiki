---
title: "Backup and recovery of Exchange server during CU installation: is only volume C: enough or all databases are required?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309871/backup-and-recovery-of-exchange-server-during-cu-i
question_id: 309871
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Backup and recovery of Exchange server during CU installation: is only volume C: enough or all databases are required?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309871/backup-and-recovery-of-exchange-server-during-cu-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day!  

There is an Exchange 2013 server with the mailbox and CAS roles, the application itself is installed on the C: drive, and the mailbox databases on other logical drives.  

If, before installing the CU, you backup only the C: volume using Windows Server Backup, then in case of an unsuccessful CU update and the need to rollback, will it be enough to restore only the C: volume from this backup? Will the serviceability of the bases remain in their current state, provided that they remain in their places?  

And it is necessary to restore the entire C volume: is it entirely or is System State enough?  

Or, after the server has been rolled back to the state before the CU installation, it is necessary to roll back all the databases from the backups to the state before the CU installation, even if they were not damaged?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-12*

Hi, @Pavel       

The best practice should be taking a full backup of the Exchange server, including the volume of the databases.    

Since Exchange backup and restore is on application-level, the database files should not be treated as individual files.    

Anyway, it is always recommended to backup your data just in case of damage since the data is priceless.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-11*

Always backup the DB's before an update  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
