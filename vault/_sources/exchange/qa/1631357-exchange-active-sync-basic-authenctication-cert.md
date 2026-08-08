---
title: "Exchange Active Sync Basic Authenctication Cert"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1631357/exchange-active-sync-basic-authenctication-cert
question_id: 1631357
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange Active Sync Basic Authenctication Cert

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1631357/exchange-active-sync-basic-authenctication-cert (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am using SCEP server on Windows 2008 Enterprise R2 SP1. The SCEP server successfully communicates with mobile devices and is able to generate certificates on them. However, although I can select the certificate and use basic authentication for accessing Outlook Web Access (OWA), I encounter a 500 error code in the server logs even when I correctly configure Active Sync basic authentication.

Here are the relevant log entries:  

2010-08-12 23:53:39 ip_address POST /PowerShell clientApplication=EMC;ExchClientVer=14.1.218.6;PSVersion=2.0 80 CONTOSO\Administrator ip_address Microsoft+WinRM+Client 500 0 0 179998

2010-08-12 23:54:30 ip_address POST /powershell serializationLevel=Full;ExchClientVer=14.1.218.6;PSVersion=2.0 80 CONTOSO\Administrator ip_address Microsoft+WinRM+Client 500 0 0 179994

2010-08-12 23:54:36 ip_address POST /PowerShell serializationLevel=Full;clientApplication=EMC;ExchClientVer=14.1.218.6;PSVersion=2.0 80 CONTOSO\Administrator ip_address Microsoft+WinRM+Client 500 0 0 179996

2010-08-12 23:56:39 ip_address POST /PowerShell clientApplication=EMC;ExchClientVer=14.1.218.6;PSVersion=2.0 80 CONTOSO\Administrator ip_address Microsoft+WinRM+Client 500 0 0 179996

I have been unable to identify the solution or the source of this issue.

Any assistance in resolving this would be greatly appreciated.

Thank you.

## Answers

_No answers on this thread._
