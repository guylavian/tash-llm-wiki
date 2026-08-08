---
title: "Deploy Flush DNS by GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/626470/deploy-flush-dns-by-gpo
question_id: 626470
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Deploy Flush DNS by GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/626470/deploy-flush-dns-by-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Teams,  

I want to create  bat script ipconfig /flushdns push by active directory GPO.  

If possible to share with me ipconfig /flushdns  bat script file deployment process of documentation for AD GPO.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-16*

You can create .bat file with below command and push via start up script or login script using gpo.    

Below is Microsoft reference guide to push script via GPO.    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789196(v=ws.11)    

-----    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-15*

Windows provides a set of policy-driven user logon, user logoff, computer startup, and computer shutdown scripts that you can manage by using the Group Policy snap-in.  

Scripts (Startup/Shutdown) Use this extension to specify the scripts that run when you start and shut down the computer. To configure the computer startup and shutdown scripts, start the Group Policy snap-in, expand Computer Configuration\Windows Settings, click Scripts (Startup/Shutdown), and then in the right pane, double-click the script that you want to configure. These scripts run with the Local System account.  

Scripts (Logon/Logoff) Use this extension to specify the scripts that run when a user logs on or logs off the computer. To configure the user logon and logoff scripts, start the Group Policy snap-in, expand User Configuration\Windows Settings, click Scripts (Logon/Logoff), and then in the right pane double-click the script that you want to configure. These scripts run with the User account and not on the Administrator account.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-15*

Dear DSPatrick,   

Thanks for your advice.  

I want to deploy dns cache clear command  (ipconfig /flushdns) push by active directory GPO. your reference link cannot be push GPO.   

if possible to share the docs throw GPO script for ipconfig flush dns.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-14*

You could do it remotely here.    

https://techgenix.com/clear-dns-cache-remote-computers/    

also check this one.    

https://learn.microsoft.com/en-us/windows-server/networking/dns/troubleshoot/disable-dns-client-side-caching    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
