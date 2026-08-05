---
title: "Problem with Exchange 2019 DAG and Cluster Service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/128194/problem-with-exchange-2019-dag-and-cluster-service
question_id: 128194
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-high-availability-clustering-high-availability"]
---
# Problem with Exchange 2019 DAG and Cluster Service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/128194/problem-with-exchange-2019-dag-and-cluster-service (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we added some exchange 2019 servers to our exchange 2013 environment to prepare for migration.  

we created a new DAG with the first two servers and we noticed, that we get EventID 1592 every 2-3 minutes on both server:  

Cluster node 'serverA' lost communication with cluster node 'serverB'.  Network communication was reestablished. This could be due to communication temporarily being blocked by a firewall or connection security policy update. If the problem persists and network communication are not reestablished, the cluster service on one or more nodes will stop.  If that happens, run the Validate a Configuration wizard to check your network configuration. Additionally, check for hardware or software errors related to the network adapters on this node, and check for failures in any other network components to which the node is connected such as hubs, switches, or bridges.  

Windows Firewall has the Cluster Group exclusions and the network between the two hosts is stable.  

Any idea what can cause this error?  

We tried to set a higher samesubnetdelay but not luck ((get-cluster).samesubnetdelay = 2000).  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

This problem drives me crazy.    

I removed all additional NIC's from the Nodes and recreated the DAG. Didn't work, same issues.    

I removed the DAG again, disabled all Windows Firewalls completely and recreated the DAG.    

No more errors, everything seems to be working now (expect IMAP4 and POP3 backend services which starts crashing now).    

The Windows Firewall has a custom rule, which allows all traffic between the nodes AND the created rules from the cluster service.    

I can't go in production without Windows Firewall, but what is missing??

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

Hi all,  

i can go back to one network, not problem, but why does my cluster take the cluster offline because of network issues?   

When i go back to one network interface, with the auto generated windows firewalls rules, EventID 1592 will come back and finally break the cluster.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-16*

Hi,  

i redeployed the cluster with the following network config:  

PS C:\Windows\system32> get-clusternetwork  

Name              State Metric             Role  

Cluster Network 1    Up  70240 ClusterAndClient  

Cluster Network 2    Up  30240          Cluster  

Network2 is the cluster network and has no other traffic (flat 10.10.10.0/24 without gateway and dns)  

1562 event disappeared, but after 15 minutes, we had the following error on both cluster nodes:  

Cluster node 'serverA' was removed from the active failover cluster membership. The Cluster service on this node may have stopped. This could also be due to the node having lost communication with other active nodes in the failover cluster. Run the Validate a Configuration wizard to check your network configuration. If the condition persists, check for hardware or software errors related to the network adapters on this node. Also check for failures in any other network components to which the node is connected such as hubs, switches, or bridges.  

any idea why that happens? Network2 has no windows firewall activated and a direct connection in the same vlan.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-16*

Hi Anne,  

thanks for your reply. I did that, we added a second NIC with Windows Firewall disabled. Then we had 2 Networks listed in that GUI and i tried to disable Cluster Communication on the "Data" Network. After closing the properties of the network and reopen it, the flag was set again.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-16*

Hi，    

If possible, it's recommended to create a separate Cluster network for Cluster only to run heartbeat packets between cluster nodes.    

To do this, please add an additional network adapter on each cluster nodes, when the network shows up in the cluster network, configure it as "Allow cluster network communication on this network."    

    

Thanks for your time!    

Best Regards,    

Anne    

-----------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
