---
title: "Exchange 2016 DAG issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/230145/exchange-2016-dag-issue
question_id: 230145
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 DAG issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/230145/exchange-2016-dag-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

I am having issue while trying to add 3rd node in existing DAG. currently i am having a DAG with two nodes in PR site . i have installed another Exchange 2016 node in DR site. When i am trying to add this node in DAG, below error occurred.  

A server-side database availability group administrative operation failed. Error The operation failed. CreateCluster errors may result from incorrectly configured static addresses. Error: The Cluster service couldn't access the Microsoft Failover Cluster Virtual Miniport network adapter. Verify that other network adapters are working and check Device Manager for errors associated with this adapter. If the configuration for this adapter has changed, you may have to reinstall the Failover Clustering feature on this computer. Learn more at http://go.microsoft.com/fwlink/?linkid=3052&kbid=973838.   

I have checked IPv6 and it is enabled as currently all nodes in DAG have IPv6 enabled.  

i also verified exchange trusted subsystem group.  

Local admin group.  

removed the failover cluster role and tried to add node again but remain same.  

Any suggestions.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-15*

Hi @Muhammad Junaid   ,    

I had a  test in my lab, and met the same issue.    

     

And I checked the Device Manager, there is no Microsoft Failover Cluster Virtual Adapter in the Network adapters list.    

So I have to create one:    

- 	Add legacy hardware:    

     

- 	Install the hardware that I manually select from a list:    

     

- 	Choose Network adapters:    

     

- 	Add the Microsoft Failover Cluster Virtual Adapter(It may takes a few seconds to show the list):    

     

Then succeeded adding the DAG member.    

     

So please check if there is the Failover cluster virtual adapter on your problematic server.     

And as AshokM said, if the issue still happens, you can share the DagTasks logs, please remember to cover your personal information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-14*

Hi @Muhammad Junaid  

Could you please provide more information,

1.Detailed version of exchange server, Get-ExchangeServer | select AdminDisplayVersion  

2.IP DAG or IP-Less DAG?

Please check the below,

1.Check whether the OS is same as the node which is part of DAG  

2.Check the network adapter configuration on the node trying to add to the DAG  

3.Are you able to ping the node trying to add and the exchange servers in PR site  

4.Firewall communication between the existing and the new member - cluster port, etc - Check using telnet  

5.Pre-requisites are properly installed on the second node trying to add  

6.Uninstall the windows failover cluster from server manager, reboot the server. Install the FailoverClustering role and then try adding the node to the member  

7.Turn off windows firewall if its on and try  

8.Try disabling IPv6 on the second node temporarily and add it

Disabling IPv6 using registry, HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\TCPIP6\Parameters  

Set DisabledComponents to ffffffff

Please Note: Take the backup of the registry before making changes and be careful in the changes as the improper configuration would lead to other issues.

Also, its not recommended to disable IPv6, this is only for addressing this issue and check if this resolves. I fixed the similar issue in an environment by disabling IPv6 and once the node is added successfully, I re-enabled it again.

If it still fails, please share the error message from the logs %systemdrive%:\ExchangeSetupLogs\DagTasks

As sometimes, it could be an issue with the GPO where there would be a policy to deny the local logins. This will be an issue because a local user account CLIUSR will be created

Computer Configuration -> Windows Settings -> Security Settings -> Local Policies -> User Rights Assignment -> Deny Log on Locally

If the above suggestion helps, please click on "Accept Answer" and upvote it
