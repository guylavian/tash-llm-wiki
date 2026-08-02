---
title: "Can't find databse error in Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1001232/cant-find-databse-error-in-exchange-2016
question_id: 1001232
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Can't find databse error in Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1001232/cant-find-databse-error-in-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to find mailbox information in comlet, but keep getting can't find data base error    

```
[PS] C:\Windows\system32>Get-MailboxDatabase  
  
Name                           Server          Recovery        ReplicationType  
----                           ------          --------        ---------------  
Mailbox Database 0181915290    SIVERMAIL       False           None  
  
  
[PS] C:\Windows\system32>Get-Mailbox -Database 0181915290 -Archive  
Couldn't find database "0181915290". Make sure you have typed it correctly.  
    + CategoryInfo          : NotSpecified: (:) [Get-Mailbox], ManagementObjectNotFoundException  
    + FullyQualifiedErrorId : [Server=SIVERMAIL,RequestId=d8e96c8b-bd5f-4522-88e3-b1c13c069c41,TimeStamp=9/9/2022 3:17  
   :40 PM] [FailureCategory=Cmdlet-ManagementObjectNotFoundException] E3DE7D95,Microsoft.Exchange.Management.Recipien  
  tTasks.GetMailbox  
    + PSComputerName        : sivermail.siverlaw.local
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-09*

Thanks much
