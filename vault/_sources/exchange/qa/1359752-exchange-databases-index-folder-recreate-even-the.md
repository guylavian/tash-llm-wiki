---
title: "Exchange database's index folder recreate even the database removed from the organization."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1359752/exchange-databases-index-folder-recreate-even-the
question_id: 1359752
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange database's index folder recreate even the database removed from the organization.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1359752/exchange-databases-index-folder-recreate-even-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

One of the exchange DB is removed from the organization and the index folder was deleted already, but the index folder will auto recreate after restart the "Microsoft Exchange Search Host controller" services

I also tried to format the disk (E:), the whole folder path will be created automatically after restarted that service.

Any idea?

Chong

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-06*

Hi @Chong ,

Thanks for posting in our Q&A forum.

First of all, please check the removed DB status, use the cmdlets `Get-MailboxDatabaseCopyStatus`. 

If you want to stop Exchange database’s index folder from recreating even after the database has been removed from the organization, you can disable indexing for that mailbox database. To do so, use the following PowerShell command:

```
Set-MailboxDatabase  -IndexEnabled $False
```

You can verify that indexing is disabled by running the following command:

```
Get-MailboxDatabase  | fl Name,IndexEnabled
```

If there are any update, feel free to let us know.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
