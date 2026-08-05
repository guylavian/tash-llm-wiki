---
title: "Have some troubles with migration to 365 exchange mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1659664/have-some-troubles-with-migration-to-365-exchange
question_id: 1659664
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Have some troubles with migration to 365 exchange mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1659664/have-some-troubles-with-migration-to-365-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day, everyone

i got some problems with migration mailboxes to exchange online,

I have a hybrid environment with on-premises Exchange 2013 and I have successfully migrated about 20 mailboxes to Exchange Online, but one of the mailboxes is not migrating with various errors, initially it had the status "NeedsApproval", with  than i used 

```
Get-MigrationBatch -Status needsapproval | Set-MigrationBatch -ApproveSkippedItems
```

but it did not bring results, then i tried repair mailbox in on-premise side with 

```
New-MailboxRepairRequest -Mailbox mailboxname -CorruptionType ProvisionedFolder, SearchFolder, AggregateCounts, Folderview
```

and it complete without any issue, and when i tried migrate again, i got error "Transient error CommunicationWithRemoteServiceFailedTransientException has occurred. The system will retry"

## Answers

_No answers on this thread._
