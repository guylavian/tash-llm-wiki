---
title: "Exchange Server and DAG Server Issues Causing Email Delays"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1377545/exchange-server-and-dag-server-issues-causing-emai
question_id: 1377545
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server and DAG Server Issues Causing Email Delays

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1377545/exchange-server-and-dag-server-issues-causing-emai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For the past six months, we have been encountering a recurring problem wherein, once a day, our server experiences a significant disruption in functionality. Specifically, users are unable to send emails, as their messages become stuck in the Drafts folder. In order to resolve this, we have been forced to perform a combination of actions, including restarting both the DAG and Exchange servers simultaneously, restarting specific Exchange services, and analyzing queue messages. Unfortunately, this has been a temporary fix and we are unable to determine whether the issue resolves itself or if it is contingent on the services we restart.

Additionally, we have identified the following error event IDs in our logs:

Event ID 1564: File share witness resource 'File Share Witness (\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local)' failed to arbitrate for the file share '\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local'. Please ensure that file share '\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local' exists and is accessible by the cluster.

Event ID 1069: Cluster resource 'File Share Witness (\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local)' of type 'File Share Witness' in clustered role 'Cluster Group' failed. Based on the failure policies for the resource and role, the cluster service may try to bring the resource online on this node or move the group to another node of the cluster and then restart it. Check the resource and group state using Failover Cluster Manager or the Get-ClusterResource Windows PowerShell cmdlet.

Event ID 1254: The Cluster service failed to bring clustered role 'Cluster Group' completely online or offline. One or more resources may be in a failed state. This may impact the availability of the clustered role.

Event ID 4657: Failover Cluster PowerShell cmdlet Get-ClusterNode: An error occurred opening cluster 'XCOMPANY-DAG'.

Given the severity of this issue and its impact on our operations, we urgently seek your assistance in identifying the root cause and implementing a permanent solution. Our team is available for any necessary troubleshooting or to provide additional information that may aid in your investigation.

We appreciate your prompt attention to this matter and look forward to your earliest response.

Thank you for your assistance.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-29*

Hi @ Yakhshikhanim Rzayeva,

Just want to confirm that you have configured the relevant permissions in the witness correctly.

Here are some of my suggestions for your reference:

1.In the file server, go to Administrative Tools and start Computer Management.

2.Expand Local Users and Groups and click on Groups. Double-click on the Administrators group and check the group Exchange Trusted Subsystem is added.

3.And ensure that the Cluster Computer account has full access.

4.Restart the cluster service in the node to test whether the witness is online, and if that doesn't work, recreate the witness share and restart the cluster.

 

Hope the above suggestions are helpful to you!

In addition, there is some delay in forum response compared to phone support, and if the problem is urgent, it is recommended that you contact phone support directly so that the issue can be resolved as soon as possible.

The following are the ways to contact local product phone support:

https://support.microsoft.com/en-us/topic/global-customer-service-phone-numbers-c0389ade-5640-e588-8b0e-28de8afeb3f2

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
