---
title: "Exchange Hybrid-Distribution group ndr"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1155786/exchange-hybrid-distribution-group-ndr
question_id: 1155786
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid-Distribution group ndr

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1155786/exchange-hybrid-distribution-group-ndr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are on hyrbid setup, I deleted few Distribution groups from on-premises exchange and created on Exchange Online. Emails sending from external email id's are getting below ndr. DL is configured to receive emails from external ids.    

Remote Server returned '550 5.1.10 RESOLVER.ADR.RecipientNotFound; Recipient not found by SMTP address lookup'    

Original message headers:    

Internal users are able to send email to the DLs on exchange online.    

MX record is pointed to on-premise exchange, I noticed routing error on the message trace logs.     

I believe this is because on-premise exchange doesn't have any object to reference the remote exchange online user.    

Please help me to fix this issue

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-08*

You will need to set the mx record to Exchange Online if you want this to work.     

Or remove the hosted only DLs and recreate on-prem if you want to keep the mx record pointing to on-prem    

Unless there is a technical reason, the recommendation is to always point the mx to Exchange Online    

```
.mail.protection.outlook.com
```
