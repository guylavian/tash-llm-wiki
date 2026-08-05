---
title: "Exchange 2016 DAG okay, but rebuilt node missing in Failover Cluster"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316785/exchange-2016-dag-okay-but-rebuilt-node-missing-in
question_id: 316785
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-high-availability-clustering-high-availability", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 DAG okay, but rebuilt node missing in Failover Cluster

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316785/exchange-2016-dag-okay-but-rebuilt-node-missing-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We recently rebuilt one of our Exchange servers, and have come across an issue with the Windows Failover Clustering, rather than the Exchange side of things.  Once the server had been rebuilt, we added that note back into the DAG via the Exchange console.  We then proceeded to re-seed the passive database copies.  All of that worked okay, but we get failures when we test the replication health.  

It looks like the process of adding the clustering service, but without being told it was waiting for a server restart to complete, which we didn't do.  I suspect that is the reason why in the Windows Failover Clustering, it only shows a single node.  When I attempt to add the newly built node to that cluster, it fails stating that the node is already part of the cluster.  

Running the following command shows:  

cluster /cluster:DAG02 /add /node:SERVER1  

Configuring node SERVER1  

12% Validating cluster state on node SERVER1.This phase encountered an error for Cluster object 'Node SERVER1 appears to be a member of a cluster. It is either a member of an existing cluster or the node was not cleaned up after being evicted from a cluster. If you are sure this is not a member of a cluster run the Remove-ClusterNode cmdlet with the -Force parameter to clean up the cluster information from the node and then try to add it to the cluster again.' but will continue. The error status is 5065 (0x000013C9).  

This phase has failed for Cluster object 'SERVER1' with an error status of 5065 (0x000013C9).  

This phase has failed for Cluster object 'SERVER1' with an error status of 5065 (0x000013C9).  

Cleaning up SERVER1.  

System error 5065 has occurred (0x000013c9).  

The cluster node is already a member of the cluster.  

cluster node  

Listing status for all available nodes:  

Node Node ID Status  

SERVER2 2 Up  

Checking the database copy status on SERVER1:  

Get-MailboxDatabaseCopyStatus -Server SERVER1  

Name Status CopyQueue ReplayQueue LastInspectedLogTime ContentIndex  

Length Length State  

EDB AC 01\SERVER1 Healthy 0 0 16/03/2021 09:50:05 Healthy  

EDB DG 01\SERVER1 Healthy 0 0 16/03/2021 09:50:21 Healthy  

EDB HJ 01\SERVER1 Healthy 0 0 16/03/2021 09:49:47 Healthy  

EDB KM 01\SERVER1 Healthy 0 0 16/03/2021 09:49:11 Healthy  

EDB NR 01\SERVER1 Healthy 0 0 16/03/2021 09:47:09 Healthy  

EDB SZ 01\SERVER1 Healthy 0 0 16/03/2021 09:49:48 Healthy  

And on SERVER2:  

Get-MailboxDatabaseCopyStatus -Server SERVER2  

Name Status CopyQueue ReplayQueue LastInspectedLogTime ContentIndex  

Length Length State  

EDB DG 01\SERVER2 Mounted 0 0 Healthy  

EDB AC 01\SERVER2 Mounted 0 0 Healthy  

EDB HJ 01\SERVER2 Mounted 0 0 Healthy  

EDB KM 01\SERVER2 Mounted 0 0 Healthy  

EDB NR 01\SERVER2 Mounted 0 0 Healthy  

EDB SZ 01\SERVER2 Mounted 0 0 Healthy  

I'm not sure how to proceed here.  

I don't know whether it would be safe to run the suggested command, "Remove-ClusterNode SERVER1 -force" to cleanup the metadata, then attempt to re-join it to to failover cluster, without upsetting anything else on the Exchange side.  

I don't know whether running the "Clear-ClusterNode" on the affected node would help, and allow me to add this node back in to the "DAGO2" cluster.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-17*

Hi @Howard Gyton   ,    

Good day!    

Please run the following cmdlet to check the the DAG and try to remove the Server1 and retry adding it if there is Server1, if not you can try adding it.    

```
Get-DatabaseAvailabilityGroup  
Remove-DatabaseAvailabilityGroupServer -Identity "DAGName" -MailboxServer Server1  
Add-DatabaseAvailabilityGroupServer -Identity "DAGName" -MailboxServer Server1
```

If this couldn't work, you should run the Remove-ClusterNode. You don't have to worry about the data loss, this command only remove the node from the cluster, it's like removing the member from a DAG.    

I think you will could add the server after removing the node.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

Both DAG, and failover cluster are now healthy!
