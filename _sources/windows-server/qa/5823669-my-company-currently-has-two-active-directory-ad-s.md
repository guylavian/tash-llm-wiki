---
title: "My company currently has two Active Directory (AD) servers, and we need to add a new AD server to the domain. How do I do this?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5823669/my-company-currently-has-two-active-directory-ad-s
question_id: 5823669
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Independent Advisor"]
---
# My company currently has two Active Directory (AD) servers, and we need to add a new AD server to the domain. How do I do this?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5823669/my-company-currently-has-two-active-directory-ad-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The specific situation is as follows:

-  The company has one forest and domain, and two Active Directory (AD) servers. These two servers communicate and synchronize data.

-  One server is deployed in the local data center, and the other is deployed on Azure Cloud.

-  The forest and domain functional levels are both Windows Server 2008 R2. Both servers are running Windows Server 2016 Standard.

-  Because there are computers running Windows XP and Windows 7 in the domain, upgrading the forest and domain functional levels is not possible. Windows Server 2008 R2 must be retained.

-  The company now needs to add a new AD server on Huawei Cloud and join it to the company's forest and domain.

The main questions are:

-  How do I determine which operating system the new server should run? Excluding Windows Server 2016.

How should I choose between Windows Server 2019, 2022, and 2025?

-  How do I determine how to allocate CPU, memory, disk, and network resources during system deployment?

-  How to determine which operating system is best suited for running a domain controller without conflicts or incompatibility?

-  What preparations should be made before deploying a new server?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-19*

Hi 宋宇杰,

How is your issue going? Has it been resolved yet? If it has, please consider accepting the answer as it helps others sharing the same problem benefit too. Thank you :)

VP

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-16*

Hi 宋宇杰,

Your assumption that upgrading forest and domain functional levels directly breaks Windows XP and Windows 7 compatibility is a common misconception. Functional levels govern backend directory features and strictly dictate which server operating systems are permitted to act as Domain Controllers, not which client systems can authenticate. The actual threat to legacy client connectivity comes from default security protocols on newer server operating systems, such as the deprecation of SMBv1 and RC4 Kerberos encryption. For Windows XP to authenticate against newer domain controllers, you must often ensure RC4 is enabled via the Network security: Configure encryption types allowed for Kerberos policy, located at Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options. You can safely raise your functional level to Windows Server 2016 since your existing servers run that operating system, though maintaining these outdated protocols to support legacy clients introduces significant security vulnerabilities to your infrastructure.

When selecting the operating system for the new Huawei Cloud server, Windows Server 2025 is completely unsupported unless you raise the functional levels, as it enforces a strict minimum functional level requirement of Windows Server 2016. If you remain on the 2008 R2 functional level, your valid options outside of 2016 are Windows Server 2019 and Windows Server 2022. Windows Server 2022 is the optimal choice for your environment, as it offers the longest remaining lifecycle and seamlessly integrates into a 2008 R2 functional level while maintaining compatibility with legacy clients, provided the necessary legacy encryption types and protocols are manually permitted.

Allocating hardware resources for a domain controller requires focusing on memory and storage integrity rather than raw processor speed. Active Directory attempts to load the entire database file, located at C:\Windows\NTDS\ntds.dit, into system RAM to process queries instantly without relying on slower disk reads. You should provision the virtual machine with at least two virtual CPUs and enough memory to exceed the size of your current database, with four to eight gigabytes serving as a typical starting point for medium environments. It is highly recommended to provision a separate virtual disk dedicated exclusively to the NTDS database, transaction logs, and the SYSVOL folder. Disabling host-level write caching on this secondary data disk is absolutely crucial to prevent Active Directory database corruption during an unexpected hypervisor reboot or cloud failure.

Preparing your cloud environment before deployment requires establishing secure routing and defining the logical network topology. You must first configure a persistent site-to-site VPN or direct interconnect between Huawei Cloud and your existing environments to guarantee continuous replication traffic. Next, assign a static IP address to the new server and configure its primary DNS server to point to one of your existing local or Azure Domain Controllers, allowing it to locate the domain during the promotion process. Finally, use the Active Directory Sites and Services console to create a new site representing the Huawei Cloud location, bind the new cloud network subnets to it, and configure site links to ensure future cloud workloads authenticate locally rather than traversing the wide area network back to your primary data center.

Hope this answer brought you some useful information. If it did, please hit “accept answer”. Should you have any questions, feel free to leave a comment.

VP

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-16*

-  Choosing the operating system version

From the provided information:

-  Forest and domain functional levels: Windows Server 2008 R2

-  Existing domain controllers: Windows Server 2016

Key points from the context:

-  Forest functional level controls which domain controller OS versions are allowed, not client OS versions like Windows XP/7. Older clients can still authenticate to newer DCs as long as protocols they need are enabled.

-  A Windows Server 2016 forest functional level supports Windows Server 2016 domain controllers and later versions of Windows Server.

-  For new forests, the minimum domain and forest functional level that can be set for Windows Server 2025 DCs is Windows Server 2016, and existing domains must already be at Windows Server 2016 domain and forest functional levels to promote a Windows Server 2025 domain controller.

Relevant excerpts:

