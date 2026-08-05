---
title: "Exchange 2019 / Edge server with working EdgeSynchronization - Relay problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329607/exchange-2019-edge-server-with-working-edgesynchro
question_id: 329607
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 / Edge server with working EdgeSynchronization - Relay problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329607/exchange-2019-edge-server-with-working-edgesynchro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an on-premises Exchange 2019 server with a subscribed Edge Transport server.     

This is working fine.     

I now need to allow an external Exchange server to use us as a relay to send external mails. This server is not part of our Exchange organization or AD domain, but we trust it sufficiently to implement this requirement.     

I have added a new FrontEndTransport Receive Connector on our Exchange server, configured it for Anonymous access and set the Scoping to only accept email from the IP address of the remote Exchange server. I have also deselected all authentication mechanisms for the connector - i'm not sure if that's correct.     

Unfortunately when I send mails from the external server I keep getting NDRs along the lines of: [FQDN on Edge server] #550 5.7.54 SMTP; Unable to relay recipient in non-accepted domain ##     

I have made sure that the Edge Subscription is synchronized but the problem persists.     

Some picture of my configuration: ![81195-image.png][1] ![81138-image.png][2] ![81187-image.png][3]     

Any hints would be nice?     

Best Regards John B     

[1]: /api/attachments/81195-image.png?platform=QnA [2]: /api/attachments/81138-image.png?platform=QnA [3]: /api/attachments/81187-image.png?platform=QnA

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-25*

Hi Eric  

thanks for your response.  

I have enabled protocol logging on receive connector "Default Frontend Transport" and on "Mail Relay".  

In the log I can see it is only receive connector "Default Frontend Transport" there are used.   

My receive connector "Mail Relay" is not used.  

I have tried to disable "Default Frontend Transport" but then I am unable to receive mail.  

I have tried to change the "Default Frontend Transport" so the wan Ip address there are on the "Mail Relay" not are included, but I still receive mail via "Default Frontend Transport".  

A hint would be nice  

Best Regards   

John B

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi,    

Enable protocol logging for the customized receive connector and check the log, make sure you are accessing your Exchange server via correct connector:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
