---
title: "3 Node exchange servers and witness server requirement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1373929/3-node-exchange-servers-and-witness-server-require
question_id: 1373929
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# 3 Node exchange servers and witness server requirement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1373929/3-node-exchange-servers-and-witness-server-require (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

We have a 3 Node DAG environment. 2 server in DC and 1 in DR. Do we need witness server across sites for this set up? If not required please suggest how quorum will be maintained during DR failover?

Cheers

Priya

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-21*

3 servers do not require a witness server no. Only if there is an even number of mailbox servers in the DAG is the witness server used. 

You will not have quorum with one server however. So you need at two servers in the DAG in the DR data center with access to a witness server. 

Otherwise you would have force quorum on the one server.

Use this as a guide:https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/datacenter-switchovers?view=exchserver-2019
