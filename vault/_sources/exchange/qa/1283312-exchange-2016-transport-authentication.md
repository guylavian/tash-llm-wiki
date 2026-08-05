---
title: "Exchange 2016 Transport Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1283312/exchange-2016-transport-authentication
question_id: 1283312
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 Transport Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1283312/exchange-2016-transport-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Environment consists of Exchange 2016 CU23 and KB5024296 Security Update

We are noticing below events in the application logs which is causing alerts to trigger

```
Log Name:      Application
Source:        MSExchangeFrontEndTransport
Date:          12/05/2023 16:02:02
Event ID:      1035
Task Category: SmtpReceive
Level:         Warning
Keywords:      Classic
User:          N/A
Computer:     ExchangeServer.domain.com
Description:
Inbound authentication failed with error LogonDenied for Receive connector Client Frontend ExchangeServer.domain.com. The authentication mechanism is Login. The source IP address of the client who tried to authenticate to Microsoft Exchange is [ip address].
Event Xml:

  
    
    1035
    3
    1
    0x80000000000000
    
    28859197
    Application
    ExchangeServer.domain.com
    
  
  
    LogonDenied
    Client Frontend ExchangeServer.domain.com
    Login
    ip address
  
```

No emails are observed in queue and when we check the health of ip address it is blacklisted. 

Any recommendations on how to avoid this events 

We checked and all permission on the connector are appropriate.

Regards,

Ajit

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-15*

Go to the Security section, and make sure that the only boxes checked off are:

-  Transport Layer Security (TLS)

-  Externally secured (for example, with IPsec)

-  Exchange servers

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-15*

Hi Ajit Terdalkar,

It may be someone who is trying to authenticate to attack or use your server as a relay.  

The authentication failure event was most likely triggered by an attempt by this blacklisted IP address to connect to the Exchange server. To avoid these incidents, you may want to consider blocking the IP addresses in the blacklist with the firewall. This will block any further connection attempts from that IP address.

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
