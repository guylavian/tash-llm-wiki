---
title: "Constrained Delegation (Without Kerberos) does not working for Windows Server 2022 only"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1275700/constrained-delegation-without-kerberos-does-not-w
question_id: 1275700
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Constrained Delegation (Without Kerberos) does not working for Windows Server 2022 only

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1275700/constrained-delegation-without-kerberos-does-not-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have following Configuration:   

ClientA run DCOM Application on ServerA for write data to SMB share on ServerB

We've configure "Constrained Delegation"/"Double Hop" in our Active Directory:  

ServerA Trust this computer for delegation to specified services only + Use any authentication protocol to ServerB.  

When we use Windows Server 2022 as a ClientA, we get an "Access is denied" error.

The Windows Server 2022 is fresh with the latest updates and located in the same OU as the other servers, which continue to work without problems:

 Windows Server 2008 R2

 Windows Server 2012 

 Windows Server 2016

 Windows Server 2019  

Possible Windows Server 2022 don't support some old protocol, because when I chose Trust this computer for delegation to any service (Kerberos only)  

or Trust this computer for delegation to specified services only + Use Kerberos only  

old servers also stop working.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-04*

Hello 

You are right, there has been different updates regarding Kerberos vulnerabilities, and Constrained Delegation in 2022.

Please check this article: https://support.microsoft.com/en-us/topic/kb5021131-how-to-manage-the-kerberos-protocol-changes-related-to-cve-2022-37966-fd837ac3-cdec-4e76-a6ec-86e67501407d

And this official guide in the Microsoft community: https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/what-happened-to-kerberos-authentication-after-installing-the/ba-p/3696351

First, the setup should be straightforward under the proper encryption configurations:

1.Open Start Menu by pressing W8K and go to Windows Administrative Tools > Active Directory Users and Computers.

-  In Active Directory Users and Computers, go to Domain Controllers. In the right pane, right click on the computer you wanted to be trusted for delegation and select Properties.

-  On the property sheet, go to Delegation tab. Here, you can select Trust this computer for delegation to any service (Kerberos only). If you want delegation for particular services only, instead select Trust this computer for delegation to specified services only. Make sure you select Use Kerberos only after that.

--If the reply is helpful, please Upvote and Accept as answer--
