---
title: "You cannot start the Active Directory Users and Computers tool because the server is not operational - Windows server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/997495/you-cannot-start-the-active-directory-users-and-co
question_id: 997495
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# You cannot start the Active Directory Users and Computers tool because the server is not operational - Windows server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/997495/you-cannot-start-the-active-directory-users-and-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am getting the following error while opening up Active directory local users and groups MMC console along with Active directory domain and trusts and Active directory Sites and services MMC console.    

You cannot start the Active Directory Users and Computers tool because the server is not operational - Windows server 2012 R2    

however, I am able to open up DNS server console and there is no issue with clients communicating with AD server.    

DNS is being resolved of the server itself.    

Only two events 4000 and 4015 are being generated.    

can anyone assist what could be the issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-08*

Hello there,    

When you install the Windows Server Active Directory Domain Services role, Windows also installs a command-line tool named dcdiag. This utility is very helpful to troubleshoot Active Directory.    

Repadmin.exe and Dcdiag.exe are available on all domain controllers that run Windows Server 2012 R2 or later versions. For more information about how to use these tools to troubleshoot problems, see the following articles.    

AD DS Troubleshooting https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-ds-troubleshooting    

Domain controller configuration error (The server is not operational) when you configure a server by using Server Manager https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/fail-to-configure-server-using-server-manager    

Please try the troubleshooting steps from the above article and see if that helps.    

----------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-07*

Hi,    

Can you please provide an output for dcdiag /c /v and update here. Do you have any portscanner or other AV using up all the RPC ports, quick way to check is nbtstat -an.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-07*

It is for Windows 2012R2

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-07*

Hi,    

Check this troubleshooting steps over here - cannot-start-active-directory-users-and-computers-tool    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
