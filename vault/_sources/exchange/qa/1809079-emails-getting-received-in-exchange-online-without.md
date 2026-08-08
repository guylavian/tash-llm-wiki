---
title: "Emails getting received in exchange online without attachment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1809079/emails-getting-received-in-exchange-online-without
question_id: 1809079
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Emails getting received in exchange online without attachment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1809079/emails-getting-received-in-exchange-online-without (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

We are using Exchange Online only With EOP as a mail filtering. we noticed Emails getting received in exchange online without attachment (.pdf,.csv etc). from a particular external sender.

We don't have any ETR blocking such extensions.

when we checked the EOP it doesn't have those attachments either. Running the content search and download the copy tells us same story missing attachment.

No additional policy is created to block such attachments in EOP as well

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-16*

In this situation, you can check the EOP settings if there are any specific attachment filtering rules for these files types. Also check the sender’s mail server settings.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-12*

What does message trace show? Review the details therein, it will show you each action taken on the message: https://learn.microsoft.com/en-us/exchange/monitoring/trace-an-email-message/message-trace-modern-eac
