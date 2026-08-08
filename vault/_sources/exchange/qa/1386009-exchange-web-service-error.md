---
title: "Exchange Web Service Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1386009/exchange-web-service-error
question_id: 1386009
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Exchange Web Service Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1386009/exchange-web-service-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
HI Team, 

WE have in house application Newcase that actually sends out email from NewCase to EWS via ttps://autodiscover.INTLSOS.com/Autodiscover/Autodiscover.svc end point. However, this url is not reachable and we are getting below error from the Newcase app Log, i may need someone with EWS expertise to assist on this matter. 

Exception Time: 10/5/2023 6:00:08 PM
Exception Message: The request failed. The remote server returned an error: (500) Internal Server Error.
Stack Trace:    at Microsoft.Exchange.WebServices.Autodiscover.AutodiscoverRequest.InternalExecute() in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\Requests\AutodiscoverRequest.cs:line 185
   at Microsoft.Exchange.WebServices.Autodiscover.GetUserSettingsRequest.Execute() in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\Requests\GetUserSettingsRequest.cs:line 95
   at Microsoft.Exchange.WebServices.Autodiscover.AutodiscoverService.InternalGetUserSettings(List`1 smtpAddresses, List`1 settings, Nullable`1 requestedVersion, Uri& autodiscoverUrl) in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\AutodiscoverService.cs:line 1064
   at Microsoft.Exchange.WebServices.Autodiscover.AutodiscoverService.GetSettings[TGetSettingsResponseCollection,TSettingName](List`1 identities, List`1 settings, Nullable`1 requestedVersion, GetSettingsMethod`2 getSettingsMethod, Func`1 getDomainMethod) in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\AutodiscoverService.cs:line 920
   at Microsoft.Exchange.WebServices.Autodiscover.AutodiscoverService.GetUserSettings(List`1 smtpAddresses, List`1 settings) in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\AutodiscoverService.cs:line 878
   at Microsoft.Exchange.WebServices.Autodiscover.AutodiscoverService.InternalGetSoapUserSettings(String smtpAddress, List`1 requestedSettings) in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\AutodiscoverService.cs:line 827
   at Microsoft.Exchange.WebServices.Autodiscover.AutodiscoverService.GetUserSettings(String userSmtpAddress, UserSettingName[] userSettingNames) in \\REDMOND\EXCHANGE\BUILD\E15\15.00.0913.015\SOURCES\sources\dev\EwsManagedApi\src\EwsManagedApi\Autodiscover\AutodiscoverService.cs:line 1667
   at GraphAPITestClient.EmailHelperEWS.GetExchangeEWsURL(String emailaddress) in C:\PoC\GraphAPITestClient\GraphAPITestClient\EmailHelperEWS.cs:line 357
   at GraphAPITestClient.EmailHelperEWS.d__5.MoveNext() in C:\PoC\GraphAPITestClient\GraphAPITestClient\EmailHelperEWS.cs:line 98

Recent changes  from Exchange Server :
```

## Answers

_No answers on this thread._
