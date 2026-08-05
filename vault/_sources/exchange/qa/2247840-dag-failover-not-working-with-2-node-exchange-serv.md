---
title: "DAG Failover Not Working with 2-Node Exchange Servers 2019 cu15 on server 2025"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2247840/dag-failover-not-working-with-2-node-exchange-serv
question_id: 2247840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# DAG Failover Not Working with 2-Node Exchange Servers 2019 cu15 on server 2025

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2247840/dag-failover-not-working-with-2-node-exchange-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a Database Availability Group (DAG) configured with two Exchange servers: EMAIL01 and EMAIL02. Everything appears to be set up correctly — both servers are members of the DAG, and the witness server is configured.

However, when I shut down one of the servers (for example, EMAIL01), the other server (EMAIL02) does not take over. The databases do not mount automatically, and Exchange services are disrupted.

I've checked the DAG membership, cluster status, and witness availability, and all seem okay. I'm unsure why failover doesn't occur as expected.

Any suggestions on what might be wrong or what else I should check?

Thanks!

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-11-13*

Update from 2025-12-10...  

Looks like 2-node DAG is not working as expected and after update CU 2025-12 for Windows Server 2025 ...  

But if you shutdown passive node - working as expected.  

If you shutdown active node - no...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-16*

Hi @parisa moghadam,

This is a common snag with 2-node DAGs, and you're right to focus on the witness server and cluster status — but there are a couple key things to double-check:

– In a 2-node DAG, the witness server becomes critical for maintaining quorum. If the active server goes down and the remaining one can't reach the witness, it won't have quorum, and databases won’t mount. Make sure:

The witness server is online and reachable from EMAIL02.

The Exchange Trusted Subsystem group has local admin rights on the witness.

– Verify the quorum configuration is set to Node and File Share Majority. You can confirm this with:

Get-Cluster | fl Name,Quorum*

If quorum is misconfigured, failover won’t happen.

– Check if EMAIL02 is marked as a lower activation preference or if there's a lag setting preventing immediate mount:

Get-MailboxDatabaseCopyStatus *

– Make sure automatic activation isn’t blocked on EMAIL02:

Get-MailboxServer EMAIL02 | fl DatabaseCopyAutoActivationPolicy

It should be Unrestricted.

Let us know what you find — it usually comes down to quorum loss or an activation block.
