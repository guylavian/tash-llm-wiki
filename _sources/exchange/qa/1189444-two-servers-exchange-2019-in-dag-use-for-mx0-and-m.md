---
title: "Two servers Exchange 2019 in DAG use for MX0 and MX1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189444/two-servers-exchange-2019-in-dag-use-for-mx0-and-m
question_id: 1189444
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Two servers Exchange 2019 in DAG use for MX0 and MX1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189444/two-servers-exchange-2019-in-dag-use-for-mx0-and-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

May i ask qustion about https://learn.microsoft.com/en-us/exchange/high-availability/deploy-ha?view=exchserver-2019

I have more simple configuration

2 server in DAG with CAS MBX roles

2 different hyper v clusters

2 ISP (2 public ip)

I use split DNS and Round Robbin  for internal clients for example 

mail.corp.com (ip1 ip2 internal like 10.10.10.x)

Can i use Round Robbin for external IP?

mail.corp.com

Public IP1

Public IP2

Where IP1 = MX0 in MX DNS records weight 10

Where IP2 = MX1 in MX DNS records weight 20

Example of an MX record:

@MX 10 mailhost1.example.com

@MX 20 mailhost2.example.com
If server1 or server2 at maintance mode or any another problems i remove one of this ip from round robbin

## Answers

_No answers on this thread._
