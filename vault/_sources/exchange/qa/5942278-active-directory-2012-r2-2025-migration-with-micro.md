---
title: "“Active Directory 2012 R2 → 2025 Migration with Microsoft 365 Sync Issues”"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5942278/active-directory-2012-r2-2025-migration-with-micro
question_id: 5942278
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# “Active Directory 2012 R2 → 2025 Migration with Microsoft 365 Sync Issues”

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5942278/active-directory-2012-r2-2025-migration-with-micro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

We are implementing a project to migrate our Active Directory (Windows Server 2012 R2) and Exchange 2010 mailboxes to Windows Server 2025 + Microsoft 365 (Exchange Online, Teams, SharePoint, OneDrive). During assessment, we identified several issues and would like guidance:

-  UPN / Domain Mismatch

-  AD domain: `EIC.COM`

-  Microsoft 365 tenant domains: `eic.com.et` and `eic-et.com`

-  Question: What is the best practice to align AD UPNs with Microsoft 365 without breaking legacy SSO apps that still use `******@EIC.COM`?

-  Identity Sync

-  We already have ~600 cloud‑only users in Microsoft 365.

-  Question: Should we use Soft Match (UPN) or Hard Match (ImmutableID) to merge these accounts with AD users? Any recommended PowerShell scripts for bulk operations?

-  Mailbox Migration

-  Exchange 2010 SP3 with ~1,645 mailboxes (Windows 2008 R2).

-  Question: What is the safest migration path (hybrid vs staged) to Exchange Online, considering bandwidth (~500 Mbps) and risk of data loss?

-  Functional Level Upgrade

-  Current AD functional level: Windows Server 2012 R2.

-  Question: Can we raise directly to 2012 R2 forest/domain functional level and then introduce Windows Server 2025 DCs without staged upgrades? Any risks with legacy apps?

-  Group Policy Replication

-  Concern: SYSVOL replication (FRS vs DFSR).

-  Question: How do we confirm DFSR is active and migrate if still using FRS before introducing 2025 DCs?

-  Legacy Dependencies

-  Some 2003/2008 apps rely on AD authentication.

-  Question: How can we safely test and maintain compatibility during UPN changes and AD functional level   

   upgrade?

-  Bandwidth & Migration Scheduling

-  Question: What are best practices to handle mailbox + SharePoint/OneDrive migration with limited bandwidth? Should we schedule off‑hours or throttle migration batches?

-  Security & Compliance

-  Plan includes MFA, Conditional Access, DLP, Defender for Office 365 P2.

-  Question: Any recommended order of enabling these features to avoid user disruption during migration?

We would appreciate step‑by‑step guidance or references to Microsoft documentation for these issues. Thank you in advance for your support.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2026-07-09*

Hi @biruhken ayana  

Thank you for reaching out. 

Regarding to your concerns: 

For UPN and domain mismatch 

Based on my research, to support a consistent hybrid identity and Single Sign-On experience, you may consider aligning on-premises UPNs with verified custom domains in Microsoft 365. This typically involves adding Microsoft 365 verified domains (such as eic.com.et or eic-et.com) as additional UPN suffixes in Active Directory. However, if legacy SSO applications depend on the existing EIC.COM format, changing UPNs may impact authentication and application compatibility. 

In this scenario, the suitable approach depends on whether EIC.COM can be verified as a custom domain in the Microsoft 365 tenant. If EIC.COM can be verified, it may be retained as the primary UPN suffix, allowing users to continue using their existing EIC.COM sign-in format. If EIC.COM cannot be verified, users may need to be transitioned to a verified Microsoft 365 domain for a consistent Microsoft 365 sign-in experience. 

Before making broader changes, you may need to validate the impact through a pilot group and identify any dependencies on the existing UPN format. The outcome can vary depending on how the legacy applications authenticate users, such as through LDAP, Kerberos, claims-based SSO, or hard-coded UPN values.  

References:  

Prepare for directory synchronization 

Troubleshoot UPN changes in Microsoft Entra ID 

Regarding Identity Sync  

For existing cloud-only users, the appropriate matching approach might depend on how your current cloud identities align with the corresponding on-premises Active Directory accounts. From what I understand, Microsoft Entra Connect supports both Soft Match and Hard Match when associating existing cloud identities with on-premises objects. Where UPNs and primary SMTP addresses are already consistent between Active Directory and Microsoft 365, Soft Match can often provide a simpler path for identity association. Where explicit control over identity mapping is required, Hard Match may be used to link specific cloud users to their corresponding on-premises accounts through ImmutableID.  

