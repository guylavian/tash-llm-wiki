---
title: "How Do I Prevent Domain Controller Changing?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/563229/how-do-i-prevent-domain-controller-changing
question_id: 563229
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How Do I Prevent Domain Controller Changing?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/563229/how-do-i-prevent-domain-controller-changing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have 3 domain controllers one of Master DC another one ADC and last one is Read Only DC.     

Read Only DC is being used for remote office domain services.    

If I login at RODC , I can click "change to domain controller" then changing domain.    

Is there anyway to disable this attribute at schema or regedit? I don't want to change domain controller for any admin who can login RODC?    

thanks.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-25*

Some ideas here.  

https://www.rebeladmin.com/2018/02/step-step-guide-manage-active-directory-permissions-using-object-acls/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-25*

Hi Patrick and Bourbita,  

You are right but our organization has different admins who have some permisson at Active Directory Console. On the other hand by default Domain users have permission to read some AD objects.  

I think that, I can remove or change passive to change domain controller menu via schema setting or attribute setting.  

If I can prevent this action by delegation, do you have any delegation sceranios?  

Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-09-24*

Hi,  

As mentioned by Patrick , you can change domain controller on MMC instance, it can be done from any machine where active directory tools installed (RODC,member server, workstation, domain controller).  

If you want prevent any change launched from RODC servers, you should check the permission of each admin account allowed to login on RODC ,avoid put all admin account on domain admin group, and prevent all domain admin account to longon on RODC servers.  

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-23*

What problem does this cause? This only changes the active domain controller in that MMC instance.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
