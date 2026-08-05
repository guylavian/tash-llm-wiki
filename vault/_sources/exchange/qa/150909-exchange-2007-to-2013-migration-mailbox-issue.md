---
title: "Exchange 2007 to 2013 Migration - Mailbox Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150909/exchange-2007-to-2013-migration-mailbox-issue
question_id: 150909
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2007 to 2013 Migration - Mailbox Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150909/exchange-2007-to-2013-migration-mailbox-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all  

We have migrated from Exchange 2007 to Exchange 2013.   

One mailbox has become an issue. Both 2007 and 2013 EACs that the mailbox is on the 2013 server, but when I run the report Get-MailboxStatistics -server <servername> the mailbox shows as still being on the 2007 server.   

On my 2007 server Event Viewer, I have multiple Event 1022. This mailbox seems to somehow be on both servers? On the client side, there are no issues. All mailbox roles are on 2013.   

Logon Failure on database "First Storage Group\Mailbox Database" - Windows account NT AUTHORITY\NETWORK SERVICE; mailbox /o=xxx/ou=First Administrative Group/cn=Recipients/cn=(MailboxName)  

Error: 1144  

Client Machine: ServerName   

Client Process: edgetransport.exe  

Client ProcessId: 0  

Client ApplicationId: Client=Transport  

Grateful for any assistance??

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-05*

@Peter Xenios       

Hi,    

Did the mailbox get migrated recently?    

If so,the result from the command Get-MailboxStatistics -server <servername> may be showing a soft deleted mailbox.    

To confirm it,you can run this command:    

```
Get-MailboxStatistics -server  | fl displayname,disconnectreason
```

If the disconnectreason shows "softdeleted",it may be the cause.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
