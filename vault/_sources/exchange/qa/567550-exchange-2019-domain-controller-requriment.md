---
title: "Exchange 2019 Domain controller requriment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/567550/exchange-2019-domain-controller-requriment
question_id: 567550
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 Domain controller requriment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/567550/exchange-2019-domain-controller-requriment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Plan to deploy the Exchange 2019 in a child domain and we have additional two more child domain in the forest, the root domain is empty and all child domain have few users in each domain (around 3k users ).  

When we deploy Exchange 2019 in child domain ,we plan to create separate AD site and have one DC/GC of each domain. is this right approach or we just need 2 DC/GC of child domain where we deploy exchange 2019?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-09-27*

Ok, I see, in that case you only really need new DCs/GCs in the LMN.ABC.com ad site.   

You can add DCs from the other domains in that same site, but not required.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-09-27*

I would bring up DCs in each AD site regardless.
