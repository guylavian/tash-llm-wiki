---
title: "Update Exchange server 2016 DAG/Cluster to Latest Update Patches"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190574/update-exchange-server-2016-dag-cluster-to-latest
question_id: 1190574
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Update Exchange server 2016 DAG/Cluster to Latest Update Patches

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190574/update-exchange-server-2016-dag-cluster-to-latest (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a DAG of four members of Exchange Server 2016 , one witness server and one alternate witness server .I want to update to latest CU of Exchange Server 2016 what is the best procedure for this as I am in live production environment

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-17*

Hi, really two steps, put the server in maintenance mode:

https://learn.microsoft.com/en-us/exchange/managing-database-availability-groups-exchange-2013-help#performing-maintenance-on-dag-members

then apply the update:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019

Bring the server out of maintenance mode when complete, and Ensure that any load balancer marks the server you are upgrading as down as well, then marked back up once the server is upgraded
