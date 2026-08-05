---
title: "In-Place Upgradation Of Active Directory from 2012R2 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/917520/in-place-upgradation-of-active-directory-from-2012
question_id: 917520
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# In-Place Upgradation Of Active Directory from 2012R2 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/917520/in-place-upgradation-of-active-directory-from-2012 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,    

We are currently in 2012R2 Windows Server, with 1 PDC and 3 BDC (all have same OS version)    

We also have 2 domains and 1 AD forest functional Level. There are over 100 users and we are using Fortigate VPN.    

We have Exchange in hybrid version and 2 ADFS servers with 2012 R2.    

What are the considerations or mitigation plan to be followed for In place Upgrade.?     

Can someone guide me? or share your insights on the same

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-11*

Hi there,     

We can follow steps below to upgrade Window server 2012 R2 DC to Window server 2019 DC.    

-Check if AD environment is healthy. Check all DCs in this domain is working fine by running Dcdiag /v. Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum.    

-Add the new Window server 2019 to this existing domain.    

-Add AD DS and DNS roles and promote this Windows server 2019 as a DC (as a GC).    

-Check if AD environment is healthy again based on step 1.    

-If step 1-step 4 is OK without any error. We can transfer FSMO roles to new 2019 DC if needed.    

-Demote Windows server 2012 R2 if needed. Before we demote 2012 R2 DC, we should check:    

If the removed DC was a DNS server, update the DNS client configuration on all member workstations, member servers, and other DCs that might have used this DNS server for name resolution. If it is required, modify the DHCP scope to reflect the removal of the DNS server.    

You can refer the below article which sheds some insights about this .    

Streamlined Migration of FRS to DFSR SYSVOL https://techcommunity.microsoft.com/t5/storage-at-microsoft/streamlined-migration-of-frs-to-dfsr-sysvol/ba-p/425405 in-place upgrade of 2012 R2 DC to 2019 DC    

in-place upgrade of 2012 R2 DC to 2019 DC https://learn.microsoft.com/en-us/answers/questions/77880/in-place-upgrade-of-2012-r2-dc-to-2019-dc.html    

I hope this information helps. If you have any questions please let me know and I will be glad to help you out.    

------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-07*

Do not do an in-place upgrade. The much simpler / safer method is to stand up new ones for replacement. Move roles off, demote decommission one at a time for rebuild.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
