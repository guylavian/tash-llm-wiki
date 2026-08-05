---
title: "Exchange 2013 CU 23 after instalation of KB5000871 still show version 15.0.1497.2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/314735/exchange-2013-cu-23-after-instalation-of-kb5000871
question_id: 314735
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 CU 23 after instalation of KB5000871 still show version 15.0.1497.2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/314735/exchange-2013-cu-23-after-instalation-of-kb5000871 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've Exchange 2013 CU23  

I've installed successfully KB5000871 - it is listed here:  

```
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName
Security Update for Exchange Server 2013 Cumulative Update 23 (KB5000871)
```

And I can see it under Control Panel > Programs > Programs and Features > Installed Updates.  

However in Exchange PowerShell shows version 15.0.1497.2 - while as far as I know - it should be 15.0.1497.12  

```
[PS] C:\Windows\system32>Get-ExchangeServer | select AdminDisplayVersion

AdminDisplayVersion
-------------------
Version 15.0 (Build 1497.2)
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Ok, sounds reasonable :)   

Thanks mate!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Thanks, Andy for a fast response.  

FileVersion is:  

```
Get-Command Exsetup.exe | ForEach {$_.FileVersionInfo}

ProductVersion   FileVersion      FileName
--------------   -----------      --------
15.00.1497.012   15.00.1497.012   C:\Program Files\Microsoft\Exchange Server\V15\bin\ExSetup.exe
```

I've restarted this server after the installation of this patch. So - not sure why Exchange itself still shows .2  - also in WebGUI

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-15*

Check the version using these steps:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues#verify-the-installation-of-cus--sus    

```
Get-Command Exsetup.exe | ForEach {$_.FileVersionInfo}
```

For CU23: 15.00.1497.012
