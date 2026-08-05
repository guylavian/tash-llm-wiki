---
title: "Microsoft Exchange DAG Management service cannot be started"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160962/microsoft-exchange-dag-management-service-cannot-b
question_id: 1160962
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Microsoft Exchange DAG Management service cannot be started

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160962/microsoft-exchange-dag-management-service-cannot-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have 3 Exchange 2019 CU12, and we deployed the DAG cluster.

Databases in DAG  successfully replicate with all members in the cluster, and "BAD COPY COUNT" is 0 for all databases

our problem is on one of the servers, in this server "Microsoft Exchange DAG Management service" service cannot be started!

after I tried to start this service, I received the below error and generated a "System Event" error with event ID 7031

The Microsoft Exchange DAG Management service terminated unexpectedly.  It has done this 1 time(s).  The following corrective action will be taken in 5000 milliseconds: Restart the service.

This issue only is on one of the Exchange Servers, I would be grateful if anyone could help me

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-22*

guys, 

I found the "Microsoft Exchange DAG Management" service started automatically, without me changing any config on Exchange Server or Windows Server,

the service was up for 24 hours. but, after rebooting the windows server, unfortunately, the service goes to stop and can't start!

is it exist a log file for this service? or how can we monitor this service exclusively what happened?

@Administrateur Microsoft Exchange  @IT - Exchange Support Lead  @Amit Singh

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-16*

Before the event occurred, did you change anything on the exchange server? Like, install updates/CUs, etc. 

You can try to upgrade this server to Exchange 2019 latest CU ( Exchange Server 2019 CU12 Jan23SU) and check if any helps.

Also, check these links for more insight - https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/frontend-transport-service-terminate-run-set-servercomponentstate

https://social.technet.microsoft.com/Forums/ie/en-US/789c27b7-0a08-44d0-b28f-150c86f97c01/microsoft-exchange-replication-service-continuously-restarting?forum=Exch2016SD

https://learn.microsoft.com/en-us/answers/questions/187901/msexchangedagmgmt-wont-start-after-upgrade-echange
