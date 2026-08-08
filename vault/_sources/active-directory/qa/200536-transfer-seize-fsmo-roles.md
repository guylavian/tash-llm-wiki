---
title: "Transfer/Seize FSMO Roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200536/transfer-seize-fsmo-roles
question_id: 200536
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Transfer/Seize FSMO Roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200536/transfer-seize-fsmo-roles (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am asking this for Server 2012 R2    

So in this article:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

If we want to seize FSMO roles of a failed DC, it says to first seize the FSMO roles by Ntdsutil utility, and then cleanup metadata of it by https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup#to-clean-up-server-metadata-by-using-ntdsutil    

But in this second article of Metadata cleanup it says "Metadata cleanup also removes File Replication Service (FRS) and Distributed File System (DFS) Replication connections and attempts to transfer or seize any operations master (also known as flexible single master operations or FSMO) roles that the retired domain controller holds."    

So that means I don't need to seize the FSMO roles by Ntdsutil utility first? I can directly use [Active Directory Users and Computers] to delete the failed DC and it will automatically [delete metadata] and transfer or seize FSMO roles?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-20*

after running commands for FSMO role captures this is the outcome. I can not  take over PDC and Naming master roles.  

C:\Users\act>netdom query fsmo  

Schema master               Servert340.domain.local  

Domain naming master        Server.domian.local  

PDC                         Server.domain.local  

RID pool manager            Servert340.domain.local  

Infrastructure master       Servert340.domain.local  

servert340 should have all roles..

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-23*

Hi,    

No, If you  use metadata cleanup method to demote the domain controller with FSMO roles, you have to seize them manually .     

transfer-or-seize-fsmo-roles-in-ad-ds    

Please Don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-23*

@Anonymous      

Thanks.    

In this case, if DC is deleted from ADUC, will it seize all 5 FSMO Roles? Or only the 3 Domain-wide FSMO roles?    

Forest-Wide    

Schema master    

Domain naming master    

Domain-Wide    

RID master    

PDC emulator    

Infrastructure master

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-16*

Before demotion you'll want to transfer the FSMO roles to another healthy domain controller. If demotion is successful then there is no need for cleanup. Metadata cleanup is more for the situation where a domain controller fails or cannot be demoted for some reason.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to Accept as answer if the reply is helpful--
