---
title: "Remote Move Migration to Exchange Online - Target Delivery Domains not showing up"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/257837/remote-move-migration-to-exchange-online-target-de
question_id: 257837
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Remote Move Migration to Exchange Online - Target Delivery Domains not showing up

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/257837/remote-move-migration-to-exchange-online-target-de (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're in a hybrid configuration right now and starting the process of migrating mailboxes. We in IT have been moved, and I moved a couple of shared mailboxes over this morning. Now however I just tried to create a new migration batch and the Target Delivery Domain option only lists ourdomain.onmicrosoft.com rather than the various domains we have configured under Accepted Domains.  

I've seen folks say it may be an Autodiscover issue, but the Microsoft Connectivity Analyzer shows no issues there. What other things could cause this?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-26*

Same issue here, but the difference that nothing is appearing is the TargetDeliveryDomain list at all.  

I have run few dry tests and I am pretty sure that Gmail API is functioning  

I appreciate your support

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

Currently, we have the same issue.  Test migrations fail because the TargetDeliveryDomain is set 'wrong'.  I need to have the 'vanity' domain be the TargetDeliveryDomain.  Many options were selectable in the past... (we're doing a tenant-to-tenant migration!)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-25*

Same deal here.  Just earlier today I moved some mailboxes and was able to select our company domain.  Now only the onmicrosoft.com domain is available.  I'm very afraid to proceed with that settings.
