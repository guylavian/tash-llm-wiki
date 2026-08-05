---
title: "Exchange Emergency Mitigation Service dont fetch mitigation from mitogation endpoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1052271/exchange-emergency-mitigation-service-dont-fetch-m
question_id: 1052271
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Emergency Mitigation Service dont fetch mitigation from mitogation endpoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1052271/exchange-emergency-mitigation-service-dont-fetch-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

since enabling EEMS i receive in certain environment (in other environments I dont see any issue)  error lower. However test are successful. I guess issue with TLS certificate. Not sure how to fix, can You help here?    

.\Test-MitigationServiceConnectivity.ps1    

Result: Success.    

Message: The Mitigation Service endpoint is accessible from this computer.    

Invoke-RestMethod -Method GET -Uri "https://officeclient.microsoft.com/getexchangemitigations"    

xml                            EOCS    

---                            ----    

version="1.0" encoding="utf-8" EOCS    

I can fetch from affected servers https://officeclient.microsoft.com/getexchangemitigations via Edge and no certificate warning received.    

    

Eventid 1008 displays each one hour:    

An unexpected exception occurred. Diagnostic information:     

Exception encountered while fetching mitigations : System.AggregateException: One or more errors occurred. ---> System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel. ---> System.Security.Authentication.AuthenticationException: The remote certificate is invalid according to the validation procedure.    

   at System.Net.TlsStream.EndWrite(IAsyncResult asyncResult)    

   at System.Net.ConnectStream.WriteHeadersCallback(IAsyncResult ar)    

   --- End of inner exception stack trace ---    

   at System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)    

   at System.Net.Http.HttpClientHandler.GetResponseCallback(IAsyncResult ar)    

   --- End of inner exception stack trace ---    

   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()    

   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)    

   at Microsoft.Exchange.Mitigation.Service.Common.Utils.<GetHttpUrlResponseAsync>d__2.MoveNext()    

   --- End of inner exception stack trace ---    

   at System.Threading.Tasks.Task.ThrowIfExceptional(Boolean includeTaskCanceledExceptions)    

   at System.Threading.Tasks.Task.Wait(Int32 millisecondsTimeout, CancellationToken cancellationToken)    

   at Microsoft.Exchange.Mitigation.Service.Common.Utils.FetchMitigationsFromUrlT    

   at Microsoft.Exchange.Mitigation.Service.MitigationCloudServiceV2.FetchMitigations()    

   at Microsoft.Exchange.Mitigation.Service.Mitigations.MitigationEngine.FetchAndApplyMitigation()    

---> (Inner Exception #0) System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel. ---> System.Security.Authentication.AuthenticationException: The remote certificate is invalid according to the validation procedure.    

   at System.Net.TlsStream.EndWrite(IAsyncResult asyncResult)    

   at System.Net.ConnectStream.WriteHeadersCallback(IAsyncResult ar)    

   --- End of inner exception stack trace ---    

   at System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)    

   at System.Net.Http.HttpClientHandler.GetResponseCallback(IAsyncResult ar)    

   --- End of inner exception stack trace ---    

   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()    

   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)    

   at Microsoft.Exchange.Mitigation.Service.Common.Utils.<GetHttpUrlResponseAsync>d__2.MoveNext()<---

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-26*

Hi @Ondrej Drobilek   ,    

Thanks for your feedback above which shared more information and glad to know that your issue is resolved now! Since our forum has the policy that The question author cannot accept their own answer. They can only accept answers by others, and according to the scenario introduced here: Answering your own questions on Microsoft Q&A    

I would make a brief summary of this post so that other forum members could easily find useful information here:    

[Exchange Emergency Mitigation Service dont fetch mitigation from mitogation endpoint - Summary]    

Issue Symptom:    

Exchange Emergency Mitigation Service dont fetch mitigation from mitogation endpoint    

Solution:    

Cause was firewall. Adding FW exception helped.    

You could "Accept Answer" for this summary to close this thread, and your action would be helpful to other users who encounter the same issue and read this thread. Thanks for your understanding!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-18*

OK, so no proxies in the path? TLS 1.2 is being enforced on the Exchange Servers?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-18*

Sounds like the Exchange Servers cant connect to the internet:    

https://granikos.eu/exchange-emergency-mitigation-service-findings/
