---
title: "Move Exchange servers to new data centre"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1089516/move-exchange-servers-to-new-data-centre
question_id: 1089516
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Move Exchange servers to new data centre

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1089516/move-exchange-servers-to-new-data-centre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

We are moving exchange server to new data centre with same internal IP but external IP will be different    

Do I need to do anything after the exchange server move to new data centre    

re-configure any dns internal or external    

Update anything to make sure everything works    

Our setup    

2 Exchange 2016 Hybrid with exchange online    

1 Exchange 2010

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-15*

Ensure internal DNS are valid and external DNS is updated as well as any firewall rules.    

If the IPs of the servers are staying the same, then really no other changes are needed.
