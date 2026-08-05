---
title: "Lotus Notes in co-existence with Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/411510/lotus-notes-in-co-existence-with-exchange-server-2
question_id: 411510
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Lotus Notes in co-existence with Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/411510/lotus-notes-in-co-existence-with-exchange-server-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi folks,   

One of our clients wants to migrate from lotus to an exchange server. During migration, they will use both the servers in co-existence. I just want to confirm from you guys that will that work like lotus can send email to exchange and vice versa. I just read somewhere that lotus can send email to exchange only if the exchange will have a different domain otherwise the mail won't leave the lotus notes and route towards exchange.  

Kindly advise me what will be the possibilities.   

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-20*

There is one product but it seems it has some challenges when you read the notes. I don't know you environment but it could work.  

https://www.quest.com/products/coexistence-manager-for-notes/  

There is no native method besides using a secondary SMTP e-mail on the Notes Profile and using forwarding to get it to the Exchange environment.   

If you come across something, I would like to hear about it.
