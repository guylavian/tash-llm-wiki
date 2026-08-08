---
title: "Security update for Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2181407/security-update-for-exchange
question_id: 2181407
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Security update for Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2181407/security-update-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am using an Exchange 2016 hybrid environment. My Exchange servers are running on Exchange Server 2016 CU23 Nov24SUv2. We have a third-party vulnerability scanning tool, and it has detected the following vulnerability on my Exchange servers:

Security updates for Microsoft Exchange Server (February 2024).

I assumed that Exchange Server 2016 CU23 Nov24SUv2 would fix this vulnerability. Could you please guide me on how to resolve it?

```
[PS] C:\windows\system32>Get-Command Exsetup.exe | ForEach {$_.FileVersionInfo}

ProductVersion   FileVersion      FileName
--------------   -----------      --------
15.01.2507.044   15.01.2507.044   C:\Program Files\Microsoft\Exchange Server\V15\bin\ExSetup.exe

[PS] C:\windows\system32>Get-Command Exsetup.exe | fl

Name            : ExSetup.exe
CommandType     : Application
Definition      : C:\Program Files\Microsoft\Exchange Server\V15\bin\ExSetup.exe
Extension       : .exe
Path            : C:\Program Files\Microsoft\Exchange Server\V15\bin\ExSetup.exe
FileVersionInfo : File:             C:\Program Files\Microsoft\Exchange Server\V15\bin\ExSetup.exe
                  InternalName:     ExSetup.exe
                  OriginalFilename: ExSetup.exe
                  FileVersion:      15.01.2507.044
                  FileDescription:
                  Product:          Microsoft® Exchange
                  ProductVersion:   15.01.2507.044
                  Debug:            False
                  Patched:          False
                  PreRelease:       False
                  PrivateBuild:     False
                  SpecialBuild:     False
                  Language:         Language Neutral
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2025-02-24*

Run the health checker against your server:

https://microsoft.github.io/CSS-Exchange/Diagnostics/HealthChecker/

If you are missing a setting like enabling extended protection, then you can do that by following:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-extended-protection?view=exchserver-2019
