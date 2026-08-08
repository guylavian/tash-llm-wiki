---
title: "Active Directory replication between multiple controllers fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4349696/active-directory-replication-between-multiple-cont
question_id: 4349696
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Active Directory replication between multiple controllers fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4349696/active-directory-replication-between-multiple-cont (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am coming to the forum because I have a big problem with the replication of my domain controllers.  

I explain the situation:  

Context :  

I have 2 local sites connected with IPSec, let's call them site A and site B.  

In each site I have two domain controllers let's call them for site A DC1 and DC2 and for site B DC3 and DC4.  

The 4 controllers are synchronized between them in inter site and intra site.  

The 2 DC of site A are virtualized with Hyper V.  

The 2 DC of site B are physical.  

Normally DC1 is the master DC.  

Problem:  

I ran a domain configuration audit script on DC1 that was supposed to run in audit mode but unfortunately made big changes on the domain. Basically the script applied the best practices of all the CIS checkpoints (which in fact is fine) but it impacted the business of the company. This is because all the DC's synced with the DC1 which pushed the changes automatically to the other DC's.  

Fortunately, we have an extremely recent backup (snapshot) of the hyper V that we used to restore the DC1. However, when we start the restored DC1 VM, the other DCs (2,3,4) that have the bad changes replicate them to the DC1 automatically (15 seconds) so we can't restore our domain controllers from the DC1 snapshot.  

In order to find a solution, we disabled the auto replication in INBOUND and OUTBOUND on the DC2,3,4 (repadmin /options DCx +DISABLE_INBOUND_REPL) (repadmin /options DCx +DISABLE_OUTBOUND_REPL) then restored the snapshot of the DC1 VM and launched the DC1. It works perfectly, the DC1 keeps the good modifications (the old ones, before the script execution), so we now want to apply the settings of the DC1 on all the DCs to get a homogeneous domain. So we force the replication of DC1 on the other DCs with the command: Repadmin /syncall DC1 /APed.  

This propagated the good configuration of DC1 on the other DCs so it's perfect.  

However, by reactivating the INBOUND and OUTBOUND (repadmin /options DCx -DISABLE_INBOUND_REPL) (repadmin /options DCx -DISABLE_OUTBOUND_REPL) auto replication on the DCs, the bad modifications unfortunately reappeared and propagated on all the DCs almost immediately.  

How is this possible knowing that at a given time "T" the 4 domain controllers all had the old good configuration (before the script was executed)?  

Where did the DC's go to get the wrong configuration (after the script was executed)?  

How do we keep the right config on all the DCs once we reactivate the replications by reactivating the INBOUND and OUTBOUND?  

I thank you in advance for your answers, the situation is very critical.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2022-05-07*

Hello TL_92,

Good day! I'm John Dev a Windows user like you and I'll be happy to assist you today.

I want to apologize that this is just a consumer forum. Due to the scope of your question, I recommend posting your query on Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue. They have IT experts there that can assist you better especially about Windows Servers, Active Directory, Domains and Group Policy configurations, etc.

Microsoft Site Q&A

https://docs.microsoft.com/en-us/answers/topics...

Kind regards,

John DeV

Independent Advisor
