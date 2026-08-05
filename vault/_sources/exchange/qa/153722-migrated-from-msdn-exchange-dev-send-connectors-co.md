---
title: "[Migrated from MSDN Exchange Dev] SEND CONNECTORS - costs and priority"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153722/migrated-from-msdn-exchange-dev-send-connectors-co
question_id: 153722
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] SEND CONNECTORS - costs and priority

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153722/migrated-from-msdn-exchange-dev-send-connectors-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a scenario when need to configure relation between send connectors. Exchange is sending mail to many different mail servers. Priority is to use MX record in DNS for each mail server. For this we have a send connector with root domain (*.domain).

In case when distant mail servers are not reachable in IP network (MX IP address resolved by DNS but host is offline) sending must be relayed thru designated smart hosts. We created additional send connector for specific subdomain group with multiple IP smart host addresses. (*.a.domain – IP(a1), IP(a2) and so on to *.z.domain – IP(z1), IP(z2) )

What does cost mean inside send connector? Is there any relation between send connectors with the same domain but different costs to reach that domain (MX vs SMART HOSTS)? How multiple smart hosts work in send connector?

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/90cf7791-f3dc-4f0f-9e2e-b4964b1cfb66/send-connectors-costs-and-priority?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-06*

The Cost value on the address space is used for mail flow optimization and fault tolerance when you have the same address spaces configured on multiple Send connectors on different source servers. A lower priority value indicates a preferred Send connector.    

Here are detail information about the send connector selection for Exchange server: Selecting the connector for an external recipient    

Cost is used in this step below:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
