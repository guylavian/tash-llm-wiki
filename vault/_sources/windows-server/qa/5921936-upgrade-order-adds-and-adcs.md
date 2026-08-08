---
title: "Upgrade Order ADDS and ADCS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5921936/upgrade-order-adds-and-adcs
question_id: 5921936
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# Upgrade Order ADDS and ADCS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5921936/upgrade-order-adds-and-adcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently running two 2012 R2 domain controllers and a 2012 R2 root CA. I’m planning to upgrade both ADDS and ADCS to Server 2022, and I want to replace the current root CA with a 2-Tier PKI setup. My question is: which one should I upgrade first, and what's the best practice here?

-  Option 1: AD first, then CA. (Pros/cons?)

-  Option 2: CA first, then AD. (Pros/cons?) Any impact?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-20*

Hi Wai Yan Oo,

Has your issue been resolved yet? If it has, please consider accepting the answer as it helps others sharing the same problem benefit too. Thank you :)

VPHAN

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-17*

Wai Yan Oo there is no article explicitly titled "Upgrade AD before CA," this sequence is the mandatory architectural standard derived directly from two official Microsoft document sets: the "Active Directory Certificate Services Migration Guide" and the "Upgrade Domain Controllers to a newer version of Windows Server" documentation. Microsoft's infrastructure framework operates on a strict dependency hierarchy where the foundational identity layer must be fully modernized before updating the tier-one security applications that rely on it.

The official Active Directory Certificate Services Migration Guide explicitly states that an Enterprise Certificate Authority requires a functioning Active Directory environment because it writes its core operational data directly into the Active Directory Configuration partition. When you follow the official deployment and migration steps for a Certificate Authority, Microsoft assumes the underlying directory is already stable and running at your target functional level. Attempting to migrate the Certificate Authority to Windows Server 2022 first violates this dependency chain because the legacy 2012 R2 directory schema lacks the updated definitions required to securely support a Server 2022 Public Key Infrastructure.

Also, the Microsoft documentation for upgrading domain controllers highlights that introducing Windows Server 2022 domain controllers fundamentally alters the forest via the adprep.exe utility. Microsoft emphasizes that schema extensions and domain functional level raises introduce significant backend changes, such as deprecating older cryptographic protocols and enforcing stricter Kerberos authentication defaults. Because your Certificate Authority is deeply integrated into the domain infrastructure, Microsoft's architectural best practice dictates that these directory-level changes must be completed and fully replicated before deploying a new Enterprise CA, ensuring your certificate services are not unpredictably disrupted by underlying directory shifts.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-16*

Hi Wai Yan Oo,

Upgrading your Active Directory Domain Services before migrating your Active Directory Certificate Services is the definitively correct approach. Introducing Windows Server 2022 domain controllers requires extending the directory schema, governed by the adprep.exe utility, which updates the dictionary of objects your network understands. Your Certificate Authority stores crucial components like Certificate Templates and Revocation Lists within the Configuration partition, specifically located at the LDAP path CN=Public Key Services,CN=Services,CN=Configuration. By upgrading the domain first, you ensure this central, forest-wide registry operates on modern code with up-to-date security defaults before you introduce a new two-tier infrastructure.

Deploying a Server 2022 PKI onto a 2012 R2 directory risks severe architectural instability. Subsequent domain controller upgrades will introduce stricter cryptographic standards, such as the deprecation of older encryption types and stricter Kerberos ticketing enforcement. These structural changes could unpredictably break your established certificate enrollment and authentication workflows if the PKI is built before the directory is fully modernized.

Your most reliable strategy is to introduce the new 2022 domain controllers, transfer the Flexible Single Master Operations roles, and completely decommission the 2012 R2 servers to successfully raise your functional levels. Once directory replication is fully stable, you can safely deploy your new offline Root CA and Enterprise Subordinate CA on Server 2022, publish the new PKI data into the modernized directory, and phase out the legacy infrastructure in a controlled manner.

Hope this answer has brought you some useful information. If it did, please hit “accept answer”. Should you have any questions, feel free to leave a comment. 

VPHAN

## Answer (community) — community member

*upvotes: 0 · updated: 2026-06-16*

Best practice is to upgrade Active Directory Domain Services (AD DS) first, then replace/upgrade the Certification Authority (CA) and move to the new 2‑tier PKI.

Reasoning and implications based on the provided material about domain controller upgrades:

-  AD DS should be modernized first

-  Windows Server 2012 R2 domain controllers can be upgraded in‑place to newer versions following supported upgrade paths and guidance.

-  The AD DS upgrade is foundational: domain controllers provide authentication, authorization, and directory services that the PKI depends on (for example, for publishing CRLs, AIA locations, and certificate templates in AD, and for authenticating domain accounts running CA services).

-  The guidance for upgrading domain controllers emphasizes getting domain controllers onto newer Windows Server versions first and handling known issues in AD DS installation and behavior before layering other services on top.

-  Why not CA first?

-  A 2012 R2 CA depends on the existing AD DS forest and domain. If domain controllers are later upgraded and schema, security defaults, or deprecated cryptography settings change, this can affect how certificates are requested, issued, or validated.

-  Windows Server 2012 and later introduce security changes (for example, disabled DES, stricter defaults like AllowNT4Crypto disabled) that can affect older or less secure clients and services. Upgrading AD DS first makes it easier to validate domain‑wide authentication and crypto behavior before introducing a redesigned PKI.

-  Option 1: AD first, then CA (recommended)
   Pros:

-  Ensures the directory environment is on the target OS level and stable before introducing a new 2‑tier PKI design.

-  Allows handling AD DS upgrade issues (such as known AD DS installation and virtualization issues) independently of PKI changes.

-  Once domain controllers are on newer Windows Server versions, new PKI servers can be joined to a fully updated domain, using current defaults and security baselines.

-  Reduces risk of having to re‑work PKI configuration if AD DS behavior or security defaults change after the CA migration.

Cons:

-  Requires careful planning of domain controller upgrade paths and known issues first, then a separate project for PKI redesign.

-  Option 2: CA first, then AD
   Pros:

-  None that are clearly supported by the provided material compared to the AD‑first approach.

Cons:

-  New PKI design would be built on an older AD DS foundation that is about to change, increasing the chance of follow‑up adjustments.

-  Potential interaction with deprecated cryptography and security defaults when AD DS is later upgraded (for example, DES disabled by default, AllowNT4Crypto behavior), which could affect certificate usage or older clients.

Summary:

-  Upgrade and modernize AD DS/domain controllers first (following supported in‑place upgrade paths and known‑issue guidance), validate domain health and authentication.

-  Then deploy the new 2‑tier PKI (new root CA and issuing CAs) on the upgraded environment and decommission the old 2012 R2 root CA in a controlled manner.

References:

-  Upgrade Domain Controllers to Windows Server 2012 R2 and Windows Server 2012
