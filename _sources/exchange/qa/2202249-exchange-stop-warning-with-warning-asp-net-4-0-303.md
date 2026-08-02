---
title: "Exchange stop warning with Warning ASP.NET 4.0.30319.0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2202249/exchange-stop-warning-with-warning-asp-net-4-0-303
question_id: 2202249
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange stop warning with Warning ASP.NET 4.0.30319.0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2202249/exchange-stop-warning-with-warning-asp-net-4-0-303 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everybody,

Exchange 2019 with last cu and su.

i get multiple warning error :

Log Name:      Application

Source:        ASP.NET 4.0.30319.0

Date:          06/03/2025 18:51:23

Event ID:      1309

Task Category: Web Event

Level:         Warning

Keywords:      Classic

User:          N/A

Application information: 

```
Application domain: /LM/W3SVC/1/ROOT/mapi-1-133857565105490468 

Trust level: Full 

Application Virtual Path: /mapi 

Application Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\mapi\ 

Machine name: MAIL-SERVER
```

Process information: 

```
Process ID: 15304 

Process name: w3wp.exe 

Account name: NT AUTHORITY\SYSTEM
```

Exception information: 

```
Exception type: HttpException 

Exception message: Timeout della richiesta.
```

When this warning appears Owa doesn't work, and any outlook client not connect. 

Reboot the server and all work correctly. 

Any idea?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-10*

Hi @Marco,

Welcome to Q&A!

May I know if this issue was resolved after rebooting the server?

If so, please keep monitoring it for a period time and feel free to post here if the issue reoccurs.

If this issue intermittently happens even after rebooting the server, please refer to this official KB(Event ID 1309 and you can't access OWA and ECP after you install Exchange Server 2016 or Exchange Server 2013 - Exchange | Microsoft Learn) to see if it could resolve your issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

 

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)) to enable e-mail notifications if you want to receive the related email notification for this thread.
