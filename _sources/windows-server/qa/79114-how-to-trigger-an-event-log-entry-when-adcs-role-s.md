---
title: "How to trigger an event log entry when ADCS Role Separation is turned on or off"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/79114/how-to-trigger-an-event-log-entry-when-adcs-role-s
question_id: 79114
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to trigger an event log entry when ADCS Role Separation is turned on or off

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/79114/how-to-trigger-an-event-log-entry-when-adcs-role-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This article indicates that if you have the CA\AuditFilter property set t the max value (127) an event log entry would be triggered when we turn Role Separation on or off.  The event ID should be 801:  

https://www.serverbrain.org/certificate-security-2003/enabling-auditing-at-the-ca.html  

This is not occurring for us, and we're not seeing any other event log entries related to the change.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-08-27*

ADCS audit is a two-step process:  

-  Enable audit filter on CA itself  

-  Enable Certification Authority Audit component in Audit Object Access in group policies.
