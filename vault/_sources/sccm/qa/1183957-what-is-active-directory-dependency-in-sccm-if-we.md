---
title: "What is Active Directory dependency in SCCM, if we decide to upgrade Active Directory version and OS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183957/what-is-active-directory-dependency-in-sccm-if-we
question_id: 1183957
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
---
# What is Active Directory dependency in SCCM, if we decide to upgrade Active Directory version and OS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183957/what-is-active-directory-dependency-in-sccm-if-we (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are upgrading the server OS version from Windows Server 2012R2 to 2019 for our Production servers which includes our Active Directory Domain Controllers VM's as well.

We also have SCCM running on version 2103, so if we decide to upgrade AD Server OS what impact it will have on our SCCM env and what should we taken care of?

Rahul.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-02-24*

Configmgr does not care about the os version of ad.
