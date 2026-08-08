---
title: "Method not found: \"Microsoft.Exchange.Security.Authentication.Utility.DeleteFbaAuthCookies\" after update to CU18 on Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/123170/method-not-found-microsoft-exchange-security-authe
question_id: 123170
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Method not found: "Microsoft.Exchange.Security.Authentication.Utility.DeleteFbaAuthCookies" after update to CU18 on Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/123170/method-not-found-microsoft-exchange-security-authe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

first - I've already posted this question here, but was told that this would be better here in Microsoft Learn Q&A.    

we updated from CU15 to CU18 recently on our Exchange 2016, which is powered by a Windows Server 2012 R2.    

The setup was successful, clients can connect, sync, send and receive emails. But /owa and /ecp don't work. As user, you get an error 500.    

As an admin you see the following:    

```
[MissingMethodException: Method not found: "Void Microsoft.Exchange.Security.Authentication.Utility.DeleteFbaAuthCookies(System.Web.HttpRequest, System.Web.HttpResponse)".]  
   Microsoft.Exchange.HttpProxy.FbaModule.RedirectToFbaLogon(HttpApplication httpApplication, LogonReason reason) +0  
   Microsoft.Exchange.HttpProxy.FbaModule.OnEndRequestInternal(HttpApplication httpApplication) +614  
   Microsoft.Exchange.HttpProxy.<>c__DisplayClass20_0.b__0() +1670  
   Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Action`1 catchDelegate) +35  
   System.Web.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute() +142  
   System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step) +75  
   System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously) +93
```

What I've already done:    

-  Regenerated SharedConfig files with DependentAssemblyGenerator.exe as shown here: https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/event-1309-code-3005-cannot-access-owa-ecp & here: https://social.technet.microsoft.com/Forums/office/de-DE/9b8da9e7-0d0c-4b48-96e7-41fcc6fc7e45/exchange-2016-nach-installation-cu16-kein-owa-und-ecp    

-  Already did .\UpdateCas.ps1 in %ExchangeInstallPath%\bin -> worked, but the error still exists    

-  Then did a .\UpdateConfigFiles.ps1 in the same directory -> also worked, but the error still exists    

-  Changed the Site Binding settings as mentioned here: https://social.technet.microsoft.com/Forums/ie/en-US/8e685c14-b88d-4f70-8e70-25f8190888a1/owa-ecp-broken-after-cu9-and-10-missingmethodexception?forum=Exch2016SD    

-  Then did a IISRESET & reboot after everything    

I really don't know what to do anymore. Has somebody the same problem and could provide me with a solution? Thanks!

## Answers

_No answers on this thread._
