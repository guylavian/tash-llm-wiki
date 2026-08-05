---
title: "Exchange 2019 for Multiple Tree Domains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1792163/exchange-2019-for-multiple-tree-domains
question_id: 1792163
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 for Multiple Tree Domains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1792163/exchange-2019-for-multiple-tree-domains (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm in the process of setting up exchange servers within a multiple tree domain environment.  example:

Parent domain: philly.com (has exchange setup)

Tree domain 1: eagles.nfl (trying to install/configure new exchange server so it will only see AD users in this domain)

Tree domain 2: sixers.BB (setup another new exchange server as above)

I was able to prepare /prepare schema, /prepareAD, /preparealldomains.  I performed the exchange server install for the eagles.nfl domain, but when I launch ecp I can see all the mailboxes in the forest.  What commands do I need to run to setup Exchange in the tree domain to only see the recipients in its respective domain and not the forest?  hopefully I explained this well.

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-03*

Thats not possible. Exchange orgs are per AD forest so you cant prevent the ability to see all the domains as admin.

Users segmentation in the GAL is possible:

https://learn.microsoft.com/en-us/exchange/address-books/address-book-policies/address-book-policies
