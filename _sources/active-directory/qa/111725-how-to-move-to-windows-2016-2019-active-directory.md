---
title: "How to move to windows 2016, 2019 Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111725/how-to-move-to-windows-2016-2019-active-directory
question_id: 111725
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to move to windows 2016, 2019 Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111725/how-to-move-to-windows-2016-2019-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one forest with a couple child domains that are all windows server 2012 r2, Domain Functional level: Windows Server 2008 R2, Forest functional level: Windows Server 2008 R2.   

Looking to introduce Windows server 2016 and or 2019 and raising the Domain/forest functional levels and move away from windows server 2012, thus upgrading our Active Directory and looking for the most smoothest transition.   

We would consult with our app teams to determine compatibility of course but just looking for general insight of folks who have made this move please.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-29*

Hi,  

If you don't have any problem with compatibility with active directory on Windows 2019 , I join Leon , it's recommended to migrate to last version Windows 2019.  

To be able to promote the first domain controller on Windows 2019 , the forest functional level must be Windows 2008 R2 or higher and use DFRS for sysvol replication.  

Regarding the functional level ,with windows 2019, the highest Forest and domain functional level is Windows 2016.  

Don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-29*

Hi @Crod  ,    

I would recommend going with the latest Windows Server versions (2019 in this case), it gives you a longer lifecycle.    

There are two (2) prerequisites before introducing the first 2019 domain controller, and they are:     

1. The domain functional level needs to be 2008 or higher.    

2. Older sysvol FRS replication needs to have been migrated to DFSR (for more information, see: https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405).    

You should use the dcdiag / repadmin tools first to verify the health, if any errors are shown you should correct all of them before proceeding.     

Next install a new Windows Server 2016/2019 and then do the following:    

-  Patch the server with the latest available updates.    

-  License the server.    

-  Domain join the server to your existing domain.    

-  Add the Active Directory Domain Services (ADDS).    

-  Promote it to a domain controller making it a Global Catalog (GC).    

-  Transfer FSMO roles over (Optional).    

-  Transfer pdc emulator role (Optional).    

-  Use dcdiag / repadmin tools to again verify the health.    

If the new 2016/2019 DC is healthy, you can then start decommissioning or demoting the old domain controllers.    

----------    

(If the reply was helpful please don't forget to upvote or accept as answer, thank you)    

Best regards,    

Leon
