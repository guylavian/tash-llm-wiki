---
title: "Support an issue with spam email in Exchange Hybrid environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689570/support-an-issue-with-spam-email-in-exchange-hybri
question_id: 1689570
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Support an issue with spam email in Exchange Hybrid environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689570/support-an-issue-with-spam-email-in-exchange-hybri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear MS Team

Currently, my organization is using your service with Microsoft 365 Business Premium. Recently days I have been having an issue in the Hybrid Exchange environment. My organization often receives spam emails due to the postmaster's address often sending emails out to strange recipients.

Let me describe the Hybrid Exchange model that the organization is using:

 We are using Exchange Server 2013 for On-premise and then configuring the Hybrid with Exchange Online, all emails are routed to Exchange Online from Exchange Server 2013.

 

Currently, we have 2 postmaster addresses on 2 environments (On-premise & Online). I also have a Mail Flow Rule under the name “Block External Sending”.

 

That means that all our employees are only sending outside emails to specific recipients. If they send outside that is not on the list configured in the rule, the postmaster address will send Non-Delivery-Report back to the administrator.

 

The problem here is that when I track logs of emails on Exchange Server 2013, I see the postmaster address on-premise sending outside with strange domain names. Therefore, it was blocked by “Block External Sending” rule from Exchange Online and then Exchange Online's postmaster address sent a Non-Delivery-Report back to the administrator's email.

xxxx

Someone can help analyze the Exchange on-premise log and tell me where the cause started

Thank in advanced

Parker

## Answers

_No answers on this thread._
