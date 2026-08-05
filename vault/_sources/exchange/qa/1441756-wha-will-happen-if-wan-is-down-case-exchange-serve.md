---
title: "Wha will happen if WAN is down? Case : Exchange Server DAG in two site configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1441756/wha-will-happen-if-wan-is-down-case-exchange-serve
question_id: 1441756
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Wha will happen if WAN is down? Case : Exchange Server DAG in two site configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1441756/wha-will-happen-if-wan-is-down-case-exchange-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Every one. 

I have this question as it has been my concern for my Exchange server topology design. 

What will happen to that system if the WAN is down which means DC cannot communicate with DRC. 

Will all databases be active in both sites? or only active on DC? as two site is running normaly except for communication between two site

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-11-27*

The DC Site will remain up and running because the Witness Server is there. 

In your scenario, you have 4 in each DC and the witness server in the primary will give you quorum. 

the DRC will not have quorum with only 4 DAG members. the alternate witness server is not used unless you tell the DAG to use it as the FSW.

See Datacenter switchovers:

https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/datacenter-switchovers?view=exchserver-2019
