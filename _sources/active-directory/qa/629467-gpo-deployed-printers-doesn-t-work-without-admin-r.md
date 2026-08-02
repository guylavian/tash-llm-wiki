---
title: "GPO Deployed Printers doesn t work without Admin rights"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/629467/gpo-deployed-printers-doesn-t-work-without-admin-r
question_id: 629467
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO Deployed Printers doesn t work without Admin rights

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/629467/gpo-deployed-printers-doesn-t-work-without-admin-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a Windows 2019 DC. When i changed the Domain Users as simple user in local machines (windows 10 pro).  

The GPO for the Deployed Printers stops working.  

The Security Filtering have only Authenticated Users.  

In the event viewer->windows logs->system  

warning event 1085   

Windows failed to apply the Deployed Printer Connections settings. Deployed Printer Connections settings might have its own log file. Please click on the "More information" link

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-11-17*

Hi,  

i dont believe that the problem is with the Print Nightmare update.  

The problem is with the windows login rights. For some reason when the windows user (domain user) is simple user(without admin rights) the deplyed printer does not work.  

What is the different between Deployed Printer and Preferences->Control Pnel Settings-> Printers. I m asking, because the printers works fine

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-17*

Hi there,    

It is the effect of the Print Nightmare update that released in August. People have found ways to temporarily fix the issue. You can follow the below thread to get hold on the steps.    

https://learn.microsoft.com/en-us/answers/questions/517533/pint-server-and-print-nightmare-update.html?page=4&pageSize=10&sort=oldest    

https://learn.microsoft.com/en-us/answers/questions/567987/windows-failed-to-apply-the-deployed-printer-conne.html    

------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
