---
title: "Does Exchange support notifying external systems on changes to calendars?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163664/does-exchange-support-notifying-external-systems-o
question_id: 1163664
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Does Exchange support notifying external systems on changes to calendars?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163664/does-exchange-support-notifying-external-systems-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are going to be integrating our own software system with Exchange using EWS (either Exchange 2016 or Exchange Online), meaning we intend to call out to Exchange for booking resources and people. We will then also store these events locally on our own system. What I am not sure how to do is how to ensure events are synchronized, should someone move events around directly in Exchange.

Does Exchange support notifying external systems on changes? For instance registering a webhook. We would typically need to be notified about the event id and we could then poll for more data if we know the event. Would love to avoid having to poll for changes ... Or maybe the general idea is to center this around the individual calendars themselves, instead of a general channel, by subscribing to the calendars? In the latter case, I am still not sure if I need to poll or if I can be notified on changes.

I am not intimate with the Microsoft sphere, LDAP or Exchange from earlier, but quite adept at software integration in general (WS*/SOAP, RMI, REST, GraphQL).

double posted on ServerFault

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-24*

Exchange Online does give you the ability to use WebHooks via the Graph API [https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions?view=graph-rest-1.0&tabs=http . 

Exchange OnPrem (eg Exchange 2016,2019) you have to use EWS notifications [https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/notification-subscriptions-mailbox-events-and-ews-in-exchange

While you can use EWS against Exchange Online it's not the best idea and may be discontinued in the future.
