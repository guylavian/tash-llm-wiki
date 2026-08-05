---
title: "remove manually added exchange server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186567/remove-manually-added-exchange-server-2019
question_id: 1186567
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# remove manually added exchange server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186567/remove-manually-added-exchange-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have upgraded my exchange server and installed new server build both are same version and build now.

my case is now I'm working on standalone server and I need to build the DAG .

I tried to add from exchange ECP the non-production server and it was added , however I need to add the second production server to DAG it is showing old DAG name which I can't see it in the ECP  

 I got this error : removed from the cluster before it can be added to database availability group.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-06*

Hi @abdulqader naji ,

Please try the following steps:

1.Remove the production server from the old DAG.

`Remove-DatabaseAvailabilityGroupServer -Identity OldDAG -MailboxServer <the second production server>`

2.Import the Failover Cluster module into Exchange Management Shell session.

`Import-Module FailoverClusters`

3.Remove a failed node from a Windows Failover Cluster.

`Get-ClusterNode <the second production server>| Remove-ClusterNode -Force`

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
