---
title: "Can I have Domain Controller 2019 and wondows server 2012"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/236883/can-i-have-domain-controller-2019-and-wondows-serv
question_id: 236883
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Can I have Domain Controller 2019 and wondows server 2012

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/236883/can-i-have-domain-controller-2019-and-wondows-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are planning to upgrade our domain controller server from 2012 R2 to server 2019.  we will have most of the other servers on windows server 2012 R2 for a while and some on windows server 2019. Please let me know if they are compatible?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-20*

Hello @Rajashekar Marri  ,

Thank you for posting here.

Based on the description "we will have most of the other servers on windows server 2012 R2 for a while and some on windows server 2019", I understand all of our DCs are WIndows server 2012 R2 DCs currently, now we want to upgrade some of domain controller servers from Windows server 2012 R2 DC to Windows server 2019 DC. Then you will keep most Windows server 2012 R2 DCs and some WIndows server 2019 DCs at the same time for a while in the same domain, if anything I misunderstood, please correct me.

As DSPatrick mentioned, The minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.

Please check forest functional level and SYSVOL replication type.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

**Q:**Please let me know if they are compatible?  

**A:**Yes, we can add Windows server 2012 R2 DCs and Windows server 2019 DCs in the same domain.  

Ensure that all domain functional levels are equal to or higher than the forest functional level;  

Ensure that the operating system level of all domain controllers is equal to or higher than the domain functional level;

Meanwhile, here are some considerations before we make any change.

1.Please check the DC health for each DC by running Dcdiag /v.  

2.Please check AD replication by running repadmin /replsum and repadmin /showrepl * /csv >c:\repsum.csv** (if there is no any error in the result, it means AD replication works fine).  

3.Please running gpupdate /force on each DC to check group policy update.  

4.For upgrading domain controller from lower operating system to higher operating system, there are two methods:  

Method 1 Perform an in-place upgrade of an existing domain controller to higher operating system.  

Method 2 Promote a new 2019 DC in the existing domain.  

We recommend we add new domain controller to the existing domain (method 2).

Hope the information above is helpful. If anything is unclear, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-19*

Hi,     

Yes, The microsoft link below confirm that a domain controller on windows 2019 is compatible with any domain controller promoted on windows 2008 R2 or higher.    

active-directory-functional-levels    

----------    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-19*

Yes, not a problem.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--
