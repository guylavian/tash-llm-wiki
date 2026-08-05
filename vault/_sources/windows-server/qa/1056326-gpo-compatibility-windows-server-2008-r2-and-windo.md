---
title: "[GPO Compatibility] Windows Server 2008 R2 and Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1056326/gpo-compatibility-windows-server-2008-r2-and-windo
question_id: 1056326
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# [GPO Compatibility] Windows Server 2008 R2 and Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1056326/gpo-compatibility-windows-server-2008-r2-and-windo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have a main server in Windows Server 2008 R2 (domain functional level and forest functional level in WS 2008 R2 as well).    

On this server I added GPO to drive a RDS Server (Windows Server 2019).    

The problem is that some GPOs are not working.    

Example: Change the Windows menu for users / Set a start page for Firefox / Hide the server manager for standard users.    

Other GPOs work perfectly like:    

Hide C: drive / Deny access to Control Panel for standard users.    

I have downloaded the admx files for Windows 10 :    

https://www.microsoft.com/en-us/download/details.aspx?id=103667    

As well as the admx for Firefox.    

Could there be a compatibility problem between WS 2008 R2 and WS 2019? (for the moment we can't upgrade our Server 2008 R2).

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-11*

Late answer, it may or may not work.
However, you can try updating your ADMX files for the GPO management console with the domain group policy directory, instructions below.
I had a previous work domain that also had an old 2008r2 domain and of course, IE11 compatibility/settings didn't exist back then. But updating the ADMX files with the domain controller (after backing them up of course) should fix most of the issues with GPO settings not working or applying properly. 
https://deploywindows.com/2015/08/20/how-do-you-update-your-group-policy-admx-files/
Also take a look at this answer, as it may answer questions on that subject also. 
https://serverfault.com/questions/1096677/how-to-update-admx-files-different-server-os-versions-in-domain
If you go down this route, I would recreate your GPOs after updating the ADMX files as updating old policies may not be best with some options missing from deprecated settings that were removed from the console.
W10 22H2 ADMX files for GPO!
https://www.microsoft.com/en-us/download/104677
