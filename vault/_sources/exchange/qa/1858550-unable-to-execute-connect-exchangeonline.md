---
title: "Unable to execute Connect-ExchangeOnline"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1858550/unable-to-execute-connect-exchangeonline
question_id: 1858550
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to execute Connect-ExchangeOnline

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1858550/unable-to-execute-connect-exchangeonline (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to execute the  exchange online cmlet Start-HistoricalSearch. I followed this guide in order to be able to access the exchange online command line.

When I type this command:

```
Connect-ExchangeOnline -UserPrincipalName ******@xxx.xx
```

I receive no error message. Instead, I receive the following text:

```
----------------------------------------------------------------------------------------
This V3 EXO PowerShell module contains new REST API backed Exchange Online cmdlets which doesn't require WinRM for Client-Server communication. You can now run these cmdlets after turning off WinRM Basic Auth in your client machine thus making it more secure.

Unlike the EXO* prefixed cmdlets, the cmdlets in this module support full functional parity with the RPS (V1) cmdlets.

V3 cmdlets in the downloaded module are resilient to transient failures, handling retries and throttling errors inherently.

REST backed EOP and SCC cmdlets are also available in the V3 module. Similar to EXO, the cmdlets can be run without WinRM basic auth enabled.

For more information check https://aka.ms/exov3-module
----------------------------------------------------------------------------------------
```

I can not type anything in the console, and after a few secconds I am returned to my powershell session.

Can you help me?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-09*

Is Powershell 7 installed?

Try that

run pwsh.exe in that PS window

then Connect-ExchangeOnline
