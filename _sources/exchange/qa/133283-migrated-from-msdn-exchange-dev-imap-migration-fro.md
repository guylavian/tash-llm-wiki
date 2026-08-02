---
title: "[Migrated from MSDN Exchange Dev]IMAP migration from Exchange 2010 to O365 results in error: The specified message set is invalid."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/133283/migrated-from-msdn-exchange-dev-imap-migration-fro
question_id: 133283
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev]IMAP migration from Exchange 2010 to O365 results in error: The specified message set is invalid.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/133283/migrated-from-msdn-exchange-dev-imap-migration-fro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I’m migrating a bunch of mailboxes from Exchange 2010 on-prem to Office 365 based on IMAP.  

The most are going fine, but approximately 10 mailboxes have a status “Synced with errors”.  

The error is:  

Error: ImapBadResponseException: Error: Imap server sent BAD response to FetchCommand. Response code: ‎'‎', message: ‎'The specified message set is invalid.‎'  

When I download the report for that user I see  

Fatal error ImapBadResponseException has occurred.  

Can someone point me in the right direction?

Below is the output of some PS commands to gather some info.

Source link : https://social.msdn.microsoft.com/Forums/office/en-US/797ba37a-d8bc-451b-a220-bdc225a791a9/imap-migration-from-exchange-2010-to-o365-results-in-error-the-specified-message-set-is-invalid?forum=exchangesvrdevelopment

33813-get-syncrequest.txt

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-21*

Since you could migrate other mailboxes successfully, it means there doesn't exist issue with the configuration for IMAP migration. This issue may relayed with those mailboxes themselves, you could try to take steps below to narrow it:

-  Make sure the CSV file that you used are correct

-  Here are also some limitation that you need pay attention to:

-  Try to migrate those mailboxes to another database, the migration action will fix some minor problems in the mailbox itself.

-  Using command below to repair this mailbox file structure.

```
New-MailboxRepairRequest -Mailbox User1 -CorruptionType ProvisionedFolder,SearchFolder,AggregateCounts,Folderview
```

If you still cannot migrate this mailbox data to Exchange online, I would suggest you take this way to migrate data for this part of the mailbox:

-  Use New-MailboxExportRequest command to export data from Exchange on-premises mailboxes.

-  Use network upload to import your organization's PST files to Microsoft 365

If the response is helpful, please click "Accept Answer" and upvote it.
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
