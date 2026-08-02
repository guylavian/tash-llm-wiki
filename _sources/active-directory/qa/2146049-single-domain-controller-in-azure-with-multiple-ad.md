---
title: "Single domain controller in Azure with multiple AD sites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2146049/single-domain-controller-in-azure-with-multiple-ad
question_id: 2146049
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Single domain controller in Azure with multiple AD sites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2146049/single-domain-controller-in-azure-with-multiple-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the process of collapsing multiple AD domains into a single AD domain.  we have 5 locations. My plan was to have a multi-site setup with a DC at each site.  However, I now need to pivot to a single Azure VM Domain Controller and no on-premises DCs. How do I implement this or is it even possible?

Thanks,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-13*

You can consolidate multiple on-premises AD domains into a single domain with an Azure VM acting as the sole Domain Controller (DC). However, moving to a single cloud-hosted DC comes with considerations regarding connectivity, performance, and redundancy. Here is an approach you can use:

-  Consolidate the AD domains
   Before moving to Azure, complete the domain consolidation:

-  Identify and migrate all objects (users, computers, groups) from the multiple domains into the target domain.

-  Resolve any conflicts (e.g., duplicate usernames or group names).

-  Update group policies, scripts, and applications to align with the new domain structure.

-  Configure Azure networking
   Create an Azure virtual network:

-  Ensure the Azure VM is deployed in a VNet that allows communication with all your remote locations.

-  Establish a secure connection between your on-premises networks and Azure. This can be done by using either a site-to-site VPN or ExpressRoute.

-  Configure the virtual network to use on-premises DNS resolvers.

-  Deploy the Azure VM Domain Controller
   Create an Azure VM:

-  Deploy a Windows Server VM in Azure that meets the requirements for a DC.

-  Install the Active Directory Domain Services (AD DS) role.

-  Promote the VM to a DC for the consolidated domain and configure it as a DNS server

-  Modify the DNS configuration of the VNet to point to the newly promoted VM as the DNS resolver

-  Set the Azure VM DC as the primary DNS server for all clients in your environment.

-  Configure DNS forwarding if needed.

-  Decommission On-Premises DCs
   After verifying that all authentication and services work with the Azure-hosted DC:

-  Demote the on-premises DCs.

-  Remove them from the domain.

Btw. you should deploy another Azure VM-hosted DC for redundancy reasons.

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
