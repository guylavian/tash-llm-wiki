---
title: "Migration Active Directory from Windows Server 2012 R2 Standard to Windows Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1262390/migration-active-directory-from-windows-server-201
question_id: 1262390
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Migration Active Directory from Windows Server 2012 R2 Standard to Windows Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1262390/migration-active-directory-from-windows-server-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am planning to migrate the Active Directory from Windows Server 2012R2 Standard to Windows Server 2022, but I have a doubt as to how to do it, considering that on my "old" server the domain functional level is Windows Server 2012 and the Forest functional level is 2003, can someone help me the exact procedure of the necessary steps in this case, the migration is done to a new hardware machine, so it is not an in place upgrade

Best Regards

Sasa Petrov

## Answer (community) — community member

*upvotes: 1 · updated: 2023-04-28*

Hi,

I'd be happy to help you out with your question. Sorry for the inconvenience caused.

Firstly, it is important to ensure that the new hardware machine meets the minimum system requirements for Windows Server 2022 and has adequate resources to support the migration. Once you have verified this, you can proceed with the migration process.

The first step is to install Windows Server 2022 on the new hardware machine and configure it with the necessary networking settings. You will also need to install any required software, such as antivirus or monitoring tools.

Next, you will need to install Active Directory on the new server using the "Add Roles and Features" wizard. Make sure to select the option to install the DNS server role as well. After installing the DNS server role, configure DNS on the new server to replicate with the existing DNS infrastructure.

You should then verify that Active Directory replication is working properly between the old and new servers. Use the "Active Directory Sites and Services" console to verify that all domain controllers are replicating properly. You will also need to transfer the Flexible Single Master Operations (FSMO) roles from the old server to the new server. These roles include the Domain Naming Master, Schema Master, PDC Emulator, RID Master, and Infrastructure Master.

After transferring the FSMO roles, you should update any DHCP and DNS settings to point to the new server as the primary DNS server. Once you have verified that all domain controllers are replicating properly and all services have been migrated to the new server, you can decommission the old server by removing Active Directory from it and demoting it.

It is also important to raise the domain and forest functional levels to the highest level supported by all domain controllers in the domain. Finally, verify that all services and applications are functioning properly after the migration.

I would recommend taking a full backup of the existing Active Directory infrastructure before beginning the migration process. This backup can be used to restore the environment in the event of any issues during the migration. It is also recommended to perform the migration during a maintenance window or non-business hours to minimize disruption to users.

If you have any other questions or need assistance with anything, please don't hesitate to let me know. I'm here to help.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-04-27*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR   

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.   

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-06*

Hi,

Can I upgrade the AD Server from 2012 R2 Datacenter to Server 2022 Standard without any conflict or incompatibility?

Best regards,

VSP

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-08*

never mind, no response here
