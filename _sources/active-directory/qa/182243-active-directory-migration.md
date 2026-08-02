---
title: "active directory migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182243/active-directory-migration
question_id: 182243
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# active directory migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182243/active-directory-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I would like to find some documentation / checkilst about what I need to check before I migrate environment ?  

I need to migrate 2012 DC / forest level to 2019 but there is exchange, sccm, forest trust with NT4 ... and I would like to know all what I need to check before the migration.  

Technically, migration is not the issue but what point I need to check is :)

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-12-04*

Hi,  

What I would like is here :  

FRS need to be migrated to DFS-R  

DFL need to be 2008+  

Verify AD is healthy  

Check matric for exchange / sccm / adfs / PKI  

Don't forget to check active directory and replication health before starting the migration.  

Trust with NT4 is security issue because I need to decrease security algorithm (rc4 enable) right ?  

Probably better to isolate it without any trust if possible should be better.  

Yes , I think it's time to migrate it or isolate it, because NT4.0 can be a source of many vulnerability because it use a weak cryptographic algorithm like RC2 , RC4 ,DES ... I invite you to read this article:  

10-questions-answers-about-nt-40-encryption  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-12-02*

Hi,

You can promote a domain controller on Windows 2019 without impacting the NT4.0 trust but it will prevent weak cryptographic algorithm

*I need to migrate 2012 DC / forest level to 2019 *

There is no Windows 2019 FFL or DFL. The highest forest and domain functional level is Windows 2016.

Regarding Exchange you can refer to the following link :

supportability-matrix

For SCCM , there is no impact when you are using a supported version.

Technically, migration is not the issue but what point I need to check is :)

If you want to migrate your domain controllers to Window 2019 , you have to check if FFL is Windows 2008 R2 or higher and the sysvol replication are using DFS-R.

I recommend you to test the migration in non production environment if possible

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-12-01*

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

For exchange / SCCM migration I'd start a new thread here.    

https://learn.microsoft.com/en-us/answers/topics/office-exchange-server-deployment.html    

https://learn.microsoft.com/en-us/answers/topics/mem-cm-site-deployment.html    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-01*

Thank you for your answer.  

Do I have to check other issue I can find for migration ?  

Does trus relationsheep can be a problem ? 2019 with NT4 ?  

There is ADFS on the environment, do I need to check if it's ok with 2019 ?   

There is CA server, same question ...  

Does microsoft write somewhere what need to be check before any operation ?   

You mentioned dfs-r + domain functionnal level but I suppose there are a lot of more.
