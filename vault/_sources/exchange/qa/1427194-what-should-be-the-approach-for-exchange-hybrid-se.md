---
title: "What should be the approach for Exchange Hybrid setup for new company for migrating existing user mailboxes in old company?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427194/what-should-be-the-approach-for-exchange-hybrid-se
question_id: 1427194
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# What should be the approach for Exchange Hybrid setup for new company for migrating existing user mailboxes in old company?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427194/what-should-be-the-approach-for-exchange-hybrid-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Suppose Company A consists of 200 users and have exchange hybrid setup and some of the mailboxes are migrated to Exchange online. Now company A made decision for some business requirements and wants to setup New Company B including new Exchange hybrid setup. Additionally decides to move around 100 existing users to new company B. So what would be the best approach that should be considered in this scenario? For Exchange Hybrid Setup.  Can we do migration from Exchange Hybrid server to another Exchange Hybrid Server in different domain.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-17*

I did a similar project some time ago. I can share our approach:

We first changed the domain used for sign-in in the current tenant (e.g. ******@company.com becomes name@temporary_company.com).

We then removed the domain from the old tenant (company.com), added it to the new tenant and configured our on-premise exchange for hybrid mode (old on-premise Exchange with new tenant Exchange Online).

We then migrated the Exchange mailboxes in batches from on-premise to the cloud. From then on, the user uses Exchange Online on the new tenant.

The end situation is the users being on the new tenant with their "old" login (******@company.com). The new tenant uses Exchange Online. Of course, they also still have their "new" login on the old tenant (name@temporary_company.com), which they keep using to access the legacy O365 cloud applications. You can then start migrating the legacy O365 applications.

Also, check these links for more insight - https://techcommunity.microsoft.com/t5/exchange/migrate-exchange-hybrid-server-to-other-domain/m-p/93773

https://community.spiceworks.com/topic/2467212-migrate-ad-connect-and-exchange-hybrid-server-to-another-domain?from_forum=33

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
