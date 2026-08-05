---
title: "Domain Controller / SQL Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/571019/domain-controller-sql-server-2019
question_id: 571019
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain Controller / SQL Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/571019/domain-controller-sql-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are currently running Server 2019 as a domain controller that gives staff access to various shared files and folders, I have now been tasked with installing SQL Server 2019 I have read various forums that say it's not recommended to install SQL Server on a server that is set up as a domain controller.  

Could anyone tell me what options there are available to me to solve this issue or would I need to purchase a separate server to run SQL Server on?   

Thank you in advance.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-09-30*

Hi @Paul Smith  ,    

For security reasons, we recommend that you do not install SQL Server on a domain controller. SQL Server Setup will not block installation on a computer that is a domain controller, but the following limitations apply:    

• You cannot run SQL Server services on a domain controller under a local service account.    

• After SQL Server is installed on a computer, you cannot change the computer from a domain member to a domain controller. You must uninstall SQL Server before you change the host computer to a domain controller.    

• After SQL Server is installed on a computer, you cannot change the computer from a domain controller to a domain member. You must uninstall SQL Server before you change the host computer to a domain member.    

• SQL Server failover cluster instances are not supported where cluster nodes are domain controllers.    

• SQL Server is not supported on a read-only domain controller. SQL Server Setup cannot create security groups or provision SQL Server service accounts on a read-only domain controller. In this scenario, Setup will fail.    

• A SQL Server failover cluster instance is not supported in an environment where only a read-only domain controller is accessible.    

Refer to MS document SQL Server 2019: Hardware and software requirements.    

If the response is helpful, please click "Accept Answer" and upvote it,  as this could help other community members looking for similar thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-30*

Hello,  

Thank you for your question.  

As a best Practice you should not install SQL on Domain controller as resource intensive and may create issue during migration or upgradation.  

Hence keep both isolated to achieve best performance .  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-29*

It is not recommended for security reasons, but it is also not prevented.  You can do it, but if someone exploits your SQL Server, they may gain access to your entire domain.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-29*

Additional see MS Support Installing SQL Server on a domain controller
