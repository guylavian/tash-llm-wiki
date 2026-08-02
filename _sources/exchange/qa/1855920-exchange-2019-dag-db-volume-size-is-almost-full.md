---
title: "Exchange 2019 DAG, DB volume size is almost full."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1855920/exchange-2019-dag-db-volume-size-is-almost-full
question_id: 1855920
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 DAG, DB volume size is almost full.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1855920/exchange-2019-dag-db-volume-size-is-almost-full (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have Exchange 2019 DAG with 4 nodes, each node has 6 volumes and each volume has 3 DBs. however volume 3 is almost full on all servers so we are planning to extend it. We need to know the best practice for this scenario.

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-07*

Before the extension process, make sure you have up-to-date backups of your database. Check that you have additional storage available to extend volume 3.

To extend volume you can do this by Windows Disk Management. Follow these steps-

·         Open Disk Management

·         Right-click on Volume 3 and select “Extend Volume”

·         Follow the further instructions to add the additional space to the volume

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-07*

Hi,

Welcome to the Microsoft Q&A forum!

I didn't find any scenario that is similar to this. But, about Expanding the Disks on Exchange Databases you can refer to:Expanding the Disks on Exchange Databases. And this article introduces best practices for supported storage configurations:Exchange Server storage configuration options.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.
