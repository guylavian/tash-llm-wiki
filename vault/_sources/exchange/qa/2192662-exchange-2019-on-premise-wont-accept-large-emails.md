---
title: "Exchange 2019 On-Premise won't accept large emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192662/exchange-2019-on-premise-wont-accept-large-emails
question_id: 2192662
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange 2019 On-Premise won't accept large emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192662/exchange-2019-on-premise-wont-accept-large-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Windows Server 2022 with Exchange 2019. It is NOT a domain controller, but it is joined to our domain. I have increased the message size limits to astronomical sizes. All of the following have been set high (2Gb or higher, for testing):

-  Transport configuration. (Set-TransportConfig)

-  Receive Connectors (Set-ReceiveConnector)

-  Send Connectors (Set-SendConnector)

-  Mailbox (MaxSendSize, MaxReceiveSize)

These were based on: https://www.alitajran.com/attachment-size-limit-exchange-server/

When I check it, they are properly set.

Mailboxes are not anywhere near the storage quotas. I've verified the disk where the mailboxes is stored is at about 2% usage, so plenty of space.

This occurs with all users. Small sized emails get through with no issue.

I have rebooted.

When I email a test message inbound that is 65MB, it is rejected by Exchange. All over the internet it says to run Set-Clutter -Enabled $false; however, this is on-premise. Clutter feature doesn't exist for on premise servers. What OTHER reason does this delivery report error mean?

```
Delivery Report for  User ‎(******@mydomain.com)‎
Pending
10/24/2023 6:42 PM exchange.sub.mydomain.com
Message was received by exchange.sub.mydomain.com from EXCHANGE.sub.mydomain.com.
Failed
10/24/2023 6:42 PM exchange.sub.mydomain.com
There's a problem with the recipients mailbox. Please try to resend your message later.
[{LED=554 5.2.0 STOREDRV.Deliver.Exception:MessageSubmissionExceededException.MapiExceptionMaxSubmissionExceeded; Failed to process message due to a permanent exception with message Cannot save changes made to an item to store. 16.55847:A9310000, 17.43559:0000000052010000000000000100000000000000, 20.52176:020F5E840700103100000000, 20.50032:020F5E847717000000000000, 0.35180:020F5E84, 255.23226:00000000, 255.27962:A3000000, 255.27962:0A000000, 255.27962:25000000, 255.17082:DA040000, 0.27745:00000000, 4.21921:DA040000, 255.27962:FA000000, 255.1494:0F010480, 1.56858:922F0000, 6.45653:050007800201F90FE47F0000, 4.41064:05000780, 4.44956:DA040000, 1.63016:25000000, 4.39640:DA040000, 8.45434:A73F9BD7A853244AB164D4FDE65DF64A302D3438, 5.10786:0000000031352E30322E313131382E3030373A45584348414E47453A37383732626634652D666562302D343835662D396338322D62656235633064616132636200000000, 255.1750:0F010480, 255.31418:0F010480, 0.22753:00000000, 255.21817:DA040000, 0.17361:00000000, 4.19665:DA040000, 0.37632:00000000, 4.37888:DA040000 [Stage: CreateMessage]};{MSG=};{FQDN=EXCHANGE.sub.mydomain.com};{IP=192.168.1.246};{LRT=10/24/2023 11:42:08 PM}]
```

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-25*

Found the solution. Also needed to increase the following...

Set-TransportConfig -InternalDsnMaxMessageAttachSize

Set-TransportConfig -ExternalDsnMaxMessageAttachSize

Set-TransportConfig -MaxDumpsterSizePerDatabase

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-26*

Hello,

Thank you for posting in Microsoft Community forum.  

Based on the description, I understand your question is related to Exchange Server.   

Since there are no engineers dedicated to Exchange Server in this forum. In order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select " Exchange Server " tag.

Thank you for your understanding and support.  If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,

Hania Lian
