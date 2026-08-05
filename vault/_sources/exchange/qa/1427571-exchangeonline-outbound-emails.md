---
title: "ExchangeOnline outbound emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427571/exchangeonline-outbound-emails
question_id: 1427571
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ExchangeOnline outbound emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427571/exchangeonline-outbound-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are in the process of co-existence configuration with Exchange Online and  On-Premises messaging and On-premises gateway Cisco IronPort.  When  we send out emails using connector from Exchange Online to On-Premises.  Ironport log shows that as incoming DNS hostname as example: "mail-mw2nam04lp2168.outbound.protection.outlook.com".  This is generic any other domain from Exchange Online outside our tenant would appear coming from similar mail-mw2nam04lp2168.outbound.protection.outlook.com  

Is it possible that messages from our company's tenenat "Exchange Online" it appears as "Company-com.mail.protection.outlook.com" as this same address we are using to send emails from On-premise to Exchange Online?  In this way on email gateway, we could see difference between emails originating from us (our company) or anyone else using Exchange Online?  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-17*

Hello Raman03

Do you mean configure Exchange Online to use a custom sender domain for outbound emails?

https://learn.microsoft.com/en-us/microsoft-365/admin/email/change-email-address?view=o365-worldwide

Regards

Shaofan
