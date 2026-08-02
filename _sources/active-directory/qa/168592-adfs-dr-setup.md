---
title: "ADFS DR Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168592/adfs-dr-setup
question_id: 168592
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS DR Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168592/adfs-dr-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have ADFS configured in one of the physical DCs. the requirement is to configure a DR site for ADFS to ensure when the primary site completely goes down all the requests should hit the DR site.  

What are the available options? Can some one out there help?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-14*

You'll have to deploy an ADFS farm (so you need another server) and put a with load balancer in the front for the port 443.    

There are some example here.
