---
title: "Exchange 2010 Public Folder Decommission Process"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/405997/exchange-2010-public-folder-decommission-process
question_id: 405997
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2010 Public Folder Decommission Process

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/405997/exchange-2010-public-folder-decommission-process (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have a Hybrid Configuration with Office 365 with Exchange 2016 Servers.

We have a Public Folder Exchange 2010 Server but We have moved all our Public Folders to Exchange online using third Party tool.

Now we want to decommission that Exchange 2010 Public Folder Server So what is the right process to uninstall Exchange 2010 Public Folder server.

I tried below commands on Exchange 2010 Public Folder Server but received error (May be due to we moved Public folders to Exchange Online)  

Get-PublicFolder "\" -Recurse -ResultSize:Unlimited  

Get-PublicFolder "\Non_Ipm_Subtree" -Recurse -ResultSize:Unlimited

But below command works on Exchange 2010 Public Folder Server & return all public folders.

Get-PublicFolderStatistics -ResultSize Unlimited

So what are the steps to remove public folders, Public Folder Database & then Exchange 2010 Public Folder Server?

Or just I need to delete the Public Folder Database from Exchange 2010 Public Folder Server before uninstall.

I also read if Public Folder database contains public Folders then we can't delete the Database but above first 2 commands gives me an error but the last command shows all the public folders so I don't understand whether the public folders still exists in Public Folder Database though we migrated those to Exchange Online.

Any suggestion highly appreciated.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-02*

Yes the provided information is helpful but I have also followed below article.  

https://medium.com/365uc/decommissioning-on-premises-public-folders-post-exchange-online-migration-daf90b73285
