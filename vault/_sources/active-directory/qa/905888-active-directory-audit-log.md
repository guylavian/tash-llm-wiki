---
title: "Active directory audit log"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/905888/active-directory-audit-log
question_id: 905888
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active directory audit log

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/905888/active-directory-audit-log (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

in my environment ,I can't install active directory tools like AD manager plus    

so I usually view some eventlogs like changing password or disable or enable the account by filtering the event ID    

but one of the users accounts was expired ,and I neeed to check the admin who made this account to expire .is there an event id for changing account expiry date

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-28*

Hi @la reine de paix      

Have a look at this article which might satisfy your request.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136    

You will have to use the event viewer on the DC or the powershell to pull the event log details from the domain controllers.    

Gary.
