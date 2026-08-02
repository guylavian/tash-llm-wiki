---
title: "Exchange Maibox unlimited"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/406071/exchange-maibox-unlimited
question_id: 406071
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Maibox unlimited

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/406071/exchange-maibox-unlimited (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey all,  

Some questions about quota management in Exchange mailboxes....  

We have applied the default quota in 2Gb to our mailboxes.  

However, we have a few users (in about 20% of them) above the quota, about 20% around the quota, and 60 % of the users utilize in about of 1Gb of 2Gbs.  

My question is -   

-  Is there a smart way to manage our quotas in the organization?  

-  Is unlimited mailboxes reccomended?, Is this feature reccomended with cahce mode within outlook clients?  

Thanks   

Tankwell

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-24*

Hi,    

1 It sounds not so smart but just FYI, if UseDatabaseQuotaDefaults value is set to true, the mailbox will use the database quota rather then itself's. So you can move those 20% mailboxes to a new database with 3GB quota, 20% to another database with 2.5GB quota and leave the rest of them with 2GB. Steps for your referrence:    

Use the EAC to create a mailbox database    

Use the EAC to create a local move request    

```
Set-MailboxDatabase db2 -IssueWarningQuota "2.8GB" -ProhibitSendQuota "3GB" -ProhibitSendReceiveQuota "3.5GB"  
Get-mailbox -database db2|Set-mailbox -UseDatabaseQuotaDefaults $true
```

2 Better not, you can set some mailboxes with high limit, 10GB or 20GB.    

Cache mode doesn't affect this, if your Outlook client shows different mailbox usage with in OWA, you should believe what OWA shows and recreate the profile.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
