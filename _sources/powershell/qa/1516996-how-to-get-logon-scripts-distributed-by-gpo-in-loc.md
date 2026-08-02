---
title: "How to get logon scripts distributed by GPO in local domain to run"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1516996/how-to-get-logon-scripts-distributed-by-gpo-in-loc
question_id: 1516996
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# How to get logon scripts distributed by GPO in local domain to run

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1516996/how-to-get-logon-scripts-distributed-by-gpo-in-loc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 
I am fairly new to sysadmin so any tips are welcome.  

I am trying to deploy a logon script for Password notifications.   

As a first step I made a testing script to run:

[system.Reflection.Assembly]:: LoadwithpartialName('System.windows.Forms')
[system.windows.Forms.Messagebox]:: Show('Logon script runnin...' , 'WARNING')
ping -n 10 10.170.4.52
I linked it to OU 'X'. OU 'X' contains my low level account. 
I am just trying to figure out how to run a script on logon in our environment.  

Firstly I stored the script in a C:\tmp folder I created for testing purposes. This didn't work, I temporarily granted all domain users and pc's access to that folder. It didn't work.   

Then I looked moor online and found out scripts are supposed to be in a folder in sysvol. something of this format:  

\servername\SysVol\doamin\Policies{F3E42D53-EBE0-49F7-8780-199C13D4B880}\User\Scripts\Logon  

I update the GPO, I do gpupdat/force on the host computer.   

Nothing happens, no script runs.   

I have little experience with scripts and running them through GPO's   

So please if you have ideas on how to solve this issue. Even a link to more documentation I failed to find would be a lifesaver.

## Answers

_No answers on this thread._
