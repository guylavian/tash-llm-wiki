---
title: "Enable Hybrid modern Auth for onpremises Exchange 2016 + Impact on Outlook thick client 2010,2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222514/enable-hybrid-modern-auth-for-onpremises-exchange
question_id: 222514
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Enable Hybrid modern Auth for onpremises Exchange 2016 + Impact on Outlook thick client 2010,2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222514/enable-hybrid-modern-auth-for-onpremises-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

We are in plan to enable the HMA for our Exchange on-premises environment for leverage Intune as MDM solution for on-premises mailbox.  

If we enable the HMA on-premises exchange server does it impact outlook thick clients which are not supported modern authentication ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-01-07*

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide    

The availability of modern authentication is determined by the combination of the client, protocol, and configuration. If modern authentication is not supported by the client, protocol, and/or configuration, then the client will continue to leverage legacy authentication.    

Clients and/or protocols that are not listed (e.g., POP3) do not support modern authentication with on-premises Exchange and continue to leverage legacy authentication mechanisms even after modern authentication is enabled in the environment.
