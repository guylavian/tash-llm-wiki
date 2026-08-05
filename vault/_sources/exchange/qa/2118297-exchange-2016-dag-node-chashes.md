---
title: "Exchange 2016 DAG node chashes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118297/exchange-2016-dag-node-chashes
question_id: 2118297
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 DAG node chashes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118297/exchange-2016-dag-node-chashes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

Need some help with my Exchange 2016 DAG.  

At last few moths we encountered problem with our DAG nodes.  

We have one DAG (ExDAG) with two nodes: Ex01 and Ex02. 

Situation. By some unknown reason Ex01 periodically crashes. Event log can't give us any explanation about reasons. But that's not the worst thing, after all we have DAG. The worst is that some times after Ex01 crashes DAG node (Ex01) not up to cluster.   

Get-clusternode returns: Ex01 - state - down  

Get-clusterNetwork returns: Ex01 - state - down  

Get-clusterNetworkInterface: Ex01- state - Unavailable  

At the same time Ex01 networking working without any problems: ping, telnet and other works fine and show no problems.  

We tried many of solutuon. Nothings helps. Except one: changing EX01 IP address to any other cause this node to up in cluster. After that all works perfectly.   

Who can help me understand what happens? Why only IP-address change help us? I try to do  

netsh int ip reset  

netsh winsock reset  

but no luck.   

Any help will be appreciated!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-13*

Hi @Евгений Котляревский,

Welcome to the Microsoft Q&A platform!

Based on your description, you are dealing with a problem in a Database Availability Group (DAG). Here are some potential causes and solutions for Exchange 2016 DAG node problems:

-  Even if your network tools do not show any problems, there may be an IP address conflict or ARP cache problem. Changing the IP address may temporarily resolve this conflict. You may want to check any devices on the network that may be causing this conflict.

-  Use the "Get-ClusterNetwork" and "Get-ClusterNetworkInterface" commands to check the cluster network configuration and its status. And make sure that the Cluster Network Name is up and running. You can try disabling and enabling the affected network interface in the Failover Cluster Manager.

-  Sometimes, a network interface card (NIC) can cause problems even if it appears to be functioning properly. Updating the NIC driver or replacing the NIC may help resolve the problem.

-  There may be a problem with the cluster service on Ex01. Restart the Cluster service on Ex01 and see if it fixes the problem:

```
Stop-Service ClusSvc

Start-Service ClusSvc
```

-  Event Log and Cluster Log: While you mentioned that the event log did not show any issues, it may be helpful to enable more detailed logging for the Cluster service. This can sometimes reveal hidden issues. You can use the Get-ClusterLog cmdlet to generate a detailed cluster log for further analysis.

-  Ensure that the network used for the DAG is isolated from other traffic as much as possible. This helps prevent any interference from other network activity.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
