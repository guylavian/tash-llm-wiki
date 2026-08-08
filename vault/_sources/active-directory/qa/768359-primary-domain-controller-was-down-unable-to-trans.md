---
title: "Primary domain controller was down, unable to transfer/seize FSMO roles to secondary domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/768359/primary-domain-controller-was-down-unable-to-trans
question_id: 768359
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Primary domain controller was down, unable to transfer/seize FSMO roles to secondary domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/768359/primary-domain-controller-was-down-unable-to-trans (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,  

We have 2 domains controller and now our primary domains controller (PDC) was down, the PDC was holding FSMO roles such as schema, domain naming and infrastructure. We unable to seize or transfer FSMO roles to Secondary domain  controller (SDC). Global catalog & DNS was enabled for both DC.  

Both DC was running on VM, no backup. The PDC which is running on faulty disk and we unable to bring it online.  

We have read all article and didnt found any solutions which is able to resolve our issues.  

I have to transfer FSMO roles to secondary DC so I can perform metadata cleanup, right?  

Regards,  

Shiro

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-03-14*

Hi,    

You can use one of the GUI tools to perform metadata cleanup : Active Directory Users and Computers or Active Directory Sites and Services:    

Clean up server metadata using GUI tools    

Concerning the command below you should replace the targetDC by the name of second domain controller still alive:    

```
Move-ADDirectoryServerOperationMasterRole -Identity **TargetDc** -OperationMasterRole SchemaMaster,DomainNamingMaster,PDCEmulator,RIDMaster,InfrastructureMaster -Force
```

Please don't forget to mark helpful reply as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-14*

Hi,    

I'm able to transfer the FSMO roles to secondary DC, however I'm not able to remove the PDC (which already offline).    

The error message as below:

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-14*

You can follow along here to seize the roles to another healthy one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup before rebuilding the failed one.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-14*

Hi Thameur,    

I was having a problem to run the command to force transfer FSMO roles to secondary DC,    

    

Attached with error message. FYI, our AD01 was totally lost, unable to recover.    

How to fix or recover back the FSMO roles (Schema, naming and infra)?    

Regard,    

Shiro

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-03-11*

Hi,    

If the primary PDC is down, try to fix it before performing a seizing for FSMO roles or metadata cleanup.    

If it's not possible to fix the failed DC , you can perform metadata cleanup and FSMO seizing.    

The FSMO role seizing can be performed through the following powershell command:    

```
Move-ADDirectoryServerOperationMasterRole -Identity TargetDc -OperationMasterRole SchemaMaster,DomainNamingMaster,PDCEmulator,RIDMaster,InfrastructureMaster -Force
```

For metadata cleanup you can refer to the following link:    

ad-ds-metadata-cleanup    

Please don't forget to mark helpful reply as answer