-  “Windows Server 2012. This forest functional level supports Windows Server 2012 domain controllers and domain controllers that are running later versions of the Windows Server operating system.”

-  “Windows Server 2016. This forest functional level supports only Windows Server 2016 domain controllers and domain controllers that are running later versions of the Windows Server operating system.”

-  “Existing domains must be at the Windows Server 2016 domain and forest functional levels to promote a Windows Server 2025 domain controller.”

Given that the current forest/domain functional level is Windows Server 2008 R2, the context only explicitly describes support matrices for 2008, 2008 R2, 2012, 2012 R2, 2016, and 2025, and explicitly states that Windows Server 2025 DCs require at least Windows Server 2016 functional level. It does not provide a complete compatibility matrix for adding Windows Server 2019 or 2022 DCs into a 2008 R2 forest.

From the context, the only fully documented and safe pattern is:

-  Newer DCs (like Windows Server 2025) can only be added once domain/forest functional levels are at least Windows Server 2016.

Because the current forest/domain functional level is Windows Server 2008 R2 and must be retained, and the context does not explicitly state that Windows Server 2019 or 2022 domain controllers can be added to a 2008 R2 forest, the only fully supported guidance in the context is to continue using a DC OS that is already known to work in the current environment: Windows Server 2016.

Therefore, based strictly on the provided documentation, the recommended and documented-safe choice is to deploy the new domain controller on Windows Server 2016, matching the existing DCs and the current functional level behavior described.

-  Sizing CPU, memory, disk, and network

The context does not provide any concrete sizing guidance (CPU, RAM, disk, or network throughput) for domain controllers. It only describes functional levels, deployment steps, and upgrade patterns. No numeric or qualitative sizing rules are given.

Therefore, no specific recommendations for CPU, memory, disk, or network allocation can be derived from the provided material.

-  Determining OS suitability and avoiding conflicts

From the context on functional levels:

-  “Forest functionality enables features across all the domains in your forest.”

-  “This forest functional level supports Windows Server 2012 domain controllers and domain controllers that are running later versions of the Windows Server operating system.”

-  “Windows Server 2016. This forest functional level supports only Windows Server 2016 domain controllers and domain controllers that are running later versions of the Windows Server operating system.”

-  “After the forest functional level is raised, domain controllers that are running earlier operating systems cannot be introduced into the forest.”

And from the article on raising functional levels:

-  “To activate the newest forest-wide features, all the domain controllers in the forest must be running the Windows Server operating system version that corresponds to the desired forest functional level… Generally, the changes to the domain and forest functional levels are irreversible.”

To avoid conflicts or incompatibility when choosing an OS for a new domain controller, the context supports these principles:

-  The OS version of any new domain controller must be compatible with the current forest and domain functional levels.

-  Raising forest/domain functional levels restricts which DC OS versions can be added later; once raised, older DC OS versions cannot be introduced.

-  When planning to introduce Windows Server 2025 domain controllers, the environment must already be at Windows Server 2016 functional levels.

Applied to this scenario, and constrained by the context:

-  Because the forest/domain functional level is Windows Server 2008 R2 and must remain there, and because the only explicitly documented requirement for newer DCs (Windows Server 2025) is that they need at least Windows Server 2016 functional levels, the safest documented choice is to use the same OS version as existing DCs (Windows Server 2016) to avoid any functional-level compatibility issues.

-  Preparations before deploying a new server

The context describes general patterns for adding a new domain controller and upgrading domain controllers:

-  “Join the new Windows Server to your forest. Restart when you're prompted.”

-  “Sign in to the new Windows Server with a domain admin account.”

-  “In Server Manager, under Add Roles and Features, install Active Directory Domain Services on the new Windows Server. This action automatically runs adprep on the earlier version forest and domain.”

-  “In Server Manager, select the yellow triangle. From the drop-down, select Promote the server to a domain controller.”

-  “On the Deployment Configuration screen, select Add a domain controller to an existing domain and click next.”

-  “On the Domain Controller options screen, enter the Directory Services Restore Mode (DSRM) password and select Next.”

And for new DCs in Azure (which is conceptually similar to adding a DC in another cloud):

-  Install AD DS using Server Manager.

-  Promote the server as “Add a domain controller to an existing domain”.

-  Ensure DNS server and Global Catalog options are selected as required.

From these, the preparatory steps supported by the context are:

-  Ensure the new server is joined to the existing domain before promotion.

-  Ensure appropriate domain admin credentials are available to perform the promotion.

-  Plan DNS: domain controllers are recommended to host DNS; Microsoft recommends DCs provide DNS for high availability.

-  Plan DSRM password according to organizational policy.

-  Verify that the OS version chosen for the new DC is compatible with the current forest and domain functional levels, and that introducing it does not require raising functional levels beyond what is acceptable.

Because the context does not provide more detailed pre-deployment checks (such as site topology, replication, or capacity planning), only these high-level preparations can be stated.

References:

-  Core network components

-  How to raise Active Directory domain and forest functional levels

-  Identifying your functional level upgrade

-  Install a New Windows Server 2012 Active Directory Forest (Level 200)

-  Install a new Active Directory forest using Azure CLI

-  Upgrade domain controllers to a newer version of Windows Server
