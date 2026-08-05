---
title: "Exchange 2016 Mailbox Replication service stuck"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2150928/exchange-2016-mailbox-replication-service-stuck
question_id: 2150928
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Mailbox Replication service stuck

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2150928/exchange-2016-mailbox-replication-service-stuck (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Just upgraded to Exchange 2016 from 2010.  All user mailboxes are moved and just migrated the Public Folders.  Now the mailbox replication service is stuck on stopping.  There is no mailbox moves that I can find in the exchange servers. Restarting the servers and even shutting down for 10 minutes and rebooting doesn't resolve the issue.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-27*

Hi @Monte Caldwell  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are dealing with an issue where the Mailbox Replication Service (MRS) is stuck in a stopped state. Here are a few steps you can try to resolve the issue:

-  Run the following PowerShell commands to make sure there are no pending move requests:

```
Get-MoveRequest | Get-MoveRequestStatistics
```

If there are, you may need to remove them using the following command:

```
Remove-MoveRequest -Identity 
```

-  Sometimes, manually restarting the service can help. Run:

```
Restart-Service MSExchangeMailboxReplication
```

-  Look for any related errors in Event Viewer under Applications and Services Logs > Microsoft > Exchange > MailboxReplication. This may give you more insight into what is causing the issue.

-  Make sure your Exchange 2016 server is updated with the latest cumulative updates and patches. Sometimes, updating can resolve underlying issues.

-  Check the health of MRS using the following command:

```
Get-ServerHealth -Identity  | Where-Object {$_.HealthSetName -eq "MailboxReplication"}
```

-  If the above steps do not work, you may need to rebuild the MRS configuration. This involves stopping the service, deleting the configuration file, and then restarting the service. Perform this step with caution and ensure you have a backup.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
