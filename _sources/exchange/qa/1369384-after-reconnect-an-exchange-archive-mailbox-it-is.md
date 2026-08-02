---
title: "After Reconnect an Exchange Archive Mailbox it is empty"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1369384/after-reconnect-an-exchange-archive-mailbox-it-is
question_id: 1369384
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# After Reconnect an Exchange Archive Mailbox it is empty

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1369384/after-reconnect-an-exchange-archive-mailbox-it-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I have a user with archive mailbox enabled (Exchange 2016)  

For some reasons i've disable mailbox for this user, Archive mailbox for this user was disabled too.  

I've recreate mailbox for this uesr. Now I need to reconnect old archive mailbox to this user.  

But I've encountered a problem: after I've reconnect old archive mailbox it turned out to be empty.  

For testing purposes I've disabled archive for this user again and then connected it to another test user. In this case connected old archive is not empty, it is contains some data as it should be.

I've reconnected this old archive back to original user and it is empty again!  

To recoonect arhive to user I've using this command:

```
Enable-Mailbox -ArchiveGuid  -ArchiveDatabase  -Identity 
```

What I am doing wrong? Why archive mailbox is it empty, although it actually has data?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-20*

Hi @ Евгений Котляревский,

In my case, the reason turned out to be that I was connecting the wrong mailbox. In my organization I had two disconnected archive mailboxes with the same GUID, but placed in different mailbox databases.

Great to know that you've already thought of a solution and really appreciate it for your sharing!

By the way, since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others.". and according to the scenario introduced here: Answering your own questions on Microsoft Q&A, I would make a brief summary of this thread:

[After Reconnect an Exchange Archive Mailbox it is empty]

 

Issue Symptom:

I have a user with archive mailbox enabled (Exchange 2016)  

For some reasons i've disable mailbox for this user, Archive mailbox for this user was disabled too.  

I've recreate mailbox for this uesr. Now I need to reconnect old archive mailbox to this user.  

But I've encountered a problem: after I've reconnect old archive mailbox it turned out to be empty.  

For testing purposes I've disabled archive for this user again and then connected it to another test user. In this case connected old archive is not empty, it is contains some data as it should be.

I've reconnected this old archive back to original user and it is empty again!

 

The Solution:

Run the following command to get the properties of the archive mailbox for the test mailbox and user mailbox connection:

```
Get-mailbox -Identity user1 |fl *ArchiveDatabase,*ArchiveGuid
```

Compare whether the parameters of the valid mailbox and the problem mailbox are consistent.

 

You could click the "Accept Answer" button for this summary to close this thread, and this can make it easier for other community member's to see the useful information when reading this thread. Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

Thanks to All for answers. But they all no my case.  

In my case, the reason turned out to be that I was connecting the wrong mailbox. In my organization I had two disconnected archive mailboxes with the same GUID, but placed in different mailbox databases.  

So I've connected "right" mailbox and  and everything worked.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

Your archive mailbox may be empty for a number of reasons.

The archive mailbox was purged. When an archive mailbox is disabled, it is kept in the mailbox database for a predetermined period of time. Exchange keeps disconnected archive mailboxes for a 30-day period by default. The original archive mailbox's contents are permanently erased (purged from the mailbox database) after 30 days and cannot be restored.

The archive mailbox is corrupted. You might not be able to access the contents of the archive mailbox if it is corrupted.

Verify that the archive mailbox was not purged

`Get-Mailbox -Identity <user mailbox identity> | Select-Object ArchiveStatus`

Also, check this article - https://learn.microsoft.com/en-us/exchange/policy-and-compliance/in-place-archiving/manage-archives?view=exchserver-2019..
