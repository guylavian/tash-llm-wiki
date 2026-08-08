---
title: "Connect-exchangeonline with certificate thumbprint failing on server when Powershell is not started in Administrative mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1397944/connect-exchangeonline-with-certificate-thumbprint
question_id: 1397944
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connect-exchangeonline with certificate thumbprint failing on server when Powershell is not started in Administrative mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1397944/connect-exchangeonline-with-certificate-thumbprint (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have registred a App-only authentication - Exchange Online PowerShell in AzureAD and created a selfsigned certificate  

I connect to Exchange Online powershell with following:  

Connect-ExchangeOnline -CertificateThumbprint "<thumbprint>"  -AppID "<AppID>" -Organization "xxxxx.onmicrosoft.com"  

On local computer it works fine when starting Powershell in Non-Administrative mode but on server it only works when I start powershell as Administrator. In Non-Administrative mode I get the error below. 

I haven't found out why. Any ideas?

```
Could not use the certificate for signing. See inner exception for details. Possible cause: this may be a known issue with apps build against .NET Desktop 4.6 or lower. Either target a higher version of .NET desktop - 4
.6.1 and above, or use a different certificate type (non-CNG) or sign your own assertion as described at https://aka.ms/msal-net-signed-assertion. 
At C:\Program Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.2.0\netFramework\ExchangeOnlineManagement.psm1:739 char:21
+                     throw $_.Exception.InnerException;
+                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (:) [], MsalClientException
    + FullyQualifiedErrorId : Could not use the certificate for signing. See inner exception for details. Possible cause: this may be a known issue with apps build against .NET Desktop 4.6 or lower. Either target a hig 
   her version of .NET desktop - 4.6.1 and above, or use a different certificate type (non-CNG) or sign your own assertion as described at https://aka.ms/msal-net-signed-assertion.
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-20*

Review the solutions in this SO thread, hopefully one of them should work here: https://stackoverflow.com/questions/22581811/invalid-provider-type-specified-cryptographicexception-when-trying-to-load-pri/34103154#34103154
