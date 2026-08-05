---
title: "Exchange 2019 on Azure VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1386557/exchange-2019-on-azure-vm
question_id: 1386557
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 on Azure VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1386557/exchange-2019-on-azure-vm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We want to install Exchange 2019 on an Azure VM, however I'm not sure whether it's totally supported for production use. If so, what is the advice for DAG IP-based vs IP-less?  I've also read Exchange for Virtualization, and although it discusses Storgae, Snapshots, Processors, and so on, there are no particular deployment best practices to follow on Azure (except Dev/test on Azure).

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-10*

@Chandra Sekhar,

Welcome to our Q&A forum!

Microsoft Exchange Server 2019 is supported for production use on Azure VMs. 

For DAG deployment, you can choose between IP-based and IP-less DAGs. IP-based DAGs are recommended for most scenarios, while IP-less DAGs are recommended for scenarios where the DAG members are in different subnets or sites.

Regarding deployment best practices, Microsoft recommends using Azure Premium Storage for Exchange Server 2019 on Azure VMs. Additionally, it is recommended to use Azure Site Recovery for disaster recovery and high availability.

https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/solutions/business-critical-apps/exchange/vmw-microsoft-exchange-server-2019-on-vmware-best-practices.pdf

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-09*

Exxchange Server 2019 is supported as an Azure-VM as long as all supportability requirements are met. => see Note

`Deployment of Exchange 2016 or Exchange 2019 on Infrastructure-as-a-Service (IaaS) providers is supported if all supportability requirements are met. In the case of providers who are provisioning virtual machines, these requirements include ensuring that the hypervisor being used for Exchange virtual machines is fully supported, and that the infrastructure to be utilized by Exchange meets the performance requirements that were determined during the sizing process. Deployment on Microsoft Azure virtual machines is supported if all storage volumes used for Exchange databases and database transaction logs (including transport databases) are configured for Azure Premium Storage.`

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/virtualization?view=exchserver-2019#requirements-for-hardware-virtualization

Decision to implement a DAG (Database Availability Group) with IP-based vs IP-less configurations depends on various factors (organization's specific requirements, infrastructure, and operational preferences)

Pros for each:

-  IP-Based DAG

-  Granular Control: IP-based DAG provides more granular control over which databases and network interfaces are used for replication and failover. You can configure specific IP addresses for each database copy.

-  Isolation:Each database copy has its own dedicated IP address, which can help isolate issues if one database copy experiences problems. This can simplify troubleshooting.

-  Complex Network Configurations: If your network environment is complex, with multiple subnets, routing rules, or specific network requirements, an IP-based DAG can provide more flexibility in handling these scenarios.

-  Custom Routing: You can use routing rules to control how replication traffic flows, which can be useful in scenarios where you want to optimize network utilization or prioritize certain traffic.

-  IP-Less DAG

-  Simplified Configuration: IP-less DAG configurations simplify the overall configuration and reduce the number of IP addresses required. This can make the setup process more straightforward.

-  Reduced IP Address Management: You don't need to manage as many IP addresses, which can reduce the administrative overhead associated with IP management, especially in larger environments.

-  Ease of Scaling: IP-less DAGs can be easier to scale because you don't have to allocate and manage additional IP addresses for each new database copy.

-  Smaller Attack Surface: With fewer IP addresses exposed, there may be a smaller attack surface, potentially enhancing security.

In general

-  IP-less will be easier to set-up and manage for a smaller organization

-  IP-based DAGs will allow for complex network requirements, allow more control and specific isolation requirements that suit larger enterprises.

And do check for support of your scenario with 3rd party providers like backup, ... (especialy about Administrative Access Point=AAP).

Afaik when you choose your architecture, you must stick with it, else create a new DAG.

So the answer is 'it depends' on your objectives.

You can read about Exchange 2019 preferred architecture here: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/preferred-architecture-2019?view=exchserver-2019

An rather old post regarding your question is here: https://social.technet.microsoft.com/wiki/contents/articles/48850.exchange-2013-ip-less-dag-vs-dag-with-ip.aspx

Regards
