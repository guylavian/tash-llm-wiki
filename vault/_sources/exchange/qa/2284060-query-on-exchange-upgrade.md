---
title: "Query on Exchange upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2284060/query-on-exchange-upgrade
question_id: 2284060
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Query on Exchange upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2284060/query-on-exchange-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am currently running Exchange Server 2016 and have upgraded to Exchange Server 2019 in my lab environment as part of the upgrade process.

My existing environment consists of two Exchange 2016 servers (Server01 and Server02). I have provisioned two new Exchange 2019 servers (Server03 and Server04). Inbound mail traffic is routed through a third-party load balancer, and I have already added the two Exchange 2019 servers to it.

Do I need to run the Hybrid Configuration Wizard in this scenario?

I’m now at the stage where I plan to decommission the Exchange 2016 servers. Besides backing up the Receive Connectors and Virtual Directories from the Exchange 2016 servers, is there anything else I should back up or document for future reference in case something is missed?

Also, how do I export the Virtual Directory configuration? For Receive Connectors, I believe the following syntax is correct:

Get-TransportService server01 | Get-ReceiveConnector | fl

Get-TransportService server02 | Get-ReceiveConnector | fl

## Answers

_No answers on this thread._
