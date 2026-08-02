---
title: "Exchange 2013 - Total Loss - Rebuild"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/258938/exchange-2013-total-loss-rebuild
question_id: 258938
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 - Total Loss - Rebuild

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/258938/exchange-2013-total-loss-rebuild (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My site has two exchange 2013 Servers. One of these looks to be a total loss due to a storage area network failure.  

This server does have ntbackup of both the mail datastores (x2) and the server itself.  

Can anyone advise on the best strategy to get a server up and running with the mailboxes operational?  

i.e do I attempt to fully recreate the existing server with the old server name or do I build a completely new exchange server and then try and restore to databases and then presumably somehow tell exchange that the user mailboxes are in a different location?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-05*

Hi @Ian Wilson   ,    

You can try Setup.exe /Mode:RecoverServer if the Exchange data didn’t loss, then restore databases: Restoring Exchange 2013 databases.    

If that didn’t help, then you could consider create a new server and move the database to the new server like Andy provided.    

I’m not sure if you’re using NTbackup or Windows Server Backup for those servers since NTbackup was disabled from Windows Server 2003, but I think you could use them to do the recovery if you have backed up Exchange server and databases correctly.    

Windows Server Backup: Use Windows Server Backup to restore a backup of Exchange.    

Bests,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
