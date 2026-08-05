---
title: "Exchange Server DAG DR Site – Failover Duration and Recommendations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2264903/exchange-server-dag-dr-site-failover-duration-and
question_id: 2264903
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server DAG DR Site – Failover Duration and Recommendations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2264903/exchange-server-dag-dr-site-failover-duration-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

We are implementing a Disaster Recovery (DR) strategy for our on-premises Exchange Server 2019 environment and would like to clarify some points regarding failover and DR site operation.

Environment:

Exchange DAG with 6 Mailbox servers:

   3 in HQ (Primary site)

```
3 in DR site
  
  Planning to use a third site for the File Share Witness.
  
  DAG replication and health are monitored and maintained.
  
  We are preparing for both **planned failovers (e.g., DR drills)** and **unplanned failovers (e.g., HQ outage)**.
```

Key Questions:

How long does it typically take for the DR site to become the active site in case of:

   A planned failover (DR drill)?

```
An **unplanned failover (HQ outage)?**
  
  What are the recommended **maximum durations** for running the DR site as the active site before failing back to HQ?
  
  Are there any **technical risks or limitations** when operating from the DR site for an extended period (days/weeks)?
  
  What are the **recommended RTO and RPO** values for such a setup?
```

-  Any best practices or things to consider regarding:

DAG quorum and File Share Witness across three sites

Failback procedures

-  Namespace or DNS adjustments during failover/failback

## Answers

_No answers on this thread._
