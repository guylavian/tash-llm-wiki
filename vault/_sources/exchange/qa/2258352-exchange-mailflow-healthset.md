---
title: "Exchange MailFlow HealthSet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2258352/exchange-mailflow-healthset
question_id: 2258352
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange MailFlow HealthSet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2258352/exchange-mailflow-healthset (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

Does anybody know why MailFlow healthset returns no result? Mail flow is ok on both servers:

Regards,  

Michael

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-16*

Hello Amit Singh,

Thank you for your reply!

Here are the screenshots:

Seems there's no MSExchangeHMWorker service on my server:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-16*

Here are a few focused things to check:- MailFlow healthset relies on the built-in synthetic probe messages. If these are disabled or not functioning (e.g., via custom config or transport rules blocking them), you might get a blank result. Run:

Get-HealthReport -Identity <ServerName> | ? {$_.HealthSetName -eq "MailFlow"}

-  Monitoring Mailboxes Missing or Corrupted – These are required for mail flow probes. Run:

Test-Mailflow -TargetMailboxServer <ServerName>

and check:

Get-Mailbox -Monitoring

– Check the Microsoft-Exchange-ManagedAvailability/Monitoring logs for related probe failures or errors.

 – Ensure the MSExchangeHM and MSExchangeHMWorker services are running and not throwing errors. Sometimes restarting these services can help reinitialize probes.

Great time to also confirm you're not hitting a known issue with outdated CU or patch level.

Let us know what you see in Get-HealthReport output!  

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
