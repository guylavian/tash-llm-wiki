---
title: "Resubscribe Exchange edge subscription"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/407253/resubscribe-exchange-edge-subscription
question_id: 407253
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Resubscribe Exchange edge subscription

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/407253/resubscribe-exchange-edge-subscription (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

current environment:    

DMZ- 1 Edge 2010 Exchange    

Domain- 2 Exchange servers.Exchange 2010(cas,hub,mailbox) and Exchange 2016(mailbox)    

It seems that Exchange 2010 hub has edge subscription imported initially.    

There is something wrong with edge subscription and 2016 start queueing mail toward edge server and I need    

To resubscribe edge subscription.    

I plan to do resubscribing this way:(Is this a correct way to resubscribe edge subscription?)    

On edge server    

New-EdgeSubscription -FileName "C:\Data\EdgeSubscriptionInfo.xml"    

On hub server import    

    

https://learn.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscription-procedures?view=exchserver-2019     

 Important    

To resubscribe an Edge Transport server, export a new Edge Subscription file on the Edge Transport server and then import the XML file on a Mailbox server. You will need to resubscribe the Edge Transport server to the same Active Directory site where it was originally subscribed. You don't need to first remove the original Edge Subscription; the resubscription process will overwrite the existing Edge Subscription.

## Answers

_No answers on this thread._
