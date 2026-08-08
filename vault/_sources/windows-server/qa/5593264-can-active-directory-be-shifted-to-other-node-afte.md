---
title: "Can Active Directory be shifted to other node after installing MS Failover Cluster which is connected to this AD?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5593264/can-active-directory-be-shifted-to-other-node-afte
question_id: 5593264
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Can Active Directory be shifted to other node after installing MS Failover Cluster which is connected to this AD?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5593264/can-active-directory-be-shifted-to-other-node-afte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hellow All,

I am nearly a biginner of such kind of works what I am going to express. I have installed a Microsoft 2 node failover cluster and during installing I was forced to install the AD on one of these 2 nodes (Node 1 having AD) and ADC on node 2 in pressure of Customer IT consultant and IT Team. Now during failover (direct power off of Node 1) I have seen that if I switch off the Node 1, VMs on cluster is not failing over (as AD is not available, and corresponding write on DNS is not possible - as per my understanding). 

But if I connect the cluster manually from Node 2, immediately VMs are failing over.

Whereas Logical failover with the help of Cluster Manager (Failover option) is happening perfectly as well as migration of VMs from Node 1 to Node 2 and vice versa.

Certainly I am going to talk with the customer regarding this incident and ask for a 3rd system to host AD but my concern is at this situation, after installation of cluster and creation of VM above the cluster, is it advisable to shift AD? If we shift then how to reconnect the Cluster for failover and other works?

Please help

Thanks in advance.

With warm regards

Somnath Nandy

## Answers

_No answers on this thread._
