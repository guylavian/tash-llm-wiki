---
title: "Exchange database edb size"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1120849/exchange-database-edb-size
question_id: 1120849
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange database edb size

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1120849/exchange-database-edb-size (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way to smoothly reduce the database edb file size?     

I've tried moving 50% mailboxes to another db, however the original db's edb file size keeps the same.     

I've learned db defrag using eseutil can release the space, but it must dismount the db which is unwanted.    

By the way, can someone tell me the clear defination of this parameter "availablenewmailboxspace"?    

Get-MailboxDatabase -Status |select name,databasesize,availablenewmailboxspace

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-09*

Hi @超 马  ,    

“Available new mailbox space” is sometimes referred to as “white space”.     

When you move mailboxes to another database, this does not reduce the size of the EDB file for the database, but only generates a 'White Space' to store the new data.    

For 'White Space' in Exchange Database, you can refer to this article: the-puzzling-mathematics-of-white-space-in-exchange-database     

Please Note: Since these web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.    

If you want to reduce Exchange database edb size, you could follow Andy's suggestion.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-08*

You can get the amount of whitespace in a database by running the following cmdlets in Exchange Management Shell:     

```
Get-MailboxDatabase -Status | Format-List Name, DatabaseSize, AvailableNewMailboxSpace –Auto
```

 Before starting defragmentation, ensure that you have enough free space (110% of the size of the database) available on the server (or the network).
