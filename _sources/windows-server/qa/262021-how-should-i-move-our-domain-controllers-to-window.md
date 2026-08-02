---
title: "How should I move our Domain Controllers to Windows Server 2019?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/262021/how-should-i-move-our-domain-controllers-to-window
question_id: 262021
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How should I move our Domain Controllers to Windows Server 2019?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/262021/how-should-i-move-our-domain-controllers-to-window (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Community,  

What is the procedure to move to Windows Server 2019? Should I first create an additional Domain Controller and move all the FSMO roles or is there anyother work around that I should do?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-10*

So do I need to upgrade both forest level and functional level to 2008 or higher  

Only domain functional is required.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Hello,    

Thank you so much for your kindly reply.    

Yes, it should be  at least a Windows Server 2008 functional level to add a Windows Server 2019 Domain Controller. That is to say, we will need to raise the functional level.     

We can set the domain functional level to a value that is equal to or higher than the forest functional level. Also, we will need to have DCs that are running OS with the same level as DFL or higher. So before raising the functional levels, verify that all DCs in the domain are, at a minimum, at the OS version to which you will raise the functional level. That is to say, we will need to demote the Windows server 2003 DC.     

There are forest and domain functional levels. The functional level of a domain or forest depends on which versions of Windows Server operating systems are running on the domain controllers in the domain or forest. It controls which advanced features are available in the domain or forest.    

All domain functional levels are equal to or higher than the forest functional level; The domain function level can only be upgraded on the PDC; The forest functional level can only be upgraded on the schema master.    

For more information, we could refer to:    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc787290(v=ws.10)    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/raise-active-directory-domain-forest-functional-levels    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-08*

Also I was doing some reasearch and found out that there are two terms under functional level, one was domain-level and ther other one was site-level? What exactly is the difference between both?  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Hello,    

Thank you so much for posting here.    

We could follow the steps below:    

1, Check DC health by running Dcdiag /v and check AD replication by running repadmin/showrepl and repadmin /replsum before joining the new DC.    

2, If all is ok, we could go next.    

3, As Dave mentioned, the minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL. So before we add 2019 DC to the existing domain, we need to ensure the functional level is at least Windows Server 2008, and the SYSVOL folder replication type is DFSR.    

4. If all is done, we could add the Windows server 2019 to existing domain.     

5, Add ADDS role and promote the new server as Domain Controller.    

6, Repeat step1 to check AD environment health.    

7, Transfer FSMO roles to the new DC if needed.    

8, Demote the old DC if needed.    

9, Raise domain /forest functional level based on our requirement and environment.    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-07*

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--
