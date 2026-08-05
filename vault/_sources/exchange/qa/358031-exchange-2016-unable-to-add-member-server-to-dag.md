---
title: "Exchange 2016 unable to add Member server to DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/358031/exchange-2016-unable-to-add-member-server-to-dag
question_id: 358031
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 unable to add Member server to DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/358031/exchange-2016-unable-to-add-member-server-to-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,  

I have a 2 node Exchange 2016 IPless DAG in the same segment running in my environment, after hardware crashed and recovered the DAG was not working and I have to force remove from the cluster. After that I was not able to add it back.  

Error that I am getting:  

WriteError! Exception = Microsoft.Exchange.Cluster.Replay.DagTaskOperationFailedException: A server-side database availability group administrative operation failed. Error The operation failed. CreateCluster errors may result from incorrectly configured static addresses. Error: An error occurred while attempting a cluster operation. Error: Cluster API failed: "AddClusterNode() (MaxPercentage=100) failed with 0x5b4. Error: This operation returned because the timeout period expired". ---> Microsoft.Exchange.Cluster.Shared.ClusterApiException: An error occurred while attempting a cluster operation. Error: Cluster API failed: "AddClusterNode() (MaxPercentage=100) failed with 0x5b4. Error: This operation returned because the timeout period expired" ---> System.ComponentModel.Win32Exception: This operation returned because the timeout period expired  

Tried the following:  

-  removed DAG and recreated DAG.  

-  uninstalled Cluster service  

-  contacted Microsoft Exchange team  

-  Turned off IPV6 (recommended by Microsoft)  

-  contacted Microsoft Cluster team  

-  Tested remote registry connectivity  

-  Tested WMI connectivity  

Nothing above had helped, any suggestions would be greatly appreciated.  

Thanks!

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-04-15*

Hi @Vince Zhuo   ,

Please try the below suggestions,

1.Run Cluster validation report and check for errors at the network level  

2.Try disabling TCP/UDP Checksum offload on the network cards  

3.Turn off windows firewall if its on and try  

4.Try disabling Antivirus if any  

5.Pre-requisites are properly installed on the second node trying to add  

6.Uninstall the windows failover cluster from server manager, reboot the server. Install the FailoverClustering role and then try adding the node to the member  

7.Check at the Group Policy settings for any deny policy on the local logins,  

Computer Configuration/ windows settings / Local Policies / User Rigths Assignment / Deny Log on Locally

If the above suggestion helps, please click on "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-16*

Hi @Vince Zhuo  ，    

Aside from the error message, have you checked if there's any relevant events logs in the Event Viewer?    

Besides, if you have any anti-virus software running in the environment, it's suggested to try temporarily removing it and check if there would be any difference. Here's a similar thread which was finally resolved by removing the AV:    

Exchange 2010 Add server to DAG failed.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
