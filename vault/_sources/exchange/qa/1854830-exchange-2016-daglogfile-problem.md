---
title: "Exchange 2016 DagLogfile problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1854830/exchange-2016-daglogfile-problem
question_id: 1854830
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 DagLogfile problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1854830/exchange-2016-daglogfile-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two server { Ex16-01 } { Ex16-02 } 

The copy of the database on 02 is not synchronizing, can I use an update to fix it?

At '2024/8/2 15:05:20' the Exchange store database 'common' copy on this server appears to be inconsistent with the active database copy or is corrupted. For more detail about the failure, consult the Event log on the server for other storage and "ExchangeStoreDb" events. The passive database copy has been suspended.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-08*

To fix this issues, you can try to update the database copy.

You can check the event logs on Ex16-02 to know the possible reason of failing of database copy. Search for any storage or “ExchangeStoreDb” events.

If there is any corruption or syncing issues in logs, you can create fresh copy of database from the active one by running give command- Update-MailboxDatabaseCopy -Identity "common\Ex16-02" –CatalogOnly After this the synchronization issues will be resolved.

As also suggested by Jake, Run eseutil to check Exchange database integrity on both the active and passive copies.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-05*

Hi @Carl Zhang  ,Welcome to the Microsoft Q&A platform!

According to your description, it sounds like you are dealing with an Exchange Server Database Availability Group (DAG) issue. Here are the general steps you can take to address and possibly resolve the synchronization problem:

-  You can try suspending and then resuming the database copy. This might help in resetting the state and allowing the replication to restart.

```
Suspend-MailboxDatabaseCopy -Identity "common\Ex16-02" Resume-MailboxDatabaseCopy -Identity "common\Ex16-02"
```

-  If suspending and resuming the copy does not work, you can use the `Update-MailboxDatabaseCopy` cmdlet to reseed the database copy. This will copy the database and logs from the active copy to the passive copy.

```
Update-MailboxDatabaseCopy -Identity "common\Ex16-02" -CatalogOnly
```

   If the `-CatalogOnly` option doesn't work, you may need to perform a full reseed:

```
Update-MailboxDatabaseCopy -Identity "common\Ex16-02" -DeleteExistingFiles
```

-  Ensure there are no network issues between `Ex16-01` and `Ex16-02` that might be causing replication failures.

-  Verify that `Ex16-02` has enough disk space and that the disk health is good. You can use tools like `chkdsk` to check the disk for errors.

-  Run `eseutil` to check the integrity of the database on both the active and passive copies. This tool is part of the Exchange toolbox and can help identify corruption issues.

```
eseutil /mh "path_to_database_file"
```

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
