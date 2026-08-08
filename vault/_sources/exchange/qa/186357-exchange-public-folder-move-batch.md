---
title: "exchange public folder move batch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186357/exchange-public-folder-move-batch
question_id: 186357
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange public folder move batch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186357/exchange-public-folder-move-batch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear

I have exchange 2016 and one public folder mailbox with 420GB.

I would like to decrease it's size(split)

search in google, I found build-in have split script. But I don't want to use it as not understandable action and very large action cause high risk.

I am seeking a way use new-publicfoldermoverequest and with understandable short script to complete this in batch.

Move it in the way: create new publicfolermailbox, then move some folder to it.

does below syntax can complete by request? But I can not understand it.  

Thank you.

https://learn.microsoft.com/en-us/powershell/module/exchange/new-publicfoldermoverequest?view=exchange-ps  

$folders = Get-PublicFolder \ -Recurse -Mailbox PUB1 -ResidentFolders | ?{$_.Name -ne "IPM_SUBTREE"} | %{$_.Identity};New-PublicFolderMoveRequest -TargetMailbox PUB2 -Folders $folders

do you know any way can complete my request.

Thanks for your valuable time.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-15*

Hello   

seems some content lost. I don't know why. I just fix some typo in past reply.  

repeat my reply again in short.  

what I mean is Update-StoreMailboxState, but I found this should not the thing I want.  

and I check at ECP, public folder primary mailbox not decrease, but second mailbox had extend.  

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-15*

I found a update database command, I will try after current migrate compelte, to see does mailbox will decrease after update database.  

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-15*

Dear Eric  

I mean "Mailbox1" never decrease.  

I try to check database size to know it's copy or move, but my exchange return "object" not found " error when get-mailboxdatabase.   

It seems have DAG but not have database. I am not so clear in Exchange mechanism. Not sure it's a problem relate to my case or it's an error can be ignore.  

Thank you.  

DisplayName                         TotalItemSize  

Mailbox1                                   465.1 GB (499,344,898,561 bytes)  

PublicFolderMailbox-2011       51.17 GB (54,941,201,343 bytes)  

PublicFolderMailbox-2010      32.63 GB (35,035,562,712 bytes)  

PublicFolderMailbox-2009      1.464 GB (1,572,339,910 bytes)  

PublicFolderMailbox-2007      283.8 MB (297,554,738 bytes)  

PublicFolderMailbox-2008      90.67 MB (95,071,501 bytes)  

PublicFolderMailbox-2021      15.45 KB (15,817 bytes)  

PublicFolderMailbox-2            15.42 KB (15,787 bytes)  

PublicFolderMailbox-2012      9.634 KB (9,865 bytes)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Use the "WhatIf" parameter to validate without actual execution https://learn.microsoft.com/en-us/powershell/exchange/exchange-cmdlet-syntax?view=exchange-ps    

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
