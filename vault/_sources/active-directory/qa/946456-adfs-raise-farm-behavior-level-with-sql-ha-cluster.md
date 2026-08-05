---
title: "ADFS Raise Farm Behavior Level with SQL HA Cluster back end."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/946456/adfs-raise-farm-behavior-level-with-sql-ha-cluster
question_id: 946456
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Raise Farm Behavior Level with SQL HA Cluster back end.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/946456/adfs-raise-farm-behavior-level-with-sql-ha-cluster (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am nearing the end of our ADFS upgrade project from ADFS 3.0 to 2019.  During the process of building new ADFS servers I migrated the ADFS database(s) to a new SQL HA cluster.  My question is: Do I have to break apart the HA to allow the Farm Behavior Raise to create the new AdfsConfigurationV4 database or will the ADFS servers be able to create the database through the cluster?     

If it cant create the new database through the cluster can I precreate a blank database in the cluster and then have the ADFS servers populate it during the behavior level raise?      

I am getting to the point in the upgrade process where I have to have a plan to submit for change control approval. I would like to avoid having my change fail if the ADFS servers cannot create the new database through the cluster.

## Answers

_No answers on this thread._
