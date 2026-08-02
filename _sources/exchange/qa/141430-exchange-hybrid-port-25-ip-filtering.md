---
title: "Exchange Hybrid Port 25 IP Filtering"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/141430/exchange-hybrid-port-25-ip-filtering
question_id: 141430
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Hybrid Port 25 IP Filtering

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/141430/exchange-hybrid-port-25-ip-filtering (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to confirm that if I want to secure inbound traffic to port 25 for my Exchange Hybrid server I would have to allow the Exchange endpoints listed below in order for Hybrid mail flow to work?     

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide    

*.mail.protection.outlook.com 40.92.0.0/15, 40.107.0.0/16, 52.100.0.0/14, 104.47.0.0/17, 2a01:111:f400::/48, 2a01:111:f403::/48 TCP: 25    

I am concerned because the document also states:    

Endpoint data below lists requirements for connectivity from a user's machine to Office 365. It does not include network connections from Microsoft into a customer network, sometimes called hybrid or inbound network connections. See Additional endpoints for more information.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-27*

Yes its confusing and I am a bit concerned because I usually open port 25 to all traffic in this scenario, leaving security to the cert.  Thanks for the clarification!
