---
title: "Microsoft Exchange mailbox database copy status healthy but get-cluster node status showing DOWN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/162968/microsoft-exchange-mailbox-database-copy-status-he
question_id: 162968
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange mailbox database copy status healthy but get-cluster node status showing DOWN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/162968/microsoft-exchange-mailbox-database-copy-status-he (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a DAG with 3 nodes, after we performed windows update and rebooted all the Exchange servers. There are 2 nodes showing "Down" when we run get-clusternode cmdlet. The mailbox database copy status for all the mailbox servers are showing Healthy/Mounted. However we are unable to do any switchover/mount the database copies on the nodes that are showing down in failover cluster.   

There is no firewall in between and the OS internal firewall has been turned off. Other than re-creating the DAG is there anyways then can overcome this?  

Any idea guys?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-14*

What does  

test-replicationhealth  

show?

Is the cluster service started on those servers?

Can you simply bring the cluster node up?

```
Start-ClusterNode 
```
