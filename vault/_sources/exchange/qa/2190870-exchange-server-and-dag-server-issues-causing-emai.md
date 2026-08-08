---
title: "Exchange Server and DAG Server Issues Causing Email Delays"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190870/exchange-server-and-dag-server-issues-causing-emai
question_id: 2190870
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Exchange Server and DAG Server Issues Causing Email Delays

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190870/exchange-server-and-dag-server-issues-causing-emai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For the past six months, we have been encountering a recurring problem wherein, once a day, our server experiences a significant disruption in functionality. Specifically, users are unable to send emails, as their messages become stuck in the Drafts folder. In order to resolve this, we have been forced to perform a combination of actions, including restarting both the DAG and Exchange servers simultaneously, restarting specific Exchange services, and analyzing queue messages. Unfortunately, this has been a temporary fix and we are unable to determine whether the issue resolves itself or if it is contingent on the services we restart.

Additionally, we have identified the following error event IDs in our logs:

-  Event ID 1564: File share witness resource 'File Share Witness (\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local)' failed to arbitrate for the file share '\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local'. Please ensure that file share '\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local' exists and is accessible by the cluster.

-  Event ID 1069: Cluster resource 'File Share Witness (\witness_srv.Xcompany.local\XCOMPANY-DAG.Xcompany.local)' of type 'File Share Witness' in clustered role 'Cluster Group' failed. Based on the failure policies for the resource and role, the cluster service may try to bring the resource online on this node or move the group to another node of the cluster and then restart it. Check the resource and group state using Failover Cluster Manager or the Get-ClusterResource Windows PowerShell cmdlet.

-  Event ID 1254: The Cluster service failed to bring clustered role 'Cluster Group' completely online or offline. One or more resources may be in a failed state. This may impact the availability of the clustered role.

-  Event ID 4657: Failover Cluster PowerShell cmdlet Get-ClusterNode: An error occurred opening cluster 'XCOMPANY-DAG'.

Given the severity of this issue and its impact on our operations, we urgently seek your assistance in identifying the root cause and implementing a permanent solution. Our team is available for any necessary troubleshooting or to provide additional information that may aid in your investigation.

We appreciate your prompt attention to this matter and look forward to your earliest response.

Thank you for your assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

Hello

Thank you for posting in Microsoft Community forum.

Based on the description, I understand your question is related to the Exchange Server.

Since there are no engineers dedicated to Exchange Server in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.

Questions - Microsoft Q&A

Click the "Ask a Question" button in the upper right corner to post your question and select "Exchange Server" tag.

Thank you for your understanding and support. If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,

Wesley Li
