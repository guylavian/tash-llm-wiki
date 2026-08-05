---
title: "Exchange 2019 OWA won't open"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289369/exchange-2019-owa-wont-open
question_id: 1289369
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2019 OWA won't open

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289369/exchange-2019-owa-wont-open (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Since we updated to CU12 ont Exchange 2019 (on-premise), we have a problem with OWA web page.

When you connect to https://exchange_server/owa, you get the usual login prompt but when you login, you get this error :

I already restarted IIS, the server and the OWA Apppool and it doesn't change anything.

I found this warning that seems related : Event 1309

```
Event code: 3005 
Event message: Une exception non gérée s'est produite. 
Event time: 22/05/2023 11:22:49 
Event time (UTC): 22/05/2023 09:22:49 
Event ID: b4c02baf3b864817b79fe700208433f4 
Event sequence: 2 
Event occurrence: 1 
Event detail code: 0 
 
Application information: 
    Application domain: /LM/W3SVC/2/ROOT/owa-3-133292209494883356 
    Trust level: Full 
    Application Virtual Path: /owa 
    Application Path: E:\EXCHANGE\ClientAccess\owa\ 
    Machine name: SRVMAIL2019 
 
Process information: 
    Process ID: 7076 
    Process name: w3wp.exe 
    Account name: AUTORITE NT\Système 
 
Exception information: 
    Exception type: ArgumentException 
    Exception message: Un élément avec la même clé a déjà été ajouté.
   à System.ThrowHelper.ThrowArgumentException(ExceptionResource resource)
   à System.Collections.Generic.Dictionary`2.Insert(TKey key, TValue value, Boolean add)
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoaderBase.InitializeLocalVersionFolders()
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoaderBase.Load()
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoader.Load()
   à Microsoft.Exchange.Clients.Owa.Core.OwaApplicationBase.ExecuteApplicationStart(Object sender, EventArgs e)
   à Microsoft.Exchange.Clients.Owa.Core.OwaModule.Init(HttpApplication context)
   à System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers)
   à System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context)
   à System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context)
   à System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext)

 
 
Request information: 
    Request URL: https://localhost:444/owa/exhealth.check 
    Request path: /owa/exhealth.check 
    User host address: ::1 
    User:  
    Is authenticated: False 
    Authentication Type:  
    Thread account name: AUTORITE NT\Système 
 
Thread information: 
    Thread ID: 25 
    Thread account name: AUTORITE NT\Système 
    Is impersonating: False 
    Stack trace:    à System.ThrowHelper.ThrowArgumentException(ExceptionResource resource)
   à System.Collections.Generic.Dictionary`2.Insert(TKey key, TValue value, Boolean add)
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoaderBase.InitializeLocalVersionFolders()
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoaderBase.Load()
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoader.Load()
   à Microsoft.Exchange.Clients.Owa.Core.OwaApplicationBase.ExecuteApplicationStart(Object sender, EventArgs e)
   à Microsoft.Exchange.Clients.Owa.Core.OwaModule.Init(HttpApplication context)
   à System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers)
   à System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context)
   à System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context)
   à System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext)
 
 
Custom event details:
```

Yet I don't find a solution, do you have an idea ?

ECP works fine.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-23*

Problem seems fixed by installing KB5019758  

Hi @Baudet Denis ,

Great to know that the issue has been resolved and thanks for the share so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )  

[Exchange 2019 OWA won't open]

Issue Symptom:

Cannot open OWA since updating to CU12 on Exchange 2019 (on-premise).  

Already restarted IIS, the server and the OWA App pool and it doesn't change anything.

Event 1309 with the following Exception information

```
Exception type: ArgumentException 
    Exception message: Un élément avec la même clé a déjà été ajouté.
   à System.ThrowHelper.ThrowArgumentException(ExceptionResource resource)
   à System.Collections.Generic.Dictionary`2.Insert(TKey key, TValue value, Boolean add)
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoaderBase.InitializeLocalVersionFolders()
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoaderBase.Load()
   à Microsoft.Exchange.Clients.Owa.Core.OwaSettingsLoader.Load()
   à Microsoft.Exchange.Clients.Owa.Core.OwaApplicationBase.ExecuteApplicationStart(Object sender, EventArgs e)
   à Microsoft.Exchange.Clients.Owa.Core.OwaModule.Init(HttpApplication context)
   à System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers)
   à System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context)
   à System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context)
   à System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext)
```

Resolution:

 Install KB5019758.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-23*

Ensure the backend site SSL is the self-signed Exchange Server cert and not your trusted one.

https://docs.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues

Also check this article for more insight - https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/owa-stops-working-after-update

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-23*

Hi @Baudet Denis  ,

I've tried searching a lot but can hardly find information about OWA issues related to the exact same event details. But I assume it's worth trying to regenerating the SharedWebConfig.config file by following the instructions in the link below:  

(If there's already a SharedWebConfig.config file in the mentioned locations, you can rename or move to another location beforehand as a backup)

Can't access EAC or OWA after Exchange installation

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
