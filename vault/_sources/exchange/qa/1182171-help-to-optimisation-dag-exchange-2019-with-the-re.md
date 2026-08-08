---
title: "help to  optimisation DAG Exchange 2019, with The really low network throughput on a site I must therefore optimize the messaging fux to overcome this problem (system optimization)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182171/help-to-optimisation-dag-exchange-2019-with-the-re
question_id: 1182171
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# help to  optimisation DAG Exchange 2019, with The really low network throughput on a site I must therefore optimize the messaging fux to overcome this problem (system optimization)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182171/help-to-optimisation-dag-exchange-2019-with-the-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello;

I am currently deploying a DAG Exchange 2019, distributed on 2 remote sites on one of them the network flow is very low could you give me system-oriented optimization advice to overcome this problem Please....

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-02-19*

Hi @AJHB  

I think you should avoid to host a active copy of mailbox database in the Exchange Server hosted in the site where network flow is very low. Using this configuration, the network bandwidth will be used only to synchronize data between mailbox database (active and passive) of the DAG without any impact on end user. 

In other hand , you should work to improve network bandwidth to ensure the high availability and same service quality in case of issue in Exchange server with active mailbox database.

Please don't forget to mark helpful answer as accepted

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-05*

Hello, sorry for my late return (personal problems).

thank you for your answer but in the best of worlds I would have had the choice to modify or not to use this low speed infrastructure but, I cannot, I am forced to take it, the money does not allow it either .

Is it really impossible to optimize this DAG Exchange 2019, spread over 2 remote sites, one of which has a very low network speed,... can we play on certain parameters, compression for example... thank you in advance for your help

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-19*

DAG sites should never have network connectivity that is not optimal. All DAG servers should be considered peers, there is really no such thing as a DAG DR site or "backup" when thinking about how clients will access a server or for database replication. If one of those sites can not handle network traffic  0 either configure it so it can, or do not use it. Just my two cents.

see network requirements:

https://learn.microsoft.com/en-us/exchange/high-availability/plan-ha?view=exchserver-2019#network-requirements
