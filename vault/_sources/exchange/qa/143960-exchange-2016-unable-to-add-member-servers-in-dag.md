---
title: "Exchange 2016 Unable to add Member Servers in DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143960/exchange-2016-unable-to-add-member-servers-in-dag
question_id: 143960
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Unable to add Member Servers in DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143960/exchange-2016-unable-to-add-member-servers-in-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

While adding Exchange member server in new DAG getting below error  

Access is denied. (Exception from HRESULT: 0x80070005 (E_ACCESSDENIED))  

ERROR  

A server-side database availability group administrative operation failed. Error The operation failed. CreateCluster errors may result from incorrectly configured static addresses. Error: An error occurred while attempting a cluster operation. Error: Cluster API failed: "CreateCluster() failed with 0x42a. Error: The service has returned a service-specific error code". [Server:]  

Microsoft.Exchange.Cluster.Replay.DagTaskOperationFailedException: A server-side database availability group administrative operation failed. Error The operation failed. CreateCluster errors may result from incorrectly configured static addresses. Error: An error occurred while attempting a cluster operation. Error: Cluster API failed: "CreateCluster() failed with 0x6ba. Error: The RPC server is unavailable". ---> Microsoft.Exchange.Cluster.Shared.ClusterApiException: An error occurred while attempting a cluster operation. Error: Cluster API failed: "CreateCluster() failed with 0x6ba. Error: The RPC server is unavailable" ---> System.ComponentModel.Win32Exception: The RPC server is unavailable  

This Exchange Servers are not part of any cluster and Network Teaming is also not configured. Prestage of DAG is also done. Solution for the same would be appreciated.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-11-01*

Hi,  

Please find below my suggestions,  

For permission error, Check if the account you are using is a member of "Organization Management"  

For error CreateCluster() failed with 0x42a. Error: The service has returned a service-specific error code  

-  Check if IPv6 is enabled on all servers  

-  Check the GPO for any deny policy on the local logins because a local user account CLIUSR will be created  

Computer Configuration -> Windows Settings -> Security Settings -> Local Policies -> User Rights Assignment/Security Options -> Deny Log on Locally/Deny access to this computer from the network  

For error CreateCluster() failed with 0x6ba. Error: The RPC server is unavailable  

-  Check if there are any network firewall communication issues. Could be possible if the session is getting established on a different interface if you have multiple NIC's on the server  

-  This  error could be due to reachability or service is not listening on the server. Telnet on port 135 and check if its allowed. also, dynamic RPC ports to be allowed along with the DAG port  

-  Temporarily disable Windows firewall/AV on the server  

If the response is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-27*

Hello, in my case, was resolved doing the following: Adding Full Permissions to the Exchange Trusted Subsystem onto the CNO of the DAG:    

    

Regards,    

Franklin

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-31*

Greetings,  

We are still facing this issue, Just for testing when we are trying to configure failover cluster, below is the error which we are receiving  

"You do not have administrative privilege on the server"  

Note -: We have tried to configure from all the administrator accounts.  

Solution for the same would be really appreciated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-30*

@ReBIT IT       

Hi,    

I noticed that you mentioned "Network Teaming is also not configured".    

Did you configured a valid ip address for the DAG?    

If so,please make sure the servers are in the same subnet and have access to it.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-29*

I suggest the following troubleshooting steps    

-  Make sure that, you started EMS with elevated privileges (Run as Administrator)    

-  Make sure that, "Exchange Trusted Subsystem" is a member of the local Administrator Group    

-  Try and give the new mailbox Server permission to the CNO Object. See the Technet Article for instructions: pre-stage-dag-cnos
