---
title: "Exchange 2010 to 2016 migration - Out of office auto responses not sent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/180741/exchange-2010-to-2016-migration-out-of-office-auto
question_id: 180741
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2010 to 2016 migration - Out of office auto responses not sent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/180741/exchange-2010-to-2016-migration-out-of-office-auto (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a hybrid domain configured in Exchange that currently consists of a single Exchange 2010 CAS server and a single Exchange 2016 server.  A migration is in progress with mail flow and user access switched over to go through the Exchange 2016 server.  The issue I am seeing is with our first batch of users migrated from 2010 to 2016 and test mailboxes created on Exchange 2016.      

When a user configures an out of office message, either in OWA or Outlook - the auto response is not sent to anyone.    

-  I can set the OOF message via the OWA, Outlook and Powershell without any error messages.    

-  Once set I can view the config in all locations - OWA, Outlook or Powershell.    

-  On both the 2010 and 2016 servers the internal and external virtual directories are configured as mail.companyname.com    

The message tracking log shows these events with the subject of an auto response.  But the response does not make it to the other users.    

```
PS> Get-MessageTrackingLog -Sender ******@companyname.com -Start "11/25/2020 16:00:00" -End "11/25/2020 16:05:00"  
  
Timestamp              EventId          Source        Sender                                              Recipients                                          MessageSubject  
---------              -------          ------        ------                                              ----------                                          --------------  
11/25/2020 4:00:54 PM  RECEIVE          MAILBOXRULE   ******@companyname.com                                {[removed]@gmail.com}                          Automatic reply: External Test  
11/25/2020 4:00:54 PM  RECEIVE          MAILBOXRULE   ******@companyname.com                                {[removed]@gmail.com}                          Automatic reply: External Test  
11/25/2020 4:01:07 PM  RECEIVE          MAILBOXRULE   ******@companyname.com                                {[removed]@companyname.com}                          Automatic reply: Internal Test  
11/25/2020 4:01:07 PM  RECEIVE          MAILBOXRULE   ******@companyname.com                                {[removed]@companyname.com}                          Automatic reply: Internal Test
```

When checking a test Outlook profile with mfcmapi, the PR_DELEGATED_BY_RULE field updates with email addresses of incoming messages.    

Mailbox used for these tests does not have forwarding enabled:    

    PS> Get-Mailbox -Identity ******@companyname.com | fl DeliverToMailboxAndForward, ForwardingSmtpAddress, ForwardingAddress  

```
DeliverToMailboxAndForward : False  
ForwardingSmtpAddress      :  
ForwardingAddress          :
```

Remote Domains allowed OOF set to External and auto replies are allowed    

    PS> Get-RemoteDomain | ft -AutoSize Name, DomainName, AllowedOOFType, AutoReplyEnabled  

```
Name                                           DomainName                     AllowedOOFType AutoReplyEnabled  
----                                           ----------                     -------------- ----------------  
Default                                        *                              External                   True  
Hybrid Domain - companyname.mail.onmicrosoft.com companyname.mail.onmicrosoft.com InternalLegacy             True  
Hybrid Domain - companyname.onmicrosoft.com      companyname.onmicrosoft.com      External                   True  
Hybrid Domain - companyname.com                  companyname.com                  External                   True
```

testconnectivity.microsoft.com    

Tested using the test mailbox on Exchange 2016 with the automatic reply option disabled.  Used autodiscover, did not manually specify server.    

Synchronization, Notification, Availability, and Automatic Replies - All tests pass    

Outlook connectivity - All tests pass

## Answers

_No answers on this thread._
