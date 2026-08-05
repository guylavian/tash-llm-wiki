---
title: "Microsoft Exchange 2019 Event ID 4999 and 1003"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190224/microsoft-exchange-2019-event-id-4999-and-1003
question_id: 2190224
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
---
# Microsoft Exchange 2019 Event ID 4999 and 1003

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190224/microsoft-exchange-2019-event-id-4999-and-1003 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Lately we have been seeing a lot of these errors in event viewer

Everything is working fine , we can connect to ECP/OWA and the OAUTH certificate is valid

we are just wondering why we get so many of them... ( Server 2019 STD with Exchange 2019 STD CU13 onpremise )

it usually start with 4999 then it's followed by about 20/30times the same 1003 error

Event 4999 occurred at 2023-11-29 13:33:20.  <br><br>-------------------  <br><br>Date Time: 2023-11-29 13:33:20  <br><br>Event Source: MSExchange Common  <br><br>Event Category: 1  <br><br>Event Type: Error  <br><br>Event ID: 4999  <br><br>Event Log Name: Application  <br><br>User: N/A  <br><br>Computer: SERVER.entreprise.local  <br><br>Description:  <br><br>Watson report about to be sent for process id: 21628, with parameters: E12IIS, c-RTL-AMD64, 15.01.2507.034, w3wp#MSExchangeECPAppPool, M.E.Data.ApplicationLogic, M.E.D.A.C.BackEndServer.FromString, System.ArgumentException, 34ec-dumptidset, 15.01.2507.034. <br><br>ErrorReportingEnabled: True  <br><br> <br><br>Event Parameters:  <br><br>21628 <br><br>E12IIS <br><br>c-RTL-AMD64  <br><br>-------------------  <br><br>Report generated on: server.entreprise.local

Event 1003 occurred at 2023-11-29 13:33:26.  <br><br>-------------------  <br><br>Date Time: 2023-11-29 13:33:26  <br><br>Event Source: MSExchange Front End HTTP Proxy  <br><br>Event Category: 1  <br><br>Event Type: Error  <br><br>Event ID: 1003  <br><br>Event Log Name: Application  <br><br>User: N/A  <br><br>Computer: SERVER.entreprise.local  <br><br>Description:  <br><br>[Ecp] An internal server error occurred. The unhandled exception was: System.ArgumentException: Invalid input value <br><br>Parameter name: input <br><br>at Microsoft.Exchange.Data.ApplicationLogic.Cafe.BackEndServer.FromString(String input) <br><br>at Microsoft.Exchange.HttpProxy.BEResourceRequestHandler.ResolveAnchorMailbox() <br><br>at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.InternalBeginCalculateTargetBackEnd(AnchorMailbox& anchorMailbox) <br><br>at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.b__279_0() <br><br>at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Action`1 catchDelegate)  <br><br>Event Parameters:  <br><br>Ecp <br><br>System.ArgumentException: Invalid input value Parameter name: input at Microsoft.Exchange.Data.ApplicationLogic.Cafe.BackEndServer.FromString(String input) at Microsoft.Exchange.HttpProxy.BEResourceRequestHandler.ResolveAnchorMailbox() at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.InternalBeginCalculateTargetBackEnd(AnchorMailbox& anchorMailbox) at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.b__279_0() at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Action`1 catchDelegate) <br><br>%String3%  <br><br>-------------------  <br><br>Report generated on: server.entreprise.local

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-30*

Hello Logibm

Good day!

Thank you for posting in Microsoft Community forum.    

    

From the description above, I understand your question is related to Exchange server.     

    

Since there are no engineers dedicated to Exchange in this forum. To be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.  
Here is the link for Q&A forum:   

Questions - Microsoft Q&A
Click the "Ask a Question" button in the upper right corner to post your question and select related tags.

Regards,

Karlie
