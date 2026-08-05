---
title: "Exchange 2016 IMAP Service stopping after installation CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1052337/exchange-2016-imap-service-stopping-after-installa
question_id: 1052337
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 IMAP Service stopping after installation CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1052337/exchange-2016-imap-service-stopping-after-installa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I installed CU23 for on premise Exchange 2016. After installation every IMAP connection stops IMAP Service.    

I try establish IMAP connection via telnet without send any data but it also stops IMAP Service.    

I even not see IMAP banner..    

In Event Viewer I can see only information service is trying to stop (event id 1002) and then information its stops successfully (event id 1001).    

Finally in EV shows " The existing worker process HasExisted value before calling CloseProcess is True" (event id 1040).    

There is no errors or warnings in Event Viewer.    

Before upgrade everything works fine.    

Have you any suggestions?

## Answer (community) — community member

*upvotes: 2 · updated: 2023-02-23*

Hi,

In my case, the server was a member of a DAG and was in Maintenance, once out of maintenance mode => no problem to start the IMAP service

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-27*

Dear Steven,  

thank You for sharing it! :-) I had the same problem and it helped.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-20*

Is this a multirole server? Check if the front end and backend receive connectors are set to port 25 instead of the backend being port 2525.    

Also, If the IMAP service is broken - Run the following command on a PowerShell window.    

```
Get-HealthReport  | where { $_.state -eq “Offline”}
```

It will return an offline IMAP.Proxy healthstate.    

Please note that IMAP and POP services are usually not enabled by default and are only done when the decision is made to use them.
