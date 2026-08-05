---
title: "Active Directory upgrade Windows Server 2008 to Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/264243/active-directory-upgrade-windows-server-2008-to-wi
question_id: 264243
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory upgrade Windows Server 2008 to Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/264243/active-directory-upgrade-windows-server-2008-to-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We’re planning to upgrade our AD infrastructure from Windows Server 2008 to Windows server 2019, current domain and forest functional level are Windows server 2008.   

The plan is to bring in a Additional Domain Controller(ADC) with Win2019 with temp name and once the replication is done. Demote the Win2008 box, rename it and change the ip.   

Then rename and change the IP of Win2019 ADC using netdom to same as the original Win2008  While I have a couple of questions.   

-  Do we need to upgrade the schema version for the above process since eventually we plan on to upgrade all DC’s to Win2019 ?  

-  Do we need to run adprep, domain prep,forestprep in this case?  

-  What are all the checks I can perform to call that replication to new ADC is completed and now I can rename it, like match the NTDS DB size and what else?  

-  What all check I can do to confirm that win2008 is properly and completely demoted before I use that name on Windows2019 AD?  

-  Please help to identify what all should be the pre & post checks?  

-  If you have any other tips as well please share.   

Thanks in advance.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-08*

The much simpler / safer method would be to move roles off to another, decommission demote, stand up the new one with correct name and addressing. When you add a new 2019 domain controller, adprep and schema update happens automatically.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can move on to next one.    

--please don't forget to Accept as answer if the reply is helpful--
