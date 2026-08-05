---
title: "Exchange 2010 Hybrid Migraiton to Office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/105475/exchange-2010-hybrid-migraiton-to-office-365
question_id: 105475
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange 2010 Hybrid Migraiton to Office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/105475/exchange-2010-hybrid-migraiton-to-office-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I understand that to migrate from Exchange 2010 to office 365 you have to use the new HCW.

Couple of questions:

1) does the HCW allow you to manage mailbox the same as a Exchange 2016 Hybrid server? In other words, create mailboxes etc. If not what would i need to do to manage mailboxes if i use the HCW

2)How is the HCW different from Exchange 2016 Hybrid server

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-24*

@KashifRashid-5415  

HCW is not a must when migrating mailboxes from Exchange 2010 to Office 365. It depends on your organizational needs, such as how many mailboxes to migrate and how long you want to migrate.  

Here is a list about ways to migrate mailboxes to Exchange online:  

1) HCW is a tool to create Hybrid relationship within Exchange on-premises and Exchange online. After creating hybrid, you can migrated mailbox from/to Exchange online from Exchange online admin center: Move mailboxes between on-premises and Exchange Online organizations in hybrid deployments  

2)You could manage synced mailboxes from Exchange 2010 EMC.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
