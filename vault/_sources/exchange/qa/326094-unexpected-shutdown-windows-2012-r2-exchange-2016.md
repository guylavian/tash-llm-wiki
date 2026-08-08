---
title: "unexpected shutdown Windows 2012 R2 exchange 2016 - event ID 1003, 6027, 1325, 4018"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/326094/unexpected-shutdown-windows-2012-r2-exchange-2016
question_id: 326094
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# unexpected shutdown Windows 2012 R2 exchange 2016 - event ID 1003, 6027, 1325, 4018

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/326094/unexpected-shutdown-windows-2012-r2-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,   

an unexpected shutdown happened on my Windows 2012 R2 running exchange 2016 standard CU19 Version 15.1 ‎(Build 2176.2)‎  

there are Application log Event ID : 1325, 9646, 4999, 4018, 3018, 3025, 6027, 1003, 1008 when i searched for the last 12 hours events.  

event source: FIPFS  

 event ID: 6027   

the description :   

 MS Filtering Engine Update process was unsuccessful to download the engine update for Microsoft from Primary Update Path.  

Update Path:http://amupdatedl.microsoft.com/server/amupdate  

UpdateVersion:0  

Reason:"There was a catastrophic error while attempting to update the engine. Error: DownloadEngine failed and there are no further update paths available.Engine Id: 1 Engine Name: Microsoft"  

event source: MSExchange Front End HTTP Proxy  

event ID:	1003  

the description :   

[Ecp] An internal server error occurred. The unhandled exception was: System.ArgumentException: Invalid value  

   at Microsoft.Exchange.HttpProxy.ServerInfoAnchorMailbox..ctor(BackEndServer backendServer, IRequestContext requestContext)  

   at Microsoft.Exchange.HttpProxy.BEResourceRequestHandler.ResolveAnchorMailbox()  

   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.InternalBeginCalculateTargetBackEnd(AnchorMailbox& anchorMailbox)  

   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.<BeginCalculateTargetBackEnd>b__280_0()  

   at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Action`1 catchDelegate)  

there're a few event ID in the system log, Event ID: 5011, 36874, 36888, 36887.  

So many events need to troubleshoot, I am in need of lots of brilliant heads, trying to fix this asap.   

Thanks for your time.  

pingatwork

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-23*

Hi, pingatwork.    

Please note that not all these events are related to Exchange server health.    

For example, event 6027 indicates the server failed to update MS Filtering Engine, it may be caused by temporary network problems.    

While event 1003 indicates EAC/OWA cannot be accessed.    

Do you currently have any actual problems with the Exchange server?     

Is mail flow, client access and EAC/EMS working fine?    

If any actual problems, I suggest that we focus on them.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
