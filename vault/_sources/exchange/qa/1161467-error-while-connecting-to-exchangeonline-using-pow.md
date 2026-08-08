---
title: "Error while connecting to ExchangeOnline using powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161467/error-while-connecting-to-exchangeonline-using-pow
question_id: 1161467
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-functions", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Error while connecting to ExchangeOnline using powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161467/error-while-connecting-to-exchangeonline-using-pow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Facing this error:  

Error occured: Error Acquiring Token: System.Exception: Case when Message contains:AADSTS70011 Invalid scope. The scope has to be of the form "https://resourceUrl/.default"Mitigation: change the scope to be as expectedAADSTS1002016: You are using TLS version 1.0, 1.1 anCase when Message contains:AADSTS70011 Invalid scope. The scope has to be of d/or 3DES cipher which are deprecated to improve the security posture of Azure AD. Your TenantID is: xxxx. Please refer to https://go.microsoft.com/fwlink/?linkid=2161187 and conduct needed actions to remediate the issue. For further questions, please contact your administrator.

Command executed: Connect-ExchangeOnline -AppId xxx -CertificateThumbprint xxx -Organization xxx

Module imported: exchangeonlinemanagement.3.1.0

Environment: 

-  Azure Functions (function app)

-  Run time env: ~4

-  TLS 1.2 

And I could able to connect for exchangeonlinemanagement.2.0.5 but not in 3.1.0

Any help regarding this would be highly helpful

Note: Tried executing [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12, still not helpful

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-17*

If everything is correctly set, I would send an email to the product owners and ask for assistance:

[https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps#report-bugs-and-issues-for-the-exchange-online-powershell-module
