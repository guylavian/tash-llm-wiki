---
title: "Cannot Move user Mail box to another Exchange database which is DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190441/cannot-move-user-mail-box-to-another-exchange-data
question_id: 1190441
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Cannot Move user Mail box to another Exchange database which is DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190441/cannot-move-user-mail-box-to-another-exchange-data (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Moving user mailbox  in Exchange Server 2016 DAG Active Database to another Active Database on another member gives following errors

Mailbox migration stops at 95 % giving the below error

Error: MigrationMRSPermanentException : Error: Mailbox changes failed to replicate: Database c0c1dbe-12f4-45b5-8498-51756a2ffc5c doesn’t satisfy the constraint Second Copy because the commit time 11/16/2022 5:00:16 AM isn’t guaranteed by replication time

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-20*

Please remove the failed move request and create a new one by adding the skipmoving parameter:

`New-MoveRequest -identity <mailbox> -skipmoving:folderviews,folderrestrictions -TargetDatabase <database>`  

And see if the shared mailbox can be moved successfully.

Set-MailboxDatabaseCopy cmdlets in the Exchange Management Shell to view and configure database copy settings, such as replay lag time, truncation lag time, and activation preference order. For detailed steps to view and configure database copy settings, see Configure mailbox database copy properties.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-16*

Is replication good between those databases? 

```
Get-mailboxdatabasecopy
```

You can bypass the restriction, but I would look at the health of the databases first.

```
Set-mailboxdatabase -identity  -DataMoveReplicationConstraint None
```
