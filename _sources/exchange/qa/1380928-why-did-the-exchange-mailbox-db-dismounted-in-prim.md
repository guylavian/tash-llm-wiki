---
title: "Why did the Exchange mailbox DB dismounted in Primary mailbox server when the secondary/passive server shutdown?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1380928/why-did-the-exchange-mailbox-db-dismounted-in-prim
question_id: 1380928
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Why did the Exchange mailbox DB dismounted in Primary mailbox server when the secondary/passive server shutdown?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1380928/why-did-the-exchange-mailbox-db-dismounted-in-prim (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

DAG setup has 2 members (1 in each 2 different sites)

DC1/Main site

Mailbox server: D1-exc-MB  

Edge transport server: D1-exc-edge  

Witness server: D1-exc-wit  

Database: DB1 and DB2 (active/mounted in D1-exc-MB)  

AD server: D1-ad1

DC2/Remote site

Mailbox server: D2-exc-MB  

Edge transport server: D2-exc-edge  

Witness server: D2-exc-wit  

Database: DB1 and DB2 (passive)  

AD server: D2-ad1

We had an activity which required shutting down of DC2 site VMs including exchange, witness and AD servers.

After shutting down the VMs in DC2 sites (mailbox, edge, witness and AD), the cluster in DC1 stopped, the databases that were active/mounted in the mailbox server also dismounted (status is unknown) automatically which cause unavailability of OWA. I tried to manually mount it via EAC and started the cluster in EMS with both no success. The cluster only started after powering on all the VMs in DC2 sites and the DBs mounted successfully in DC1.

I'm sure that is not the normal behavior when another member (in different site) of the DAG goes down. I thought the benefit of having a DAG aside from failover is redundancy in which if one of the members shutdown, the exchange operation will not have downtime.

## Answers

_No answers on this thread._
