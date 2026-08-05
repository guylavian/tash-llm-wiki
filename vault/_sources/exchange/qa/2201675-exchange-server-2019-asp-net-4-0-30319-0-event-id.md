---
title: "Exchange Server 2019 - ASP.NET 4.0.30319.0 Event ID 1309"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2201675/exchange-server-2019-asp-net-4-0-30319-0-event-id
question_id: 2201675
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 - ASP.NET 4.0.30319.0 Event ID 1309

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2201675/exchange-server-2019-asp-net-4-0-30319-0-event-id (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have an Exchange 2019 CU14 and it was working fine till I installed the Security Update for Exchange 2019 Cumulative Update 14 (KB5036401).

since then my Event viewer is filled with ASP.NET 4.0.30319.0 Event ID 1309. ECP and OWA are working fine 

Event code: 3005 

Event message: An unhandled exception has occurred. 

Event time: 3/5/2025 6:28:06 PM 

Event time (UTC): 3/5/2025 4:28:06 PM 

Event ID: 4ec8677e5ebc451d9237cb12da82d41b 

Event sequence: 31608 

Event occurrence: 694 

Event detail code: 0 

 

Application information: 

    Application domain: /LM/W3SVC/2/ROOT/owa-2-133850245435189009 

    Trust level: Full 

    Application Virtual Path: /owa 

    Application Path: C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\owa\ 

    Machine name: ServerName

 

Process information: 

    Process ID: 1376 

    Process name: w3wp.exe 

    Account name: NT AUTHORITY\SYSTEM 

 

Exception information: 

    Exception type: NullReferenceException 

    Exception message: Object reference not set to an instance of an object.

   at Microsoft.Exchange.Clients.Owa2.Server.Core.OwaModule.ShouldBlockIncomingRequest(HttpContext httpContext)

   at Microsoft.Exchange.Clients.Owa2.Server.Core.OwaModule.OnAuthenticateRequest(Object sender, EventArgs e)

   at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

   at System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)

   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

 

 

Request information: 

    Request URL: https://domain:444/owa/prem/15.2.1544.9/ext/def/a216ceed-7791-4635-a752-5a4ac0a5eb93/images/app_icon.png 

    Request path: /owa/prem/15.2.1544.9/ext/def/a216ceed-7791-4635-a752-5a4ac0a5eb93/images/app_icon.png 

    User host address: 192.168.3.17 

    User:  

    Is authenticated: False 

    Authentication Type:  

    Thread account name: NT AUTHORITY\SYSTEM 

 

Thread information: 

    Thread ID: 50 

    Thread account name: NT AUTHORITY\SYSTEM 

    Is impersonating: False 

    Stack trace:    at Microsoft.Exchange.Clients.Owa2.Server.Core.OwaModule.ShouldBlockIncomingRequest(HttpContext httpContext)

   at Microsoft.Exchange.Clients.Owa2.Server.Core.OwaModule.OnAuthenticateRequest(Object sender, EventArgs e)

   at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

   at System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)

   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-17*

Hello Again,

i confirm after installing Exchange2019-KB5037224-x64-en the ASP.net error stopped. and the outlook search also is working again.

thank you for your help

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-06*

Hi @EDDY RAFFOUL,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, your issue is with Event ID 1309 after installing the security update for Exchange 2019 Cumulative Update 14 (KB5036401). Below are some suggestions that we hope will help you.

-  Please check your .net framework version first. According to the official documentation, it should be 4.8. If your current version does not match, we recommend you to upgrade it to ensure the compatibility and stability of your system. 

-  In the thread with similar issue as yours, there is feedback from users that deleting ‘targetFramework="4.5.1" ’ in the file ‘X:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\rest\web.config’ , and then run IISRESET or restart the server, which may effectively solve the problem. You can try this method, but be sure to make a backup of this file before the operation, so that you can restore the original state in time to avoid unnecessary losses if the operation is abnormal.

In addition, I would like to know, in addition to the current error message, have you encountered any other problems with Exchange?

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
