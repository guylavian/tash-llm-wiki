---
title: "installing Exchange Server 2016 CU 20"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/376597/installing-exchange-server-2016-cu-20
question_id: 376597
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# installing Exchange Server 2016 CU 20

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/376597/installing-exchange-server-2016-cu-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Dear,

I tried to install Exchange Server 2016 CU 20 on windows server 2019 (up-to-date) and I have this error :

Error:  

The following error was generated when "$error.Clear();  

if (Get-Service MpsSvc* | ?{$_.Name -eq 'MpsSvc'})  

{  

Set-Service MpsSvc -StartupType Automatic  

Start-SetupService -ServiceName MpsSvc  

}  

" was run: "Microsoft.PowerShell.Commands.ServiceCommandException: Service 'Windows Defender Firewall (MpsSvc)' cannot be configured due to the following error: Access is denied ---> System.ComponentModel.Win32Exception: Access is denied  

--- End of inner exception stack trace ---".

Note: I tried to disable windows firewall and defender and I have the same issue

can you support me please ?

## Answers

_No answers on this thread._
