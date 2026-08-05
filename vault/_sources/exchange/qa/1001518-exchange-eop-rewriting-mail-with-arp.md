---
title: "Exchange EOP rewriting mail with ARP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1001518/exchange-eop-rewriting-mail-with-arp
question_id: 1001518
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange EOP rewriting mail with ARP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1001518/exchange-eop-rewriting-mail-with-arp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a hybrid setup with both on-prem and O365 mailboxes. When one particular domain sends us an email from the Internet the mail is rewritten seemingly by O365 EOP. As a result the source IP is changed and the email fails SPF authentication. There is nothing strange about the sending domain, they send directly to the Internet so I don't understand why I'm seeing ARC entries in the message headers.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-12*

No email filter between on-prem and O365. The sender does not receive an NDR. I don't want to create a transport rule because the sender only has SPF enabled, which is not enough security.
