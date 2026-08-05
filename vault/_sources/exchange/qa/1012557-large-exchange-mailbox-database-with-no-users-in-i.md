---
title: "large exchange mailbox database with no users in it"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1012557/large-exchange-mailbox-database-with-no-users-in-i
question_id: 1012557
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# large exchange mailbox database with no users in it

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1012557/large-exchange-mailbox-database-with-no-users-in-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We had several mailboxes in an exchange 2013 mailbox database. The size of the EDB file was over 100GB. All user mailboxes have been migrated to another mailbox database located on another exchange server. Once migration completed we dismounted an empty mailbox database and ran Eseutil /d against it. For some reason we only got 60GB back as the new database is using 48GB.    

Both Keep deleted items for (days) and Keep deleted mailboxes for (days): are set to 0    

Exchange backup has been taken after moving all user mailboxes to another database.    

Get-MailboxDatabase -Status -Identity old | select Name,DatabaseSize,AvailableNewMailboxSpace    

Name                                                     DatabaseSize                                             AvailableNewMailboxSpace                                   

----                                                     ------------                                             ------------------------                                   

Old                                                      45.76 GB (49,132,077,056 bytes)                          7.938 MB (8,323,072 bytes)                                 

=========================================================================    

Get-MailboxDatabase "old" | Get-mailbox - returns no results    

=========================================================================    

 Get-MailboxDatabase "old" | Get-mailbox -Monitoring | select name    

Name                                                                                                                                                                         

----                                                                                                                                                                         

HealthMailboxe3fe9a9233a54f6a94ab77a1cd10cd01                                                                                                                                

HealthMailbox39fb77268a8e4179a7e65be9a77c7b02                                                                                                                                

HealthMailboxc1b2c9a2bd79471c98ea1f40f39761a6    

What could be using 48GB os space in an empty mailbox database?    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-18*

We ran defrag to understand how much space is really being used by HealthMailboxes. Seeing 50GB taken by Healthmailbox seemed excessive.    

HealthMailbox-exch1-Old was only using 2.6 GB, but In-Place Archive for it was using the remaining 45 GB    

We ran Get-Mailbox -Monitoring  -Database Old | Remove-Mailbox and removed 3 Health Mailboxes from the Old mailbox database. After running another defrag, EDB file size went down to 64MB.     

Based on the discovery we are assuming that In-Place Archive for HealthMailboxes is out of control in other mailbox databases. Is there a way to check? What would be a right way to maintain the size of the HealthMailboxes & In-Place Archive HealthMailboxes at a minimum?    

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-18*

"AvailableNewMailboxSpace" is not accurate and should not be used really:    

https://blog.rmilne.ca/2013/08/20/how-to-check-database-white-space-in-exchange/    

Having said all that, why did you defrag? Just remove and delete the database on disk if it no longer used:)
