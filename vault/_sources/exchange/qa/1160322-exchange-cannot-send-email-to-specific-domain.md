---
title: "Exchange Cannot Send Email to Specific Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160322/exchange-cannot-send-email-to-specific-domain
question_id: 1160322
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# Exchange Cannot Send Email to Specific Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160322/exchange-cannot-send-email-to-specific-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Domain1 is hosted on Microsoft 365 while domain2 is hosted in gsuite (dns record is at wix.com)

Unfortunately, domain1 cannot send outgoing emails to recipients in domain2 even they are 100% valid and below is the error.

Error: ‎550 5.1.10 RESOLVER.ADR.RecipientNotFound; Recipient <email address> not found by SMTP address lookup‎

If domain2 will send email to domain1, it will be received as junk. If you will reply to this email, above error will also show.

There are no issues if domain1 will send/receive email to and from other domain.

Domain2 is alredy added on the accepted domain under exchange admin center.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-13*

Hi @Tom Jensen,

You could check your anti-spam policy, there may be a policy blocking the communication between domian1 and domain2.

For the error you provided, you could refer to these two documents：

Fix email delivery issues for error code 550 5.1.0 in Exchange Online

(550 5.1.10 RESOLVER.ADR.RecipientNotFound) NDR error when a Microsoft 365 user tries to send mail to on-premises users in a hybrid deployment

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
