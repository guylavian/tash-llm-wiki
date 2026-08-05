---
title: "Exchange 2019 name space and exchange 2013 name space requirements if they are deployed in different load balancer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1256841/exchange-2019-name-space-and-exchange-2013-name-sp
question_id: 1256841
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 name space and exchange 2013 name space requirements if they are deployed in different load balancer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1256841/exchange-2019-name-space-and-exchange-2013-name-sp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are planning to install exchange 2019 in Azure datacenter. exchange 2013 is in a local data center. while deploying the DNS names space,
Exchange 2019 name space and exchange 2013 name space requirements if they are deployed in different load balancer.
How proxying happens if different DNS namespace are assigned to exchange 2019 and 2013.
cheers
Priya

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-26*

Hi @Priya Jayaraman  ,  

I read through the description but got confused about your query. Could you try to elaborate a bit more about the architecture of your environment?    

If Exchange 2019 and Exchange 2013 are two different organizations, per my understanding, there's no need of proxy.
If Exchange 2019 is in coexistence with Exchange 2013, normally they would be deployed in the same load balancer with same namespace. And for details about the client connectivity procedure, you can refer to the explanation in the blog below:  

Client Connectivity in an Exchange 2016 Coexistence Environment with Exchange 2013  

*(*Note: While not explicitly called out in this blog post and graphics, Exchange 2019 behavior is the same as Exchange 2016 behavior.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
