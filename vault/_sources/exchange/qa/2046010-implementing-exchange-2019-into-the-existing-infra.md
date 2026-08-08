---
title: "implementing exchange 2019 into the existing infrastructure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2046010/implementing-exchange-2019-into-the-existing-infra
question_id: 2046010
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# implementing exchange 2019 into the existing infrastructure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2046010/implementing-exchange-2019-into-the-existing-infra (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

There is an existing exchange organization with Exchange 2013 and Exchange 2016 servers. 

It is necessary to implement new Exchange 2019 servers in the organization for subsequent gradual migration to new servers.

I know the steps to install new servers: 

-  Updating the schema 

-  AD update 

-  Exchange 2019 

Are there any problems, moments, tips when implementing this plan? Please share your thoughts, tips, hints, links.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-09-10*

Hi, @Михаил Андросов

Just to make some additions to the answers above.

1.Make sure your Active Directory schema is updated to support Exchange 2019. This step is very important because it prepares the AD environment for the new functions and features of Exchange 2019.

2.Necessary prerequisites for installing Exchange 2019. Exchange Server prerequisites, Exchange 2019 system requirements, Exchange 2019 requirements | Microsoft Learn

3.For more information, please refer to the migration Complete Guide to Migrate Exchange Server 2016 to Exchange Server 2019 (stellarinfo.com)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-10*

Thank you very much for the detailed answer. He will help me with the implementation of the plan for the introduction of new servers.
