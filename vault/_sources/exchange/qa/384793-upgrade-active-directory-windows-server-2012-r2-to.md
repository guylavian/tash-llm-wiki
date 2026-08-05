---
title: "Upgrade Active Directory Windows server 2012  R2 to Windows server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384793/upgrade-active-directory-windows-server-2012-r2-to
question_id: 384793
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Upgrade Active Directory Windows server 2012  R2 to Windows server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384793/upgrade-active-directory-windows-server-2012-r2-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

we plan to make Migrate our Active Directory from Windows Server 2012 R2 to 2019 and I have some of questions below.  

-  Active Directory 2019 support on windows server 2016/2012 R2 ?  

-  We have Exchange Server 2016 CU9 that run on Windows Server 2012 R2 ,Active Directory 2019 will support ?  

-  We have Microsoft Lync Server 2013 (5.0.8308.0) run on Window Server 2012 R2, Active Directory 2019 will support?  

-  We have a few clients computers that still run Windows 7, there are any compatibles problem with Active Directory 2019 ?  

-  How's we can upgrade and keep hostname &IP address on on Active Directory 2019 with the same old Active Directory 2012.  

Thanks!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-10*

Just check if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-06*

No problems what so  ever having 2012 R2 domain controllers along side 2019 domain controllers.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-06*

Hi,  

Based on my understanding, you want to upgrade your 2012 DCs to 2019DCs, right?  

The minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.  

For your questions:  

1, Active Directory 2019 support on windows server 2016/2012 R2?  

If you want to upgrade all your DCs to 2019 servers and you want to upgrade the functional level to 2016,  

then you must demote all the DCs below windows 2016 version.  

If you want to upgrade all your DCs to 2019 servers but keep the functional level as before (2008 or 2012),  

then you can keep the 2012 DCs.  

No matter which situation, the windows server 2012 will be supported as domain member servers.  

2, We have Exchange Server 2016 CU9 that run on Windows Server 2012 R2, Active Directory 2019 will support?  

I would suggest creating a new thread and add the exchange tag to get professional advice.  

3, We have Microsoft Lync Server 2013 (5.0.8308.0) run on Window Server 2012 R2, Active Directory 2019 will support?  

From the documentation: Active Directory Domain Services support in Lync Server 2013, the minimum Domain Functional Level / Forest Functional Level is 2003.  

The minimum domain functional level for introducing the first 2016 domain controller is also 2003.  

It is not officially known whether it will work or not, because there are no documentations or claims for this,  

We have a few client's computers that still run Windows 7, there are any compatibles problem with Active Directory 2019.  

WIN7 is not supported any more by MS, and there will not updates for WIN7 clients. There may be some any compatibles problem unexpected.  

It is suggested to upgrade the clients to new OS.  

4, How can we upgrade and keep hostname &IP address on Active Directory 2019 with the same old Active Directory 2012.  

There are 2 methods to upgrade and keep hostname &IP address on Active Directory, you can refer to the first method in the following link:   

Rename DC to preserve OLD Name and IP address   

Best Regards,
