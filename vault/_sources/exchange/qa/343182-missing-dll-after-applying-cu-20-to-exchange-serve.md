---
title: "Missing DLL after applying CU 20 to Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/343182/missing-dll-after-applying-cu-20-to-exchange-serve
question_id: 343182
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Missing DLL after applying CU 20 to Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/343182/missing-dll-after-applying-cu-20-to-exchange-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a 4-node Exchange 2016 DAG as part of a hybrid installation.  I have applied CU 20 to 2 of the nodes, and I am seeing a flood of Information events in the System log on both of them:  

Source: Application Popup  

Event ID: 26  

Application popup: exchange_client.exe - System Error : The program can't start because MSVCP110.dll is missing from your computer.  Try reinstalling the program to fix this problem.  

Comparing the locations of this file in the file system between the affected servers and a server I haven't patched yet shows that the file is present in the same locations in both servers, so I don't know why it can't seem to find it.  

From researching this, it appears this is a Visual C++ 2010 Redistributable file.  I downloaded the  installation for the redistributable and ran it on one of the affected servers.  I first ran a repair, and this did not correct the problem.  I then uninstalled the redistributable and reinstalled it, but that didn't correct the problem either.  

Exchange Server itself seems to be running fine.  I really am not sure which component even needs the Visual C++ 2012 redistributable package.  These events are information events,  

Is there something about the CU 20 installation that causes this problem?  What can I do to correct this?  

Thank you very much for your help with this.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-03*

I had reinstalled the redistributable, but I found what was wrong.  I had only the x64 package installed.  Apparently, I now need both the 32-bit and the 64-bit version installed.  Once I installed the 32-bit version, the error cleared up.  

Thank you very much for your response.  Much appreciated.
