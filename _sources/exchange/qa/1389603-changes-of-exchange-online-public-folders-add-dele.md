---
title: "Changes of Exchange Online Public Folders (Add/Delete/Move) is only executed overnight after successful migration from OnPrem."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1389603/changes-of-exchange-online-public-folders-add-dele
question_id: 1389603
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Changes of Exchange Online Public Folders (Add/Delete/Move) is only executed overnight after successful migration from OnPrem.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1389603/changes-of-exchange-online-public-folders-add-dele (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everybody,  

after a successfull migration of OnPremise Exchange 2016 PublicFolders to ExchangeOnline I´ve a strange effect.  

When a user with "owner" privileges tries to add a new PublicFolder (in EXO) he get´s an error message in his Outlook 365:  

"Ein Clientvorgang ist Fehlgeschlagen" (Sorry, I don´t know the english error message)  

Nevertheless, the next day this Folder is visible for the user. (Same effect, when moving an existing folder to a different folder).

The Exchange-Admin can see this folder at that moment when it is created (Standard behaviour) and he can also do all the standard tasks (Add/Delete/Move) just in time.  

All User Mailboxes had been migrated successfully to EXO before the Migration of the OnPrem-PublicFolders. The PF-Migration had been completely finalized as described in:

https://learn.microsoft.com/en-us/exchange/collaboration/public-folders/migrate-to-exchange-online?view=exchserver-2019

Anybody an idea?

Thank´s in advance!  

Cheers  

Rudi

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-13*

Hi @Rudel, Rüdiger,

Welcome to our Q&A forum!

It seems that the user with “owner” privileges is receiving an error message in Outlook 365 when trying to add a new PublicFolder (in EXO): “A client operation failed”. However, the next day this folder is visible for the user. The same effect occurs when moving an existing folder to a different folder. This issue usually occurs when the replication of the public folder hierarchy is incomplete or faulty.

To resolve this issue, you can manually replicate the permissions on the user’s public folder mailbox by running the following command:

```
Update-PublicFolderMailbox pubmbx1 -InvokeSynchronizer
```

Then, verify the permissions again by running the following command:

```
Get-PublicFolderClientPermission \\puf1 -User User1 -Mailbox pubmbx1
```

Please note that it may take a few minutes for the permission change to be displayed. For more information on troubleshooting public folder issues, please refer to this Microsoft article: https://learn.microsoft.com/en-us/exchange/troubleshoot/public-folders/public-folder-permission-issues

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-13*

This issue typically occurs because the public folder hierarchy replication isn't completed or has problems.

Check this MS article - https://learn.microsoft.com/en-us/exchange/troubleshoot/public-folders/public-folder-permission-issues
