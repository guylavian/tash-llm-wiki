---
title: "Issue with adding Node to Exchange 2016 DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237191/issue-with-adding-node-to-exchange-2016-dag
question_id: 2237191
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Issue with adding Node to Exchange 2016 DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237191/issue-with-adding-node-to-exchange-2016-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

Have some weird issue with my exchange 2016 DAG.  

I have DAG (name: ExDAG) with two nodes in it.  

I've installed new Exchange server in other site and want to add it to existing dag.  

While adding this new node to DAG no problems were occured. Node successfully joined to DAG.   

But now I see weird:  

-  In ECP in dag properties I see all three nodes, no problem.  

-  If I run command "Get-ClusterNode" on one of two old nodes I gets only these old nodes, new node not in list.  

-  If I run command "Get-ClusterNode" on new node I gets only this new node. Old nodes not in list.  

-  If I compare failover cluster IDs (whic I get with command "Get-Cluster <Node name> | fl ID) I see, that ID got from old nodes is equal, and ID got from new node is different.  

So its looks like that at Exchange level new node succesfully joined the dag, but at ms failover cluster new node joined to new created cluster with name equal old cluster name.   

Why this happened? Where i was missing?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-25*

You can try to check below troubleshooting steps:

-  Validate cluster communication:

-  Check that all nodes can ping each other by FQDN

-  Verify TCP ports 445, 135, and 593 are open between nodes

-  Ensure all nodes are in the same AD site or have proper site link costs

-  Remove the problematic node from the DAG:

```
Remove-DatabaseAvailabilityGroupServer -Identity ExDAG -MailboxServer  -Confirm:$false
```

-  Clean up the failed cluster join:

-  On the new node, run:

```
Test-Cluster -Node 

   Stop-ClusterNode -Cleanup
```

-  Rejoin the node to DAG:

```
Add-DatabaseAvailabilityGroupServer -Identity ExDAG -MailboxServer 
```

-  Verify proper cluster membership:

```
Get-ClusterNode | Format-Table -AutoSize

   Test-Cluster
```

Additional Checks

-  Verify all nodes have the same Windows updates installed

-  Check the cluster log for errors (located in `C:\Windows\Cluster\Reports`)

-  Ensure all nodes have the same time synchronization source

-  Confirm all network interfaces used for cluster communication are properly configured

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-21*

It seems like the new node joined a new cluster with the same name as the existing cluster. This can happen if the cluster creation process for the new node was not properly synchronized with the existing DAG, causing it to create a new cluster instead of joining the existing one. Or If the new node was added to the DAG using ECP, but there are underlying issues with the configuration of the Failover Cluster (where DAGs reside), then Exchange might think it’s part of the DAG, but the Failover Cluster sees it as a separate cluster.

Possible Solutions:

1.      Remove and Re-add the Node to the DAG: If the node is incorrectly joined to a new cluster, you may need to remove it from the DAG and from the Failover Cluster, then attempt to rejoin it correctly to the existing DAG. Here’s how you can do that:

-  Remove Node from DAG:

```
Remove-DatabaseAvailabilityGroupServer -Identity ExDAG -MailboxServer 
```

-  Remove Node from Cluster: Use Failover Cluster Manager or PowerShell to remove the node from the cluster:

```
Remove-ClusterNode -Name 
```

-  Re-add Node to DAG (make sure to do this after removing it):

```
Add-DatabaseAvailabilityGroupServer -Identity ExDAG -MailboxServer 
```

2.      Verify Cluster Configuration: Ensure that the Cluster service on the new node is fully synchronized and configured to join the existing DAG cluster:

-  Check Cluster Status:

```
Get-Cluster 
```

-  Verify Cluster Nodes: On the old node, check the cluster nodes:

```
Get-ClusterNode
```

3.      Make sure the cluster configuration reflects all three nodes as part of the same cluster.

4.      Cluster Failover ID Comparison: If the cluster IDs are still mismatched after re-adding the node, there might be lingering configuration issues with the failover cluster. It might require you to investigate the event logs for any errors or warnings related to cluster joins or misconfigurations.

5.      Check DAG Health: After adding the node back to the DAG, check the overall DAG health and configuration of the DAG to ensure it is correctly recognizing the new node:

```
Get-DatabaseAvailabilityGroup -Identity ExDAG | fl *
```

6.      Verify DNS and Network: Ensure that there are no DNS or network-related issues preventing the new node from properly joining the existing DAG cluster. This includes checking name resolution between all nodes and ensuring no firewalls or security settings are blocking communication.
