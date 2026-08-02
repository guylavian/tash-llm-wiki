---
title: "EWS manage API subscribes to a specific mailbox and returns errorexeedconnectioncount"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316472/ews-manage-api-subscribes-to-a-specific-mailbox-an
question_id: 316472
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# EWS manage API subscribes to a specific mailbox and returns errorexeedconnectioncount

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316472/ews-manage-api-subscribes-to-a-specific-mailbox-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Environmental information: 2016 cu14    

At present, there is a specific mailbox user, and the mailbox can be used normally. However, when you try to stream notifications to the calendar folder of the user, the,    

EWS returns error information:    

Error code: errorexeedconnectioncount    

Policy：MaxStreamingConcurrency    

MaxConcurrencyLimit：10    

ErrorMessage: this operation will exceed the budget limit of policy part "maxstreamingconcurrency", budget value "10", budget type: "EWS". The recommended fallback time is 0 Ms. You have exceeded the number of concurrent connections available to your account. Please try again after other requests have completed.    

After trying to migrate the user's mailbox database, subscribe again, and still return such as report error.    

The service account used to subscribe to this mailbox has opened applicationimpersonation, and simulates this user before subscribing.    

Whether the mailbox is set to x-anchormalbox or not, this error will be returned.    

In this case, there are the following questions:    

-  According to the related documents, errorexeedconnectioncount is related to the limitation of hangingconnectionlimit.    

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/handling-notification-related-errors-in-ews-in-exchange    

-  If it is related to hangingconnectionlimit, is there any way to:        a. Query the usage of hangingconnectionlimit of the user      b. Configure the hangingconnectionlimit limit for this user separately      c. Clear the hangingconnectionlimit of the user  

-  If it is irrelevant, how can we locate the problem.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

a. No there are no API's to get the current connection count or the number of streaming subscriptions that a user has open.    

b. Yes create another policy for that user and include them in it https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/ews-throttling-in-exchange .  The default for MaxConcurrencyLimit was increased to 27 in Exchange 2013 but it sounds like your policies are still set to their 2010 values.    

c. No
