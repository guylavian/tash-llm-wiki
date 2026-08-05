---
title: "Exchange 2016 Migration to EOL CMT Configuration for Host Spam Service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2070579/exchange-2016-migration-to-eol-cmt-configuration-f
question_id: 2070579
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange 2016 Migration to EOL CMT Configuration for Host Spam Service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2070579/exchange-2016-migration-to-eol-cmt-configuration-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to perform a migration with CMT and a hosted spam service that currently handles all inbound and outbound email outside the organization. I would like to keep that in place until all mailboxes have been moved from EOP to EOL over a period of a few weeks.

Currently no one has a "forward" on their mailbox, so this is not a concern right now.

I read through this MS article:  https://techcommunity.microsoft.com/t5/exchange-team-blog/demystifying-centralized-mail-transport-and-criteria-based/ba-p/2927777

Reading the article it mentions using CBR, but I am still not sure if I would be required to implement it. The article mentions that CMT might have some routing issues between EOL and EOP, or there might be issues with EOP emailing to EOP mailboxes.

Do I need CBR at all?

How does CMT route email for internal users? I believe it uses its own connector, is this correct?

I also saw mention of a certificate, I know it is recommended it be a 3rd party cert with the A record name of the mail server, are there any gothcas here?

## Answers

_No answers on this thread._
