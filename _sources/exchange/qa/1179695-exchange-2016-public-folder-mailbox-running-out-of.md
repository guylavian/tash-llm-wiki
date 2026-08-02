---
title: "Exchange 2016 Public Folder mailbox running out of space...how do I clear up space?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179695/exchange-2016-public-folder-mailbox-running-out-of
question_id: 1179695
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Public Folder mailbox running out of space...how do I clear up space?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179695/exchange-2016-public-folder-mailbox-running-out-of (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all. I have an Exchange 2016 server being used by a customer that over-utilizes their public folders. There are 6 public folder mailboxes on this server that are all set to maximum size...100 GB. The first mailbox is very close to being out of space. I ran a powershell command to move one of the larger public folders in this mailbox to a different mailbox that has plenty of free space. The command worked, and I can see that the folder did indeed migrate to the alternate mailbox. My problem is that I did not gain any space on the original mailbox. I'm guessing this is some sort of white space issue, but I have no idea how to resolve it. Any ideas out there? TIA!

## Answer (community) — community member

*upvotes: 1 · updated: 2023-02-15*

I'm writing this follow-up for any Googlers out there that run into my same situation. Using the Move-PublicFolderBranch.ps1 script did work for me. In my case, it was the first mailbox (Primary Hierarchy) that was almost full. I found a PowerShell script that created a .csv file which listed my public folders by size. I then used the Move-PublicFolderBranch.ps1 script to move the bigger public folders into a new mailbox I created. When you run the Move script, you can check on the progress of the move by running Get-PublicFolderMoveRequest | format-list. When the status shows as "completed", you then have to run remove-publicfoldermoverequest to remove your request. If you don't do that, you won't be able to run your next "move" command. You will be asked for the identity of your remove request, which is the RequestGuid shown in the Get-PublicFolderMoveRequest. Basically you can only move one branch at a time, so it is not a very efficient process.

One thing to note is that you will NOT see the free space in your full mailbox grow at all. It becomes white space instead. My understanding is that the white space will be utilized over time. In my case, the first mailbox is 95 percent full. I moved 32 GB into a new mailbox, but I still see 95 percent usage on the first mailbox. I expect that number to stay at 95 percent for quite a long time, as the white space of 32 GB gets consumed.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-11*

OK this looks more like what I want. Let me dig into those links and see if that works. Thanks so much for the links. I'll report back with my progress.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-11*

Hi Andy...thanks for the response. Unfortunately that won't solve my problem. My problem here isn't with the database, it's with one of the public folder mailboxes being full at 100 GB. The public folder database is a separate database I created specifically to store public folders. It is not running out of space. My problem is that one of public folder mailboxes inside that database is at its size limit...100 GB. If I move all the public folders in that mailbox to a new mailbox, I'll have the same problem (100 GB size limit). I guess I could create two new mailboxes and then move half the public folders to one mailbox, and half to the other. I have no idea how I would do that in an orderly fashion though?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-10*

The recommended way would be to move all the public and user mailboxes from that database to new databases, then remove the source database once done.

The only way to reclaim disk space is to do an offline defrag of the database and that is never recommended as it means downtime to take the database offline.

https://practical365.com/defrag-exchange-server-mailbox-databases/
