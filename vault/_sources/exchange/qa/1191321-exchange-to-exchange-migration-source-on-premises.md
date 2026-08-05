---
title: "Exchange to Exchange Migration (Source :On-premises destination: IAAS) same domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191321/exchange-to-exchange-migration-source-on-premises
question_id: 1191321
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange to Exchange Migration (Source :On-premises destination: IAAS) same domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191321/exchange-to-exchange-migration-source-on-premises (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i want to move exchange server from on-premises to our cloud but not as email hosting but we will create VM and them move mailboxes to, it will same Domain  and same organization 

i have two option as my understanding

one is that i will setup new exchange server after making connectivity then start moving mailbox to destination server.

second , i will create dag copy of whole mailbox database and then one complete i will activate the destination copy and then later demount source exchange server ?

is the second option is practical and will work ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-20*

@Andy David - MVP  

Thanks for quick reply and suggestion , i will make sure to open all ports , but between two what do u thing is best practice ? 

mailbox move one by one or full DB via DAG and active once ? any pro or cons ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-20*

The second option will only work if you have network connectivity and ports open between the servers ( ALL Ports must be open) that are  sufficient to allow you to replicate the copy to the hosted provider to replicate the database

https://learn.microsoft.com/en-us/exchange/high-availability/plan-ha?view=exchserver-2019
