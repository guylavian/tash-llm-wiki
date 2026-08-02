---
title: "Exchange 2016 hybrid external recipients in distribution group not receiving emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/427532/exchange-2016-hybrid-external-recipients-in-distri
question_id: 427532
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange 2016 hybrid external recipients in distribution group not receiving emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/427532/exchange-2016-hybrid-external-recipients-in-distri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Our organization has hybrid environment with Exchange 2016 CU20 and Office 365, all mailboxes are already migrated to the cloud. In on-premise Exchange admin center I have created (universal) distribution group. I have added some internal users and some mail contacts and mail users with external SMTP addresses to this group. After sync I can see the group and all the members in the cloud.  

The problem starts when I send email to this group - internal users receive it, but external recipients not. In on-premise Get-MessageTrackingLog returns that the email was successfully sent through send connector, but in the end it just gone to nowhere. Office 365 message trace only returns information that email has been successfully delivered to internal users, but nothing is returned about external recipients, nothing. When I send email directly to the mail contacts and mail users, everything works as it should.  

I have no idea what is causing this and what to check next.

## Answers

_No answers on this thread._
