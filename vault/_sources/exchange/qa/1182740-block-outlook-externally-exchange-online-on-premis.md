---
title: "Block Outlook externally - Exchange Online/On-Premises"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182740/block-outlook-externally-exchange-online-on-premis
question_id: 1182740
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
---
# Block Outlook externally - Exchange Online/On-Premises

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182740/block-outlook-externally-exchange-online-on-premis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

 

We have a hybrid (Exchange 2016) with Exchange Online and wants to block/restrict users connecting Outlook, outside of our network.

 

What options do we have to achieve this?

 

Regards,

Kavindu

## Answer (community) — community member

*upvotes: 1 · updated: 2023-02-22*

It decied by wherer your mailboxes hosted.

For Exchange on-premises mailboxes, you could block MAPI and Outlook anywhere for them.

For Exchange online mailboxes, they hosted outside of your network by default. You could use Conditional Access to limit them by IP range(within your organization)
