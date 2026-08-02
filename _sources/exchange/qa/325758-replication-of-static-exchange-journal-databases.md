---
title: "Replication of Static Exchange Journal Databases"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/325758/replication-of-static-exchange-journal-databases
question_id: 325758
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Replication of Static Exchange Journal Databases

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/325758/replication-of-static-exchange-journal-databases (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of standing up a new Exchange Server 2019 CU8. It will be the 2nd (and alternate) Exchange 2019 server in our Exchange environment. I will be creating a DAG with the two servers.   

I have a couple concerns I could use advise on.  

The second Exchange Server is currently on the same subnet as the 1st (and primary) Exchange server. But after all the databases are replicated over, it will be moved to different site within the same domain but on a different subnet ...Meaning I will need to change the IP address on the second Exchange 2019 server when it moves to the alternate NOC site.    

Does change the physical IP address affect how the DAG interacts?   

I am assuming the virtual IP configured for the DAG is used only for internal replication and does not play into how clients (outlook, owa, ecp) access the servers. Am I correct in this assumption?  

I have several static Journal Databased I need to copy over to the new Exchange server. Do I need to create the DAG first? Or is there a way to copy over the journal bases without the DAG?  

Please advise.  

Thank you,

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-22*

Got it...thank you so much for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-22*

Hi Andy!  

That makes sense. But I thought you need 2 Exchange servers before you can create a DAG. I only have two Exchange servers in my environment. Well...Actually one right now. I will be installing Exchange 2019 on the Alt box tomorrow. Can I create a DAG with just one Exchange server?   

Quick question....And I think I already know the answer but want to confirm my thinking. There is nothing special in installing an exchange box that will be part of DAG. It's just an Exchange server. Correct?  

Thank you for your advise on this....I really appreciate it.
