---
title: "Connect-ExchangeOnline -CertificateThumbprint \"xxx\" -AppId \"xxx\" -Organization company.com throwing below error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1071405/connect-exchangeonline-certificatethumbprint-x-app
question_id: 1071405
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connect-ExchangeOnline -CertificateThumbprint "xxx" -AppId "xxx" -Organization company.com throwing below error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1071405/connect-exchangeonline-certificatethumbprint-x-app (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Connect-ExchangeOnline -CertificateThumbprint "xxx" -AppId "xxx" -Organization company.com    

getting below error for above command please guide me where I'm lagged    

Error Acquiring Token:    

System.Exception: Case when Message contains:AADSTS70011 Invalid scope. The scope has to be of the form "https://resourceUrl/.default"Mitigatio    

n: change the scope to be as expectedAADSTS1002016: You are using TLS version 1.0, 1.1 and/or 3DES cipher which are deprecated to improve the s    

ecurity posture of Azure AD. Your TenantID is: tttjrs5558a3. Please refer to https://go.microsoft.com/fwlink/?linkid=21    

61187 and conduct needed actions to remediate the issue. For further questions, please contact your administrator.    

Trace ID: 6776    

Correlation ID: 564g457    

Timestamp: 2022-11-01 17:20:17Z ---> Microsoft.Identity.Client.MsalServiceException: AADSTS1002016: You are using TLS version 1.0, 1.1 and/or 3    

DES cipher which are deprecated to improve the security posture of Azure AD. Your TenantID is: 655ghb5 Please ref    

er to https://go.microsoft.com/fwlink/?linkid=2161187 and conduct needed actions to remediate the issue. For further questions, please contact    

your administrator.    

Trace ID: oiyuyo77    

Correlation ID: a545ff    

Timestamp: 2022-11-01 17:20:17Z    

   at Microsoft.Identity.Client.Internal.Requests.RequestBase.<HandleTokenRefreshErrorAsync>d__26.MoveNext()    

--- End of stack trace from previous location where exception was thrown ---    

   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()    

   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)    

   at Microsoft.Identity.Client.Internal.Requests.ClientCredentialRequest.<ExecuteAsync>d__2.MoveNext()    

--- End of stack trace from previous location where exception was thrown ---    

   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()    

   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)    

   at Microsoft.Identity.Client.Internal.Requests.RequestBase.<RunAsync>d__12.MoveNext()    

--- End of stack trace from previous location where exception was thrown ---    

   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()    

   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)    

   at Microsoft.Identity.Client.ApiConfig.Executors.ConfidentialClientExecutor.<ExecuteAsync>d__3.MoveNext()    

--- End of stack trace from previous location where exception was thrown ---    

   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()    

   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)    

   at Microsoft.Exchange.Management.AdminApiProvider.Authentication.MSALTokenProvider.<GetAccessTokenAsync>d__29.MoveNext()    

   --- End of inner exception stack trace ---    

   at Microsoft.Exchange.Management.AdminApiProvider.Authentication.MSALTokenProvider.<GetAccessTokenAsync>d__29.MoveNext()    

Case when Message contains:AADSTS70011 Invalid scope. The scope has to be of the form "https://resourceUrl/.default"Mitigation: change the    

scope to be as expectedAADSTS1002016: You are using TLS version 1.0, 1.1 and/or 3DES cipher which are deprecated to improve the security    

posture of Azure AD. Your TenantID is: 1y. Please refer to https://go.microsoft.com/fwlink/?linkid=2161187    

and conduct needed actions to remediate the issue. For further questions, please contact your administrator.    

Trace ID: 5t55t    

Correlation ID: t555t    

Timestamp: 2022-11-01 17:20:17Z    

At C:\Program Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.0.0\netFramework\ExchangeOnlineManagement.psm1:726 char:21    

- 

```
throw $_.Exception.InnerException;
```

- 

```
\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~
```

-  CategoryInfo          : OperationStopped: (:) [], Exception  

-  FullyQualifiedErrorId : Case when Message contains:AADSTS70011 Invalid scope. The scope has to be of the form "https://resourceUrl/.def  

   ault"Mitigation: change the scope to be as expectedAADSTS1002016: You are using TLS version 1.0, 1.1 and/or 3DES cipher which are deprecated    

Any suggestion will greatly appreciated    

Thanks,    

Pavan

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-01*

Was it working before?    

https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/enable-support-tls-environment?tabs=azure-monitor    

Make sure the client you are running this from is enforcing TLS 1.2    

Apply those registry settings and reboot and try again:    

https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/enable-support-tls-environment?tabs=azure-monitor#enable-tls-12-on-client-or-server-operating-systems-
