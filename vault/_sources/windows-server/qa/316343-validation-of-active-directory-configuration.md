---
title: "Validation of Active Directory configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316343/validation-of-active-directory-configuration
question_id: 316343
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-clustering-high-availability"]
---
# Validation of Active Directory configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316343/validation-of-active-directory-configuration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, when creating the HA cluster in Windows Server 2016 Std and validating the Active Directory section, the error checked: Could not determine RT1.local node site with error: Could not name the domain controller from RT1.local. Let me mention that the computer is joined to the domain and I am functioning true. A virtual machine acting as the controller controller operates on the physical site of RT1. What might be in the error that you receive?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-19*

Does anybody have an idea ? any tips ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Thank you for your answer.  

domain name - wip.local  

RT1.wip.local  

KS2.wip.local  

on the node RT1.wip.local is VM domain controller ISLA.wip.local  

cluster name Cluster_HA.wip.local  

==============================  

Cluster verification  

Cluster configuration -> Check resource status   

Verifying the network name resource Name: Cluster_HA for Active Directory problems.  

The cluster service on node 'RT1' was unable to connect to the domain controller. This can reduce the functionality that depends on the cluster network names. Make sure the node is configured with at least one domain controller available.   

System Configuration -> Validate Active Directory Configuration   

Verifying that all nodes have the same domain, domain role, and OU.   

Name FQDN 	Domain 	           Role 	                 Site name  	                       OU  

KS2.wip.local 	wip.local 	Member server   Default-First-Site-Name 	 Computers  

RT1.wip.local 	wip.local 	Member server  		                                 Computers  

The node site name RT1.wip.local could not be determined due to the following error: Cannot retrieve domain controller name from RT1.wip.local.  

Connectivity to the writable domain controller from RT1.wip.local could not be established with the following error: Cannot retrieve the domain controller name from RT1.  

Nodes (KS2.wip.local) can access a writable domain controller.  

The nodes (RT1.wip.local) cannot access the writable domain controller. Check connectivity between them and the domain controllers.   

==============================  

I run Failover Cluster Manager on KS2.wip.local and there are errors in the events:   

Node RT1.wip.local ID 1228  

Cluster network name resource 'Nazwa klastra' encountered an error enabling the network name on this node. The reason for the failure was:   

'Unable to obtain a logon token'.  

The error code was '1311'.   

You may take the network name resource offline and online again to retry.  

Node RT1.wip.local ID 1683  

The cluster service was unable to reach any available domain controller on the domain. This may impact functionality that is dependent on Cluster network name authentication.  

DC Server: Nazwa klastra   

Guidance: Verify that domain controllers are accessible on the network to the cluster nodes.  

Node RT1.wip.local ID 1196  

Cluster network name resource 'Nazwa klastra' failed registration of one or more associated DNS name(s) for the following reason:  

Błąd serwera DNS.  

Ensure that the network adapters associated with dependent IP address resources are configured with at least one accessible DNS server.  

=============================  

On node RT1.wip.local I run failover cluster manager -> connecting to cluster, unfortunately there are no available. I understand that I should be able to manage a failover cluster on both nodes?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi,    

-  I would like to check what is the domain name, what is the cluster node name that failed to create the cluster, what is the DC name?    

-  Do you get an error message when creating the cluster? If yes, please provide the screenshot of the error message.    

-  If the issue is that the cluster node is unable to connect to DC when creating Cluster, please check if the following firewall port is opened:    

    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements    

Thanks for your time!    

Best Regards,    

Anne    

-----------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

I noticed that I get a message when connecting rdp to a node. Disabling authentication doesn't change anything.     

    

When I ping the ip DC address I get a reply from the DC address. When I ping the DC name I get a reply from the ipv6 address.
