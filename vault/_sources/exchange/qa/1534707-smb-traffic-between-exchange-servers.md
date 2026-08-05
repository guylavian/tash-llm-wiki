---
title: "SMB traffic between Exchange Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1534707/smb-traffic-between-exchange-servers
question_id: 1534707
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# SMB traffic between Exchange Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1534707/smb-traffic-between-exchange-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi , 

We have Exchange 2019 CU13 in our environment with multiple exchange servers placed in different AD sites running in the windows servers 2022 OS, we are seeing the SMB traffic between the Exchange severs, we would like to understand the following queries

-  When exchange servers uses SMB protocol and what type of data is replicated between the Exchange servers over SMB ?

-  Any MS article which talks about the SMB traffic between the Exchange servers ?

-  Is the DAG replication happening between the exchange nodes, use SMB by any chance ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-01*

Thank you @Andy David - MVP  will perform the Wireshark trace and analyze it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-16*

I suspect it using SMB for cluster communications:
https://techcommunity.microsoft.com/t5/storage-at-microsoft/smb-transparent-failover-8211-making-file-shares-continuously/ba-p/425693
https://learn.microsoft.com/en-us/exchange/high-availability/database-availability-groups/active-manager?view=exchserver-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-16*

Hi @Andy David - MVP  
Thank you for your prompt answer, I understand the exchange server running in the windows server will use the SMB to communicate with the file share witness.
My question is, I am seeing the SMB traffic flowing between the Exchange servers installed in windows server 2022, Is this usual behavior ? if yes, may i know what type of data or contents is transferred over SMB between the Exchange servers installed in windows server 2022 ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-16*

Windows Servers use SMB to communicate as does the File Share Witness server in a DAG specifically:
https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/manage-dags?view=exchserver-2019
By default, all DAGs use TCP port 64327 for continuous replication.
https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/manage-ha?view=exchserver-2019
