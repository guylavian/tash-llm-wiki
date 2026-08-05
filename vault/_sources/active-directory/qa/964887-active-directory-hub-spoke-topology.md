---
title: "active directory hub spoke topology"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/964887/active-directory-hub-spoke-topology
question_id: 964887
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# active directory hub spoke topology

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/964887/active-directory-hub-spoke-topology (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When designing AD sites and services, microsoft typically recommends a hub spoke topology.  What I can't find is a definitive answer on the site link membership.  Each spoke will have a site link that connects to the hub.  In turn, does the hub site link contain ALL spoke sites as members?    

the alternatives would be    

sitea-hub    

siteb-hub    

sitec-hub    

sitea-siteb-sitec-hub    

or    

sitea-hub    

siteb-hub    

sitec-hub    

bridge all site links would be enabled in both scenarios.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-12*

Thanks for the reply.  I have been poring over the MS documentation on this topic and even the link you provided doesn't speak directly to my question.  As each site will need to replicate to the with the hub its easy to say that that site link will only have the spoke and the hub site as members.  I guess my question is should each site have a second site link associated with it?  the hub site link will have all spoke sites as well as itself as members?     

This question is more relevant if we are dealing with 3 or more sites in the same domain.
