---
title: "can't join exchange dag"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2265321/cant-join-exchange-dag
question_id: 2265321
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# can't join exchange dag

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2265321/cant-join-exchange-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can't join an on-prem exch 2019 serve to the DAG. The error says " the server is already joined the DAG". I previously removed the server from the DAG, changed the IP address to a different subnet. Now the Cluster service can't start and it can't rejoin to the DAG. I suspect the previous operation to remove from the DAG was not clean. There is  some corruption in AD. Does anyone know where to look for corruption?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-13*

Get-DatabaseAvailabilityGroup DAG_name | Format-List shows that this server isnot a member of the dag.

Get-Cluster & get-ClusterNode returns error: The cluster service is not running.  Make sure that the service is running on all nodes in the cluster.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-13*

Hi alan g,

Thank you for posting your question in the Microsoft Q&A forum.

If the cluster service is running, the server may have issues to join the cluster and work as dag member as expected.

 Here are some suggestions for you:

-  Please use the following command to check if the server is still a member of DAG and cluster node:

Get-DatabaseAvailabilityGroup DAG_name | Format-List

Get-Cluster

Get-ClusterNode

-  If previous server still is a DAG member or cluster node, please use the following command from DAG again. In general, it could be removed from cluster at the same time:   Remove-DatabaseAvailabilityGroupServer -Identity DAG_name -MailboxServer servername   If the server is not a DAG member but still show as the cluster node. We can use the following command to evict it from a failover cluster:   Clear-ClusterNode -Name node_name -Force

-  Please make sure that no network or port limitation between Exchange server and Exchange server, or between Exchange server and DCs. Otherwise, this will cause issues for Exchange communication or services cannot run successfully.

-  If you have any third-party scan tool or antivirus software is installed on Exchange servers, please perform Exchange related folder, file and process exclusion according to the following document. This could avoid any file lock or service interference when Exchange function:

Running Windows antivirus software on Exchange servers | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
