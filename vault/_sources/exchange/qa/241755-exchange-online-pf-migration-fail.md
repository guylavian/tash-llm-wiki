---
title: "Exchange Online - PF Migration fail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/241755/exchange-online-pf-migration-fail
question_id: 241755
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange Online - PF Migration fail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/241755/exchange-online-pf-migration-fail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm currently in the middle of a EX2010 to 365 migration.  I have followed the article to batch migrate legacy EX2010 folders to 365 and as part of the sync and complete stage I had several malboxes that would go from synced to failed.  Due to this i decided to cancel migrating via batch files and revert to the PST method.    

I'm in a position now where i'm unable to run "Set-OrganizationConfig -PublicFoldersEnabled Local" as it states the following  

PublicFoldersEnabled state must remain set to "Remote" while Public Folder mailboxes are on hold for migration. Before  

you can change your Public Folder deployment to "Local", you must first complete Public Folder migration. If you do  

not want to migrate your Public Folders, you can remove the existing Public Folder mailboxes and recreate them without  

-HoldForMigration switch. For additional information please see  

If i run get-mailbox -publicfolder i can see there is a public folder, and if i run remove-mailbox -publicfolder -Identity Mailbox1 I'm told   

The mailbox "Mailbox1" is the primary public folder mailbox for the users. To remove this mailbox, first remove all  

other public folder mailboxes.  

Kind of feels like i'm going around in circles - any advice is greatly appreciated.  

Thanks,  

Alex

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

Hi @Alex Derbyshire      

What's your Exchange 2010 UR version?    

First check if there is any existing batch migration requests, if yes, remove them    

```
$batch = Get-MigrationBatch | ?{$_.MigrationType.ToString() -eq "PublicFolder"}  
$batch | Remove-MigrationBatch -Confirm:$false
```

Then try using below commands to remove the public folder mailbox in your environment    

```
Get-Mailbox -PublicFolder | Where{$_.IsRootPublicFolderMailbox -eq $false} | Remove-Mailbox -PublicFolder -Force -Confirm:$false
```

Or    

```
Get-Mailbox -PublicFolder | Remove-Mailbox -PublicFolder -Force -Confirm:$false
```

Then run the command avove again Set-OrganizationConfig -PublicFoldersEnabled Local    

We could also refer to this link to get more information: How to Create a Public Folder in Hybrid Office 365?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
