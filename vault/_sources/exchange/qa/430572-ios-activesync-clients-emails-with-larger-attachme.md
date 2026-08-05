---
title: "IOS ActiveSync Clients emails with larger attachments being rejected AFTER changing attachment, message size and requestlength limitations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430572/ios-activesync-clients-emails-with-larger-attachme
question_id: 430572
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# IOS ActiveSync Clients emails with larger attachments being rejected AFTER changing attachment, message size and requestlength limitations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430572/ios-activesync-clients-emails-with-larger-attachme (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 2019 Standard with Exchange 2019 Enterprise    

Following this guide (https://learn.microsoft.com/en-us/exchange/architecture/client-access/client-message-size-limits?view=exchserver-2019) I have changed the message size, attachment size and request length restrictions to be far larger than what some of my ios clients are attempting to send.  I still get the notification that the server rejected my message due to message size.  I made sure to perform an iisreset to make the new settings take effect.    

Is there something specific to Exchange 2019 that is not mentioned in that article that I am missing?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

That did present some interesting finds.  Most of what is gone over I have already tried including setting the "uploadreadaheadsize" to a higher value - which could possibly be not high enough(it is currently set to 49152).  I will change this to an even higher value but I won't be able to test until after EOB.  I also was going through the IIS logs and searched for my account when sending a normal email and an email that was rejected:  

Normal:  

2021-06-11 13:58:41 192.168.113.41 POST /Microsoft-Server-ActiveSync/default.eas User=seanryan&DeviceId=N273TC3QE567H90G6LH4LTK89G&DeviceType=iPad&Cmd=Search&CorrelationID=<empty>;&cafeReqId=fffa581c-de62-4a3b-a609-8e99f9882d63; 443 XXXXXXX\seanryan 192.168.124.83 Apple-iPad7C2/1805.212 - 200 0 0 63  

2021-06-11 13:58:41 192.168.113.41 POST /Microsoft-Server-ActiveSync/default.eas User=seanryan&DeviceId=N273TC3QE567H90G6LH4LTK89G&DeviceType=iPad&Cmd=Search&CorrelationID=<empty>;&cafeReqId=fffa581c-de62-4a3b-a609-8e99f9882d63; 443 XXXXXXX\seanryan 192.168.124.83 Apple-iPad7C2/1805.212 - 200 0 0 63  

Rejected  

2021-06-11 13:58:47 192.168.113.41 POST /Microsoft-Server-ActiveSync/default.eas User=seanryan&DeviceId=N273TC3QE567H90G6LH4LTK89G&DeviceType=iPad&Cmd=SendMail&CorrelationID=<empty>;&cafeReqId=7da0922c-354c-4cc4-963f-e3f6ee34c8da; 443 XXXXXXX\seanryan 192.168.124.83 Apple-iPad7C2/1805.212 - 500 0 0 59  

2021-06-11 13:58:47 192.168.113.41 POST /Microsoft-Server-ActiveSync/default.eas User=seanryan&DeviceId=N273TC3QE567H90G6LH4LTK89G&DeviceType=iPad&Cmd=SendMail&CorrelationID=<empty>;&cafeReqId=7da0922c-354c-4cc4-963f-e3f6ee34c8da; 443 XXXXXXX\seanryan 192.168.124.83 Apple-iPad7C2/1805.212 - 500 0 0 59  

The rejected emails are getting a 500 internal server error and I cannot determine why - unless this is directly related to the uploadreadaheadsize values.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-11*

Any help from this?  

https://blog.shiraj.com/2020/04/cannot-send-large-messages-via-activesync-iphone-ipad/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

Hi,    

I'm not sure if you have read this: https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits?view=exchserver-2019    

Run the following command to check your server configuration (some of them are for senders and some are for recipients):    

```
Get-TransportConfig | Format-List MaxReceiveSize,MaxSendSize  
Get-ReceiveConnector | Format-Table Name,Max*Size  
Get-SendConnector | Format-Table Name,MaxMessageSize  
Get-Mailbox  | Format-List MaxReceiveSize,MaxSendSize
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
