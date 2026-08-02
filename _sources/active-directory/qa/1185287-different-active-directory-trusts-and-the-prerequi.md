---
title: "different active directory trusts and the prerequisites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185287/different-active-directory-trusts-and-the-prerequi
question_id: 1185287
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# different active directory trusts and the prerequisites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185287/different-active-directory-trusts-and-the-prerequi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,  

due to historic reason, our company exists of 2 different domains.  let' say A.com and B.com,  B.com current integrated with O365 and Microsoft AAD.  but A.com is an local and used for A site user's authentication.  A.com has a subdomain called  sh.a.com. 

 Right now we want to merge A to B or use domain trust relationship to do bidirectionally trust in between A.com and B.com to contribute to work collaboration both side.  

 My question would be:

-  Merge A.com to B.com  or do trust relationship between A and B which is the best choices.  what is the Pros and Cons of both solutions ?

-  as now A.com has lost of some credentials like forest admin and recovery password and etc. by previous IT he created one sub domain called.  sh.A.com. and now we have the administrator information only of sh.A.com this subdomain.  will this impact the domain trust between A.com and B.com ? what is the prerequisites for a successful domain trust ?

-   Any great tooling for the domain merge which will not cause of downtime where we're able to merge A.com users and security groups whatever to B.com. and after migration the users still able to login via his previous accounts and password and nothing changes ? or make a lowest impacts to users and applications like Devops integrations,  NFS share folders and etc.  ?

Thanks very much for your answers.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-01*

Hi @Mike(Liangshuai) Wang

-  Merge A.com to B.com or do trust relationship between A and B which is the best choices. what is the Pros and Cons of both solutions ?      The migration is better because you will be able  reduce the number of domain controller and high privileged .
    In other hand , if the migration is complicated, you can create a trust during the migration process.

-  as now A.com has lost of some credentials like forest admin and recovery password and etc. by previous IT he created one sub domain called. sh.A.com. and now we have the administrator information only of sh.A.com this subdomain. will this impact the domain trust between A.com and B.com ? what is the prerequisites for a successful domain trust ?
    Yes it will impact because ,you have to use a administrator account memberof enterprise group or domain group in root domain.   

    For more details please read the following link : Active Directory Forest Trust: Attention Points

-  Any great tooling for the domain merge which will not cause of downtime where we're able to merge A.com users and security groups whatever to B.com. and after migration the users still able to login via his previous accounts and password and nothing changes ? or make a lowest impacts to users and applications like Devops integrations, NFS share folders and etc. ?    During the migration ,you can reduce downtime by using a trust relationship between the source and target forest and enable SIDhistory.You can use admt tools , but I recommend you to use a third party tool like Quest Migration Manager

Please don't forget to mark helpful answer as accepted

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-01*

Something here could help.  

https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/multi-forest/plan-a-multi-forest-deployment#plan-trust-between-forests  

or possibly ADMT tool for migration to new forest / domain.  

https://www.microsoft.com/en-us/download/details.aspx?id=56570  

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
