---
title: "ADCS cluster in-place upgrade from 2012r2 --> 2016 --> 2019 - Issue with the secondary node"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5846437/adcs-cluster-in-place-upgrade-from-2012r2-2016-201
question_id: 5846437
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# ADCS cluster in-place upgrade from 2012r2 --> 2016 --> 2019 - Issue with the secondary node

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5846437/adcs-cluster-in-place-upgrade-from-2012r2-2016-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Ref: Windows Failover Cluster running ADCS role

Please advise, if anyone had attempted ADCS failover cluster "in-place upgrade from 2012r2 --> 2016 --> 2019" and had seen issue with the secondary node showing offline after the upgrade to 2019 or unable to add the secondary node to the cluster. 

Also, if they had experienced the ADCS service cluster role not staying online after the nodes were upgraded from 2012r2 --> 2016 --> 2019.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-04-01*

Hi BK,

 Thank you for raising the question regarding the Windows Failover Cluster running the ADCS role and the in-place upgrade path from 2012 R2 to 2016 to 2019. The ADCS role is not supported as a clustered role in newer versions of Windows Server. During upgrades, issues such as secondary nodes showing offline or the ADCS cluster role failing to stay online are expected behaviors due to this change in supportability. The recommended approach is to deploy ADCS on standalone servers rather than attempting to cluster the role. This ensures stability and compliance with Microsoft’s current design guidance.

 If this answer addresses your concern, please click Accept the answer to support me.

Thank you!!!

Best regards, 

QQ.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-01*

For an ADCS role running on a Windows Failover Cluster that is being upgraded in-place from Windows Server 2012 R2 → 2016 → 2019, issues with a secondary node not joining the cluster or the ADCS clustered role not staying online after the upgrade typically fall into the general categories seen with cluster rolling upgrades and post-upgrade resource failures.

Based on the documented behavior and troubleshooting guidance for Windows Server failover clusters and rolling upgrades, the following checks and steps are relevant:

-  Validate the rolling upgrade path and node compatibility

-  Ensure the upgrade path is sequential and supported (2012 R2 → 2016 → 2019) and that each node is fully updated (latest cumulative updates) before rejoining the cluster. Version incompatibility can prevent a node from joining or staying in the cluster.

-  When a node cannot rejoin and you see version mismatch or incompatibility errors, the guidance is:

-  Verify the supported OS and cluster version mix.

-  Update the node to the latest CU.

-  Upgrade OS versions sequentially.

-  Use `Get-ClusterLog` to identify versioning errors.

-  Re-add or resume upgraded nodes correctly

-  After a clean OS installation as part of the upgrade, the node must be explicitly added back to the cluster using Windows Admin Center, Failover Cluster Manager, or `Add-ClusterNode`:

```
Add-ClusterNode -Name 
```

-  If the node was upgraded in-place and remained part of the cluster, it must be resumed after the upgrade:

```
Resume-ClusterNode -Name  -Failback Immediate
```

-  Once the node is up and part of the cluster, workloads (including the ADCS clustered role) can be moved or balanced across nodes.

-  Troubleshoot resources or services that do not come online

-  If the ADCS clustered role (or any other clustered resource) does not stay online after the upgrade, treat it as a generic “resource or service doesn’t come online” issue:

-  Check cluster events in Failover Cluster Manager for Event IDs such as 1069, 1146, or 1230 that indicate resource failures.

-  Verify resource owner configurations with:

```
Get-ClusterResource | Get-ClusterOwnerNode
```

        Confirm that the ADCS role is allowed to run on the upgraded nodes and that preferred owners/possible owners are correctly configured.

-  Repair or re-create missing dependencies (for example, if the ADCS role depends on specific services, disks, or network names that were misconfigured or lost during the upgrade).

-  Restart the cluster service on affected nodes if needed:

```
Restart-Service ClusSvc
```

-  Address cluster name/DNS permission issues that can block roles from coming online

-  If the ADCS clustered role relies on a cluster network name and that name cannot register in DNS after the rebuild/upgrade, the role may fail to come online on one or more nodes.

-  A common cause is missing permissions for the Cluster Name Object (CNO) in Active Directory to update records in a secure DNS zone. Symptoms include event log entries such as:

Cluster network name resource failed registration of one or more associated DNS name(s) because the access to update the secure DNS was denied.

-  To resolve:

-  Verify that the CNO exists in Active Directory and is not disabled.

-  In DNS Manager, open the forward lookup zone for the cluster domain, go to Properties → Security, and confirm the CNO has Create all child objects and Write all properties permissions. Add them if missing.

-  Bring the ADCS cluster role online again and test failover between nodes.

-  If issues persist

-  Collect cluster logs from all nodes:

```
Get-ClusterLog -UseLocalTime -Destination 
```

-  Collect relevant event logs from FailoverClustering and DNS Server channels, and details of the CNO object and its permissions.

-  Use this data when engaging Microsoft Support for deeper analysis of ADCS-specific behavior on the upgraded cluster.

These steps and checks apply generally to clustered roles (including ADCS) that fail to stay online or nodes that fail to join or remain in the cluster after an in-place OS upgrade sequence.

References:

-  Windows Server 2019 cluster role doesn't come online after you rebuild the cluster

-  Upgrade a Windows Server failover cluster with a cluster OS rolling upgrade

-  Troubleshoot rolling upgrade issues
