---
title: "Exchange 2016 DAG Database Mount Issues and Active Manager Errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2152262/exchange-2016-dag-database-mount-issues-and-active
question_id: 2152262
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2016 DAG Database Mount Issues and Active Manager Errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2152262/exchange-2016-dag-database-mount-issues-and-active (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Active Manager encountered an error when trying to refresh configuration information from Active Directory. Error: The server is in a database availability group, but Active Manager was unable to access the cluster database for the value ClusterGroup. The server may have just been removed from the database availability group. There are 2 servers in the DAG, and the witness share is available. However, no commands related to managing the DAG work; all return an Active Manager error. 

I have removed database copies from the secondary server but still cannot mount databases or remove either server from the DAG group. Additionally, OWA and Exchange services do not work on either server. I can put the secondary server in maintenance mode, but it made no difference.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-29*

You can refer same thread here-

https://community.spiceworks.com/t/exchange-2016-dag-already-joined-to-a-dag/711492

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-29*

Hi @Leroy Sumlin  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are dealing with a complex issue involving Database Availability Groups (DAGs) and Active Manager. Here are some steps you can take to troubleshoot and possibly resolve the issue:

-  Make sure the cluster service is running on both servers. You can do this by running the following command in PowerShell:

```
Get-Service -Name ClusSvc
```

-  Check the status of the DAG using the following command:

```
Get-DatabaseAvailabilityGroup -Status | Format-List
```

This will provide detailed information about the DAG and its members.

-  Run the Test-ReplicationHealth command to check the health of the replication service:

```
Test-ReplicationHealth
```

-  If there is an issue with the cluster node, you may need to clear the cluster node and re-add it. Use the following command:

```
Clear-ClusterNode -Name 
```

Then, add the server back to the DAG:

```
Add-DatabaseAvailabilityGroupServer -Identity  -MailboxServer 
```

-  Make sure the DAG has quorum. You can check the quorum status using the following command:

```
Get-ClusterQuorum
```

-  Check the event logs on both servers for any errors related to the Cluster service or Active Manager. This can provide more insight into what may be causing the problem.

-  Sometimes restarting the Exchange services can help resolve the issue. You can restart the services using the following commands:

```
Restart-Service MSExchangeIS
Restart-Service MSExchangeADTopology
Restart-Service MSExchangeMailboxReplication
```

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-28*

Make sure both servers are in the "Exchange  Trusted Subsystem" security group
