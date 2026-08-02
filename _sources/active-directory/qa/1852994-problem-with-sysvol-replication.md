---
title: "Problem with SysVol Replication."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1852994/problem-with-sysvol-replication
question_id: 1852994
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Problem with SysVol Replication.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1852994/problem-with-sysvol-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone.

Recently i encounter a problem. A customer want to migrate the 2 DC to a new version of Windows Server ( One 2016 and the other 2022). The old DCs is a 2008 R2 and a 2016. A coworker has add the new 2016 to the domain(as DC) and the other day i try to make the 2022 a dc but i have the error that told me the sysvol is using FRS to replicate and so i cant continue. I know the solution is to migrate to DFSR and that was the plan.   

The 2008 has all the FSMO roles, the domain and forest function lvl is 2008 R2. I see error to FRS at all DC ( 2 old and the new one) that say "The File Replication Service is having trouble enabling replication from 2008_Srv to 2016_New" (screen1). 
At this time a have already start the migration ( i have enter the dfsrmig /setglobalstate 1 to the 2008 server) show at this time only the 2008 server is on prepared state the other is on Start. After that i have start and searching about why there is this errors for the sysvol replication, i check the sysvol folder at all  servers and i found this. On the 2008 there is all the gpo listing, on the 2016_old there is one gpo missing and at the new one the sysvol/domain folder is empty. Also at both 2016 the sysvol folder is not shared (screen2) and the repadmin show no errors (screen3). 

I ask the chatgpt if a wondows server 2008 can replicate the sysvol using FRS between a 2016 and answer it cant. Also consider that both the old servers after we join the new ones to the domain as DC we demote the old and the domain they have 2 DC ( the new 2016 and 2022 ) My questions is:

-  Can i continue with the migration or i need to resolve the replication issue first. And if i can is normal that i enter the dfsrmig /setglobalstate 1 at the one server and olny this is on prepare state or after a time there is all the server go at this state automatic or i need to enter the command on each one? 

-  If i need to resolve the replication issue can u have any advice?

-  Can the sysvol replicate between a 2008 and a 2016 servers using FSR? if not what i can do at this state?

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-05*

Hello

Thank you for posting in Q&A forum.

1.Can sysvol replicate using FRS between 2008 and 2016?

FRS has been Deprecated from the windows server 2008r2, to know if you can use FRS between Windows server2008 and 2016, We need to know if they all use FRS.

you can run cmd as admin to know if you are using FRS or DFSR

dcdiag/v >c:\dcdiag.txt

The End is Nigh (for FRS) – updated for WS2016 - Microsoft Community Hub

2.Can u continue with the migration or i need to solve the errors?

No, we need to fix the error, Before the migration we need to make sure FRS running well

3.If u need to resolve them, do u have any guide to provide?

we need to make sure Active directory replication is work fine before fixed your FRS issue. You can follow the below document try to fix your problem.

Use BurFlags to reinitialize File Replication Service (FRS) - Windows Server | Microsoft Learn

4.If not, is normal to enter the dfsrmig /setglobalstate 1 to one computer and only this hase change state or i need to enter the command on each DC and is not change the state automatic to others whene u enter the command

Setglobalstate 1 is the first step of migration, after we enter the command, we need to check all the rest DC to make sure that they are following the order to get to the state 1. and then we can set the next command set global state 2 or 3

Migration link:

Streamlined Migration of FRS to DFSR SYSVOL - Microsoft Community Hub

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
