---
title: "Exchange 2019 - OWA 500 Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1852925/exchange-2019-owa-500-error
question_id: 1852925
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 - OWA 500 Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1852925/exchange-2019-owa-500-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey out there,

we have a problem with an Exchange 2019 Server. OWA throws a 500 error after login with no information under details. This happens with internal and external access (Server behind a reverse proxy)

Exchange is an 2019 CU14 with latest SU installed on a Windows Server 2022 Standard VM.

EAC is working fine.

What I've done so far:

-  Restart Server ;-)

-  Recreated Virtual Directory for OWA

-  Reinstalled latest SU

-  Create new Auth Certificate

-  Update CAS and Assemblies

-  Checked the bindings in the IIS

After trying to login it shows me the following error in the eventlog of the Server:

Event code: 3005 

Event message: Es ist eine unbehandelte Ausnahme aufgetreten. 

Event time: 02.08.2024 08:18:50 

Event time (UTC): 02.08.2024 06:18:50 

Event ID: 882fcea0bf0945ec9dc358d4846b40c5 

Event sequence: 2 

Event occurrence: 1 

Event detail code: 0 

 

Application information: 

    Application domain: /LM/W3SVC/2/ROOT/owa-633-133670531266125478 

    Trust level: Full 

    Application Virtual Path: /owa 

    Application Path: E:\ExchangeServer\ClientAccess\owa\ 

    Machine name: <EX-Server-Name> 

 

Process information: 

    Process ID: 10796 

    Process name: w3wp.exe 

    Account name: NT-AUTORITÄT\SYSTEM 

 

Exception information: 

    Exception type: HttpException 

    Exception message: Die Datei oder Assembly "Microsoft.Exchange.Services.Json, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" oder eine Abhängigkeit davon wurde nicht gefunden. Das System kann die angegebene Datei nicht finden.

   bei System.Web.HttpApplicationFactory.EnsureAppStartCalledForIntegratedMode(HttpContext context, HttpApplication app)

   bei System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers)

   bei System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context)

   bei System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context)

   bei System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext)

Die Datei oder Assembly "Microsoft.Exchange.Services.Json, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" oder eine Abhängigkeit davon wurde nicht gefunden. Das System kann die angegebene Datei nicht finden.

   bei Microsoft.Exchange.Clients.Owa2.Server.Core.BaseApplication.ExecuteApplicationStart(Object sender, EventArgs e)

   bei Microsoft.Exchange.Clients.Owa2.Server.Core.Global.Application_Start(Object sender, EventArgs e)

 

 

Request information: 

    Request URL: https://localhost:444/owa/exhealth.check 

    Request path: /owa/exhealth.check 

    User host address: ::1 

    User:  

    Is authenticated: False 

    Authentication Type:  

    Thread account name: NT-AUTORITÄT\SYSTEM 

 

Thread information: 

    Thread ID: 43 

    Thread account name: NT-AUTORITÄT\SYSTEM 

    Is impersonating: False 

    Stack trace:    bei System.Web.HttpApplicationFactory.EnsureAppStartCalledForIntegratedMode(HttpContext context, HttpApplication app)

   bei System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers)

   bei System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context)

   bei System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context)

   bei System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext)

 

 

Custom event details:

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-05*

Hi,

Welcome to the Microsoft Q&A forum!

This error occurs within the app's code during startup or while creating a response. The response may contain no content, or the response may appear as a 500 Internal Server Error in the browser. The Application Event Log usually states that the app started normally. From the server's perspective, that's correct. The app did start, but it can't generate a valid response. Run the app at a command prompt on the server or enable the ASP.NET Core Module stdout log to troubleshoot the problem.

This error also may occur when the .NET Core Hosting Bundle isn't installed or is corrupted. Installing or repairing the installation of the .NET Core Hosting Bundle (for IIS) or Visual Studio (for IIS Express) may fix the problem.

So, I recommend you reinstall .NET framework 4.8 and see if it works.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.
