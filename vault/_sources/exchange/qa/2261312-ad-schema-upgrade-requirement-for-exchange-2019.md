---
title: "AD Schema Upgrade Requirement for Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261312/ad-schema-upgrade-requirement-for-exchange-2019
question_id: 2261312
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# AD Schema Upgrade Requirement for Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261312/ad-schema-upgrade-requirement-for-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A planned in-place upgrade from Exchange 2016 to Exchange 2019 is underway, with the current infrastructure including an AD server running Windows Server 2016 and AD schema version 87. The new Exchange 2019 server will be installed on Windows Server 2019/2022.

Is it necessary to upgrade the AD schema from version 87 to 88 to support Exchange 2019 in this scenario?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-25*

Ok, here are the supported AD versions and Exch:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#supported-active-directory-environments

It looks you are fine with 87

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-25*

in place upgrades are not supported from 2016> 2019 Exchange
