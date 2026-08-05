---
title: "How to Migrate Child Domain Controller from 2012 R2 To 2022?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1301638/how-to-migrate-child-domain-controller-from-2012-r
question_id: 1301638
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# How to Migrate Child Domain Controller from 2012 R2 To 2022?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1301638/how-to-migrate-child-domain-controller-from-2012-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team  

Windows 2012 R2 is End of life on October 2023  

I would like to plan migrations of Servers with exchange

My Current Infra  

Servers are running VMWare

1-Primary Domain Controller**(Win2012)**  

TLS.LOCAL

1-Secondary Domain Controller + File Server (Win2012)

2-RODC :-UK-RODC**(Win2012)**

2 Child Domain**(Win2012)**  

CDC01.BLR.TLS.LOCAL  

CDC02.BLR.TLS.LOCAL

1 Exchange Server 2016 (CU23) (No DAG Configured) (Win2012)  

C Drive (OS) NTFS  

DB01**(ReFS Partition)**  

DB02**(ReFS Partition)**  

DB03**(ReFS Partition)**  

DB04**(ReFS Partion)

2 Child Domain**(Win2012)**  

CDC01.BLR.TLS.LOCAL  

CDC02.BLR.TLS.LOCAL

I have added New Primary Controller Moved to FSMO. Working fine.  

Now i would like to Migrate without any impact. Because Exchange is live.  

After Adding one more Child Domain with 2022.Transfering 3FSMO Roles (PDC,RID,Infra,)  

Then How to demote Old Child Domains? CDC01.BLR.TLS.LOCAL and  CDC02.BLR.TLS.LOCAL  

What are the things to be unchecked and checked. Because if i remove old server CDC01.BLR.TLS.LOCAL getting DNS is Getting removed, What is the problem?

Please advise

2 Child Domain**(Win2022)**  

CDC01.BLR.TLS.LOCAL  

CDC02.BLR.TLS.LOCAL

What is the best practice After server migrated can we rename the old host name and IP Address?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-06-09*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

What is the best practice After server migrated can we rename the old host name and IP Address?  

Renaming is extremely risky. A better option may be to decommission demote the old one as first step. Then the new one can be built with correct naming. Re-ip'ing a domain controller may be a minor disruption but generally is a safe operation.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-09*

```
Hello Sathishkumar,

Thank you for your question and for reaching out with your question today.

When migrating the Child Domains from Windows Server 2012 to Windows Server 2022, there are several steps you can follow to ensure a smooth transition:

1. Prepare the new Windows Server 2022 Child Domain Controllers:
   - Install Windows Server 2022 on the new servers that will host the Child Domain Controllers.
   - Join the new servers to the existing domain as member servers.
   - Install the Active Directory Domain Services (AD DS) role on the new servers.

2. Promote the new servers to Child Domain Controllers:
   - Use the Server Manager or PowerShell to promote the new servers to Child Domain Controllers in the existing domain.
   - Ensure that replication occurs between the new and existing Child Domain Controllers.

3. Transfer FSMO roles:
   - Transfer the FSMO roles (PDC, RID, Infrastructure) from the old Child Domain Controllers to the new ones.
   - You can use PowerShell commands or the Active Directory Users and Computers MMC to transfer the roles.

4. Validate the new Child Domain Controllers:
   - Perform tests to ensure that the new Child Domain Controllers are functioning correctly.
   - Verify DNS resolution, replication, authentication, and other Active Directory operations.

5. Update dependent services and applications:
   - Update any services or applications that rely on the old Child Domain Controllers to use the new ones.
   - Update DNS configurations, Group Policies, and other settings as necessary.

6. Demote and remove the old Child Domain Controllers:
   - After verifying the functionality of the new Child Domain Controllers, you can demote and remove the old ones.
   - Use the appropriate method (Server Manager or PowerShell) to gracefully demote the old Child Domain Controllers.
   - Ensure that you transfer any necessary roles and services before demoting the old servers.

Regarding the DNS issue you mentioned when removing the old server, make sure that the DNS roles and configurations are correctly set up on the new Child Domain Controllers. You can check the DNS settings and update them if necessary.

After the migration, it is possible to rename the old host name and IP address, but it is recommended to plan and execute such changes carefully to avoid any disruption. It's important to update the DNS records, network configurations, and any dependent services or applications that rely on the old host name or IP address.

It's always advisable to have a backup and thoroughly test the migration process in a non-production environment before performing it in a production environment. 

I used AI provided by ChatGPT to formulate part of this response. I have verified that the information is accurate before sharing it with you.

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
```
