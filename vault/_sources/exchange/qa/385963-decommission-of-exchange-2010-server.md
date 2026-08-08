---
title: "Decommission of Exchange 2010 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385963/decommission-of-exchange-2010-server
question_id: 385963
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Decommission of Exchange 2010 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385963/decommission-of-exchange-2010-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're currently using Exchange Online but were informed we should not decommission our last Exchange server if we run Azure AD connect in our network. I spun up a new VM and installed Exchange 2016 on it and migrated all the mailboxes from the 2010 server. I'm at the point where I want to get rid of the 2010 server but when I try to uninstall via Control Panel, I get the following messages:  

Uninstall cannot continue. Database 'Mailbox Database': This mailbox database contains one or more mailboxes, mailbox plans, archive mailboxes, or arbitration mailboxes. To get a list of all mailboxes in this database, run the command Get-Mailbox -Database <Database ID>. To get a list of all mailbox plans in this database, run the command Get-MailboxPlan. To get a list of archive mailboxes in this database, run the command Get-Mailbox -Database <Database ID> -Archive. To get a list of all arbitration mailboxes in this database, run the command Get-Mailbox -Database <Database ID> -Arbitration. To disable a non-arbitration mailbox so that you can delete the mailbox database, run the command Disable-Mailbox <Mailbox ID>. To disable an archive mailbox so you can delete the mailbox database, run the command Disable-Mailbox <Mailbox ID> -Archive. Arbitration mailboxes should be moved to another server; to do this, run the command New-MoveRequest <parameters>. If this is the last server in the organization, run the command Disable-Mailbox <Mailbox ID> -Arbitration -DisableLastArbitrationMailboxAllowed to disable the arbitration mailbox. Mailbox plans should be moved to another server; to do this, run the command Set-MailboxPlan <MailboxPlan ID> -Database <Database ID>.  

Uninstall cannot continue. Database 'Public Folder Database': The public folder database "Public Folder Database" contains folder replicas. Before deleting the public folder database, remove the folders or move the replicas to another public folder database. For detailed instructions about how to remove a public folder database, see http://go.microsoft.com/fwlink/?linkid=81409&clcid=0x409.  

On the Exchange 2010 server when I run Get-Mailbox -Database "Mailbox Database" I get nothing in return  

On the Exchange 2010 server when I run Get-Mailbox -Database "Mailbox Database" - Arbitration I get nothing in return  

On the Exchange 2010 server when I run Get-Mailbox -Database "Mailbox Database" - Archive I get nothing in return  

What else am I missing?  

As far as the public folders, I really don't need to move them to another server since we're not using them. Is there another way to delete the Public Folder database?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-07*

@Gary Leung      

Try to run command below to check again:      

```
Get-MailboxDatabase -Server exch2010 | Get-Mailbox  
Get-MailboxDatabase -Server exch2010 | Get-Mailbox -Archive  
Get-MailboxDatabase -Server exch2010 | Get-Mailbox -Arbitration
```

About Public Database, you need to delete public folder first, then delete public folder database:    

Delete all public folder under "Default Public folders". You need to delete it from parent patch, such as if you want to delete pf01, you need to click on Default Public folders:    

    

Then you can delete the public folder database:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
