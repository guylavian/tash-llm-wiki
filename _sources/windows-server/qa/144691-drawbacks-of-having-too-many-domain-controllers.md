---
title: "drawbacks of having too many domain controllers?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144691/drawbacks-of-having-too-many-domain-controllers
question_id: 144691
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# drawbacks of having too many domain controllers?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144691/drawbacks-of-having-too-many-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 3 regions, region A has 4 sites with 2 DCs each. Each of the sites are in different subnets. Region B and C has 3 sites (region B has 2 sites, region C has 1) and region B has 2 domain controllers. The 3 sites in region B and C are in the same subnet.  We also have 4 domain controllers on the cloud. Now management is planning to add 2 more DCs in the one site in Region C. That makes a total of 16 domain controllers if management will push the additional two.  

My question is, what will be the drawback of having this much domain controllers? Will it make replication path more confusing and chaotic? That a slight replication problem in one site will infect the other replication partners and would take longer time to self heal. The company is not a global company and serves not more than 100,000 users and computers.  

Second question is, is the 4 domain controllers on the cloud an overkill? Given this much number of domain controllers.

## Answers

_No answers on this thread._
