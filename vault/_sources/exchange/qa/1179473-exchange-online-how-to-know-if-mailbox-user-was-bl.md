---
title: "exchange online how to know if mailbox user was blocked"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179473/exchange-online-how-to-know-if-mailbox-user-was-bl
question_id: 1179473
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# exchange online how to know if mailbox user was blocked

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179473/exchange-online-how-to-know-if-mailbox-user-was-bl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I suspect that 1 of my users has exceeded the limit - sent over 10000 messages a day and is blocked , how can I know for sure ? where can I find it ?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-02-10*

I have used Message trace to search all message from my suspect user in 7 days , many messages have status "Failed" but  trace results is not clear , as you can see below

The subject is blank , so I think , my user password is revealed (she has changed it) and her mailbox was used to send many spam messages (exceed 10000 message a day), but I want to know for sure and remaining time of blocking.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-10*

You can check the message trace logs in the Exchange Admin Center to see if that user has exceeded the message send limit by following the steps below:

-  Log in to the Exchange Admin Center (EAC) by going to https://outlook.com/admin and signing in with your admin credentials.

-  In the EAC, go to the Mail flow > Message trace.

-  You can select the date range for the trace logs you want to view on the message trace page and then click the search button.

-  The message trace results will be displayed, and you can check for any blocked messages due to exceeding the message send limit.

-  To filter the results, you can use the filter options on the right side of the screen, such as the result type, sender or recipient address, and message subject.

The documentation I suggest that may help with your question also is as follows:

-  Message trace in Exchange Online - https://docs.microsoft.com/en-us/exchange/mail-flow-tools/message-trace/message-trace-in-exchange-online?view=exchserver-2019

-  Understanding message trace in Exchange Online Protection - https://docs.microsoft.com/en-us/exchange/security-and-compliance/message-trace/understand-message-trace-in-exchange-online-protection?view=exchserver-2019

-  Connection filtering in Exchange Online Protection - https://docs.microsoft.com/en-us/exchange/security-and-compliance/connection-filtering/connection-filtering-in-exchange-online-protection?view=exchserver-2019

Give it a go, and it will be great to hear your feedback.
