---
title: "Planning to Extend Volume size in Exchange 2019 DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2121188/planning-to-extend-volume-size-in-exchange-2019-da
question_id: 2121188
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Planning to Extend Volume size in Exchange 2019 DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2121188/planning-to-extend-volume-size-in-exchange-2019-da (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We Have Exchange 2019 DAG with 4 Servers in a single DAG. Each Server has 6 volumes and each volume has 4 DBs. all Servers are holidng the same volume size and number of DBs. Now we have noticed Volume 2 on two servers are nearly 10%, so planning to extend it. Since we have Virtualized environments, Already extend the volume on VMs, now before extend it from Disk Management, just need to make sure whether we need to extend the volume size on all servers or only 2 servers that are showing the 10% warning.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-20*

You would only need to extend the volumes on the affected servers, though its typically recommended that all volumes across the DAG members match in size.
