---
title: "How to move Primary Active Manager role - Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/363142/how-to-move-primary-active-manager-role-exchange-2
question_id: 363142
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# How to move Primary Active Manager role - Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/363142/how-to-move-primary-active-manager-role-exchange-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a DAG with two member servers (PRIM-EXCH and ALT-EXCH). There is one witness server (witness server is not an exchange server) for the DAG. Get-DatabaseAvailabilityGroup | FL command states ALT-EXCH is the Primary Active Manager. ALT-EXCH does not have any database copies on it and is currently at HQ site so 7 static journal DBs, one active Journal DB and one active mailbox DB can be replicated over to it over the LAN. After all the static DBs are copied over and the 2 active DBs are replicated over and in sync, the ALT-EXCH server will be taken to an alternative NOC, given a new IP address and will be used strictly as an alternative exchange server (in the event PRIM-EXCH goes down.) The two servers will remain in the DAG with continuous replication running across the two different subnets.  

Because I only have two servers (and a witness server) I am using Datacenter Activation Coordinator (DAC mode) - as Microsoft recommends.  

I am thinking PRIM-EXCH needs to have the Primary Active Manager role as this will remain in the same subnet with the Witness server and it is our primary Exchange server. Is my thinking correct? And if so, how do I move the PAM to PRIM-EXCH and SAM to ALT-EXCH?   

Please advise.  

Thank you,

## Answers

_No answers on this thread._
