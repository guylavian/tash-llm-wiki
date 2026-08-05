---
title: "Exchange 2016 stuck in maintenance mode CU20"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334424/exchange-2016-stuck-in-maintenance-mode-cu20
question_id: 334424
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange 2016 stuck in maintenance mode CU20

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334424/exchange-2016-stuck-in-maintenance-mode-cu20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After installing CU20, which completed successfully and restarting I can't get Exchange out of maintenance mode.  

I tried these commands running PS as administrator, which all completed successfully, and restarted.  

Set-ServerComponentState SERVERNAME –Component ServerWideOffline –State Active –Requester Maintenance  

Set-ServerComponentState SERVERNAME –Component HubTransport –State Active –Requester Maintenance  

Set-ServerComponentState SERVERNAME -Component Monitoring -Requester Functional -State Active  

Set-ServerComponentState SERVERNAME -Component RecoveryActionsEnabled -Requester Functional -State Active  

Set-ServerComponentState SERVERNAME -Component ServerWideOffline -Requester Functional -State Active  

When these commands did not work, I ran CU20 again, which completed successfully again, and restarted.  

What should I try next?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-28*

Google dpaulson45 healthchecker.ps1 and run it.  Make sure all is healthy
