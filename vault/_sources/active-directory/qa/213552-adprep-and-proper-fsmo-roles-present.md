---
title: "Adprep and proper FSMO roles present"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/213552/adprep-and-proper-fsmo-roles-present
question_id: 213552
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Adprep and proper FSMO roles present

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/213552/adprep-and-proper-fsmo-roles-present (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

In order to run adprep successfully, particular switches need to have some FSMO roles present(not mentioning the proper permissions).     

    

So what FSMO roles particular adprep switch need to connect? Schema Master for /forestprep. What about other roles? /rodcprep is not run automatically and has to be run manually if not run in previous versions. We are talking about running adprep for upgrading to 2012r2. The roles needed are Rid , Domain Naming and Infra. So can somebody match those roles to commands listed in the picture?    

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-03*

Hi,

*What about other roles? /rodcprep is not run automatically and has to be run manually if not run in previous versions. *

You need to run this command when you want to promote a the first RODC.

adprep /forestprep and adprep /domainprep can be launched automatically when you promote the first domain controller 2012r2 in forest and domain.

Before launch adprep /forestprep on each forest, check if the DC with schema master role is online. ( forest level)  

Before launch adprep /domainprep on each domain , check if the DC with infrastructure master role is online. ( domain level)  

Before launch adprep /rodcprep on each domain , check if the DC with infrastructure master role is online. (domain level)

Please don't forget to mark helpful reply as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-30*

Hello,    

Thank you so much for posting here.    

/forestprep    

You must run this command on the domain controller that holds the schema operations master role (also known as flexible single master operations or FSMO) for the forest.    

/domainprep    

You must run this command on the domain controller that holds the infrastructure operations master role for the domain.    

/domainprep /gpprep    

You must run this command on the infrastructure master for the domain.     

/rodcprep    

It contacts the infrastructure master in each domain to update the permissions. You need to run this command only once in the forest.     

Reference: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731728(v=ws.11)    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-29*

Something here may help.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers-to-windows-server-2012-r2-and-windows-server-2012    

--please don't forget to Accept as answer if the reply is helpful--
