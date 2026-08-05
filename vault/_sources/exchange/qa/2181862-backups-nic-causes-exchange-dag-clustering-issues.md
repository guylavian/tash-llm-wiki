---
title: "Backups NIC Causes Exchange DAG Clustering Issues and Exchange Information Store Worker Process Alert"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2181862/backups-nic-causes-exchange-dag-clustering-issues
question_id: 2181862
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Backups NIC Causes Exchange DAG Clustering Issues and Exchange Information Store Worker Process Alert

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2181862/backups-nic-causes-exchange-dag-clustering-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

1. Product & Service Pack:

-  Windows Server DC 2019 - Version 1809 (OS Build 17763.4377)

-  Exchange 2019 – CU 15 with November 2024 SU (15.02.1748.010)

2. Cluster Type (For WINDOWS only):

-  DAG

3. Troubleshooting Performed:

-  Unregistering DNS Addresses: Unchecking the "Register this connection’s addresses in DNS" checkbox for the backups NIC was attempted but has not definitively resolved the issue.

-  Database and Server Removal: The mailbox database copy was removed, and the server was removed from the DAG. Then, the backups NIC was disabled. After re-adding the server to the DAG and creating a new mailbox database copy, the issue was resolved until the backups NIC was reenabled.

-  Temporary Network Interface Disabling: If the mailbox database copy is still valid, disabling the NIC and waiting 15 minutes allows the server to start the cluster service again.

-  Metric Adjustment Attempt: Adjusting the network metric for the backups NIC using PowerShell and netsh commands was attempted to deprioritize the network.

-  Manual Configuration: Ensuring "ManualDagNetworkConfiguration" is set to True and running the DiscoverNetworks task to see if automatic configuration aligns with the intended network settings.

-  Cluster Module Verification: Ensuring the Failover Clustering feature and its tools are properly installed and the correct module is imported for consistent command execution.

-  Network Interface Review: Listing all cluster network interfaces and verifying their states to identify any discrepancies or misconfigurations.

4. Recent Changes:

-  Installed Exchange 2019 CU 14

-  Installed Exchange 2019 CU 14 SU February 2024

-  Installed Exchange 2019 CU 14 SU November 2024

-  Installed Exchange 2019 CU 15

5. When did the problem start?

-  Tuesday 05 March 2023 (initial build out, noticed with backups started)

6. Problem Frequency:

Permanent (if the NIC is enabled)

ISSUE:

The Backups Network Interface Card (NIC) is causing clustering issues in the Exchange Database Availability Group (DAG). The DAG keeps using the subnets assigned to the backups NIC for replication, even when the "ManualDagNetworkConfiguration" setting is set to True. This problem persists after a reset or when the DiscoverNetworks task is run. Additionally, there is an alert (msg252) indicating that the Exchange Information Store Worker Process is not being found. The server currently has a backups NIC, which is definitively causing the issue. The multiple NICs with conflicting settings can cause network misconfigurations, disrupting communication between cluster nodes and services. This misconfiguration prevents the Exchange Information Store Worker Process from functioning correctly, leading to the alert. This issue only occurs while the NIC is enabled on msg252. The other server, msg251, also has the backups NIC on the same subnet but does not experience this issue unless it is not the DAG manager and the other server's NIC is functioning.  msg251 can interchangeably experience the same issue depending on when its Backups NIC is activated or when the Backups NIC on msg252 is activated.  One always works while the other fails in the cluster.

Replication Issues: The Exchange DAG is using the subnets assigned to the backups NIC for replication instead of the intended network, leading to unexpected replication paths and potential network congestion.

Persistent Problems: Despite setting "ManualDagNetworkConfiguration" to True, the issue persists after running the DiscoverNetworks task or resetting the configuration.

Network Misconfiguration Alerts: There is an alert on the msg252 server indicating that the Exchange Information Store Worker Process is not being found, pointing to underlying network misconfiguration issues.

Service Disruptions: The Information Store Worker Process is not functioning correctly, disrupting communication between cluster nodes and services.

Temporary Fixes: Temporary fixes, such as removing/re-adding the mailbox database/Server DAG Membership and disabling the backups NIC, resolve the issue only until the backups NIC is reenabled.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-02-24*

Why the need for a backup NIC? 

Seriously, Im not trying to be a smart a$$. :) 

I think that over complicates things and if you are going to do backups ( those are not really needed however : https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/disaster-recovery?view=exchserver-2019 

then I would run with just one NIC if possible
