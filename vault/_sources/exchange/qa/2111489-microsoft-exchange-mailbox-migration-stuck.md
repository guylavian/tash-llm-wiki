---
title: "Microsoft Exchange mailbox migration stuck"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2111489/microsoft-exchange-mailbox-migration-stuck
question_id: 2111489
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft Exchange mailbox migration stuck

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2111489/microsoft-exchange-mailbox-migration-stuck (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We started migrating mailboxes from databases on Exchange 2016 to ones on Exchange 2019. We had migrated about 65 mailboxes with no issue but on one of our batches some of the larger mailboxes(30-50GB) were taking a long time so we started another batch in the meantime. Both batches got stuck so we have since deleted them and planned to move some larger mailboxes one by one, but now the migrations seem stuck and won't get started, when checking the details, they don't see to move beyond 0 bytes.   

What should we do to fix the issue?  

Thanks,  

George

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-28*

Hi @George Gaprindashvili  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are currently experiencing a stuck Microsoft Exchange mailbox migration process. Here are some steps you can take to troubleshoot and resolve the issue:

-  Sometimes, a previous move request can interfere with the new migration. Run the following command to check if there are any existing move requests:

```
Get-MoveRequest | Get-MoveRequestStatistics
```

If you find any stuck requests, you can remove them with the following command:

```
Remove-MoveRequest -Identity 
```

-  Restarting the Exchange services on both the source and target servers can sometimes resolve the stuck migration issue. You can do this through the Services console or using PowerShell:

```
Restart-Service MSExchangeMailboxReplication
```

-  Modify the MSExchangeMailboxReplication.exe.config file to increase the value that controls performance. This file is located in C:\Program Files\Microsoft\Exchange Server\V15\Bin. Find the MRSConfiguration section and adjust the value to improve performance.

-  If there are corrupted items that could cause the migration to stall, you can skip them by using the Set-MoveRequest cmdlet with the MoveOptions parameter:

```
Set-MoveRequest -Identity  -MoveOptions:SkipFolderPromotedProperties,SkipFolderViews,SkipFolderRestrictions
```

-  Large mailboxes may take longer to migrate. Consider breaking the migration into smaller batches or migrating large mailboxes during off-peak hours to reduce the load on the server.

-  Download and review the migration report for any errors or warnings that may give you more insight into why the migration is stalled.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