Currently, I have not identified any Microsoft-published documentation that provides a standardized, Microsoft-recommended PowerShell solution for performing bulk Soft/Hard Match operations. Looks like bulk matching is generally handled through custom scripting, and any such approach should be thoroughly validated in a pilot environment before being deployed at scale. 

Reference:  Configure Microsoft Entra Connect for an existing tenant - Microsoft Entra ID | Microsoft Learn 

Related to Mailbox Migration  

As far as I know, for an Exchange 2010 environment with approximately 1,645 mailboxes, Hybrid Migration is generally the most appropriate migration path because it supports phased mailbox moves, coexistence, shared address lists, free/busy functionality, and reduced user disruption during migration.  

The suitability of a 500 Mbps connection might depend on mailbox sizes, total data volume, source Exchange performance, and migration batch design. You could consider running a pilot migration to establish realistic throughput expectations before large-scale migration. 

Reference: 

Decide on a migration path in Exchange Online 

Functional Level Upgrade 

Based on my research, it is not possible to directly introduce Windows Server 2025 domain controllers into an Active Directory environment that remains at the Windows Server 2012 R2 Forest Functional Level and Domain Functional Level. Before promoting Windows Server 2025 domain controllers, the Forest Functional Level and Domain Functional Level must be raised to at least Windows Server 2016. Microsoft does not support adding new Windows Server 2025 domain controllers to a domain operating below the Windows Server 2016 functional level. 

The only exception is when performing an in-place upgrade of an existing supported domain controller to Windows Server 2025. However, for introducing new Windows Server 2025 domain controllers into the environment, the domain and forest functional levels must first meet the minimum supported requirement. 

Regarding legacy applications, although raising the Functional Level generally has minimal impact because existing Active Directory features remain supported, there are still some potential risks that should be considered, such as 

-  Some older applications may rely on deprecated Active Directory features or specific behaviors that were available in earlier Functional Levels. 

-  Applications that perform complex LDAP queries or bind directly to specific domain controllers may experience unexpected issues. 

-  Certain legacy systems may have hardcoded assumptions about the environment, which could lead to compatibility problems after the upgrade. 

-  Once the Functional Level is raised, it cannot be lowered again. This makes proper testing important before proceeding. 

Reference: 

Upgrade Active Directory Domain Services to Windows Server 2025 

For Group Policy Replication  

To confirm whether DFSR is active, you can use the DFSRMIG tool to verify the current SYSVOL replication state and migration status before introducing Windows Server 2025 domain controllers. 

References: 

Migrate SYSVOL replication from FRS to DFS Replication 

dfsrmig | Microsoft Learn 

Legacy Dependencies  

With legacy applications, I would recommend reviewing and testing them before implementing UPN changes, functional level changes, or domain controller modernization activities. Particular attention should be given to applications relying on LDAP authentication, Kerberos, NTLM, service accounts, SPNs, or hard-coded domain and UPN references, as compatibility requirements can vary between environments. 

Regarding Bandwidth and Migration Scheduling 

With a large volume of mailboxes, SharePoint, and OneDrive data to migrate, I recommend adopting a phased migration approach. Migration performance can be affected by several factors, including available bandwidth, mailbox size, source server performance, and migration configuration. 

To set realistic expectations and minimize risk, I strongly advise starting with a pilot migration to measure actual throughput and identify any potential bottlenecks before scaling up. It is also recommended to schedule larger migration batches during off-peak hours and, where possible, separate mailbox migrations from SharePoint and OneDrive migrations to reduce the impact on end users. 

For Security and Compliance Considerations 

I would recommend enabling security features in a phased manner to minimize user disruption. You can start by creating Emergency Access accounts and blocking legacy authentication. Next, enforce MFA for administrative accounts first, followed by a gradual rollout of MFA for all users. Conditional Access policies can then be evaluated in Report-only mode before enforcement to assess potential impact on user sign-ins. Defender for Office 365 protection policies may be introduced after identity and MFA adoption have stabilized. Conditional Access and DLP policies can be enforced in later phases once the environment has reached a steady operational state.  

Please note that this summary is based on my own findings and may not fully address your concerns. To help you reach your goal more effectively, I recommend engaging with Tech Community Discussion | Microsoft Community Hub for a deeper technical dive or to connect with individuals who have relevant experience and expertise. Some approaches may behave differently or be restricted depending on your specific environment and configuration. These forums include many experienced developers and Microsoft specialists who can assist with troubleshooting and guidance.     

Apologies for redirecting you to the related development team support. As moderators in this community, we do not have access to your specific tenant configuration, and my testing environment is limited. Therefore, my guidance is based on available Microsoft documentation and resources. That said, I’ll do my best to provide additional insight where possible.  

I hope this helps. 

If you have any additional concerns, feel free to comment below. I would be more than happy to assist. 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
