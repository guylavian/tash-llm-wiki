---
title: "Exchange Hybrid Connection encountered error while running organisation configuration transfer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1304515/exchange-hybrid-connection-encountered-error-while
question_id: 1304515
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid Connection encountered error while running organisation configuration transfer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1304515/exchange-hybrid-connection-encountered-error-while (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we are going to migrate from Exchange on-prem (2016) to Exchange Online and have configured Hybrid connection. HCW is completed with a warning HCW8110 - Encountered error while running organisation configuration transfer. We have checked the MS doc referring to this error and also checked the logs. We can see an error in the log:

"ERROR 10277 [Client=UX, Session=Tenant, Cmdlet=Set-TransportConfig, Thread=8] FINISH Time=365.2ms Results=PowerShell failed to invoke 'Set-TransportConfig': Before you create a journal rule, you must specify an email account to receive journal reports that can't be delivered to the journal destination. To do this, click OK. On the Journal rules page, select an email address to send undeliverable journal reports to. Browse to select a mailbox in your organization or an external contact to receive the undeliverable reports. {CategoryInfo={Activity=[System.String] Set-TransportConfig,Category=[System.Management.Automation.ErrorCategory] InvalidOperation,Reason=[System.String] InvalidOperationException,TargetName=[System.String] ,TargetType=[System.String] },ErrorDetails=,Exception=[System.Management.Automation.RemoteException]"

We have some configuration policies that we would like to copy from on-prem to Exchange online. If we unselect the configuration transfer option, the HCW gets completed with success without any error. Could I please get some advice on how to get this resolved and also if there is a way that we can manually create those organisation configuration policies when we are migrated to Exchange online (there are only handful of these in our Exchange on-prem)? Many thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-13*

Is this defined in on-prem journal rules?
