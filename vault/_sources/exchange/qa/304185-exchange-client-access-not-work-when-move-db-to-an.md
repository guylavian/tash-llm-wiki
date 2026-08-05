---
title: "Exchange Client access not work when move DB to another MBX server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304185/exchange-client-access-not-work-when-move-db-to-an
question_id: 304185
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Client access not work when move DB to another MBX server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304185/exchange-client-access-not-work-when-move-db-to-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,   

I have 4 exchange 2013 cu22 server (2 CAS and 2 MBX servers). 2 MBX is configured a DAG and witness configure to other server.   

When the DB mount on MBX2, everything fine.   

When I mount the database to MBX1, both OWA and ECP can access. Outlook can send/receive email but the connection show "trying to connect. Then if i restart either one of the CAS, both OWA and ECP will show HTTP503 error and Outlook cannot connect. In this moment, all DB still mount and failover cluster all resource is "UP", so the DAG should be fine. But all client access not work.   

Services will not resume even all CAS and MBX servers are started. It will solve until I mount the DB back to MBX2. Seems the MBX1 is not in function but don't have any error message. Any idea?   

Thanks   

Chong

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-11*

Recreate the self-sign certificate and bind to https (444 port) in MBX1 server IIS solved the problem
