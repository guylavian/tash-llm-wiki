---
title: "SMTP Relay in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2075972/smtp-relay-in-exchange-online
question_id: 2075972
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# SMTP Relay in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2075972/smtp-relay-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently we run Exchnage 2019 hybrid. We have not moved our MX records to Exchange Online yet for specific reasons so all mail flow is through Exchange 2019. That said, nearly all user/shared mailboxes have been migrated to Exchange Online. We also have many devices using SMTP relay through Exchange 2019 on-prem (printers etc.) to send mails mainly internally but also some externally (UPS devices for example). Most of these devices do not support authentication so we have setup a mail connector that uses an IP whitelist on Exchange 2019 to handle this. If we get rid of the hybrid and move to Exchange Online what options would we have for this type of unauthenticated relay?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-09-22*

Here are your options:

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365

3 probably fits. 

If you need to do this, I recommend keeping an Exch Server on-prem or an Exchange Edge Role server to route mail .
