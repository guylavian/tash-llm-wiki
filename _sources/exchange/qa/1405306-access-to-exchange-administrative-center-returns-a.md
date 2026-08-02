---
title: "Access to Exchange administrative center returns an error after the login credentials are entered"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1405306/access-to-exchange-administrative-center-returns-a
question_id: 1405306
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Access to Exchange administrative center returns an error after the login credentials are entered

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1405306/access-to-exchange-administrative-center-returns-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Inexplicably the server does not allow OWA and access to the Exchange management center.  OWA reports that the site cannot be reached and Exchange Management Center reports "Server Error in  '/owa' Application.

```
Event code: 3005 
Event message: An unhandled exception has occurred. 
Event time: 10/26/2023 2:19:10 PM 
Event time (UTC): 10/26/2023 6:19:10 PM 
Event ID: 8914976f609e409d959edee10eda3924 
Event sequence: 18116 
Event occurrence: 6048 
Event detail code: 0 
 
Application information: 
    Application domain: /LM/W3SVC/1/ROOT/owa-2-133426363981133032 
    Trust level: Full 
    Application Virtual Path: /owa 
    Application Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\ 
    Machine name: ES 
 
Process information: 
    Process ID: 28744 
    Process name: w3wp.exe 
    Account name: NT AUTHORITY\SYSTEM 
 
Exception information: 
    Exception type: ExAssertException 
    Exception message: ASSERT: HMACProvider.GetCertificates:protectionCertificates.Lengthc__DisplayClass3f.b__3e()
   at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(TryDelegate tryDelegate, FilterDelegate filterDelegate, CatchDelegate catchDelegate)
   at Microsoft.Exchange.HttpProxy.Diagnostics.SendWatsonReportOnUnhandledException(MethodDelegate methodDelegate, LastChanceExceptionHandler exceptionHandler)
   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.CallThreadEntranceMethod(MethodDelegate method)

 
 
Request information: 
    Request URL: https://localhost:443/owa/auth.owa 
    Request path: /owa/auth.owa 
    User host address: ::1 
    User: NEBHD1\HealthMailboxd899cdf 
    Is authenticated: True 
    Authentication Type: Basic 
    Thread account name: NT AUTHORITY\SYSTEM 
 
Thread information: 
    Thread ID: 137 
    Thread account name: NT AUTHORITY\SYSTEM 
    Is impersonating: False 
    Stack trace:    at Microsoft.Exchange.Diagnostics.ExAssert.AssertInternal(String formatString, Object[] parameters)
   at Microsoft.Exchange.Clients.Common.HmacProvider.GetCertificates()
   at Microsoft.Exchange.Clients.Common.HmacProvider.GetHmacProvider()
   at Microsoft.Exchange.Clients.Common.HmacProvider.ComputeHmac(Byte[][] messageArrays)
   at Microsoft.Exchange.HttpProxy.FbaModule.SetCadataCookies(HttpApplication httpApplication)
   at Microsoft.Exchange.HttpProxy.FbaFormPostProxyRequestHandler.HandleFbaFormPost(BackEndServer backEndServer)
   at Microsoft.Exchange.HttpProxy.FbaFormPostProxyRequestHandler.ShouldContinueProxy()
   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.BeginProxyRequestOrRecalculate()
   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.InternalOnCalculateTargetBackEndCompleted(TargetCalculationCallbackBeacon beacon)
   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.<>c__DisplayClass3f.b__3e()
   at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(TryDelegate tryDelegate, FilterDelegate filterDelegate, CatchDelegate catchDelegate)
   at Microsoft.Exchange.HttpProxy.Diagnostics.SendWatsonReportOnUnhandledException(MethodDelegate methodDelegate, LastChanceExceptionHandler exceptionHandler)
   at Microsoft.Exchange.HttpProxy.ProxyRequestHandler.CallThreadEntranceMethod(MethodDelegate method)
 
 
Custom event details:
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-27*

Hello @Christopher Eddy  

Use the following command to check the status of your existing OAuth certificate and create a new one if expired.

`(Get-AuthConfig).CurrentCertificateThumbprint | Get-ExchangeCertificate | Format-List`

More details: Exchange Server error in '/owa' application

Or you can refer to KarlT700's answer and try to register the old certificate (If the certificate has not expired.). 

Also, you can check if a CU update is available.

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
