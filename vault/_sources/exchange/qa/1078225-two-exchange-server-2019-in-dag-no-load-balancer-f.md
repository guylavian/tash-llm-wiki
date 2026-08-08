---
title: "Two Exchange Server 2019 in DAG - No load balancer - failover still works"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1078225/two-exchange-server-2019-in-dag-no-load-balancer-f
question_id: 1078225
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Two Exchange Server 2019 in DAG - No load balancer - failover still works

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1078225/two-exchange-server-2019-in-dag-no-load-balancer-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've set up two Exchange 2019 servers on two Server 2022 HyperV VMs in a DAG with a witness server.    

I've got MDB01 one EX01 with copy on EX02 and MDB02 on EX02 with copy on EX01.    

I've a single AD DNS entry of mailgate.xxx.com pointing at the IP from my DAG computer account, not the IP of either EX01 or EX02. The DNS is setup with Split Brain and the firewall has a single address for port forwarding SMTP, HTTP and HTTPS pointing at mailgate.xxx.com, the DAG IP address.    

No Round Robin at all.    

If I disable the NIC on EX01, somehow EX02 knows to take over MDB01 from EX01. Users are not aware of any disconnection in Outlook 2013 (online mode, not offline cached) and incoming/outgoing SMTP email carries on working.    

When I enable the NIC I can then activate the databases where they normally live and they get silently moved back    

Same for Maintenance mode, all just works.    

Please can anyone tell me why I would need a Load Balancer if the failover and maintenance modes seem to work ?    

We have 60 user mailboxes spread across the two databases.    

Thanks

## Answers

_No answers on this thread._
